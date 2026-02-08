"""
Google Drive integration for the Vendor Intelligence System.

Handles authentication, folder creation, file upload, and sharing
for automatic delivery of reports to Google Drive.

Supports two authentication methods:
1. Service Account (headless/automated) — recommended for CI/CD
2. OAuth2 (interactive) — for local/user runs with browser flow

Usage:
    # With service account
    drive = GoogleDriveClient.from_service_account("service_account.json")

    # With OAuth2
    drive = GoogleDriveClient.from_oauth("credentials.json", "token.json")

    # Create folder structure and upload
    folders = drive.create_intelligence_folders("Reco AI", "2026-02-08")
    drive.upload_report(folders["01_Market_Research"], "report.md", content)
"""

import io
import json
import logging
import os
import mimetypes
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

try:
    from google.oauth2 import service_account
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaIoBaseUpload, MediaFileUpload
    GOOGLE_DRIVE_AVAILABLE = True
except BaseException as _exc:
    GOOGLE_DRIVE_AVAILABLE = False
    logger.debug(
        "Google Drive libraries not available: %s. "
        "Install with: pip install google-api-python-client google-auth google-auth-oauthlib",
        _exc,
    )

# Scopes required for folder creation and file upload
SCOPES = [
    "https://www.googleapis.com/auth/drive.file",
]

# Google Docs MIME type for conversion
GOOGLE_DOC_MIME = "application/vnd.google-apps.document"
GOOGLE_FOLDER_MIME = "application/vnd.google-apps.folder"
MARKDOWN_MIME = "text/markdown"
PLAIN_TEXT_MIME = "text/plain"
JSON_MIME = "application/json"

# Folder structure matching the agent outputs
INTELLIGENCE_FOLDERS = [
    ("01_Market_Research", "Market landscape, competitive analysis, and industry trends"),
    ("02_Customer_Reviews_Analysis", "Customer reviews, sentiment analysis, and pain points"),
    ("03_Product_Documentation", "Product features, technical specs, and AI/ML deep dive"),
    ("04_QA_Validation_Reports", "Data quality validation and consistency checks"),
    ("05_Gap_Analysis", "Competitive gaps, feature parity, and recommendations"),
    ("06_Executive_Summary", "One-page executive summary for leadership"),
]


