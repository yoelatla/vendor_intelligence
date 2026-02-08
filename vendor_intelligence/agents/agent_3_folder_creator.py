"""
Agent 3: Folder Structure Creator

Priority: HIGHEST (Runs First)
Creates organized output folder structure before any other agent begins work.
Also creates Google Drive folder hierarchy when credentials are available.
"""

import os
import json
import logging
from typing import Optional

from vendor_intelligence.agents.base import BaseAgent, AgentResult
from vendor_intelligence.config import AnalysisConfig
from vendor_intelligence.utils.web_search import WebSearchClient
from vendor_intelligence.utils.report_writer import ReportWriter, format_timestamp
from vendor_intelligence.utils.google_drive import (
    GoogleDriveClient,
    is_google_drive_available,
    find_credentials,
)

logger = logging.getLogger(__name__)

# Folder structure definition
FOLDER_HIERARCHY = [
    ("01_Market_Research", "Market landscape, competitive analysis, and industry trends"),
    ("02_Customer_Reviews_Analysis", "Aggregated customer reviews, sentiment analysis, and pain points"),
    ("03_Product_Documentation", "Product features, technical specs, and AI/ML deep dive"),
    ("04_QA_Validation_Reports", "Data quality validation, source verification, and consistency checks"),
    ("05_Gap_Analysis", "Competitive gaps, feature parity, and strategic recommendations"),
    ("06_Executive_Summary", "One-page executive summary for senior leadership"),
]


