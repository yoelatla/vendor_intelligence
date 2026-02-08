"""
Multi-Agent Vendor Intelligence Orchestrator

Master orchestrator managing the execution flow of all 7 agents:

PHASE 1 (Sequential):
  Agent 3: Folder Structure Creator [RUNS FIRST]

PHASE 2 (Parallel Execution):
  Agent 1: Market Research & Competitive Analysis
  Agent 2: Review Intelligence Scanner
  Agent 4: Product Documentation Analyzer (with AI/ML Deep Dive)

PHASE 3 (Sequential Quality & Analysis):
  Agent 5: Quality Assurance & Validation Engine [RUNS AFTER 1,2,4]
  Agent 6: Product Gap Analysis [RUNS AFTER 5]
  Agent 7: Executive Summary Generator [RUNS LAST]
"""

import asyncio
import json
import logging
import os
import sys
from datetime import datetime
from typing import Optional

from vendor_intelligence.config import AnalysisConfig
from vendor_intelligence.utils.web_search import WebSearchClient
from vendor_intelligence.utils.report_writer import ReportWriter, format_timestamp
try:
    from vendor_intelligence.utils.google_drive import GoogleDriveClient, is_google_drive_available
except BaseException:
    GoogleDriveClient = None  # type: ignore[misc, assignment]
    def is_google_drive_available() -> bool:  # type: ignore[no-redef]
        return False
from vendor_intelligence.agents.base import AgentResult
from vendor_intelligence.agents.agent_1_market_research import MarketResearchAgent
from vendor_intelligence.agents.agent_2_review_scanner import ReviewScannerAgent
from vendor_intelligence.agents.agent_3_folder_creator import FolderCreatorAgent
from vendor_intelligence.agents.agent_4_product_docs import ProductDocsAgent
from vendor_intelligence.agents.agent_5_qa_validation import QAValidationAgent
from vendor_intelligence.agents.agent_6_gap_analysis import GapAnalysisAgent
from vendor_intelligence.agents.agent_7_executive_summary import ExecutiveSummaryAgent

logger = logging.getLogger(__name__)


