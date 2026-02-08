"""
Agent 1: Market Research & Competitive Analysis

Execution: Parallel (after Agent 3)
Output: 01_Market_Research/ folder

Conducts deep-dive market research on the Data Security industry
and comprehensive competitive analysis for the target vendor.
"""

import logging
from typing import Optional

from vendor_intelligence.agents.base import BaseAgent
from vendor_intelligence.config import (
    AnalysisConfig,
    VENDOR_CATEGORIES,
    CATEGORY_KEYWORDS,
    MARKET_RESEARCH_SOURCES,
    INDUSTRY_PUBLICATIONS,
    MIN_COMPETITORS,
)
from vendor_intelligence.utils.report_writer import (
    format_timestamp,
    format_table,
    format_section,
    format_bullet_list,
    format_source_citation,
)

logger = logging.getLogger(__name__)


class MarketResearchAgent(BaseAgent):
    """
    Agent 1: Market Research & Competitive Analysis

    Responsibilities:
    - Auto-detect vendor's primary category
    - Identify major competitors (user-provided or auto-detected)
    - Analyze market landscape and trends (2025-2026)
    - Map competitive positioning
    - Identify SMB vs Enterprise pain points
    - Assess technology stack trends
    """

    agent_number = 1
    agent_name = "Market_Research"
    output_folder = "01_Market_Research"

    async def run_analysis(self) -> tuple[str, dict]:
        """
        Execute market research and competitive analysis.

        Returns:
            Tuple of (markdown_report, structured_data)
        """
        vendor = self.config.vendor_name
        product = self.config.product_name

        # Step 1: Detect vendor category
        category = await self._detect_vendor_category(vendor)

        # Step 2: Determine competitor list
        competitors = await self._identify_competitors(vendor, category)

        # Step 3: Generate search queries
        search_queries = self._build_search_queries(vendor, category, competitors)

        # Step 4: Build market landscape data
        market_data = self._build_market_landscape(vendor, category)

        # Step 5: Build competitive analysis data
        competitive_data = self._build_competitive_analysis(
            vendor, category, competitors
        )

        # Step 6: Build customer segmentation analysis
        segmentation_data = self._build_segmentation_analysis(category)

        # Step 7: Build technology landscape
        tech_data = self._build_technology_landscape(category)

        # Compile all data
        data = {
            "vendor_name": vendor,
            "product_name": product,
            "detected_category": category,
            "competitors": competitors,
            "user_provided_competitors": self.config.user_provided_competitors,
            "search_queries": search_queries,
            "market_landscape": market_data,
            "competitive_analysis": competitive_data,
            "customer_segmentation": segmentation_data,
            "technology_landscape": tech_data,
        }

        # Generate report
        report = self._generate_report(data)

        return report, data

    async def _detect_vendor_category(self, vendor: str) -> str:
        """Auto-detect vendor's primary category based on product offerings."""
        queries = [
            f"{vendor} company overview data security category",
            f"{vendor} products DLP SSPM DSPM CASB cloud security",
        ]

        # Generate category detection queries for the search plan
        detected = "Data Security"  # Default

        # Match against known category keywords
        vendor_lower = vendor.lower()
        for category, keywords in CATEGORY_KEYWORDS.items():
            for keyword in keywords:
                if keyword in vendor_lower:
                    detected = category
                    break

        logger.info(f"Detected vendor category: {detected}")
        return detected

    async def _identify_competitors(
        self, vendor: str, category: str
    ) -> list[dict]:
        """
        Identify competitors either from user input or auto-detection.

        Returns list of competitor dicts with name, category, position, etc.
        """
        competitors = []

        if self.config.user_provided_competitors:
            # User provided a list - validate and supplement
            logger.info(
                f"User provided {len(self.config.user_provided_competitors)} competitors"
            )
            for name in self.config.user_provided_competitors:
                competitors.append({
                    "name": name,
                    "category": category,
                    "source": "user_provided",
                    "validated": True,
                    "market_position": "To be determined",
                    "target_segment": "To be determined",
                })

            # Supplement if fewer than threshold
            if len(competitors) < 5:
                supplemental = self._get_known_competitors(category, exclude=[
                    c["name"] for c in competitors
                ])
                for comp in supplemental[:10]:
                    competitors.append(comp)
                    logger.info(f"Supplemented competitor: {comp['name']}")
            elif len(competitors) < MIN_COMPETITORS:
                supplemental = self._get_known_competitors(category, exclude=[
                    c["name"] for c in competitors
                ])
                for comp in supplemental[:3]:
                    competitors.append(comp)
        else:
            # Auto-detect all major competitors
            logger.info(f"Auto-detecting competitors for category: {category}")
            competitors = self._get_known_competitors(category)

        logger.info(f"Total competitors identified: {len(competitors)}")
        return competitors

    def _get_known_competitors(
        self, category: str, exclude: Optional[list[str]] = None
    ) -> list[dict]:
        """
        Return known competitors for a given category.

        This provides a baseline competitor list. The orchestrator enriches
        this with web search results during execution.
        """
        exclude = exclude or []
        exclude_lower = [e.lower() for e in exclude]

        # Comprehensive competitor database by category
        competitor_db = {
            "DLP": [
                {"name": "Symantec (Broadcom)", "market_position": "Leader", "target_segment": "Enterprise"},
                {"name": "Digital Guardian (Fortra)", "market_position": "Strong", "target_segment": "Enterprise"},
                {"name": "Forcepoint", "market_position": "Leader", "target_segment": "Both"},
                {"name": "Trellix", "market_position": "Challenger", "target_segment": "Enterprise"},
                {"name": "Microsoft Purview", "market_position": "Leader", "target_segment": "Both"},
                {"name": "Zscaler", "market_position": "Leader", "target_segment": "Enterprise"},
                {"name": "Netskope", "market_position": "Leader", "target_segment": "Both"},
                {"name": "Palo Alto Networks", "market_position": "Leader", "target_segment": "Enterprise"},
                {"name": "Code42", "market_position": "Niche", "target_segment": "Both"},
                {"name": "Proofpoint", "market_position": "Strong", "target_segment": "Enterprise"},
                {"name": "CoSoSys Endpoint Protector", "market_position": "Niche", "target_segment": "SMB"},
                {"name": "Safetica", "market_position": "Niche", "target_segment": "SMB"},
                {"name": "Tessian", "market_position": "Niche", "target_segment": "Both"},
                {"name": "DTEX Systems", "market_position": "Niche", "target_segment": "Enterprise"},
                {"name": "Nightfall AI", "market_position": "Niche", "target_segment": "Both"},
            ],
            "DSPM": [
                {"name": "Varonis", "market_position": "Leader", "target_segment": "Enterprise"},
                {"name": "BigID", "market_position": "Leader", "target_segment": "Enterprise"},
                {"name": "Sentra", "market_position": "Challenger", "target_segment": "Enterprise"},
                {"name": "Laminar (now Rubrik)", "market_position": "Strong", "target_segment": "Enterprise"},
                {"name": "Dig Security (now Palo Alto)", "market_position": "Strong", "target_segment": "Enterprise"},
                {"name": "Cyera", "market_position": "Challenger", "target_segment": "Enterprise"},
                {"name": "Normalyze", "market_position": "Niche", "target_segment": "Enterprise"},
                {"name": "Polar Security (now IBM)", "market_position": "Strong", "target_segment": "Enterprise"},
                {"name": "Securiti", "market_position": "Leader", "target_segment": "Both"},
                {"name": "Open Raven", "market_position": "Niche", "target_segment": "Enterprise"},
                {"name": "Symmetry Systems", "market_position": "Niche", "target_segment": "Enterprise"},
                {"name": "Concentric AI", "market_position": "Niche", "target_segment": "Enterprise"},
                {"name": "Flow Security", "market_position": "Niche", "target_segment": "Enterprise"},
                {"name": "Eureka Security", "market_position": "Niche", "target_segment": "Enterprise"},
            ],
            "SSPM": [
                {"name": "AppOmni", "market_position": "Leader", "target_segment": "Enterprise"},
                {"name": "Obsidian Security", "market_position": "Strong", "target_segment": "Enterprise"},
                {"name": "Adaptive Shield", "market_position": "Leader", "target_segment": "Both"},
                {"name": "Valence Security", "market_position": "Challenger", "target_segment": "Enterprise"},
                {"name": "Wing Security", "market_position": "Challenger", "target_segment": "Both"},
                {"name": "Spin.AI", "market_position": "Niche", "target_segment": "SMB"},
                {"name": "DoControl", "market_position": "Niche", "target_segment": "Both"},
                {"name": "Nudge Security", "market_position": "Niche", "target_segment": "Both"},
                {"name": "Savvy Security", "market_position": "Niche", "target_segment": "Enterprise"},
                {"name": "Netskope", "market_position": "Leader", "target_segment": "Enterprise"},
                {"name": "Zscaler", "market_position": "Leader", "target_segment": "Enterprise"},
                {"name": "Microsoft Defender", "market_position": "Leader", "target_segment": "Both"},
            ],
            "Outbound CASB": [
                {"name": "Netskope", "market_position": "Leader", "target_segment": "Enterprise"},
                {"name": "Zscaler", "market_position": "Leader", "target_segment": "Enterprise"},
                {"name": "Palo Alto Networks", "market_position": "Leader", "target_segment": "Enterprise"},
                {"name": "Microsoft Defender for Cloud Apps", "market_position": "Leader", "target_segment": "Both"},
                {"name": "Skyhigh Security", "market_position": "Strong", "target_segment": "Enterprise"},
                {"name": "Forcepoint", "market_position": "Strong", "target_segment": "Both"},
                {"name": "Lookout", "market_position": "Challenger", "target_segment": "Both"},
                {"name": "Cisco Cloudlock", "market_position": "Niche", "target_segment": "Enterprise"},
                {"name": "Broadcom (Symantec)", "market_position": "Strong", "target_segment": "Enterprise"},
                {"name": "iboss", "market_position": "Niche", "target_segment": "Both"},
                {"name": "Cato Networks", "market_position": "Challenger", "target_segment": "Both"},
                {"name": "Bitglass (now Forcepoint)", "market_position": "Niche", "target_segment": "Both"},
            ],
            "Cloud Security": [
                {"name": "Palo Alto Networks (Prisma Cloud)", "market_position": "Leader", "target_segment": "Enterprise"},
                {"name": "CrowdStrike", "market_position": "Leader", "target_segment": "Enterprise"},
                {"name": "Wiz", "market_position": "Leader", "target_segment": "Both"},
                {"name": "Orca Security", "market_position": "Strong", "target_segment": "Enterprise"},
                {"name": "Lacework", "market_position": "Challenger", "target_segment": "Enterprise"},
                {"name": "Aqua Security", "market_position": "Strong", "target_segment": "Enterprise"},
                {"name": "Sysdig", "market_position": "Strong", "target_segment": "Enterprise"},
                {"name": "Trend Micro", "market_position": "Leader", "target_segment": "Both"},
                {"name": "Check Point", "market_position": "Leader", "target_segment": "Enterprise"},
                {"name": "Fortinet", "market_position": "Leader", "target_segment": "Both"},
                {"name": "Tenable", "market_position": "Strong", "target_segment": "Enterprise"},
                {"name": "Rapid7", "market_position": "Strong", "target_segment": "Both"},
            ],
            "Data Security": [
                {"name": "Varonis", "market_position": "Leader", "target_segment": "Enterprise"},
                {"name": "Microsoft Purview", "market_position": "Leader", "target_segment": "Both"},
                {"name": "Forcepoint", "market_position": "Strong", "target_segment": "Both"},
                {"name": "Digital Guardian (Fortra)", "market_position": "Strong", "target_segment": "Enterprise"},
                {"name": "Netskope", "market_position": "Leader", "target_segment": "Enterprise"},
                {"name": "Zscaler", "market_position": "Leader", "target_segment": "Enterprise"},
                {"name": "BigID", "market_position": "Leader", "target_segment": "Enterprise"},
                {"name": "Securiti", "market_position": "Strong", "target_segment": "Both"},
                {"name": "Thales (CipherTrust)", "market_position": "Leader", "target_segment": "Enterprise"},
                {"name": "Imperva", "market_position": "Strong", "target_segment": "Enterprise"},
                {"name": "Proofpoint", "market_position": "Strong", "target_segment": "Enterprise"},
                {"name": "Trellix", "market_position": "Challenger", "target_segment": "Enterprise"},
                {"name": "Cyera", "market_position": "Challenger", "target_segment": "Enterprise"},
                {"name": "Rubrik", "market_position": "Strong", "target_segment": "Enterprise"},
            ],
        }

        category_competitors = competitor_db.get(category, competitor_db["Data Security"])

        result = []
        for comp in category_competitors:
            if comp["name"].lower() not in exclude_lower:
                comp["category"] = category
                comp["source"] = "auto_detected"
                comp["validated"] = True
                result.append(comp)

        return result

    def _build_search_queries(
        self,
        vendor: str,
        category: str,
        competitors: list[dict],
    ) -> list[str]:
        """Build comprehensive search query list for market research."""
        queries = [
            f"{vendor} company overview {category}",
            f"{vendor} competitors comparison 2025 2026",
            f"{vendor} market position {category}",
            f"{category} market analysis 2025 2026",
            f"Gartner Magic Quadrant {category} 2025",
            f"Forrester Wave {category} 2025 2026",
            f"{vendor} funding acquisitions 2025 2026",
            f"{category} market trends 2025 2026",
            f"SMB enterprise {category} challenges 2025",
            f"{vendor} partnerships integrations ecosystem",
            f"{category} market size growth forecast 2025 2026",
            f"{vendor} pricing model plans",
            f"{category} competitive landscape 2025",
            f"{category} regulatory drivers GDPR CCPA SOC2 2025",
            f"zero trust {category} trends 2026",
            f"AI machine learning {category} trends 2025 2026",
        ]

        # Add competitor-specific queries
        for comp in competitors[:5]:
            queries.append(f"{vendor} vs {comp['name']} comparison")

        return queries

    def _build_market_landscape(
        self, vendor: str, category: str
    ) -> dict:
        """Build market landscape analysis structure."""
        return {
            "current_state": {
                "description": f"The {category} market continues to evolve rapidly, "
                    f"driven by increasing cloud adoption, regulatory requirements, "
                    f"and AI-powered security threats.",
                "key_drivers": [
                    "Accelerated cloud migration and multi-cloud adoption",
                    "Increasing regulatory compliance requirements (GDPR, CCPA, DORA)",
                    "Rise of AI-powered threats and need for AI-powered defense",
                    "Remote/hybrid workforce security challenges",
                    "Zero Trust architecture adoption",
                    "Data sovereignty and residency requirements",
                    "Supply chain security concerns",
                ],
            },
            "trends_2025_2026": [
                {
                    "trend": "AI/ML-Driven Security",
                    "description": "Adoption of generative AI and ML models for threat detection, "
                        "policy generation, and automated response",
                    "impact": "High",
                    "adoption_stage": "Growing",
                },
                {
                    "trend": "Data Security Posture Management (DSPM) Convergence",
                    "description": "DSPM capabilities merging with DLP, CASB, and CSPM platforms",
                    "impact": "High",
                    "adoption_stage": "Emerging",
                },
                {
                    "trend": "Platform Consolidation",
                    "description": "Vendors consolidating point solutions into unified security platforms",
                    "impact": "High",
                    "adoption_stage": "Growing",
                },
                {
                    "trend": "Zero Trust Data Security",
                    "description": "Data-centric security approaches replacing perimeter-based models",
                    "impact": "Medium-High",
                    "adoption_stage": "Growing",
                },
                {
                    "trend": "SaaS Security Posture Management",
                    "description": "Growing need to secure SaaS application configurations and data",
                    "impact": "Medium",
                    "adoption_stage": "Maturing",
                },
                {
                    "trend": "API Security Integration",
                    "description": "Data security extending to API traffic and data flows",
                    "impact": "Medium",
                    "adoption_stage": "Emerging",
                },
                {
                    "trend": "Privacy-Enhancing Technologies",
                    "description": "Adoption of PETs for data processing without exposure",
                    "impact": "Medium",
                    "adoption_stage": "Emerging",
                },
            ],
            "market_size": {
                "description": "Global data security market projected to grow significantly",
                "note": "[To be enriched with specific figures from web search during orchestration]",
            },
        }

    def _build_competitive_analysis(
        self,
        vendor: str,
        category: str,
        competitors: list[dict],
    ) -> dict:
        """Build competitive analysis structure."""
        positioning_matrix = []
        for comp in competitors:
            positioning_matrix.append({
                "competitor": comp["name"],
                "market_position": comp.get("market_position", "To be determined"),
                "target_segment": comp.get("target_segment", "To be determined"),
                "key_strengths": "[To be enriched from web search]",
                "key_weaknesses": "[To be enriched from web search]",
                "source": comp.get("source", "auto_detected"),
            })

        return {
            "vendor_name": vendor,
            "category": category,
            "total_competitors": len(competitors),
            "positioning_matrix": positioning_matrix,
            "search_queries_for_enrichment": [
                f"{comp['name']} {category} features strengths weaknesses"
                for comp in competitors[:10]
            ],
        }

    def _build_segmentation_analysis(self, category: str) -> dict:
        """Build customer segmentation analysis."""
        return {
            "smb": {
                "definition": "Companies with fewer than 500 employees",
                "top_challenges": [
                    {
                        "challenge": "Budget constraints for security tools",
                        "why_it_matters": "SMBs need cost-effective solutions that provide essential coverage "
                            "without enterprise-level pricing",
                    },
                    {
                        "challenge": "Limited security team expertise",
                        "why_it_matters": "Lack of dedicated security staff means tools must be "
                            "intuitive and require minimal management",
                    },
                    {
                        "challenge": "Deployment and integration complexity",
                        "why_it_matters": "SMBs cannot afford lengthy deployment cycles; they need "
                            "quick time-to-value with existing infrastructure",
                    },
                    {
                        "challenge": "Compliance requirements with limited resources",
                        "why_it_matters": "Growing regulatory pressure on smaller companies without "
                            "the staff to manage compliance manually",
                    },
                    {
                        "challenge": "Shadow IT and SaaS sprawl",
                        "why_it_matters": "Employees adopting unsanctioned apps without IT oversight, "
                            "creating data exposure risks",
                    },
                ],
                "buying_criteria": [
                    {"criterion": "Price / Total Cost of Ownership", "priority": "Critical"},
                    {"criterion": "Ease of deployment and management", "priority": "Critical"},
                    {"criterion": "Out-of-the-box policy templates", "priority": "High"},
                    {"criterion": "Vendor support quality", "priority": "High"},
                    {"criterion": "Integration with existing tools", "priority": "Medium"},
                    {"criterion": "Scalability for growth", "priority": "Medium"},
                ],
            },
            "enterprise": {
                "definition": "Companies with more than 5,000 employees",
                "top_challenges": [
                    {
                        "challenge": "Multi-cloud and hybrid environment security",
                        "why_it_matters": "Enterprises operate across AWS, Azure, GCP, and on-prem, "
                            "requiring unified data security across all environments",
                    },
                    {
                        "challenge": "Scale and performance at volume",
                        "why_it_matters": "Processing millions of events and monitoring petabytes "
                            "of data without performance degradation",
                    },
                    {
                        "challenge": "Complex regulatory compliance",
                        "why_it_matters": "Multi-jurisdiction compliance (GDPR, CCPA, HIPAA, SOX) "
                            "requires sophisticated policy management",
                    },
                    {
                        "challenge": "Advanced persistent threats and insider risks",
                        "why_it_matters": "Sophisticated threat actors require advanced detection "
                            "capabilities including behavioral analytics",
                    },
                    {
                        "challenge": "Integration with enterprise security stack",
                        "why_it_matters": "Must work with SIEM, SOAR, IAM, GRC, and other enterprise "
                            "security tools seamlessly",
                    },
                    {
                        "challenge": "Data sovereignty and residency",
                        "why_it_matters": "Global operations require data to stay within specific "
                            "geographic boundaries per regulation",
                    },
                ],
                "buying_criteria": [
                    {"criterion": "Scalability and performance", "priority": "Critical"},
                    {"criterion": "Multi-cloud support", "priority": "Critical"},
                    {"criterion": "Advanced analytics and AI/ML capabilities", "priority": "High"},
                    {"criterion": "Enterprise integrations (SIEM, SOAR)", "priority": "High"},
                    {"criterion": "Granular policy management", "priority": "High"},
                    {"criterion": "Professional services and support", "priority": "High"},
                    {"criterion": "Compliance certifications", "priority": "High"},
                    {"criterion": "API extensibility", "priority": "Medium"},
                ],
            },
        }

    def _build_technology_landscape(self, category: str) -> dict:
        """Build technology landscape analysis."""
        return {
            "core_technologies": [
                {
                    "technology": "Content Inspection / Deep Packet Inspection",
                    "description": "Analyzing data content in transit and at rest for sensitive information",
                    "adoption": "Mature",
                },
                {
                    "technology": "Machine Learning Classification",
                    "description": "AI-driven data classification and sensitivity labeling",
                    "adoption": "Growing",
                },
                {
                    "technology": "API-Based Cloud Integration",
                    "description": "Agentless connectivity to cloud services via APIs",
                    "adoption": "Standard",
                },
                {
                    "technology": "Behavioral Analytics (UEBA)",
                    "description": "User and entity behavior analysis for anomaly detection",
                    "adoption": "Growing",
                },
                {
                    "technology": "Zero Trust Network Access (ZTNA)",
                    "description": "Identity-verified, least-privilege access to resources",
                    "adoption": "Growing",
                },
                {
                    "technology": "Data Discovery and Classification",
                    "description": "Automated scanning and labeling of data across environments",
                    "adoption": "Standard",
                },
            ],
            "integration_ecosystem": [
                "SIEM platforms (Splunk, Microsoft Sentinel, IBM QRadar)",
                "SOAR platforms (Palo Alto XSOAR, Splunk SOAR, ServiceNow)",
                "Identity providers (Okta, Azure AD, Ping Identity)",
                "Cloud platforms (AWS, Azure, GCP)",
                "Collaboration tools (Microsoft 365, Google Workspace, Slack)",
                "Endpoint solutions (CrowdStrike, SentinelOne, Microsoft Defender)",
                "GRC platforms (ServiceNow, Archer, OneTrust)",
                "Ticketing systems (Jira, ServiceNow, Zendesk)",
            ],
            "future_bets": [
                {
                    "technology": "Generative AI for Security Operations",
                    "description": "Using LLMs for policy generation, incident investigation, and remediation guidance",
                    "timeline": "2025-2026",
                },
                {
                    "technology": "Data Security Mesh Architecture",
                    "description": "Distributed data security controls following data across environments",
                    "timeline": "2025-2027",
                },
                {
                    "technology": "Autonomous SOC Capabilities",
                    "description": "Self-healing security systems with minimal human intervention",
                    "timeline": "2026-2028",
                },
                {
                    "technology": "Quantum-Resistant Encryption",
                    "description": "Preparing data protection for post-quantum computing era",
                    "timeline": "2026-2030",
                },
            ],
        }

    def _generate_report(self, data: dict) -> str:
        """Generate the full Markdown report."""
        vendor = data["vendor_name"]
        category = data["detected_category"]
        competitors = data["competitors"]
        user_provided = data.get("user_provided_competitors")

        lines = [
            f"# Market Research: {vendor} - {category}",
            f"**Generated:** {format_timestamp()}",
            f"**Analyst:** Claude Agent 1 - Market Research & Competitive Analysis",
            f"**Sources:** {len(self.sources)} verified sources",
            "",
            "---",
            "",
            "## Executive Market Summary",
            "",
            f"{vendor} operates in the {category} segment of the data security market, "
            f"which continues to experience significant growth driven by cloud adoption, "
            f"regulatory pressures, and evolving cyber threats. The competitive landscape "
            f"includes {len(competitors)} major players ranging from established leaders "
            f"to innovative challengers.",
            "",
            f"The {category} market in 2025-2026 is characterized by platform consolidation, "
            f"AI/ML-driven detection capabilities, and the convergence of multiple security "
            f"disciplines into unified platforms. Vendors are increasingly competing on "
            f"AI sophistication, deployment simplicity, and cross-environment coverage.",
            "",
            "## Competitor Identification Method",
            "",
        ]

        # Competitor identification method
        if user_provided:
            lines.extend([
                f"**Method Used:** User-Provided List (supplemented by agent)",
                f"**User-Provided Competitors:** {', '.join(user_provided)}",
            ])
            auto_added = [
                c["name"] for c in competitors if c.get("source") == "auto_detected"
            ]
            if auto_added:
                lines.append(
                    f"**Additional Competitors Added by Agent:** {', '.join(auto_added)}"
                )
        else:
            lines.append("**Method Used:** Auto-Detected")
            lines.append("**User-Provided Competitors:** N/A")

        lines.append(f"**Total Competitors Analyzed:** {len(competitors)}")
        lines.extend(["", "---", ""])

        # Industry Landscape
        market = data["market_landscape"]
        lines.extend([
            "## Industry Landscape",
            "",
            f"### Current Market State (2025-2026)",
            "",
            market["current_state"]["description"],
            "",
            "**Key Market Drivers:**",
        ])
        for driver in market["current_state"]["key_drivers"]:
            lines.append(f"- {driver}")

        lines.extend(["", "### Key Trends (2025-2026)", ""])
        for trend in market["trends_2025_2026"]:
            lines.append(
                f"- **{trend['trend']}** (Impact: {trend['impact']}, "
                f"Stage: {trend['adoption_stage']}): {trend['description']}"
            )

        # Competitive Analysis
        lines.extend(["", "---", "", "## Competitive Analysis", ""])

        # Positioning matrix table
        lines.append("### Market Positioning Matrix")
        lines.append("")

        headers = [
            "Competitor", "Market Position", "Target Segment",
            "Source",
        ]
        rows = []
        for comp in competitors:
            rows.append([
                comp["name"],
                comp.get("market_position", "TBD"),
                comp.get("target_segment", "TBD"),
                comp.get("source", "auto"),
            ])
        lines.append(format_table(headers, rows))

        # Detailed competitor profiles
        lines.extend(["", "### Detailed Competitor Profiles", ""])
        for comp in competitors:
            lines.extend([
                f"**{comp['name']}**",
                f"- **Category:** {comp.get('category', category)}",
                f"- **Market Position:** {comp.get('market_position', 'To be determined')}",
                f"- **Target Customers:** {comp.get('target_segment', 'To be determined')}",
                f"- **Source:** {comp.get('source', 'auto_detected')}",
                f"- **Key Features:** [To be enriched via web search during orchestration]",
                f"- **Differentiators:** [To be enriched via web search during orchestration]",
                f"- **Recent News:** [To be enriched via web search during orchestration]",
                "",
            ])

        # Customer Pain Points
        seg = data["customer_segmentation"]
        lines.extend(["---", "", "## Customer Pain Points Analysis", ""])

        lines.extend(["### SMB Segment", "", "**Top Challenges:**"])
        for i, item in enumerate(seg["smb"]["top_challenges"], 1):
            lines.append(f"{i}. **{item['challenge']}** - {item['why_it_matters']}")

        lines.extend(["", "**Buying Criteria:**"])
        for item in seg["smb"]["buying_criteria"]:
            lines.append(
                f"- {item['criterion']} (Priority: {item['priority']})"
            )

        lines.extend(["", "### Enterprise Segment", "", "**Top Challenges:**"])
        for i, item in enumerate(seg["enterprise"]["top_challenges"], 1):
            lines.append(f"{i}. **{item['challenge']}** - {item['why_it_matters']}")

        lines.extend(["", "**Buying Criteria:**"])
        for item in seg["enterprise"]["buying_criteria"]:
            lines.append(
                f"- {item['criterion']} (Priority: {item['priority']})"
            )

        # Technology Landscape
        tech = data["technology_landscape"]
        lines.extend(["", "---", "", "## Technology Landscape", ""])

        lines.append("### Core Technologies")
        for t in tech["core_technologies"]:
            lines.append(
                f"- **{t['technology']}** ({t['adoption']}): {t['description']}"
            )

        lines.extend(["", "### Integration Ecosystem"])
        for integration in tech["integration_ecosystem"]:
            lines.append(f"- {integration}")

        lines.extend(["", "### Future Technology Bets"])
        for bet in tech["future_bets"]:
            lines.append(
                f"- **{bet['technology']}** ({bet['timeline']}): {bet['description']}"
            )

        # Search queries for orchestrator
        lines.extend([
            "",
            "---",
            "",
            "## Search Queries for Enrichment",
            "",
            "The following queries should be executed during orchestration "
            "to enrich this report with live data:",
            "",
        ])
        for query in data["search_queries"]:
            lines.append(f"- `{query}`")

        # Sources
        lines.extend(["", "---", "", "## Sources", ""])
        if self.sources:
            for i, source in enumerate(self.sources, 1):
                lines.append(format_source_citation(
                    source["title"], source["url"],
                    source.get("access_date"), i
                ))
        else:
            lines.append(
                "*Sources will be populated during orchestration when "
                "web searches are executed.*"
            )

        return "\n".join(lines)
