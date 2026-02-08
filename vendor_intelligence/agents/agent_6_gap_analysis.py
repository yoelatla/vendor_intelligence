"""
Agent 6: Product Gap Analysis

Execution: Sequential (AFTER Agent 5)
Output: 05_Gap_Analysis/ folder

Identifies gaps in vendor's product offerings compared to competitors,
including comprehensive AI/ML capability gap analysis.
"""

import logging
from typing import Optional

from vendor_intelligence.agents.base import BaseAgent, AgentResult
from vendor_intelligence.config import GAP_CATEGORIES
from vendor_intelligence.utils.report_writer import (
    format_timestamp,
    format_table,
)

logger = logging.getLogger(__name__)


class GapAnalysisAgent(BaseAgent):
    """
    Agent 6: Product Gap Analysis

    Responsibilities:
    - Feature parity analysis vs competitors
    - AI/ML capability gap analysis
    - Customer-requested feature gap mapping
    - Market trend alignment assessment
    - Segment-specific gap identification (SMB/Enterprise)
    - Competitive disadvantage analysis
    - Strategic roadmap recommendations
    """

    agent_number = 6
    agent_name = "Gap_Analysis"
    output_folder = "05_Gap_Analysis"

    def __init__(self, *args, agent_results: Optional[dict] = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.agent_results = agent_results or {}

    async def run_analysis(self) -> tuple[str, dict]:
        """
        Execute product gap analysis.

        Returns:
            Tuple of (markdown_report, structured_data)
        """
        vendor = self.config.vendor_name

        # Extract data from previous agents
        agent_1_data = self._extract_agent_data("agent_1")
        agent_2_data = self._extract_agent_data("agent_2")
        agent_4_data = self._extract_agent_data("agent_4")
        agent_5_data = self._extract_agent_data("agent_5")

        # Step 1: Feature parity analysis
        feature_gaps = self._analyze_feature_parity(
            vendor, agent_1_data, agent_4_data
        )

        # Step 2: AI/ML gap analysis
        ai_ml_gaps = self._analyze_ai_ml_gaps(
            vendor, agent_1_data, agent_4_data
        )

        # Step 3: Customer-requested feature gaps
        customer_gaps = self._analyze_customer_requests(
            agent_2_data, agent_4_data
        )

        # Step 4: Market trend gaps
        trend_gaps = self._analyze_trend_alignment(
            agent_1_data, agent_4_data
        )

        # Step 5: Segment-specific gaps
        segment_gaps = self._analyze_segment_gaps(
            agent_1_data, agent_2_data, agent_4_data
        )

        # Step 6: Prioritization
        prioritized_gaps = self._prioritize_gaps(
            feature_gaps, ai_ml_gaps, customer_gaps, trend_gaps, segment_gaps
        )

        # Step 7: Strategic recommendations
        recommendations = self._build_recommendations(prioritized_gaps)

        # Compile data
        data = {
            "vendor_name": vendor,
            "feature_gaps": feature_gaps,
            "ai_ml_gaps": ai_ml_gaps,
            "customer_gaps": customer_gaps,
            "trend_gaps": trend_gaps,
            "segment_gaps": segment_gaps,
            "prioritized_gaps": prioritized_gaps,
            "recommendations": recommendations,
            "gap_categories": GAP_CATEGORIES,
            "qa_score": (
                agent_5_data.get("quality_score", "N/A")
                if agent_5_data else "N/A"
            ),
        }

        # Generate report
        report = self._generate_report(data)

        return report, data

    def _extract_agent_data(self, agent_key: str) -> Optional[dict]:
        """Extract data from a previous agent's result."""
        agent_result = self.agent_results.get(agent_key)
        if not agent_result:
            return None
        if isinstance(agent_result, AgentResult):
            return agent_result.data
        return agent_result

    def _analyze_feature_parity(
        self,
        vendor: str,
        agent_1_data: Optional[dict],
        agent_4_data: Optional[dict],
    ) -> dict:
        """Analyze feature parity between vendor and competitors."""
        gaps = {
            "total_gaps": 0,
            "critical_gaps": [],
            "high_gaps": [],
            "medium_gaps": [],
            "low_gaps": [],
            "by_category": {cat: [] for cat in GAP_CATEGORIES},
        }

        if not agent_1_data:
            gaps["note"] = "Agent 1 data not available for feature parity analysis"
            return gaps

        competitors = agent_1_data.get("competitors", [])

        # Build gap templates for each category
        for category in GAP_CATEGORIES:
            gaps["by_category"][category] = {
                "gap_count": 0,
                "gaps": [],
                "gap_template": {
                    "feature_name": "[Feature/Capability]",
                    "priority": "[Critical/High/Medium/Low]",
                    "competitors_with_feature": [],
                    "customer_demand": "[High/Medium/Low]",
                    "ai_related": False,
                    "business_impact": "[Revenue/Churn/Market Share]",
                    "implementation_complexity": "[High/Medium/Low]",
                    "recommendation": "[Action]",
                },
            }

        gaps["analysis_note"] = (
            "Feature parity analysis to be enriched during orchestration "
            "with specific feature comparisons from web search data. "
            f"Comparing against {len(competitors)} identified competitors."
        )

        return gaps

    def _analyze_ai_ml_gaps(
        self,
        vendor: str,
        agent_1_data: Optional[dict],
        agent_4_data: Optional[dict],
    ) -> dict:
        """Analyze AI/ML-specific capability gaps."""
        ai_gaps = {
            "total_ai_gaps": 0,
            "critical_ai_gaps": 0,
            "ai_competitive_position": "[Leader / Competitive / Behind / Lagging]",
            "gaps": [],
            "gap_template": {
                "capability_name": "[AI/ML Capability]",
                "ai_category": "[LLM/ML/NLP/CV/Anomaly Detection/etc.]",
                "priority": "[Critical/High/Medium]",
                "competitors_with_capability": [],
                "industry_adoption": "[High/Medium/Low]",
                "customer_demand": "[Evidence]",
                "implementation_approach": {
                    "build": {"effort": "[High/Med/Low]", "description": ""},
                    "buy": {"options": [], "description": ""},
                    "partner": {"options": [], "description": ""},
                },
                "business_impact": "[Revenue/Competitive/Innovation]",
            },
            "ai_capabilities_to_assess": [
                {
                    "capability": "LLM-Powered Policy Generation",
                    "description": "Using large language models to auto-generate "
                        "and optimize security policies",
                    "market_adoption": "Emerging",
                    "competitive_importance": "High",
                },
                {
                    "capability": "AI-Driven Data Classification",
                    "description": "ML-powered automatic classification of "
                        "sensitive data across environments",
                    "market_adoption": "Growing",
                    "competitive_importance": "Critical",
                },
                {
                    "capability": "Behavioral Analytics (UEBA)",
                    "description": "User and entity behavior analysis using "
                        "ML to detect anomalies and insider threats",
                    "market_adoption": "Standard",
                    "competitive_importance": "High",
                },
                {
                    "capability": "Predictive Risk Scoring",
                    "description": "ML models that predict security risks "
                        "before incidents occur",
                    "market_adoption": "Growing",
                    "competitive_importance": "High",
                },
                {
                    "capability": "NLP for Content Inspection",
                    "description": "Natural language processing for "
                        "understanding document context and sensitivity",
                    "market_adoption": "Growing",
                    "competitive_importance": "High",
                },
                {
                    "capability": "Automated Incident Response",
                    "description": "AI-driven automated response and "
                        "remediation for security incidents",
                    "market_adoption": "Growing",
                    "competitive_importance": "Medium-High",
                },
                {
                    "capability": "AI-Powered Threat Intelligence",
                    "description": "ML models analyzing threat feeds and "
                        "correlating with internal data",
                    "market_adoption": "Standard",
                    "competitive_importance": "Medium",
                },
                {
                    "capability": "Generative AI for Security Ops",
                    "description": "GenAI assistants for security analysts, "
                        "investigation summaries, and report generation",
                    "market_adoption": "Emerging",
                    "competitive_importance": "High",
                },
                {
                    "capability": "Computer Vision for Document Analysis",
                    "description": "Image/document analysis for detecting "
                        "sensitive content in visual formats",
                    "market_adoption": "Emerging",
                    "competitive_importance": "Medium",
                },
                {
                    "capability": "Federated Learning",
                    "description": "Privacy-preserving ML that learns across "
                        "customers without sharing raw data",
                    "market_adoption": "Emerging",
                    "competitive_importance": "Medium",
                },
            ],
            "summary_table": {
                "headers": [
                    "AI Capability", "Competitors Have", "Customer Demand",
                    "Market Trend", "Priority", "Recommendation",
                ],
                "note": "To be populated during orchestration",
            },
        }

        return ai_gaps

    def _analyze_customer_requests(
        self,
        agent_2_data: Optional[dict],
        agent_4_data: Optional[dict],
    ) -> dict:
        """Analyze unmet customer feature requests."""
        return {
            "total_unmet_requests": 0,
            "requests": [],
            "request_template": {
                "feature_name": "[Feature]",
                "request_count": 0,
                "ai_related": False,
                "segment": "[SMB/Enterprise/Both]",
                "current_status": "[Missing/Partial/Exists]",
                "competitor_availability": "[X competitors have it]",
                "priority": "[High/Medium/Low]",
                "customer_quote": "[Verbatim]",
                "implementation_path": "[Technical approach]",
                "expected_impact": "[Satisfaction/retention improvement]",
            },
            "analysis_note": (
                "Customer request analysis to be enriched during orchestration "
                "by cross-referencing Agent 2 feature requests with Agent 4 "
                "product capabilities."
            ),
        }

    def _analyze_trend_alignment(
        self,
        agent_1_data: Optional[dict],
        agent_4_data: Optional[dict],
    ) -> dict:
        """Analyze vendor alignment with market trends."""
        trends_to_check = []

        if agent_1_data:
            market = agent_1_data.get("market_landscape", {})
            for trend in market.get("trends_2025_2026", []):
                trends_to_check.append({
                    "trend": trend["trend"],
                    "description": trend["description"],
                    "impact": trend["impact"],
                    "vendor_readiness": "[To be assessed]",
                    "gap_status": "[Ready / Partial / Gap]",
                })

        return {
            "trends_assessed": len(trends_to_check),
            "trends": trends_to_check,
            "emerging_tech_gaps": [],
            "analysis_note": (
                "Trend alignment to be fully assessed during orchestration "
                "by comparing vendor capabilities with market trends."
            ),
        }

    def _analyze_segment_gaps(
        self,
        agent_1_data: Optional[dict],
        agent_2_data: Optional[dict],
        agent_4_data: Optional[dict],
    ) -> dict:
        """Analyze segment-specific gaps."""
        return {
            "smb_gaps": {
                "blocking_adoption": [],
                "gap_template": {
                    "gap": "[Feature/Capability missing]",
                    "why_smbs_need_it": "[Explanation]",
                    "competitor_advantage": "[Which competitors serve SMBs better]",
                    "customer_evidence": "[Quote]",
                    "ai_related": False,
                },
            },
            "enterprise_gaps": {
                "blocking_deals": [],
                "gap_template": {
                    "gap": "[Feature/Capability missing]",
                    "why_enterprises_require_it": "[Explanation]",
                    "competitor_advantage": "[Enterprise-focused competitors]",
                    "customer_evidence": "[Quote]",
                    "ai_related": False,
                },
            },
        }

    def _prioritize_gaps(self, *gap_sources) -> dict:
        """Prioritize all identified gaps."""
        return {
            "prioritization_matrix": {
                "high_impact_low_effort": {
                    "label": "Quick Wins",
                    "gaps": [],
                },
                "high_impact_high_effort": {
                    "label": "Strategic Investments",
                    "gaps": [],
                },
                "low_impact_low_effort": {
                    "label": "Nice to Have",
                    "gaps": [],
                },
                "low_impact_high_effort": {
                    "label": "Avoid/Deprioritize",
                    "gaps": [],
                },
            },
            "competitive_parity_checklist": {
                "description": "Minimum features needed to compete effectively",
                "items": [],
            },
            "note": (
                "Gap prioritization to be completed during orchestration "
                "when all gap data is populated from web searches."
            ),
        }

    def _build_recommendations(self, prioritized_gaps: dict) -> dict:
        """Build strategic roadmap recommendations."""
        return {
            "immediate_0_3_months": {
                "focus": "Address critical competitive gaps",
                "actions": [],
            },
            "short_term_3_6_months": {
                "focus": "High-priority customer requests + market trends",
                "actions": [],
            },
            "medium_term_6_12_months": {
                "focus": "Strategic positioning + AI advancement",
                "actions": [],
            },
            "long_term_12_plus_months": {
                "focus": "Market leadership + AI innovation",
                "actions": [],
            },
            "business_impact": {
                "estimated_lost_deals": "[Analysis from review mentions]",
                "ai_gap_impact": "[Revenue impact of AI capability gaps]",
                "churn_risk": "[Assessment based on customer complaints]",
                "market_share_at_risk": "[Segment-specific analysis]",
            },
        }

    def _generate_report(self, data: dict) -> str:
        """Generate the gap analysis report."""
        vendor = data["vendor_name"]

        lines = [
            f"# Product Gap Analysis: {vendor}",
            f"**Analysis Date:** {format_timestamp()}",
            f"**Based on Data From:** Agents 1, 2, 4 (Validated by Agent 5)",
            f"**QA Score:** {data.get('qa_score', 'N/A')}/100",
            f"**Analyst:** Claude Agent 6 - Gap Analysis",
            "",
            "---",
            "",
            "## Executive Summary",
            "",
            f"This gap analysis identifies competitive gaps in {vendor}'s product "
            f"offerings compared to market competitors, customer expectations, and "
            f"industry trends. The analysis includes a dedicated AI/ML capability "
            f"gap assessment.",
            "",
            "**Key Findings:**",
            "- **Critical Gaps:** [To be populated during orchestration]",
            "- **AI/ML Gaps:** [To be populated during orchestration]",
            "- **High-Priority Gaps:** [To be populated during orchestration]",
            "- **Strategic Opportunities:** [To be populated during orchestration]",
            "",
            "---",
            "",
            "## Gap Analysis Framework",
            "",
            "### Gap Categories Analyzed",
            "",
        ]

        for cat in data["gap_categories"]:
            lines.append(f"- {cat}")

        # Feature Parity Section
        lines.extend([
            "",
            "---",
            "",
            "## Feature Parity Analysis",
            "",
            "### Methodology",
            f"Comparing {vendor}'s features against identified competitors "
            "using data from Agent 1 (competitive landscape) and Agent 4 "
            "(product capabilities).",
            "",
        ])

        feature_gaps = data["feature_gaps"]
        if feature_gaps.get("analysis_note"):
            lines.append(f"**Note:** {feature_gaps['analysis_note']}")
            lines.append("")

        # Gap template
        lines.extend([
            "### Gap Template (Applied to Each Gap)",
            "",
            "**Gap: [Feature/Capability Name]**",
            "- **Priority:** [Critical/High/Medium/Low]",
            "- **Category:** [Security/AI-ML/Integration/etc.]",
            "- **Competitors with Feature:** [List]",
            "- **Customer Demand:** [High/Medium/Low]",
            "- **AI-Related:** [Yes/No]",
            "- **Business Impact:** [Revenue/Churn/Market Share]",
            "- **Implementation Complexity:** [High/Medium/Low]",
            "- **Recommendation:** [Action]",
            "",
        ])

        # By category
        lines.extend(["### Gaps by Category", ""])
        for cat in data["gap_categories"]:
            lines.append(f"#### {cat}")
            lines.append("*To be populated during orchestration.*")
            lines.append("")

        # AI/ML Gap Section (Critical)
        ai_gaps = data["ai_ml_gaps"]
        lines.extend([
            "---",
            "",
            "## AI/ML-SPECIFIC GAPS (DETAILED ANALYSIS)",
            "",
            "### AI/ML Gap Overview",
            f"**Total AI/ML Gaps:** [To be determined]",
            f"**AI Competitive Position:** {ai_gaps['ai_competitive_position']}",
            "",
            "### AI Capabilities Assessment",
            "",
        ])

        # AI capabilities table
        headers = [
            "AI Capability", "Market Adoption",
            "Competitive Importance", "Vendor Status",
        ]
        rows = []
        for cap in ai_gaps["ai_capabilities_to_assess"]:
            rows.append([
                cap["capability"],
                cap["market_adoption"],
                cap["competitive_importance"],
                "[To be assessed]",
            ])
        lines.append(format_table(headers, rows))

        lines.extend([
            "",
            "### Detailed AI Gap Analysis",
            "",
        ])

        for cap in ai_gaps["ai_capabilities_to_assess"]:
            lines.extend([
                f"#### {cap['capability']}",
                f"**Description:** {cap['description']}",
                f"**Market Adoption:** {cap['market_adoption']}",
                f"**Competitive Importance:** {cap['competitive_importance']}",
                "",
                "**Gap Assessment:**",
                "- **Vendor Status:** [To be assessed during orchestration]",
                "- **Competitors with Capability:** [To be identified]",
                "- **Customer Evidence:** [From Agent 2 data]",
                "",
                "**Implementation Approach:**",
                "- **Build:** [Effort assessment]",
                "- **Buy:** [Third-party options]",
                "- **Partner:** [Integration options]",
                "",
            ])

        # Customer-Requested Features
        customer_gaps = data["customer_gaps"]
        lines.extend([
            "---",
            "",
            "## Customer-Requested Features (Unmet)",
            "",
            f"**Note:** {customer_gaps['analysis_note']}",
            "",
            "### Request Analysis Template",
            "",
        ])

        headers = [
            "Feature Request", "Count", "AI-Related",
            "Segment", "Status", "Priority",
        ]
        rows = [["[Feature]", "[X]", "[Y/N]", "[Segment]", "[Status]", "[Priority]"]]
        lines.append(format_table(headers, rows))

        # Trend Alignment
        trend_gaps = data["trend_gaps"]
        lines.extend([
            "",
            "---",
            "",
            "## Market Trend Alignment",
            "",
        ])

        if trend_gaps["trends"]:
            headers = ["Trend", "Impact", "Vendor Readiness", "Gap Status"]
            rows = []
            for trend in trend_gaps["trends"]:
                rows.append([
                    trend["trend"],
                    trend["impact"],
                    trend["vendor_readiness"],
                    trend["gap_status"],
                ])
            lines.append(format_table(headers, rows))
        else:
            lines.append("*To be populated during orchestration.*")

        # Segment-Specific Gaps
        lines.extend([
            "",
            "---",
            "",
            "## Segment-Specific Gap Analysis",
            "",
            "### SMB Market Gaps",
            "**Blocking SMB Adoption:**",
            "*To be identified during orchestration by cross-referencing "
            "SMB pain points (Agent 1) with product capabilities (Agent 4).*",
            "",
            "### Enterprise Market Gaps",
            "**Blocking Enterprise Deals:**",
            "*To be identified during orchestration by cross-referencing "
            "enterprise requirements (Agent 1) with product capabilities (Agent 4).*",
            "",
        ])

        # Strategic Recommendations
        recs = data["recommendations"]
        lines.extend([
            "---",
            "",
            "## Strategic Roadmap Recommendations",
            "",
        ])

        for timeframe, rec_data in [
            ("Immediate Actions (0-3 months)", recs["immediate_0_3_months"]),
            ("Short-Term (3-6 months)", recs["short_term_3_6_months"]),
            ("Medium-Term (6-12 months)", recs["medium_term_6_12_months"]),
            ("Long-Term (12+ months)", recs["long_term_12_plus_months"]),
        ]:
            lines.extend([
                f"### {timeframe}",
                f"**Focus:** {rec_data['focus']}",
                "",
                "*Specific actions to be populated during orchestration "
                "based on gap analysis results.*",
                "",
            ])

        # Business Impact
        bi = recs["business_impact"]
        lines.extend([
            "---",
            "",
            "## Business Impact Analysis",
            "",
            f"- **Estimated Lost Deals:** {bi['estimated_lost_deals']}",
            f"- **AI Gap Impact:** {bi['ai_gap_impact']}",
            f"- **Churn Risk:** {bi['churn_risk']}",
            f"- **Market Share at Risk:** {bi['market_share_at_risk']}",
            "",
        ])

        # Prioritization Matrix
        lines.extend([
            "---",
            "",
            "## Prioritization Matrix",
            "",
            "### Effort vs Impact",
            "",
            "**High Impact, Low Effort (Quick Wins):**",
            "- [To be populated]",
            "",
            "**High Impact, High Effort (Strategic Investments):**",
            "- [To be populated]",
            "",
            "**Low Impact, Low Effort (Nice to Have):**",
            "- [To be populated]",
            "",
            "**Low Impact, High Effort (Avoid/Deprioritize):**",
            "- [To be populated]",
            "",
        ])

        # Competitive Parity Checklist
        lines.extend([
            "---",
            "",
            "## Competitive Parity Checklist",
            "",
        ])

        headers = [
            "Feature", "Vendor Has?", "Competitors With It",
            "AI-Related", "Customer Demand", "Status",
        ]
        rows = [["[Feature]", "[Y/N]", "[X/Total]", "[Y/N]", "[Level]", "[Gap/Parity]"]]
        lines.append(format_table(headers, rows))

        lines.extend([
            "",
            "*To be populated during orchestration.*",
            "",
            "---",
            "",
            f"**Analysis Completed:** {format_timestamp()}",
            "**Next Steps:** Proceed to Executive Summary (Agent 7)",
        ])

        return "\n".join(lines)