class VendorIntelligenceOrchestrator:
    """
    Master orchestrator for the 7-agent competitive intelligence system.

    Manages the complete lifecycle of a vendor analysis:
    1. Folder structure creation
    2. Parallel data gathering (market research, reviews, product docs)
    3. Sequential quality assurance and analysis
    4. Executive summary generation

    Usage:
        config = AnalysisConfig(vendor_name="Zscaler")
        orchestrator = VendorIntelligenceOrchestrator(config)
        results = await orchestrator.run()
    """

    def __init__(self, config: AnalysisConfig):
        self.config = config
        self.search_client = WebSearchClient()
        self.report_writer = ReportWriter(config.output_dir)
        self.agent_results: dict[str, AgentResult] = {}
        self.start_time: Optional[datetime] = None
        self.folder_data: Optional[dict] = None

    async def run(self) -> dict:
        """
        Execute the full multi-agent analysis workflow.

        Returns:
            Dict containing all agent results and metadata
        """
        self.start_time = datetime.now()

        self._log_header()

        try:
            # ============================================
            # PHASE 1: Folder Structure (Sequential)
            # ============================================
            self._log_phase("PHASE 1", "Creating Output Structure")
            folder_result = await self._run_agent_3()

            if folder_result.status == "failed":
                self._log_error("Folder creation failed. Cannot proceed.")
                return self._build_final_result("failed")

            # Update report writer with new base directory
            if folder_result.data.get("base_dir"):
                self.report_writer.output_base_dir = folder_result.data["base_dir"]
                self.folder_data = folder_result.data

            self._log_success(
                f"Folder structure created: {folder_result.data.get('base_dir', 'N/A')}"
            )

            # ============================================
            # PHASE 2: Data Gathering (Parallel)
            # ============================================
            self._log_phase("PHASE 2", "Gathering Intelligence (Parallel)")

            agent_1_task = self._run_agent_1()
            agent_2_task = self._run_agent_2()
            agent_4_task = self._run_agent_4()

            results = await asyncio.gather(
                agent_1_task, agent_2_task, agent_4_task,
                return_exceptions=True,
            )

            # Process parallel results
            agent_names = ["agent_1", "agent_2", "agent_4"]
            for name, result in zip(agent_names, results):
                if isinstance(result, Exception):
                    logger.error(f"{name} raised exception: {result}")
                    self.agent_results[name] = AgentResult(
                        agent_name=name,
                        agent_number=int(name.split("_")[1]),
                        status="failed",
                        errors=[str(result)],
                    )
                else:
                    self.agent_results[name] = result
                    status_icon = (
                        "OK" if result.status == "success"
                        else "WARN" if result.status == "partial"
                        else "FAIL"
                    )
                    self._log_agent_complete(name, status_icon, result.duration_seconds)

            self._log_success("All intelligence gathering complete")

            # ============================================
            # PHASE 3: Analysis & Synthesis (Sequential)
            # ============================================
            self._log_phase("PHASE 3", "Quality Assurance & Analysis")

            # Agent 5: QA Validation
            self._log_agent_start("Agent 5", "QA Validation")
            qa_result = await self._run_agent_5()

            qa_status = qa_result.data.get("overall_status", "UNKNOWN")
            qa_score = qa_result.data.get("quality_score", 0)

            if qa_status == "REQUIRES REVISION":
                self._log_warning(
                    f"QA flagged issues (score: {qa_score}/100). "
                    "Proceeding with warnings."
                )
                self._notify_user_issues(qa_result.data)
            elif qa_status == "APPROVED WITH NOTES":
                self._log_warning(
                    f"QA passed with notes (score: {qa_score}/100)"
                )
            else:
                self._log_success(f"QA passed (score: {qa_score}/100)")

            # Agent 6: Gap Analysis
            self._log_agent_start("Agent 6", "Gap Analysis")
            gap_result = await self._run_agent_6()
            self._log_agent_complete("agent_6", "OK", gap_result.duration_seconds)

            # Agent 7: Executive Summary
            self._log_agent_start("Agent 7", "Executive Summary")
            summary_result = await self._run_agent_7()
            self._log_agent_complete("agent_7", "OK", summary_result.duration_seconds)

            # ============================================
            # Google Drive Upload (if configured)
            # ============================================
            drive_result = await self._upload_to_google_drive()

            # ============================================
            # FINAL: Compile Results
            # ============================================
            final_result = self._build_final_result("success")

            if drive_result:
                final_result["google_drive"] = drive_result

            self._log_completion(final_result)

            return final_result

        except Exception as e:
            logger.error(f"Orchestration failed: {e}", exc_info=True)
            self._log_error(f"CRITICAL ERROR: {e}")
            return self._build_final_result("failed")

    # ================================================================
    # Agent Execution Methods
    # ================================================================

    async def _run_agent_3(self) -> AgentResult:
        """Run Agent 3: Folder Structure Creator."""
        agent = FolderCreatorAgent(
            config=self.config,
            search_client=self.search_client,
            report_writer=self.report_writer,
        )
        result = await agent.execute()
        self.agent_results["agent_3"] = result
        return result

    async def _run_agent_1(self) -> AgentResult:
        """Run Agent 1: Market Research & Competitive Analysis."""
        agent = MarketResearchAgent(
            config=self.config,
            search_client=self.search_client,
            report_writer=self.report_writer,
        )
        return await agent.execute()

    async def _run_agent_2(self) -> AgentResult:
        """Run Agent 2: Review Intelligence Scanner."""
        agent = ReviewScannerAgent(
            config=self.config,
            search_client=self.search_client,
            report_writer=self.report_writer,
        )
        return await agent.execute()

    async def _run_agent_4(self) -> AgentResult:
        """Run Agent 4: Product Documentation Analyzer."""
        agent = ProductDocsAgent(
            config=self.config,
            search_client=self.search_client,
            report_writer=self.report_writer,
        )
        return await agent.execute()

    async def _run_agent_5(self) -> AgentResult:
        """Run Agent 5: QA Validation Engine."""
        agent = QAValidationAgent(
            config=self.config,
            search_client=self.search_client,
            report_writer=self.report_writer,
            agent_results=self.agent_results,
        )
        result = await agent.execute()
        self.agent_results["agent_5"] = result
        return result

    async def _run_agent_6(self) -> AgentResult:
        """Run Agent 6: Gap Analysis."""
        agent = GapAnalysisAgent(
            config=self.config,
            search_client=self.search_client,
            report_writer=self.report_writer,
            agent_results=self.agent_results,
        )
        result = await agent.execute()
        self.agent_results["agent_6"] = result
        return result

    async def _run_agent_7(self) -> AgentResult:
        """Run Agent 7: Executive Summary Generator."""
        agent = ExecutiveSummaryAgent(
            config=self.config,
            search_client=self.search_client,
            report_writer=self.report_writer,
            agent_results=self.agent_results,
        )
        result = await agent.execute()
        self.agent_results["agent_7"] = result
        return result

    # ================================================================
    # Google Drive Upload
    # ================================================================

    async def _upload_to_google_drive(self) -> Optional[dict]:
        """
        Upload all generated reports to Google Drive.

        Uses the Drive client and folder structure created by Agent 3.
        Returns upload metadata or None if Drive is not configured.
        """
        if not self.config.upload_to_google_drive:
            return None

        # Get the Drive client stored by Agent 3
        drive_client: Optional[GoogleDriveClient] = getattr(
            self.config, "_drive_client", None
        )
        if not drive_client:
            logger.info("No Google Drive client available — skipping upload")
            return None

        # Get Drive folders from Agent 3's result
        agent_3_result = self.agent_results.get("agent_3")
        if not agent_3_result or not isinstance(agent_3_result, AgentResult):
            return None

        drive_folders = agent_3_result.data.get("google_drive")
        if not drive_folders:
            return None

        local_output_dir = agent_3_result.data.get("base_dir")
        if not local_output_dir:
            return None

        self._log_phase("UPLOAD", "Uploading Reports to Google Drive")

        try:
            uploaded = drive_client.upload_all_reports(
                local_output_dir=local_output_dir,
                drive_folders=drive_folders,
                convert_to_gdoc=True,
            )

            total_files = sum(
                len(v) if isinstance(v, list) else 1
                for v in uploaded.values()
            )

            base_url = drive_folders["base"].get("url", "")
            self._log_success(
                f"Uploaded {total_files} files to Google Drive"
            )
            if base_url:
                self._log_success(f"Drive folder: {base_url}")

            # Share if configured
            share_email = getattr(self.config, "google_drive_share_email", None)
            if share_email:
                drive_client.share_folder(
                    drive_folders["base"]["id"],
                    email=share_email,
                    role="reader",
                )
                self._log_success(f"Shared with: {share_email}")

            return {
                "uploaded_files": total_files,
                "base_folder_url": base_url,
                "base_folder_id": drive_folders["base"]["id"],
                "file_details": uploaded,
            }

        except Exception as e:
            logger.error(f"Google Drive upload failed: {e}")
            self._log_warning(f"Drive upload failed: {e}")
            return None

    # ================================================================
    # Result Compilation
    # ================================================================

    def _build_final_result(self, status: str) -> dict:
        """Build the final orchestration result."""
        end_time = datetime.now()
        duration = (end_time - self.start_time).total_seconds() if self.start_time else 0

        output_files = {}
        for key, result in self.agent_results.items():
            if isinstance(result, AgentResult) and result.output_path:
                output_files[key] = result.output_path

        qa_data = {}
        if "agent_5" in self.agent_results:
            qa_result = self.agent_results["agent_5"]
            if isinstance(qa_result, AgentResult):
                qa_data = {
                    "quality_score": qa_result.data.get("quality_score", "N/A"),
                    "overall_status": qa_result.data.get("overall_status", "N/A"),
                    "critical_issues": qa_result.data.get("critical_issues", []),
                    "warnings": qa_result.data.get("warnings", []),
                }

        return {
            "status": status,
            "vendor_name": self.config.vendor_name,
            "product_name": self.config.product_name,
            "analysis_id": self.config.analysis_id,
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_time": end_time.isoformat(),
            "duration_seconds": duration,
            "output_directory": (
                self.folder_data.get("base_dir") if self.folder_data else None
            ),
            "output_files": output_files,
            "qa_summary": qa_data,
            "agent_statuses": {
                key: {
                    "status": (
                        result.status
                        if isinstance(result, AgentResult)
                        else "unknown"
                    ),
                    "duration": (
                        result.duration_seconds
                        if isinstance(result, AgentResult)
                        else 0
                    ),
                    "errors": (
                        result.errors
                        if isinstance(result, AgentResult)
                        else []
                    ),
                }
                for key, result in self.agent_results.items()
            },
        }

    # ================================================================
    # User Notifications
    # ================================================================

    def _notify_user_issues(self, qa_data: dict) -> None:
        """Notify user of critical issues from QA."""
        critical = qa_data.get("critical_issues", [])
        warnings = qa_data.get("warnings", [])

        if critical:
            print("\n  CRITICAL ISSUES DETECTED:")
            for i, issue in enumerate(critical, 1):
                print(f"    {i}. [{issue.get('agent', '?')}] {issue.get('title', '?')}")
                print(f"       {issue.get('description', '')}")

        if warnings:
            print("\n  WARNINGS:")
            for warning in warnings:
                print(f"    - [{warning.get('agent', '?')}] {warning.get('message', '?')}")

    # ================================================================
    # Logging Helpers
    # ================================================================

    def _log_header(self) -> None:
        """Log the analysis header."""
        print("=" * 72)
        print("  VENDOR COMPETITIVE INTELLIGENCE SYSTEM")
        print("=" * 72)
        print(f"  Vendor:    {self.config.vendor_name}")
        if self.config.product_name:
            print(f"  Product:   {self.config.product_name}")
        print(f"  Date:      {self.config.timestamp}")
        print(f"  Analysis:  {self.config.analysis_id}")
        print("=" * 72)

    def _log_phase(self, phase: str, description: str) -> None:
        """Log a phase start."""
        print(f"\n--- {phase}: {description} ---")

    def _log_agent_start(self, agent: str, description: str) -> None:
        """Log an agent starting."""
        print(f"  [{agent}] Starting: {description}...")

    def _log_agent_complete(
        self, agent: str, status: str, duration: float
    ) -> None:
        """Log an agent completion."""
        print(f"  [{agent}] {status} ({duration:.1f}s)")

    def _log_success(self, message: str) -> None:
        """Log a success message."""
        print(f"  [OK] {message}")

    def _log_warning(self, message: str) -> None:
        """Log a warning."""
        print(f"  [WARN] {message}")

    def _log_error(self, message: str) -> None:
        """Log an error."""
        print(f"  [ERROR] {message}")

    def _log_completion(self, result: dict) -> None:
        """Log the final completion summary."""
        duration = result.get("duration_seconds", 0)
        qa = result.get("qa_summary", {})

        print("\n" + "=" * 72)
        print("  ANALYSIS COMPLETE")
        print("=" * 72)
        print(f"  Duration:     {duration:.1f}s")
        print(f"  QA Score:     {qa.get('quality_score', 'N/A')}/100")
        print(f"  QA Status:    {qa.get('overall_status', 'N/A')}")
        print(f"  Output:       {result.get('output_directory', 'N/A')}")

        print("\n  Agent Results:")
        for key, status_data in result.get("agent_statuses", {}).items():
            status = status_data.get("status", "unknown")
            dur = status_data.get("duration", 0)
            icon = (
                "[OK]" if status == "success"
                else "[WARN]" if status == "partial"
                else "[FAIL]"
            )
            print(f"    {icon} {key}: {status} ({dur:.1f}s)")

        output_files = result.get("output_files", {})
        if output_files:
            print("\n  Output Files:")
            for key, path in output_files.items():
                print(f"    - {key}: {path}")

        drive_info = result.get("google_drive")
        if drive_info:
            print(f"\n  Google Drive:")
            print(f"    Files uploaded: {drive_info.get('uploaded_files', 0)}")
            print(f"    Folder URL:     {drive_info.get('base_folder_url', 'N/A')}")

        print("\n  Next Steps:")
        print("    1. Review Executive Summary (06_Executive_Summary)")
        print("    2. Deep dive into Gap Analysis (05_Gap_Analysis)")
        print("    3. Check AI/ML Analysis (03_Product_Documentation)")
        print("    4. Review QA report for data limitations (04_QA_Validation_Reports)")
        print("=" * 72)


async def run_analysis(
    vendor_name: str,
    product_name: Optional[str] = None,
    competitors: Optional[list[str]] = None,
    output_dir: str = "output",
) -> dict:
    """
    Convenience function to run a complete vendor analysis.

    Args:
        vendor_name: Name of the vendor to analyze
        product_name: Optional specific product to focus on
        competitors: Optional list of competitor names
        output_dir: Directory for output files

    Returns:
        Dict with complete analysis results
    """
    config = AnalysisConfig(
        vendor_name=vendor_name,
        product_name=product_name,
        user_provided_competitors=competitors,
        auto_detect_competitors=competitors is None,
        output_dir=output_dir,
    )

    orchestrator = VendorIntelligenceOrchestrator(config)
    return await orchestrator.run()