class FolderCreatorAgent(BaseAgent):
    """
    Agent 3: Creates the output folder structure for the analysis.

    This agent runs first and must complete before any other agent begins.
    It creates the organized folder hierarchy and returns folder paths
    for all subsequent agents to use.
    """

    agent_number = 3
    agent_name = "Folder_Structure_Creator"
    output_folder = ""  # This agent creates the folders, not writes to one

    async def run_analysis(self) -> tuple[str, dict]:
        """
        Create folder structure locally and optionally in Google Drive.

        Returns:
            Tuple of (report_content, folder_data_dict)
        """
        base_dir = os.path.join(
            self.config.output_dir,
            f"{self.config.vendor_name.replace(' ', '_')}_Competitive_Intelligence_{self.config.timestamp}",
        )

        folder_paths = {}
        created_folders = []

        # Create base directory (local)
        os.makedirs(base_dir, exist_ok=True)
        logger.info(f"Created base directory: {base_dir}")

        # Create each subfolder (local)
        for folder_name, description in FOLDER_HIERARCHY:
            folder_path = os.path.join(base_dir, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            folder_paths[folder_name] = folder_path
            created_folders.append({
                "name": folder_name,
                "path": folder_path,
                "description": description,
            })
            logger.info(f"Created folder: {folder_path}")

        # Write a manifest file in the base directory
        manifest = self._generate_manifest(base_dir, created_folders)
        manifest_path = os.path.join(base_dir, "MANIFEST.md")
        with open(manifest_path, "w", encoding="utf-8") as f:
            f.write(manifest)

        # Update the report writer's base directory
        self.report_writer.output_base_dir = base_dir

        data = {
            "base_dir": base_dir,
            "folder_paths": folder_paths,
            "created_folders": created_folders,
            "manifest_path": manifest_path,
            "google_drive": None,
        }

        # Attempt Google Drive folder creation
        drive_folders = await self._create_google_drive_folders()
        if drive_folders:
            data["google_drive"] = drive_folders
            logger.info(
                f"Google Drive folder created: "
                f"{drive_folders['base']['url']}"
            )

        report = self._generate_report(base_dir, created_folders, drive_folders)
        return report, data

    async def _create_google_drive_folders(self) -> Optional[dict]:
        """
        Create Google Drive folder structure if credentials are available.

        Returns:
            Dict of Drive folder metadata, or None if unavailable
        """
        if not is_google_drive_available():
            logger.info(
                "Google Drive libraries not installed — skipping Drive upload. "
                "Install with: pip install google-api-python-client google-auth google-auth-oauthlib"
            )
            return None

        creds_path = self.config.google_drive_credentials or find_credentials()
        if not creds_path:
            logger.info(
                "No Google Drive credentials found — skipping Drive upload. "
                "Place credentials.json or service_account.json in the project root."
            )
            return None

        try:
            # Detect credential type
            with open(creds_path, "r") as f:
                creds_data = json.load(f)

            if "type" in creds_data and creds_data["type"] == "service_account":
                drive = GoogleDriveClient.from_service_account(creds_path)
            else:
                token_path = os.path.join(
                    os.path.dirname(creds_path), "token.json"
                )
                drive = GoogleDriveClient.from_oauth(creds_path, token_path)

            if not drive.verify_connection():
                logger.warning("Google Drive connection verification failed")
                return None

            # Create the folder hierarchy
            folders = drive.create_intelligence_folders(
                vendor_name=self.config.vendor_name,
                date_stamp=self.config.timestamp,
                parent_id=self.config.google_drive_folder_id,
            )

            # Store the Drive client on the config for later use by orchestrator
            self.config._drive_client = drive

            return folders

        except Exception as e:
            logger.warning(f"Google Drive folder creation failed: {e}")
            self.add_warning(f"Google Drive unavailable: {e}")
            return None

    def _generate_manifest(
        self, base_dir: str, folders: list[dict]
    ) -> str:
        """Generate the MANIFEST.md file content."""
        lines = [
            f"# {self.config.vendor_name} - Competitive Intelligence Analysis",
            f"**Generated:** {format_timestamp()}",
            f"**Analysis ID:** {self.config.analysis_id}",
            "",
            "---",
            "",
            "## Folder Structure",
            "",
        ]

        for folder in folders:
            lines.append(f"### {folder['name']}")
            lines.append(f"**Purpose:** {folder['description']}")
            lines.append(f"**Path:** `{folder['path']}`")
            lines.append("")

        lines.extend([
            "---",
            "",
            "## Analysis Configuration",
            "",
            f"- **Vendor:** {self.config.vendor_name}",
            f"- **Product Focus:** {self.config.product_name or 'All Products'}",
            f"- **Date Range:** {self.config.date_range}",
            f"- **Review Period:** Last {self.config.review_months} months",
            f"- **Min Competitors:** {self.config.min_competitors}",
            f"- **Min Reviews:** {self.config.min_reviews}",
            "",
            "---",
            "",
            "## Agent Execution Order",
            "",
            "| Phase | Agent | Description | Status |",
            "|-------|-------|-------------|--------|",
            "| 1 | Agent 3: Folder Creator | Create output structure | Complete |",
            "| 2 | Agent 1: Market Research | Competitive landscape analysis | Pending |",
            "| 2 | Agent 2: Review Scanner | Customer review intelligence | Pending |",
            "| 2 | Agent 4: Product Docs | Product & AI/ML analysis | Pending |",
            "| 3 | Agent 5: QA Validation | Data quality assurance | Pending |",
            "| 3 | Agent 6: Gap Analysis | Product gap identification | Pending |",
            "| 3 | Agent 7: Executive Summary | Leadership summary | Pending |",
        ])

        return "\n".join(lines)

    def _generate_report(
        self,
        base_dir: str,
        folders: list[dict],
        drive_folders: Optional[dict] = None,
    ) -> str:
        """Generate the agent's completion report."""
        lines = [
            "# Agent 3: Folder Structure Creation Report",
            f"**Status:** Complete",
            f"**Timestamp:** {format_timestamp()}",
            "",
            "## Created Structure",
            "",
            f"**Local Directory:** `{base_dir}`",
        ]

        if drive_folders:
            lines.append(
                f"**Google Drive:** [{drive_folders['base']['name']}]"
                f"({drive_folders['base']['url']})"
            )
        else:
            lines.append("**Google Drive:** Not configured")

        lines.append("")

        for folder in folders:
            line = f"- `{folder['name']}/` - {folder['description']}"
            if drive_folders and folder["name"] in drive_folders:
                line += f" — [Drive]({drive_folders[folder['name']]['url']})"
            lines.append(line)

        lines.extend([
            "",
            "## Next Steps",
            "",
            "All folders are ready. Agents 1, 2, and 4 can now execute in parallel.",
        ])

        if drive_folders:
            lines.append(
                "Reports will be automatically uploaded to Google Drive after completion."
            )

        return "\n".join(lines)
