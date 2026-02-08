"""
Agent 7: Executive Summary Generator

Execution: Sequential (RUNS LAST)
Output: 06_Executive_Summary/ folder

Creates a concise, one-page executive summary synthesizing
all insights from Agents 1-6 for senior leadership.
"""

import logging
from typing import Optional

from vendor_intelligence.agents.base import BaseAgent, AgentResult
from vendor_intelligence.utils.report_writer import format_timestamp

logger = logging.getLogger(__name__)


class ExecutiveSummaryAgent(BaseAgent):
    """
    Agent 7: Executive Summary Generator

    Responsibilities:
    - Synthesize all agent outputs into one-page summary
    - Highlight top 3 strategic priorities
    - Summarize AI/ML positioning
    - Provide clear action items
    - Link to detailed analysis documents
    - Optimize for <5 minute executive reading
    """

    agent_number = 7
    agent_name = "Executive_Summary"
    output_folder = "06_Executive_Summary"

    def __init__(self, *args, agent_results: Optional[dict] = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.agent_results = agent_results or {}

    async def run_analysis(self) -> tuple[str, dict]:
        """
        Generate executive summary from all agent outputs.

        Returns:
            Tuple of (markdown_report, structured_data)
        """
        vendor = self.config.vendor_name

        # Extract data from all agents
        agent_1_data = self._extract_agent_data("agent_1")
        agent_2_data = self._extract_agent_data("agent_2")
        agent_4_data = self._extract_agent_data("agent_4")
        agent_5_data = self._extract_agent_data("agent_5")
        agent_6_data = self._extract_agent_data("agent_6")

        # Build executive summary data
        summary_data = self._build_summary(
            vendor, agent_1_data, agent_2_data,
            agent_4_data, agent_5_data, agent_6_data
        )

        # Generate report
        report = self._generate_report(summary_data)

        return report, summary_data

    def _extract_agent_data(self, agent_key: str) -> Optional[dict]:
        """Extract data from a previous agent's result."""
        agent_result = self.agent_results.get(agent_key)
        if not agent_result:
            return None
        if isinstance(agent_result, AgentResult):
            return agent_result.data
        return agent_result

    def _build_summary(
        self,
        vendor: str,
        agent_1_data: Optional[dict],
        agent_2_data: Optional[dict],
        agent_4_data: Optional[dict],
        agent_5_data: Optional[dict],
        agent_6_data: Optional[dict],
    ) -> dict:
        """Build the executive summary data structure."""
        # Extract key metrics
        competitor_count = 0
        category = "Data Security"
        if agent_1_data:
            competitor_count = len(agent_1_data.get("competitors", []))
            category = agent_1_data.get("detected_category", "Data Security")

        # QA score
        qa_score = "N/A"
        qa_reliability = "N/A"
        if agent_5_data:
            qa_score = agent_5_data.get("quality_score", "N/A")
            if isinstance(qa_score, (int, float)):
                qa_reliability = (
                    "High" if qa_score >= 80
                    else "Medium" if qa_score >= 60
                    else "Low"
                )

        # Competitor summary
        top_competitors = []
        if agent_1_data:
            competitors = agent_1_data.get("competitors", [])
            leaders = [c for c in competitors if c.get("market_position") == "Leader"]
            top_competitors = leaders[:5] if leaders else competitors[:5]

        # Market trends
        market_trends = []
        if agent_1_data:
            market = agent_1_data.get("market_landscape", {})
            market_trends = market.get("trends_2025_2026", [])[:3]

        # AI capabilities to assess from gap analysis
        ai_capabilities = []
        if agent_6_data:
            ai_gaps = agent_6_data.get("ai_ml_gaps", {})
            ai_capabilities = ai_gaps.get("ai_capabilities_to_assess", [])[:3]

        return {
            "vendor_name": vendor,
            "category": category,
            "competitor_count": competitor_count,
            "top_competitors": top_competitors,
            "qa_score": qa_score,
            "qa_reliability": qa_reliability,
            "market_trends": market_trends,
            "ai_capabilities": ai_capabilities,
            "agent_outputs": {
                "agent_1": bool(agent_1_data),
                "agent_2": bool(agent_2_data),
                "agent_4": bool(agent_4_data),
                "agent_5": bool(agent_5_data),
                "agent_6": bool(agent_6_data),
            },
        }

    def _generate_report(self, data: dict) -> str:
        """Generate the one-page executive summary."""
        vendor = data["vendor_name"]
        category = data["category"]
        qa_score = data["qa_score"]
        qa_rel = data["qa_reliability"]

        lines = [
            f"# Executive Summary: {vendor} Competitive Intelligence",
            f"**Date:** {format_timestamp()}",
            f"**Prepared For:** CPO / VP Product / Senior Product Management",
            f"**Analysis Scope:** Market Research | Customer Intelligence | "
            f"Product Analysis | AI/ML Assessment | Gap Assessment",
            f"**Data Quality:** {qa_rel} (Agent 5 Score: {qa_score}/100)",
            "",
            "---",
            "",
            "## SITUATION AT A GLANCE",
            "",
            f"**Vendor:** {vendor}",
            f"**Category:** {category} (Auto-detected)",
            "**Market Position:** [To be determined from analysis]",
            "**AI/ML Maturity:** [To be assessed from Agent 4 analysis]",
            "**Primary Products:** [From Agent 4 product portfolio]",
            "",
            "**Key Metrics:**",
            f"- **Major Competitors:** {data['competitor_count']} identified",
            "- **Customer Reviews Analyzed:** [From Agent 2]",
            "- **Avg Customer Rating:** [From Agent 2] / 5.0",
            "- **Critical Product Gaps:** [From Agent 6]",
            "- **Sources Validated:** [From Agent 5]",
            "",
            "---",
            "",
            "## STRATEGIC HIGHLIGHTS (Top 3)",
            "",
            "### 1. [Most Critical Finding]",
            "**Impact:** [Revenue/Market Share/Competitive/Customer Satisfaction]",
            "**Key Insight:** [To be populated from analysis synthesis]",
            "**AI-Related:** [Yes/No]",
            "**Action Required:** [Specific recommendation]",
            "",
            "### 2. [Second Most Important]",
            "**Impact:** [Type]",
            "**Key Insight:** [To be populated]",
            "**Action Required:** [Recommendation]",
            "",
            "### 3. [Third Priority]",
            "**Impact:** [Type]",
            "**Key Insight:** [To be populated]",
            "**Action Required:** [Recommendation]",
            "",
            "*Strategic highlights will be synthesized from all agent "
            "outputs during orchestration.*",
            "",
            "---",
            "",
            "## COMPETITIVE LANDSCAPE",
            "",
            f"**Market Dynamics (2025-2026):**",
        ]

        # Add market trends
        if data["market_trends"]:
            for trend in data["market_trends"]:
                lines.append(
                    f"- {trend.get('trend', 'N/A')}: "
                    f"{trend.get('description', 'N/A')} "
                    f"(Impact: {trend.get('impact', 'N/A')})"
                )
        else:
            lines.append("- [To be populated from Agent 1 analysis]")

        lines.extend([
            "",
            "**Top Competitors:**",
        ])

        if data["top_competitors"]:
            for i, comp in enumerate(data["top_competitors"], 1):
                lines.append(
                    f"{i}. **{comp['name']}** - "
                    f"{comp.get('market_position', 'TBD')} - "
                    f"Target: {comp.get('target_segment', 'TBD')}"
                )
        else:
            lines.append("- [To be populated from Agent 1 analysis]")

        lines.extend([
            "",
            "**Vendor's Competitive Position:**",
            "- **Strengths:** [From Agent 4 product analysis]",
            "- **Weaknesses:** [From Agent 6 gap analysis]",
            "",
            "---",
            "",
            "## CUSTOMER VOICE",
            "",
            "**Satisfaction Overview:**",
            "- **Overall Rating:** [From Agent 2] / 5",
            "- **Sentiment:** [From Agent 2]",
            "",
            "**Top Customer Pain Points:**",
            "1. [From Agent 2 critical issues]",
            "2. [From Agent 2 common issues]",
            "3. [From Agent 2 common issues]",
            "",
            "**Most Requested Features:**",
            "1. [From Agent 2 feature requests]",
            "2. [From Agent 2 feature requests]",
            "3. [From Agent 2 feature requests]",
            "",
            "---",
            "",
            "## AI/ML POSITION",
            "",
            "**Current AI Capabilities:**",
            "- **AI Maturity:** [From Agent 4 AI/ML deep dive]",
            "- **Key AI Technologies:** [From Agent 4]",
            "- **AI Differentiators:** [From Agent 4]",
            "",
            "**AI Competitive Gap:**",
            "- **Critical AI Gaps:** [From Agent 6 AI/ML gaps]",
            "- **AI Market Position:** [From Agent 6 assessment]",
            "",
        ])

        if data["ai_capabilities"]:
            lines.append("**Key AI Capabilities Assessed:**")
            for cap in data["ai_capabilities"]:
                lines.append(
                    f"- {cap.get('capability', 'N/A')} "
                    f"(Importance: {cap.get('competitive_importance', 'N/A')})"
                )
            lines.append("")

        lines.extend([
            "---",
            "",
            "## CRITICAL GAPS & PRIORITIES",
            "",
            "### Immediate Action Required (Critical)",
            "",
            "**Gap #1:** [From Agent 6 critical gaps]",
            "- **Why Critical:** [Impact]",
            "- **Competitors Have It:** [Count]",
            "- **AI-Related:** [Yes/No]",
            "",
            "**Gap #2:** [From Agent 6 critical gaps]",
            "- [Condensed format]",
            "",
            "### High-Priority Opportunities",
            "- [From Agent 6 high-priority gaps]",
            "- [To be populated during orchestration]",
            "",
            "---",
            "",
            "## TECHNOLOGY & MARKET TRENDS (2025-2026)",
            "",
            "**Emerging Trends Impacting Category:**",
        ])

        if data["market_trends"]:
            for trend in data["market_trends"]:
                lines.append(
                    f"- **{trend.get('trend', 'N/A')}** - "
                    f"Vendor readiness: [To be assessed]"
                )
        else:
            lines.append("- [To be populated from analysis]")

        lines.extend([
            "",
            "---",
            "",
            "## BUSINESS IMPACT ASSESSMENT",
            "",
            "**Market Opportunities:**",
            "- [From gap analysis]",
            "",
            "**At-Risk Areas:**",
            "- [From gap analysis]",
            "",
            "**Revenue Implications:**",
            "- **Potential Upside:** [If gaps closed]",
            "- **Downside Risk:** [If gaps persist]",
            "",
            "---",
            "",
            "## RECOMMENDED ACTIONS",
            "",
            "### Week 1 (Immediate):",
            "- [ ] Review Critical Gap #1 with engineering team",
            "- [ ] Assess AI/ML investment priorities vs competitors",
            "- [ ] Share this report with product leadership",
            "",
            "### Month 1 (Short-term):",
            "- [ ] Develop gap closure roadmap",
            "- [ ] Prioritize customer-requested features",
            "- [ ] Evaluate AI/ML build vs buy decisions",
            "",
            "### Quarter 1 (Medium-term):",
            "- [ ] Execute roadmap prioritization including AI",
            "- [ ] Adjust market positioning based on gaps",
            "- [ ] Plan competitive response strategy",
            "",
            "---",
            "",
            "## SUPPORTING DOCUMENTATION",
            "",
            "**Detailed Analysis Available:**",
            "",
        ])

        # Document links
        docs = [
            ("01_Market_Research", "Market Research Report (Agent 1)", "Competitive landscape and industry analysis"),
            ("02_Customer_Reviews_Analysis", "Customer Review Analysis (Agent 2)", "Sentiment analysis and pain points"),
            ("03_Product_Documentation", "Product Documentation Study (Agent 4)", "Product features and AI/ML deep dive"),
            ("04_QA_Validation_Reports", "QA Validation Report (Agent 5)", "Data quality and reliability assessment"),
            ("05_Gap_Analysis", "Gap Analysis (Agent 6)", "Competitive gaps and strategic priorities"),
        ]

        for folder, title, desc in docs:
            status = "Available" if data["agent_outputs"].get(
                f"agent_{folder[1]}", True
            ) else "Pending"
            lines.append(f"- **{title}** - {desc} [{status}]")

        lines.extend([
            "",
            f"**Data Reliability:** {qa_rel} "
            f"(QA Score: {qa_score}/100)",
            "",
            "---",
            "",
            "## IMPORTANT NOTES",
            "",
            f"**Data Currency:** Analysis based on data through {format_timestamp().split(' ')[0]}",
            "**Limitations:** Some data points require enrichment during full "
            "orchestration with live web searches",
            "**Assumptions:** Market positioning based on available public data "
            "and analyst reports",
            "",
            "---",
            "",
            "**Prepared by:** Claude Multi-Agent Intelligence System",
            f"**Last Updated:** {format_timestamp()}",
        ])

        return "\n".join(lines)
