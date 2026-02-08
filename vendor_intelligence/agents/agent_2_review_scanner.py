"""
Agent 2: Review Intelligence Scanner

Execution: Parallel (after Agent 3)
Output: 02_Customer_Reviews_Analysis/ folder

Scans, aggregates, and analyzes customer reviews to identify
pain points, satisfaction gaps, and feature requests.
"""

import logging
from typing import Optional

from vendor_intelligence.agents.base import BaseAgent
from vendor_intelligence.config import (
    REVIEW_PLATFORMS,
    SECONDARY_REVIEW_SOURCES,
    PAIN_POINT_CATEGORIES,
    CRITICAL_MENTION_THRESHOLD,
    COMMON_MENTION_THRESHOLD,
)
from vendor_intelligence.utils.report_writer import (
    format_timestamp,
    format_table,
    format_section,
    format_source_citation,
)

logger = logging.getLogger(__name__)


class ReviewScannerAgent(BaseAgent):
    """
    Agent 2: Review Intelligence Scanner

    Responsibilities:
    - Scan major review platforms (G2, Gartner Peer Insights, TrustRadius, etc.)
    - Analyze sentiment by customer segment
    - Identify critical and common pain points
    - Extract feature requests with frequency
    - Document competitive mentions in reviews
    - Track unsatisfied customers and churn indicators
    """

    agent_number = 2
    agent_name = "Review_Intelligence"
    output_folder = "02_Customer_Reviews_Analysis"

    async def run_analysis(self) -> tuple[str, dict]:
        """
        Execute review intelligence scanning and analysis.

        Returns:
            Tuple of (markdown_report, structured_data)
        """
        vendor = self.config.vendor_name

        # Step 1: Build search queries for all review platforms
        search_queries = self._build_review_search_queries(vendor)

        # Step 2: Initialize analysis structure
        review_data = self._initialize_review_data(vendor)

        # Step 3: Build pain point analysis framework
        pain_points = self._build_pain_point_framework()

        # Step 4: Build feature request framework
        feature_requests = self._build_feature_request_framework()

        # Step 5: Build competitive mention tracking
        competitive_mentions = self._build_competitive_mention_framework()

        # Compile all data
        data = {
            "vendor_name": vendor,
            "search_queries": search_queries,
            "review_data": review_data,
            "pain_points": pain_points,
            "feature_requests": feature_requests,
            "competitive_mentions": competitive_mentions,
            "platforms_to_scan": [p["name"] for p in REVIEW_PLATFORMS],
            "secondary_sources": [s["name"] for s in SECONDARY_REVIEW_SOURCES],
            "analysis_period_months": self.config.review_months,
        }

        # Generate report
        report = self._generate_report(data)

        return report, data

    def _build_review_search_queries(self, vendor: str) -> list[str]:
        """Build comprehensive review search queries."""
        queries = []

        # Primary platform queries
        for platform in REVIEW_PLATFORMS:
            queries.append(f"{vendor} {platform['search_suffix']}")

        # Pain point queries
        queries.extend([
            f"{vendor} customer complaints issues",
            f"{vendor} problems drawbacks cons",
            f"{vendor} feature requests wishlist",
            f"{vendor} customer experience feedback",
            f"{vendor} user review 2024 2025",
        ])

        # Secondary source queries
        for source in SECONDARY_REVIEW_SOURCES:
            if source["name"] == "Reddit":
                for sub in source["subreddits"]:
                    queries.append(f"site:reddit.com r/{sub} {vendor}")
            else:
                queries.append(f"{vendor} {source['search_suffix']}")

        # Competitor comparison queries
        queries.extend([
            f"{vendor} vs alternative comparison review",
            f"{vendor} switching from migration",
            f"{vendor} replaced by competitor",
        ])

        return queries

    def _initialize_review_data(self, vendor: str) -> dict:
        """Initialize the review data collection structure."""
        return {
            "total_reviews_analyzed": 0,
            "analysis_period": {
                "months": self.config.review_months,
                "note": f"Last {self.config.review_months} months rolling from current date",
            },
            "overall_sentiment": {
                "average_rating": 0.0,
                "rating_distribution": {
                    "5_star": {"count": 0, "percentage": 0.0},
                    "4_star": {"count": 0, "percentage": 0.0},
                    "3_star": {"count": 0, "percentage": 0.0},
                    "2_star": {"count": 0, "percentage": 0.0},
                    "1_star": {"count": 0, "percentage": 0.0},
                },
                "trend": "To be determined",
            },
            "sentiment_by_segment": {
                "smb": {
                    "avg_rating": 0.0,
                    "sample_size": 0,
                    "trend": "TBD",
                },
                "mid_market": {
                    "avg_rating": 0.0,
                    "sample_size": 0,
                    "trend": "TBD",
                },
                "enterprise": {
                    "avg_rating": 0.0,
                    "sample_size": 0,
                    "trend": "TBD",
                },
            },
            "platforms_analyzed": {
                platform["name"]: {
                    "reviews_found": 0,
                    "avg_rating": 0.0,
                    "url": f"[To be populated from search for {vendor} on {platform['name']}]",
                }
                for platform in REVIEW_PLATFORMS
            },
        }

    def _build_pain_point_framework(self) -> dict:
        """Build the pain point analysis framework."""
        categories = {}
        for cat in PAIN_POINT_CATEGORIES:
            categories[cat] = {
                "mention_count": 0,
                "severity": "Low",
                "affects_segment": "TBD",
                "sample_quotes": [],
                "related_features": [],
            }

        return {
            "categories": categories,
            "severity_thresholds": {
                "critical": f"Mentioned {CRITICAL_MENTION_THRESHOLD}+ times",
                "common": f"Mentioned {COMMON_MENTION_THRESHOLD}-{CRITICAL_MENTION_THRESHOLD-1} times",
                "isolated": f"Mentioned fewer than {COMMON_MENTION_THRESHOLD} times",
            },
            "analysis_template": {
                "issue_name": "[Identified from reviews]",
                "mention_count": 0,
                "impact_area": "[Performance/Cost/Usability/etc.]",
                "affects_segment": "[SMB/Enterprise/Both]",
                "customer_quotes": [],
                "severity": "[Critical/Common/Isolated]",
            },
        }

    def _build_feature_request_framework(self) -> dict:
        """Build the feature request tracking framework."""
        return {
            "request_tracking": {
                "total_unique_requests": 0,
                "requests_by_priority": {
                    "high": [],
                    "medium": [],
                    "low": [],
                },
            },
            "request_template": {
                "feature_name": "[Feature]",
                "request_count": 0,
                "requesting_segment": "[SMB/Enterprise/Both]",
                "urgency": "[High/Medium/Low]",
                "use_case": "[Why customers want it]",
                "customer_quote": "[Verbatim]",
                "competitive_context": "[Which competitors have this]",
                "ai_related": False,
            },
            "common_request_categories": [
                "AI/ML Capabilities",
                "Integration Connectors",
                "Reporting & Dashboards",
                "Policy Management",
                "Automation & Orchestration",
                "Cloud Platform Support",
                "Compliance Features",
                "User Experience Improvements",
                "API Enhancements",
                "Performance Improvements",
            ],
        }

    def _build_competitive_mention_framework(self) -> dict:
        """Build competitive mention tracking framework."""
        return {
            "tracking_template": {
                "competitor_name": "[Name]",
                "mention_count": 0,
                "context": "[Switching to/from, comparison, etc.]",
                "differentiators_mentioned": [],
                "switching_direction": "[To competitor / From competitor]",
            },
            "switching_analysis": {
                "switched_to": [],
                "switched_from": [],
                "compared_with": [],
            },
        }

    def _generate_report(self, data: dict) -> str:
        """Generate the full Markdown review intelligence report."""
        vendor = data["vendor_name"]
        review = data["review_data"]
        period = data["analysis_period_months"]

        lines = [
            f"# Customer Review Intelligence: {vendor}",
            f"**Analysis Period:** Last {period} months (rolling from current date)",
            f"**Total Reviews Analyzed:** [To be populated during orchestration]",
            f"**Sources:** {len(data['platforms_to_scan'])} primary platforms + "
            f"{len(data['secondary_sources'])} secondary sources",
            f"**Generated:** {format_timestamp()}",
            "",
            "---",
            "",
            "## Executive Summary",
            "",
            f"This report aggregates and analyzes customer reviews of {vendor} "
            f"from {len(data['platforms_to_scan'])} major review platforms and "
            f"{len(data['secondary_sources'])} secondary sources over the last "
            f"{period} months. The analysis identifies critical pain points, "
            f"satisfaction trends, feature requests, and competitive intelligence "
            f"from the customer voice.",
            "",
            "**Key Findings:**",
            "- **Critical Issues:** [To be identified from review analysis]",
            "- **Common Complaints:** [To be identified from review analysis]",
            "- **Most Requested Features:** [To be identified from review analysis]",
            "- **Satisfaction Trend:** [To be determined from review analysis]",
            "",
            "---",
            "",
            "## Overall Sentiment Analysis",
            "",
            "### Rating Distribution",
            "",
            "| Rating | Count | Percentage |",
            "|--------|-------|------------|",
            "| 5 stars | [Count] | [X%] |",
            "| 4 stars | [Count] | [X%] |",
            "| 3 stars | [Count] | [X%] |",
            "| 2 stars | [Count] | [X%] |",
            "| 1 star  | [Count] | [X%] |",
            "",
            "**Average Rating:** [X.X] / 5.0",
            "",
            "### Sentiment by Customer Segment",
            "",
        ]

        # Segment sentiment table
        headers = ["Segment", "Avg Rating", "Sample Size", "Trend"]
        rows = [
            ["SMB (<500 employees)", "[X.X]/5", "[N] reviews", "[TBD]"],
            ["Mid-Market (500-5000)", "[X.X]/5", "[N] reviews", "[TBD]"],
            ["Enterprise (>5000)", "[X.X]/5", "[N] reviews", "[TBD]"],
        ]
        lines.append(format_table(headers, rows))

        # Pain Points section
        lines.extend([
            "",
            "---",
            "",
            "## Pain Points Analysis",
            "",
            "### Analysis Framework",
            "",
            f"Issues are categorized by frequency of mention:",
            f"- **Critical:** Mentioned {CRITICAL_MENTION_THRESHOLD}+ times across reviews",
            f"- **Common:** Mentioned {COMMON_MENTION_THRESHOLD}-{CRITICAL_MENTION_THRESHOLD-1} times",
            f"- **Isolated:** Mentioned fewer than {COMMON_MENTION_THRESHOLD} times",
            "",
            "### Pain Point Categories Tracked",
            "",
        ])

        for cat in PAIN_POINT_CATEGORIES:
            lines.append(f"- **{cat}**")

        lines.extend([
            "",
            "### Critical Issues (Mentioned 10+ times)",
            "",
            "*To be populated from review analysis during orchestration.*",
            "",
            "**Template for each critical issue:**",
            "",
            "**[Issue Name]** - Mentioned [X] times",
            "- **Impact:** [Performance/Cost/Usability/etc.]",
            "- **Affects:** [SMB/Enterprise/Both]",
            "- **Customer Quote:** \"[Verbatim quote]\" - [Source, Date]",
            "- **Example Reviews:**",
            "  - \"[Quote]\" - [Company size], [Date], [Source]",
            "",
            "### Common Issues (Mentioned 3-9 times)",
            "",
            "*To be populated from review analysis during orchestration.*",
            "",
            "### Issue Category Breakdown",
            "",
        ])

        # Issue category table
        headers = ["Category", "Count", "% of Total", "Severity"]
        rows = [[cat, "[X]", "[X%]", "[TBD]"] for cat in PAIN_POINT_CATEGORIES]
        lines.append(format_table(headers, rows))

        # Unsatisfied Customers
        lines.extend([
            "",
            "---",
            "",
            "## Unsatisfied Customers Deep Dive",
            "",
            "### Low-Rated Reviews (3 stars or below)",
            "**Count:** [X] reviews ([X%] of total)",
            "",
            "**Top Reasons for Dissatisfaction:**",
            "*To be populated from review analysis during orchestration.*",
            "",
            "### Churn Indicators",
            "**Customers Who Switched:**",
            "*To be populated from review analysis during orchestration.*",
            "",
        ])

        # Feature Requests
        lines.extend([
            "---",
            "",
            "## Feature Requests",
            "",
            "### Most Requested Features",
            "",
        ])

        headers = ["Feature", "Request Count", "Segment", "Urgency", "AI-Related"]
        rows = [
            ["[Feature name]", "[X]", "[SMB/Enterprise/Both]", "[High/Med/Low]", "[Y/N]"],
        ]
        lines.append(format_table(headers, rows))

        lines.extend([
            "",
            "*To be populated from review analysis during orchestration.*",
            "",
            "### Feature Request Categories",
            "",
        ])
        for cat in data["feature_requests"]["common_request_categories"]:
            lines.append(f"- {cat}")

        # Competitive Mentions
        lines.extend([
            "",
            "---",
            "",
            "## Competitive Mentions in Reviews",
            "",
            "### Comparison Context",
            "",
            "*To be populated from review analysis during orchestration.*",
            "",
            "**Template:**",
            "",
            "**[Competitor Name]:**",
            "- Mentioned in [X] reviews",
            "- Context: [Switching to/from, feature comparison, etc.]",
            "- Key Differentiators mentioned: [List]",
            "",
        ])

        # Platform Breakdown
        lines.extend([
            "---",
            "",
            "## Platform-by-Platform Breakdown",
            "",
        ])

        for platform in REVIEW_PLATFORMS:
            lines.extend([
                f"### {platform['name']}",
                f"- **Reviews Analyzed:** [To be populated]",
                f"- **Average Rating:** [X.X]/5",
                f"- **Search Query:** `{vendor} {platform['search_suffix']}`",
                f"- **URL Pattern:** {platform['url_pattern']}",
                f"- **Top Issues:** [To be populated]",
                "",
            ])

        # Secondary Sources
        lines.extend(["### Secondary Sources", ""])
        for source in SECONDARY_REVIEW_SOURCES:
            lines.extend([
                f"**{source['name']}:**",
                f"- **Discussions Found:** [To be populated]",
            ])
            if source["name"] == "Reddit":
                for sub in source["subreddits"]:
                    lines.append(f"  - r/{sub}: [X] relevant posts")
            lines.append("")

        # Search Queries for Orchestrator
        lines.extend([
            "---",
            "",
            "## Search Queries for Enrichment",
            "",
            "The following queries should be executed during orchestration:",
            "",
        ])
        for query in data["search_queries"]:
            lines.append(f"- `{query}`")

        # Sources
        lines.extend([
            "",
            "---",
            "",
            "## Sources & Review References",
            "",
            "### Review Platform Summary",
            "",
        ])

        for i, platform in enumerate(REVIEW_PLATFORMS, 1):
            lines.append(
                f"{i}. **{platform['name']}** - [X] reviews - "
                f"[URL] - Accessed [Date]"
            )

        lines.extend([
            "",
            "### Notable Reviews (Full References)",
            "*To be populated with timestamped references during orchestration.*",
        ])

        return "\n".join(lines)
