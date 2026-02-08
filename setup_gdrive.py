#!/usr/bin/env python3
"""
Google Drive Setup Script for Vendor Intelligence System.

This script helps you configure Google Drive integration for automatic
report uploads. It guides you through credential setup and verification.

Usage:
    python setup_gdrive.py --service-account path/to/key.json
    python setup_gdrive.py --oauth path/to/credentials.json
    python setup_gdrive.py --verify
"""

import argparse
import json
import os
import sys


def check_dependencies() -> bool:
    """Check if required Google libraries are installed."""
    try:
        import google.oauth2  # noqa: F401
        import googleapiclient  # noqa: F401
        print("[OK] Google API libraries are installed")
        return True
    except ImportError:
        print("[MISSING] Google API libraries not found")
        print()
        print("Install with:")
        print("  pip install google-api-python-client google-auth google-auth-oauthlib")
        return False


def verify_credentials(creds_path: str) -> bool:
    """Verify that credentials file is valid and can connect."""
    if not os.path.exists(creds_path):
        print(f"[ERROR] File not found: {creds_path}")
        return False

    try:
        with open(creds_path) as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"[ERROR] Invalid JSON: {creds_path}")
        return False

    print(f"[OK] Valid JSON file: {creds_path}")

    # Detect credential type
    if data.get("type") == "service_account":
        print(f"[OK] Credential type: Service Account")
        print(f"     Email: {data.get('client_email', 'N/A')}")
        print(f"     Project: {data.get('project_id', 'N/A')}")
    elif "installed" in data or "web" in data:
        print(f"[OK] Credential type: OAuth2 Client")
        client_type = "installed" if "installed" in data else "web"
        print(f"     Client ID: {data[client_type].get('client_id', 'N/A')[:40]}...")
    else:
        print(f"[WARN] Unknown credential type")

    # Try to connect
    if not check_dependencies():
        return False

    try:
        from vendor_intelligence.utils.google_drive import GoogleDriveClient

        if data.get("type") == "service_account":
            client = GoogleDriveClient.from_service_account(creds_path)
        else:
            token_path = os.path.join(os.path.dirname(creds_path), "token.json")
            client = GoogleDriveClient.from_oauth(creds_path, token_path)

        if client.verify_connection():
            print("[OK] Successfully connected to Google Drive!")
            return True
        else:
            print("[ERROR] Connection verification failed")
            return False

    except Exception as e:
        print(f"[ERROR] Connection failed: {e}")
        return False


def setup_service_account(key_path: str) -> None:
    """Set up service account credentials."""
    print("=" * 60)
    print("  Google Drive Setup - Service Account")
    print("=" * 60)
    print()

    if verify_credentials(key_path):
        print()
        print("Setup complete! Run the system with:")
        print(f'  python -m vendor_intelligence --vendor "Reco AI" \\')
        print(f'    --google-drive-credentials {key_path}')
    else:
        print()
        print("Setup failed. Please check your credentials.")
        print()
        print("To create a service account:")
        print("  1. Go to https://console.cloud.google.com/iam-admin/serviceaccounts")
        print("  2. Create a new service account")
        print("  3. Enable the Google Drive API")
        print("  4. Create and download a JSON key")
        print("  5. Share your target Drive folder with the service account email")


def setup_oauth(creds_path: str) -> None:
    """Set up OAuth2 credentials."""
    print("=" * 60)
    print("  Google Drive Setup - OAuth2")
    print("=" * 60)
    print()

    if verify_credentials(creds_path):
        print()
        print("Setup complete! Run the system with:")
        print(f'  python -m vendor_intelligence --vendor "Reco AI" \\')
        print(f'    --google-drive-credentials {creds_path}')
    else:
        print()
        print("Setup failed. Please check your credentials.")
        print()
        print("To create OAuth2 credentials:")
        print("  1. Go to https://console.cloud.google.com/apis/credentials")
        print("  2. Create an OAuth 2.0 Client ID (Desktop application)")
        print("  3. Enable the Google Drive API")
        print("  4. Download the credentials JSON")
        print("  5. On first run, a browser window will open for consent")


def show_status() -> None:
    """Show current Google Drive configuration status."""
    print("=" * 60)
    print("  Google Drive Integration Status")
    print("=" * 60)
    print()

    # Check libraries
    libs_ok = check_dependencies()
    print()

    # Check for credentials in common locations
    from vendor_intelligence.utils.google_drive import find_credentials

    creds = find_credentials()
    if creds:
        print(f"[OK] Credentials found: {creds}")
        if libs_ok:
            print()
            verify_credentials(creds)
    else:
        print("[MISSING] No credentials found")
        print()
        print("Searched locations:")
        print("  - ./credentials.json")
        print("  - ./service_account.json")
        print("  - ~/.config/google/credentials.json")
        print("  - ~/.google/credentials.json")
        print("  - $GOOGLE_APPLICATION_CREDENTIALS")

    print()
    print("For setup instructions, run:")
    print("  python setup_gdrive.py --service-account <path>")
    print("  python setup_gdrive.py --oauth <path>")


def main():
    parser = argparse.ArgumentParser(
        description="Set up Google Drive integration for Vendor Intelligence System"
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--service-account",
        metavar="KEY_PATH",
        help="Path to service account JSON key file",
    )
    group.add_argument(
        "--oauth",
        metavar="CREDS_PATH",
        help="Path to OAuth2 client credentials JSON",
    )
    group.add_argument(
        "--verify",
        action="store_true",
        help="Check current configuration status",
    )

    args = parser.parse_args()

    if args.service_account:
        setup_service_account(args.service_account)
    elif args.oauth:
        setup_oauth(args.oauth)
    else:
        show_status()


if __name__ == "__main__":
    main()
