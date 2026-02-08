"""
Web search and content fetching utilities.

Provides async web search and page fetching capabilities
for the agent system. Supports multiple search strategies
and content extraction.
"""

import asyncio
import json
import logging
import re
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from urllib.parse import quote_plus, urlparse

logger = logging.getLogger(__name__)


@dataclass
class SearchResult:
    """A single search result."""
    title: str
    url: str
    snippet: str
    source: str = ""
    timestamp: Optional[str] = None
    relevance_score: float = 0.0


@dataclass
class WebPage:
    """Fetched web page content."""
    url: str
    title: str
    content: str
    fetch_date: str = field(default_factory=lambda: datetime.now().isoformat())
    status: str = "success"
    error: Optional[str] = None


class WebSearchClient:
    """
    Async web search client that abstracts search provider details.

    In production, this connects to search APIs (Google, Bing, etc.).
    For Claude Code integration, it generates structured search queries
    that the orchestrator executes via Claude's web search capabilities.
    """

    def __init__(self, rate_limit_delay: float = 1.0):
        self.rate_limit_delay = rate_limit_delay
        self._search_cache: dict[str, list[SearchResult]] = {}
        self._page_cache: dict[str, WebPage] = {}

    async def search(
        self,
        query: str,
        num_results: int = 10,
        date_range: Optional[str] = None,
        site_filter: Optional[str] = None,
    ) -> list[SearchResult]:
        """
        Execute a web search query.

        Args:
            query: Search query string
            num_results: Maximum number of results to return
            date_range: Optional date filter (e.g., "2025-2026")
            site_filter: Optional site restriction (e.g., "g2.com")

        Returns:
            List of SearchResult objects
        """
        full_query = self._build_query(query, date_range, site_filter)
        cache_key = f"{full_query}:{num_results}"

        if cache_key in self._search_cache:
            logger.debug(f"Cache hit for query: {full_query}")
            return self._search_cache[cache_key]

        logger.info(f"Searching: {full_query}")
        results = await self._execute_search(full_query, num_results)

        self._search_cache[cache_key] = results
        await asyncio.sleep(self.rate_limit_delay)

        return results

    async def fetch_page(self, url: str) -> WebPage:
        """
        Fetch and extract content from a web page.

        Args:
            url: URL to fetch

        Returns:
            WebPage object with extracted content
        """
        if url in self._page_cache:
            return self._page_cache[url]

        logger.info(f"Fetching: {url}")
        page = await self._execute_fetch(url)
        self._page_cache[url] = page
        await asyncio.sleep(self.rate_limit_delay)

        return page

    async def search_multiple(
        self,
        queries: list[str],
        num_results: int = 10,
        date_range: Optional[str] = None,
    ) -> dict[str, list[SearchResult]]:
        """
        Execute multiple search queries concurrently.

        Args:
            queries: List of search query strings
            num_results: Max results per query
            date_range: Optional date filter

        Returns:
            Dict mapping query -> results
        """
        tasks = [
            self.search(q, num_results, date_range)
            for q in queries
        ]
        results_list = await asyncio.gather(*tasks, return_exceptions=True)

        results = {}
        for query, result in zip(queries, results_list):
            if isinstance(result, Exception):
                logger.error(f"Search failed for '{query}': {result}")
                results[query] = []
            else:
                results[query] = result

        return results

    def _build_query(
        self,
        query: str,
        date_range: Optional[str] = None,
        site_filter: Optional[str] = None,
    ) -> str:
        """Build a complete search query with filters."""
        parts = [query]
        if date_range:
            parts.append(date_range)
        if site_filter:
            parts.insert(0, f"site:{site_filter}")
        return " ".join(parts)

    async def _execute_search(
        self, query: str, num_results: int
    ) -> list[SearchResult]:
        """
        Execute search via available provider.

        This method is designed to be overridden by specific implementations.
        The base implementation returns a structured query descriptor that
        the Claude Code orchestrator processes via its web search tool.
        """
        return [
            SearchResult(
                title=f"[Search Required] {query}",
                url="",
                snippet=f"Execute web search for: {query}",
                source="pending",
            )
        ]

    async def _execute_fetch(self, url: str) -> WebPage:
        """
        Fetch page content.

        Base implementation returns a fetch descriptor for the orchestrator.
        """
        return WebPage(
            url=url,
            title="[Fetch Required]",
            content=f"Fetch content from: {url}",
            status="pending",
        )

    def generate_search_plan(
        self,
        vendor_name: str,
        search_type: str = "market_research",
    ) -> list[str]:
        """
        Generate a comprehensive list of search queries for a vendor analysis.

        Args:
            vendor_name: Name of the vendor to research
            search_type: Type of research to conduct

        Returns:
            List of search query strings
        """
        queries = []

        if search_type == "market_research":
            queries = [
                f"{vendor_name} company overview data security",
                f"{vendor_name} competitors comparison 2025 2026",
                f"{vendor_name} market position data security",
                f"Gartner Magic Quadrant data security 2025",
                f"Forrester Wave data security 2025 2026",
                f"{vendor_name} funding acquisitions 2025",
                f"data security market trends 2025 2026",
                f"DLP DSPM SSPM CASB market analysis 2025",
                f"SMB enterprise data security challenges 2025",
                f"{vendor_name} partnerships integrations",
                f"data security market size growth 2025 2026",
                f"{vendor_name} pricing model",
                f"cloud data security competitive landscape 2025",
                f"data security regulatory drivers GDPR CCPA 2025",
                f"zero trust data security trends 2026",
            ]
        elif search_type == "reviews":
            queries = [
                f"{vendor_name} reviews G2 2024 2025",
                f"{vendor_name} reviews Gartner Peer Insights",
                f"{vendor_name} reviews TrustRadius",
                f"{vendor_name} reviews Capterra",
                f"{vendor_name} customer complaints",
                f"{vendor_name} reddit review cybersecurity",
                f"{vendor_name} feature requests",
                f"{vendor_name} customer experience",
                f"{vendor_name} vs competitors review",
                f"{vendor_name} pros cons user review",
            ]
        elif search_type == "product_docs":
            queries = [
                f"{vendor_name} official documentation",
                f"{vendor_name} product features",
                f"{vendor_name} release notes latest 2025",
                f"{vendor_name} API documentation",
                f"{vendor_name} architecture technical",
                f"{vendor_name} deployment guide",
                f"{vendor_name} integration guide",
                f"{vendor_name} compliance certifications SOC2",
                f"{vendor_name} admin guide",
                f"{vendor_name} use cases data security",
            ]
        elif search_type == "ai_ml":
            queries = [
                f"{vendor_name} AI technology",
                f"{vendor_name} machine learning capabilities",
                f"{vendor_name} large language model LLM",
                f"{vendor_name} artificial intelligence architecture",
                f"{vendor_name} ML model detection",
                f"{vendor_name} AI research paper",
                f"{vendor_name} NLP natural language processing",
                f"{vendor_name} anomaly detection AI",
                f"{vendor_name} predictive analytics",
                f"{vendor_name} neural network deep learning",
                f"{vendor_name} GitHub machine learning",
                f"{vendor_name} AI whitepaper",
                f"{vendor_name} generative AI security",
                f"{vendor_name} AI patent",
                f"{vendor_name} GPT BERT transformer model",
            ]

        return queries


def extract_domain(url: str) -> str:
    """Extract domain from URL."""
    try:
        parsed = urlparse(url)
        return parsed.netloc
    except Exception:
        return ""


def is_authoritative_source(url: str) -> bool:
    """Check if a URL is from an authoritative source."""
    authoritative_domains = {
        "gartner.com", "forrester.com", "idc.com",
        "g2.com", "trustradius.com", "capterra.com",
        "darkreading.com", "csoonline.com",
        "techcrunch.com", "venturebeat.com",
        "securityweek.com", "scmagazine.com",
        "peerspot.com", "linkedin.com",
        "github.com", "arxiv.org",
    }
    domain = extract_domain(url).lower()
    return any(auth in domain for auth in authoritative_domains)


def sanitize_filename(name: str) -> str:
    """Sanitize a string for use as a filename."""
    return re.sub(r'[^\w\s-]', '', name).strip().replace(' ', '_')