class GoogleDriveClient:
    """
    Google Drive client for creating folders and uploading reports.

    Wraps the Google Drive API v3 with convenience methods for
    the Vendor Intelligence System's specific needs.
    """

    def __init__(self, credentials):
        """
        Initialize with authenticated credentials.

        Use the factory methods from_service_account() or from_oauth()
        instead of calling this directly.
        """
        if not GOOGLE_DRIVE_AVAILABLE:
            raise RuntimeError(
                "Google Drive libraries not installed. "
                "Run: pip install google-api-python-client google-auth google-auth-oauthlib"
            )
        self.credentials = credentials
        self.service = build("drive", "v3", credentials=credentials)
        logger.info("Google Drive client initialized successfully")

    @classmethod
    def from_service_account(cls, key_path: str) -> "GoogleDriveClient":
        """
        Authenticate using a service account JSON key file.

        Args:
            key_path: Path to the service account JSON key file

        Returns:
            Authenticated GoogleDriveClient
        """
        if not GOOGLE_DRIVE_AVAILABLE:
            raise RuntimeError("Google Drive libraries not installed.")

        credentials = service_account.Credentials.from_service_account_file(
            key_path, scopes=SCOPES
        )
        logger.info(f"Authenticated via service account: {key_path}")
        return cls(credentials)

    @classmethod
    def from_oauth(
        cls,
        credentials_path: str = "credentials.json",
        token_path: str = "token.json",
    ) -> "GoogleDriveClient":
        """
        Authenticate using OAuth2 with browser-based consent flow.

        On first run, opens a browser for user consent and saves the
        token for future use. Subsequent runs reuse the saved token.

        Args:
            credentials_path: Path to OAuth2 client credentials JSON
            token_path: Path to save/load the user's access token

        Returns:
            Authenticated GoogleDriveClient
        """
        if not GOOGLE_DRIVE_AVAILABLE:
            raise RuntimeError("Google Drive libraries not installed.")

        creds = None

        # Load existing token if available
        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(token_path, SCOPES)

        # Refresh or create new credentials
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
                logger.info("Refreshed expired OAuth token")
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_path, SCOPES
                )
                creds = flow.run_local_server(port=0)
                logger.info("Completed OAuth consent flow")

            # Save token for future use
            with open(token_path, "w") as f:
                f.write(creds.to_json())
            logger.info(f"Saved OAuth token to {token_path}")

        return cls(creds)

    # ================================================================
    # Folder Operations
    # ================================================================

    def create_folder(
        self,
        name: str,
        parent_id: Optional[str] = None,
    ) -> dict:
        """
        Create a folder in Google Drive.

        Args:
            name: Folder name
            parent_id: Parent folder ID (None for root)

        Returns:
            Dict with 'id', 'name', and 'url' of the created folder
        """
        metadata = {
            "name": name,
            "mimeType": GOOGLE_FOLDER_MIME,
        }
        if parent_id:
            metadata["parents"] = [parent_id]

        folder = self.service.files().create(
            body=metadata,
            fields="id, name, webViewLink",
        ).execute()

        result = {
            "id": folder["id"],
            "name": folder["name"],
            "url": folder.get("webViewLink", ""),
        }
        logger.info(f"Created folder: {name} (ID: {folder['id']})")
        return result

    def create_intelligence_folders(
        self,
        vendor_name: str,
        date_stamp: str,
        parent_id: Optional[str] = None,
    ) -> dict:
        """
        Create the full intelligence folder hierarchy in Google Drive.

        Args:
            vendor_name: Name of the vendor being analyzed
            date_stamp: Date string for the folder name (YYYY-MM-DD)
            parent_id: Optional parent folder ID

        Returns:
            Dict mapping folder keys to their Drive metadata:
            {
                "base": {"id": "...", "name": "...", "url": "..."},
                "01_Market_Research": {"id": "...", ...},
                ...
            }
        """
        # Create base folder
        base_name = f"{vendor_name} - Competitive Intelligence {date_stamp}"
        base_folder = self.create_folder(base_name, parent_id)

        folders = {"base": base_folder}

        # Create subfolders
        for folder_name, _description in INTELLIGENCE_FOLDERS:
            subfolder = self.create_folder(folder_name, base_folder["id"])
            folders[folder_name] = subfolder
            logger.info(f"  Created subfolder: {folder_name}")

        logger.info(
            f"Created full folder structure: {base_name} "
            f"({len(INTELLIGENCE_FOLDERS)} subfolders)"
        )
        return folders

    # ================================================================
    # File Upload Operations
    # ================================================================

    def upload_report(
        self,
        folder_id: str,
        filename: str,
        content: str,
        convert_to_gdoc: bool = True,
    ) -> dict:
        """
        Upload a Markdown report to Google Drive.

        Args:
            folder_id: Target folder ID in Google Drive
            filename: Name for the file
            content: Markdown content to upload
            convert_to_gdoc: If True, convert to Google Docs format

        Returns:
            Dict with 'id', 'name', and 'url' of the uploaded file
        """
        metadata = {
            "name": filename.replace(".md", "") if convert_to_gdoc else filename,
            "parents": [folder_id],
        }

        if convert_to_gdoc:
            metadata["mimeType"] = GOOGLE_DOC_MIME

        media = MediaIoBaseUpload(
            io.BytesIO(content.encode("utf-8")),
            mimetype=PLAIN_TEXT_MIME,
            resumable=True,
        )

        uploaded = self.service.files().create(
            body=metadata,
            media_body=media,
            fields="id, name, webViewLink",
        ).execute()

        result = {
            "id": uploaded["id"],
            "name": uploaded["name"],
            "url": uploaded.get("webViewLink", ""),
        }
        logger.info(f"Uploaded: {filename} -> {result['url']}")
        return result

    def upload_file_from_path(
        self,
        folder_id: str,
        file_path: str,
        convert_to_gdoc: bool = True,
    ) -> dict:
        """
        Upload a local file to Google Drive.

        Args:
            folder_id: Target folder ID
            file_path: Local path to the file
            convert_to_gdoc: Convert .md files to Google Docs

        Returns:
            Dict with 'id', 'name', and 'url'
        """
        path = Path(file_path)
        filename = path.name

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        return self.upload_report(folder_id, filename, content, convert_to_gdoc)

    def upload_json(
        self,
        folder_id: str,
        filename: str,
        data: dict,
    ) -> dict:
        """
        Upload a JSON file to Google Drive.

        Args:
            folder_id: Target folder ID
            filename: Name for the JSON file
            data: Dict to serialize as JSON

        Returns:
            Dict with 'id', 'name', and 'url'
        """
        content = json.dumps(data, indent=2, default=str)

        metadata = {
            "name": filename,
            "parents": [folder_id],
        }

        media = MediaIoBaseUpload(
            io.BytesIO(content.encode("utf-8")),
            mimetype=JSON_MIME,
            resumable=True,
        )

        uploaded = self.service.files().create(
            body=metadata,
            media_body=media,
            fields="id, name, webViewLink",
        ).execute()

        result = {
            "id": uploaded["id"],
            "name": uploaded["name"],
            "url": uploaded.get("webViewLink", ""),
        }
        logger.info(f"Uploaded JSON: {filename} -> {result['url']}")
        return result

    # ================================================================
    # Batch Upload (All Reports)
    # ================================================================

    def upload_all_reports(
        self,
        local_output_dir: str,
        drive_folders: dict,
        convert_to_gdoc: bool = True,
    ) -> dict:
        """
        Upload all generated reports from local output to Google Drive.

        Args:
            local_output_dir: Path to the local output directory
            drive_folders: Dict from create_intelligence_folders()
            convert_to_gdoc: Convert Markdown to Google Docs

        Returns:
            Dict mapping folder names to lists of uploaded file metadata
        """
        uploaded_files = {}

        # Upload MANIFEST.md to base folder
        manifest_path = os.path.join(local_output_dir, "MANIFEST.md")
        if os.path.exists(manifest_path):
            result = self.upload_file_from_path(
                drive_folders["base"]["id"],
                manifest_path,
                convert_to_gdoc,
            )
            uploaded_files["MANIFEST"] = result

        # Upload reports from each subfolder
        for folder_name, _desc in INTELLIGENCE_FOLDERS:
            local_folder = os.path.join(local_output_dir, folder_name)
            if not os.path.exists(local_folder):
                logger.warning(f"Local folder not found: {local_folder}")
                continue

            drive_folder_id = drive_folders.get(folder_name, {}).get("id")
            if not drive_folder_id:
                logger.warning(f"No Drive folder ID for: {folder_name}")
                continue

            uploaded_files[folder_name] = []

            for file_name in sorted(os.listdir(local_folder)):
                file_path = os.path.join(local_folder, file_name)
                if not os.path.isfile(file_path):
                    continue

                is_markdown = file_name.endswith(".md")
                result = self.upload_file_from_path(
                    drive_folder_id,
                    file_path,
                    convert_to_gdoc=convert_to_gdoc and is_markdown,
                )
                uploaded_files[folder_name].append(result)

        total = sum(
            len(v) if isinstance(v, list) else 1
            for v in uploaded_files.values()
        )
        logger.info(f"Uploaded {total} files to Google Drive")
        return uploaded_files

    # ================================================================
    # Sharing
    # ================================================================

    def share_folder(
        self,
        folder_id: str,
        email: Optional[str] = None,
        role: str = "reader",
        anyone_with_link: bool = False,
    ) -> None:
        """
        Share a Google Drive folder.

        Args:
            folder_id: Folder ID to share
            email: Email address to share with (if specific user)
            role: Permission role ('reader', 'writer', 'commenter')
            anyone_with_link: If True, make accessible to anyone with link
        """
        if anyone_with_link:
            permission = {"type": "anyone", "role": role}
        elif email:
            permission = {
                "type": "user",
                "role": role,
                "emailAddress": email,
            }
        else:
            logger.warning("No email or anyone_with_link specified, skipping share")
            return

        self.service.permissions().create(
            fileId=folder_id,
            body=permission,
            sendNotificationEmail=bool(email),
        ).execute()

        target = email or "anyone with link"
        logger.info(f"Shared folder {folder_id} with {target} ({role})")

    # ================================================================
    # Utility
    # ================================================================

    def get_folder_url(self, folder_id: str) -> str:
        """Get the web URL for a Drive folder."""
        return f"https://drive.google.com/drive/folders/{folder_id}"

    def verify_connection(self) -> bool:
        """Test that the Drive connection works."""
        try:
            about = self.service.about().get(fields="user").execute()
            user = about.get("user", {})
            logger.info(
                f"Connected to Google Drive as: "
                f"{user.get('displayName', 'Unknown')} "
                f"({user.get('emailAddress', 'Unknown')})"
            )
            return True
        except Exception as e:
            logger.error(f"Google Drive connection failed: {e}")
            return False


def is_google_drive_available() -> bool:
    """Check if Google Drive libraries are installed."""
    return GOOGLE_DRIVE_AVAILABLE


def find_credentials() -> Optional[str]:
    """
    Search for Google Drive credentials in common locations.

    Returns:
        Path to credentials file, or None if not found
    """
    search_paths = [
        "credentials.json",
        "service_account.json",
        os.path.expanduser("~/.config/google/credentials.json"),
        os.path.expanduser("~/.google/credentials.json"),
        os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", ""),
    ]

    for path in search_paths:
        if path and os.path.exists(path):
            logger.info(f"Found credentials at: {path}")
            return path

    return None
