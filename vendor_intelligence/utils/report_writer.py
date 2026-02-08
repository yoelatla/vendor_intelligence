"""
Report writing utilities for generating Markdown reports.

Handles report generation, formatting, and file output for all agents.
"""

import os
import logging
from datetime import datetime
from typing import Optional

logger = logging.getLogger(__name__)


class ReportWriter:
    """Generates and writes Markdown reports to the output directory."""

    def __init__(self, output_base_dir: str):
        self.output_base_dir = output_base_dir

    def write_report(
        self,
        folder: str,
        filename: str,
        content: str,
    ) -> str:
        """
        Write a report to the specified folder.

        Args:
            folder: Subfolder name within output directory
            filename: Report filename (should end in .md)
            content: Markdown content of the report

        Returns:
            Full path to the written file
        """
        folder_path = os.path.join(self.output_base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)

        if not filename.endswith(".md"):
            filename += ".md"

        filepath = os.path.join(folder_path, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        logger.info(f"Report written: {filepath}")
        return filepath

    def append_to_report(self, filepath: str, content: str) -> None:
        """Append content to an existing report."""
        with open(filepath, "a", encoding="utf-8") as f:
            f.write("\n" + content)


def format_timestamp() -> str:
    """Return formatted current timestamp."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")


def format_table(headers: list[str], rows: list[list[str]]) -> str:
    """
    Format data as a Markdown table.

    Args:
        headers: List of column header strings
        rows: List of rows, each row is a list of cell strings

    Returns:
        Formatted Markdown table string
    """
    if not headers:
        return ""

    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < len(col_widths):
                col_widths[i] = max(col_widths[i], len(str(cell)))

    header_line = "| " + " | ".join(
        h.ljust(col_widths[i]) for i, h in enumerate(headers)
    ) + " |"
    separator = "|-" + "-|-".join(
        "-" * w for w in col_widths
    ) + "-|"

    data_lines = []
    for row in rows:
        padded = []
        for i, cell in enumerate(row):
            width = col_widths[i] if i < len(col_widths) else len(str(cell))
            padded.append(str(cell).ljust(width))
        data_lines.append("| " + " | ".join(padded) + " |")

    return "\n".join([header_line, separator] + data_lines)


def format_section(title: str, level: int = 2) -> str:
    """Format a section header."""
    prefix = "#" * level
    return f"\n{prefix} {title}\n"


def format_bullet_list(items: list[str], indent: int = 0) -> str:
    """Format a bullet list."""
    prefix = "  " * indent + "- "
    return "\n".join(f"{prefix}{item}" for item in items)


def format_numbered_list(items: list[str]) -> str:
    """Format a numbered list."""
    return "\n".join(f"{i}. {item}" for i, item in enumerate(items, 1))


def format_key_value(key: str, value: str, bold_key: bool = True) -> str:
    """Format a key-value pair."""
    if bold_key:
        return f"**{key}:** {value}"
    return f"{key}: {value}"


def format_status_badge(status: str) -> str:
    """Format a status indicator."""
    badges = {
        "pass": "PASS",
        "fail": "FAIL",
        "warning": "PASS WITH WARNINGS",
        "critical": "Critical",
        "high": "High",
        "medium": "Medium",
        "low": "Low",
    }
    return badges.get(status.lower(), status)


def format_source_citation(
    title: str,
    url: str,
    access_date: Optional[str] = None,
    number: Optional[int] = None,
) -> str:
    """Format a source citation."""
    date_str = access_date or format_timestamp().split(" ")[0]
    prefix = f"{number}. " if number else "- "
    return f"{prefix}[{title}]({url}) - Accessed {date_str}"
