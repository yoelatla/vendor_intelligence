"""
Base agent class for the Vendor Intelligence System.

All agents inherit from BaseAgent which provides common functionality
for search, report generation, and result tracking.
"""

import asyncio
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional

from vendor_intelligence.config import AnalysisConfig
from vendor_intelligence.utils.web_search import WebSearchClient, SearchResult
from vendor_intelligence.utils.report_writer import ReportWriter, format_timestamp

logger = logging.getLogger(__name__)


@dataclass
class AgentResult:
    """Result from an agent execution."""
    agent_name: str
    agent_number: int
    status: str  # "success", "partial", "failed"
    output_path: Optional[str] = None
    report_content: str = ""
    data: dict = field(default_factory=dict)
    sources: list = field(default_factory=list)
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    duration_seconds: float = 0.0


class BaseAgent(ABC):
    """
    Abstract base class for all intelligence agents.

    Provides common functionality:
    - Web search capabilities
    - Report writing
    - Progress tracking
    - Error handling
    - Source management
    """

    agent_number: int = 0
    agent_name: str = "BaseAgent"
    output_folder: str = ""

    def __init__(
        self,
        config: AnalysisConfig,
        search_client: WebSearchClient,
        report_writer: ReportWriter,
    ):
        self.config = config
        self.search_client = search_client
        self.report_writer = report_writer
        self.sources: list[dict] = []
        self.warnings: list[str] = []
        self.errors: list[str] = []
        self._start_time: Optional[datetime] = None

    async def execute(self) -> AgentResult:
        """
        Execute the agent's analysis workflow.

        Returns:
            AgentResult with status, output path, and collected data
        """
        self._start_time = datetime.now()
        logger.info(
            f"Agent {self.agent_number} ({self.agent_name}): Starting execution"
        )

        try:
            report_content, data = await self.run_analysis()

            output_path = None
            if report_content and self.output_folder:
                filename = self._generate_filename()
                output_path = self.report_writer.write_report(
                    folder=self.output_folder,
                    filename=filename,
                    content=report_content,
                )

            end_time = datetime.now()
            duration = (end_time - self._start_time).total_seconds()

            status = "success"
            if self.errors:
                status = "partial" if report_content else "failed"

            result = AgentResult(
                agent_name=self.agent_name,
                agent_number=self.agent_number,
                status=status,
                output_path=output_path,
                report_content=report_content,
                data=data,
                sources=self.sources.copy(),
                errors=self.errors.copy(),
                warnings=self.warnings.copy(),
                start_time=self._start_time.isoformat(),
                end_time=end_time.isoformat(),
                duration_seconds=duration,
            )

            logger.info(
                f"Agent {self.agent_number} ({self.agent_name}): "
                f"Completed with status={status} in {duration:.1f}s"
            )
            return result

        except Exception as e:
            logger.error(
                f"Agent {self.agent_number} ({self.agent_name}): "
                f"Fatal error: {e}"
            )
            end_time = datetime.now()
            duration = (end_time - self._start_time).total_seconds()
            return AgentResult(
                agent_name=self.agent_name,
                agent_number=self.agent_number,
                status="failed",
                errors=[str(e)],
                start_time=self._start_time.isoformat(),
                end_time=end_time.isoformat(),
                duration_seconds=duration,
            )

    @abstractmethod
    async def run_analysis(self) -> tuple[str, dict]:
        """
        Run the agent's specific analysis.

        Returns:
            Tuple of (report_content_markdown, structured_data_dict)
        """
        ...

    async def search(
        self,
        query: str,
        num_results: int = 10,
        date_range: Optional[str] = None,
        site_filter: Optional[str] = None,
    ) -> list[SearchResult]:
        """Execute a web search and track the query."""
        results = await self.search_client.search(
            query, num_results, date_range, site_filter
        )
        return results

    async def search_batch(
        self,
        queries: list[str],
        num_results: int = 10,
        date_range: Optional[str] = None,
    ) -> dict[str, list[SearchResult]]:
        """Execute multiple searches concurrently."""
        return await self.search_client.search_multiple(
            queries, num_results, date_range
        )

    def add_source(
        self,
        title: str,
        url: str,
        source_type: str = "web",
        access_date: Optional[str] = None,
    ) -> None:
        """Track a source used in the analysis."""
        self.sources.append({
            "title": title,
            "url": url,
            "type": source_type,
            "access_date": access_date or format_timestamp().split(" ")[0],
        })

    def add_warning(self, message: str) -> None:
        """Record a warning."""
        self.warnings.append(message)
        logger.warning(
            f"Agent {self.agent_number} ({self.agent_name}): {message}"
        )

    def add_error(self, message: str) -> None:
        """Record an error."""
        self.errors.append(message)
        logger.error(
            f"Agent {self.agent_number} ({self.agent_name}): {message}"
        )

    def _generate_filename(self) -> str:
        """Generate a report filename."""
        safe_vendor = self.config.vendor_name.replace(" ", "_")
        return f"{safe_vendor}_{self.agent_name.replace(' ', '_')}.md"
