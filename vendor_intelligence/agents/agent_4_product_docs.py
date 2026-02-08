"""
Agent 4: Product Documentation Analyzer (with AI/ML Deep Dive)

Execution: Parallel (after Agent 3)
Output: 03_Product_Documentation/ folder

Analyzes official documentation, release notes, technical resources,
and conducts comprehensive AI/ML/LLM technology analysis.
"""

import logging
from typing import Optional

from vendor_intelligence.agents.base import BaseAgent
from vendor_intelligence.config import AI_ML_SEARCH_TERMS
from vendor_intelligence.utils.report_writer import (
    format_timestamp,
    format_table,
    format_section,
    format_source_citation,
)

logger = logging.getLogger(__name__)


class ProductDocsAgent(BaseAgent):
    """
    Agent 4: Product Documentation Analyzer with AI/ML Deep Dive

    Responsibilities:
    - Map complete product portfolio
    - Deep-dive feature analysis by category
    - Comprehensive AI/ML/LLM technology analysis
    - Latest release notes review
    - Technical specifications and architecture
    - API and developer resource assessment
    - Documentation quality evaluation
    """

    agent_number = 4
    agent_name = "Product_Documentation"
    output_folder = "03_Product_Documentation"

    async def run_analysis(self) -> tuple[str, dict]:
        """
        Execute product documentation analysis with AI/ML deep dive.

        Returns:
            Tuple of (markdown_report, structured_data)
        """
        vendor = self.config.vendor_name
        product = self.config.product_name

        # Step 1: Build search queries for product docs
        doc_queries = self._build_doc_search_queries(vendor, product)

        # Step 2: Build AI/ML search queries
        ai_queries = self._build_ai_ml_search_queries(vendor, product)

        # Step 3: Initialize product portfolio structure
        portfolio = self._build_portfolio_structure(vendor, product)

        # Step 4: Build feature analysis framework
        features = self._build_feature_framework()

        # Step 5: Build AI/ML analysis framework
        ai_ml_framework = self._build_ai_ml_framework(vendor)

        # Step 6: Build technical specs framework
        tech_specs = self._build_tech_specs_framework()

        # Compile data
        data = {
            "vendor_name": vendor,
            "product_name": product,
            "doc_search_queries": doc_queries,
            "ai_ml_search_queries": ai_queries,
            "product_portfolio": portfolio,
            "feature_framework": features,
            "ai_ml_framework": ai_ml_framework,
            "tech_specs": tech_specs,
        }

        # Generate report
        report = self._generate_report(data)

        return report, data

    def _build_doc_search_queries(
        self, vendor: str, product: Optional[str]
    ) -> list[str]:
        """Build search queries for product documentation."""
        target = f"{vendor} {product}" if product else vendor
        queries = [
            f"{target} official documentation",
            f"{target} product features capabilities",
            f"{target} release notes latest 2025",
            f"{target} API documentation developer",
            f"{target} architecture technical overview",
            f"{target} deployment guide installation",
            f"{target} integration guide connectors",
            f"{target} compliance certifications SOC2 ISO27001",
            f"{target} admin guide administration",
            f"{target} use cases data security",
            f"{target} whitepaper technical",
            f"{target} product roadmap 2025 2026",
            f"{target} pricing tiers plans",
            f"{target} system requirements specifications",
        ]
        return queries

    def _build_ai_ml_search_queries(
        self, vendor: str, product: Optional[str]
    ) -> list[str]:
        """Build AI/ML-specific search queries."""
        target = f"{vendor} {product}" if product else vendor
        queries = []
        for term in AI_ML_SEARCH_TERMS:
            queries.append(f"{target} {term}")
        return queries

    def _build_portfolio_structure(
        self, vendor: str, product: Optional[str]
    ) -> dict:
        """Build product portfolio mapping structure."""
        return {
            "vendor_name": vendor,
            "product_focus": product,
            "products": [],
            "product_template": {
                "name": "[Product Name]",
                "category": "[DLP/SSPM/DSPM/CASB/etc.]",
                "current_version": "[Version]",
                "last_updated": "[Date]",
                "description": "[What it does]",
                "deployment_model": "[SaaS/On-prem/Hybrid]",
                "architecture_type": "[Agent-based/Agentless/API-based]",
                "target_segment": "[SMB/Enterprise/Both]",
                "ai_ml_enabled": False,
            },
            "product_relationships": "[How products work together - suite vs standalone]",
        }

    def _build_feature_framework(self) -> dict:
        """Build comprehensive feature analysis framework."""
        return {
            "categories": {
                "security_features": {
                    "label": "Security Features",
                    "icon": "lock",
                    "subcategories": [
                        "Data Loss Prevention",
                        "Threat Detection",
                        "Access Control",
                        "Encryption",
                        "Endpoint Protection",
                        "Cloud Security",
                    ],
                },
                "compliance_governance": {
                    "label": "Compliance & Governance",
                    "icon": "clipboard",
                    "subcategories": [
                        "Regulatory Frameworks (GDPR, CCPA, HIPAA, SOX)",
                        "Audit & Reporting",
                        "Policy Management",
                        "Data Residency",
                        "Risk Assessment",
                    ],
                },
                "integration_capabilities": {
                    "label": "Integration Capabilities",
                    "icon": "link",
                    "subcategories": [
                        "Native Integrations",
                        "API Capabilities",
                        "Webhook Support",
                        "SIEM/SOAR Integration",
                        "Identity Provider Integration",
                        "Cloud Platform Integration",
                    ],
                },
                "automation_orchestration": {
                    "label": "Automation & Orchestration",
                    "icon": "robot",
                    "subcategories": [
                        "Automated Response",
                        "Workflow Automation",
                        "Policy Automation",
                        "Incident Response Automation",
                        "AI-Powered Automation",
                    ],
                },
                "analytics_reporting": {
                    "label": "Analytics & Reporting",
                    "icon": "chart",
                    "subcategories": [
                        "Dashboards",
                        "Custom Reports",
                        "Trend Analysis",
                        "Executive Reporting",
                        "Real-time Monitoring",
                    ],
                },
                "admin_management": {
                    "label": "User Management & Admin",
                    "icon": "users",
                    "subcategories": [
                        "RBAC",
                        "Multi-tenancy",
                        "User Management",
                        "Admin Portal",
                        "Delegated Administration",
                    ],
                },
                "user_experience": {
                    "label": "User Experience",
                    "icon": "eye",
                    "subcategories": [
                        "Interface Type",
                        "Mobile Support",
                        "Self-Service Portal",
                        "Onboarding Experience",
                        "Documentation Quality",
                    ],
                },
            },
        }

    def _build_ai_ml_framework(self, vendor: str) -> dict:
        """
        Build comprehensive AI/ML/LLM analysis framework.

        This is the core framework for the AI/ML deep dive.
        """
        return {
            "overview": {
                "ai_ml_maturity_level": "[Leading / Advanced / Moderate / Basic / None]",
                "primary_ai_technologies": [],
                "ai_powered_features_count": 0,
                "ai_implementation_approach": "[Proprietary / Third-party / Hybrid]",
            },
            "technology_analysis_template": {
                "technology_name": "[Technology Name/Type]",
                "identification": {
                    "type": "[ML / LLM / NLP / Computer Vision / Anomaly Detection / etc.]",
                    "specific_model": "[e.g., GPT-4, Custom BERT, Random Forest]",
                    "implementation": "[Proprietary / Third-party / Hybrid]",
                    "first_introduced": "[Version/Date]",
                },
                "use_case": {
                    "problem_solved": "[What business/security problem this AI solves]",
                    "features_utilizing": [],
                    "concrete_example": "[Real-world scenario]",
                    "target_users": [],
                },
                "technical_implementation": {
                    "architecture_overview": "[Text description of AI architecture]",
                    "training": {
                        "data_sources": "[Type of training data]",
                        "data_volume": "[If disclosed]",
                        "data_privacy": "[How sensitive data is handled]",
                        "method": "[Supervised/Unsupervised/Semi-supervised/RL/Transfer]",
                        "technique": "[Specific ML technique]",
                        "update_frequency": "[Continuous/Daily/Weekly/Monthly/Static]",
                        "update_method": "[Online learning/Batch retraining/Fine-tuning]",
                        "customer_control": "[Opt-out options]",
                        "infrastructure": "[Cloud/On-premise/Hybrid]",
                        "cloud_provider": "[AWS/Azure/GCP/Vendor's own]",
                    },
                    "inference": {
                        "processing_location": "[Cloud/Edge/Hybrid]",
                        "data_residency": "[Where inference happens]",
                        "processing_mode": "[Real-time/Near real-time/Batch]",
                        "latency": "[Response time if published]",
                        "scalability": "[How it handles growing data]",
                    },
                    "tech_stack": {
                        "frameworks": "[TensorFlow/PyTorch/scikit-learn/Custom]",
                        "languages": "[Python/R/Java/etc.]",
                        "infrastructure": "[Kubernetes/Serverless/etc.]",
                    },
                },
                "performance_metrics": {
                    "accuracy": "[If published]",
                    "precision": "[If available]",
                    "recall": "[If available]",
                    "f1_score": "[If available]",
                    "false_positive_rate": "[If published]",
                    "false_negative_rate": "[If published]",
                    "throughput": "[Events/second or similar]",
                    "latency": "[Average response time]",
                    "validation_method": "[How vendor validates AI performance]",
                    "third_party_testing": "[Independent validation]",
                },
                "competitive_differentiation": {
                    "unique_aspects": [],
                    "patents": "[AI-related patents]",
                    "published_research": "[Academic papers]",
                    "proprietary_vs_cots": "[Assessment]",
                    "competitive_advantages": [],
                    "competitive_gaps": [],
                    "innovation_level": "[Cutting-edge/Competitive/Catching up/Behind]",
                },
                "limitations": {
                    "known_limitations": [],
                    "data_privacy": {
                        "data_handling": "[How sensitive data is processed by AI]",
                        "gdpr_compliance": "[AI processing compliance]",
                        "data_residency": "[Where AI data is stored]",
                        "user_rights": "[Opt-out, deletion, etc.]",
                    },
                    "computational_requirements": "[Resource intensity]",
                    "language_support": [],
                    "regional_availability": "[Geographic limitations]",
                    "edge_cases": "[Scenarios where AI underperforms]",
                    "failure_handling": "[How system handles AI failures]",
                    "bias_mitigation": "[Approaches to reduce bias]",
                },
                "evolution_roadmap": {
                    "first_introduction": "[When AI was added]",
                    "major_milestones": [],
                    "recent_updates": [],
                    "maturity_state": "[Beta/GA/Mature/Production-hardened]",
                    "future_plans": [],
                    "research_publications": [],
                    "open_source_contributions": [],
                    "innovation_indicators": {
                        "rd_investment": "[If disclosed]",
                        "ai_team_size": "[If mentioned]",
                        "patents_filed": "[Number]",
                    },
                },
            },
            "ai_categories_to_investigate": [
                "Machine Learning Classification",
                "Large Language Models (LLM)",
                "Natural Language Processing (NLP)",
                "Computer Vision / Image Recognition",
                "Anomaly Detection",
                "Predictive Analytics",
                "Deep Learning",
                "Behavioral Analytics",
                "Generative AI",
                "Reinforcement Learning",
            ],
        }

    def _build_tech_specs_framework(self) -> dict:
        """Build technical specifications framework."""
        return {
            "system_requirements": {
                "minimum": "[Hardware/Software specs]",
                "recommended": "[Specs]",
            },
            "scalability": {
                "user_limits": "[If specified]",
                "data_volume": "[If specified]",
                "performance_benchmarks": "[If published]",
            },
            "supported_platforms": {
                "cloud": ["AWS", "Azure", "GCP"],
                "operating_systems": ["Windows", "Linux", "macOS"],
                "browsers": ["Chrome", "Firefox", "Safari", "Edge"],
            },
            "api": {
                "type": "[REST/SOAP/GraphQL]",
                "authentication": "[OAuth/API Key/etc.]",
                "documentation_quality": "[Assessment]",
                "sdk_languages": [],
                "rate_limits": "[If specified]",
            },
            "security_certifications": [],
            "compliance_frameworks": [],
        }

    def _generate_report(self, data: dict) -> str:
        """Generate the full product documentation analysis report."""
        vendor = data["vendor_name"]
        product = data.get("product_name")

        lines = [
            f"# Product Documentation Analysis: {vendor}",
            f"**Analysis Date:** {format_timestamp()}",
            f"**Documentation Version:** [Latest version analyzed]",
            f"**Products Covered:** [To be determined during orchestration]",
            f"**Analyst:** Claude Agent 4 - Product Documentation & AI/ML Analyzer",
            "",
            "---",
            "",
            "## Executive Product Summary",
            "",
            f"This report provides a comprehensive analysis of {vendor}'s product "
            f"offerings based on official documentation, technical resources, and "
            f"publicly available information. It includes an in-depth assessment of "
            f"AI/ML/LLM technologies used in the product.",
            "",
            f"**Product Focus:** {product or 'All Products'}",
            "**Product Philosophy:** [To be determined from documentation analysis]",
            "**Target Users:** [To be identified from documentation]",
            "**Deployment Models:** [To be identified from documentation]",
            "**AI/ML Integration Level:** [To be assessed during analysis]",
            "",
            "---",
            "",
            "## Product Portfolio",
            "",
            "### Product Suite Overview",
            "",
        ]

        # Product portfolio table
        headers = [
            "Product Name", "Category", "Purpose",
            "Target Segment", "AI/ML Enabled",
        ]
        rows = [["[Product]", "[Category]", "[Description]", "[Segment]", "[Y/N]"]]
        lines.append(format_table(headers, rows))

        lines.extend([
            "",
            "*To be populated during orchestration from official documentation.*",
            "",
            "### Product Relationships",
            "[To be mapped from documentation - suite vs standalone relationships]",
            "",
            "---",
            "",
        ])

        # Feature Breakdown Section
        lines.extend([
            "## Feature Analysis",
            "",
            "### Feature Categories",
            "",
        ])

        features = data["feature_framework"]["categories"]
        for key, cat in features.items():
            lines.extend([
                f"#### {cat['label']}",
                "",
            ])
            for subcat in cat["subcategories"]:
                lines.append(f"- **{subcat}:** [To be populated from documentation]")
            lines.append("")

        # Core Architecture Section
        lines.extend([
            "---",
            "",
            "## Core Architecture",
            "",
            "### Deployment Model",
            "- **Type:** [SaaS/On-prem/Hybrid]",
            "- **Architecture:** [Agent-based/Agentless/API-based]",
            "- **Technology Stack:** [If disclosed]",
            "- **AI/ML Components:** [Present/Absent]",
            "",
        ])

        # ==========================================
        # AI/ML DEEP DIVE SECTION (CRITICAL)
        # ==========================================
        lines.extend([
            "---",
            "",
            "## AI/ML/LLM TECHNOLOGY DEEP DIVE",
            "",
            "### AI/ML Technology Overview",
            "",
            "**AI/ML Maturity Level:** [Leading / Advanced / Moderate / Basic / None]",
            "**Primary AI Technologies:** [To be identified during analysis]",
            "**AI-Powered Features Count:** [X]",
            "**AI Implementation Approach:** [Proprietary / Third-party / Hybrid]",
            "",
            "**Overall Assessment:**",
            "[To be provided after comprehensive AI/ML analysis during orchestration]",
            "",
            "---",
            "",
            "### AI/ML Technologies to Investigate",
            "",
        ])

        for cat in data["ai_ml_framework"]["ai_categories_to_investigate"]:
            lines.append(f"- {cat}")

        # AI/ML Technology Template
        lines.extend([
            "",
            "---",
            "",
            "### AI/ML Technology Analysis Template",
            "",
            "*(The following template is applied to EACH AI/ML technology identified)*",
            "",
            "#### Technology: [Technology Name/Type]",
            "",
            "**Overview:**",
            "- **Type:** [ML / LLM / NLP / Computer Vision / Anomaly Detection / etc.]",
            "- **Specific Model/Framework:** [e.g., GPT-4, Custom BERT, Random Forest ensemble]",
            "- **Implementation:** [Proprietary / Third-party / Hybrid]",
            "- **First Introduced:** [Version/Date if available]",
            "",
            "**Use Case & Application:**",
            "",
            "- **Problem Solved:** [What business/security problem this AI solves]",
            "- **Features Utilizing This Technology:**",
            "  - [Feature 1]: [How AI is used]",
            "  - [Feature 2]: [How AI enhances capability]",
            "- **Concrete Example:** [Real-world scenario of AI in action]",
            "- **Target Users:** [Who benefits and how]",
            "",
            "**Technical Implementation:**",
            "",
            "- **Architecture Overview:**",
            "  ```",
            "  [Data flow description: Input -> Processing -> Model -> Output -> Action]",
            "  ```",
            "",
            "- **Training Details:**",
            "  - **Data Sources:** [Type of training data]",
            "  - **Training Method:** [Supervised/Unsupervised/RL/Transfer Learning]",
            "  - **Model Updates:** [Frequency and method]",
            "  - **Customer Control:** [Opt-out options]",
            "",
            "- **Inference & Deployment:**",
            "  - **Processing Location:** [Cloud/Edge/Hybrid]",
            "  - **Processing Mode:** [Real-time/Batch]",
            "  - **Latency:** [Response time]",
            "  - **Scalability:** [Approach]",
            "",
            "- **Technology Stack:**",
            "  - **Frameworks:** [TensorFlow/PyTorch/Custom]",
            "  - **Languages:** [Python/etc.]",
            "",
            "**Performance & Accuracy Metrics:**",
            "",
            "| Metric | Value | Source |",
            "|--------|-------|--------|",
            "| Accuracy | [X%] | [Source] |",
            "| False Positive Rate | [X%] | [Source] |",
            "| False Negative Rate | [X%] | [Source] |",
            "| Throughput | [X events/sec] | [Source] |",
            "| Latency | [X ms] | [Source] |",
            "",
            "**Competitive Differentiation:**",
            "",
            "| Aspect | This Vendor | Competitors | Industry Standard |",
            "|--------|-------------|-------------|-------------------|",
            "| AI Model Type | [Type] | [Types] | [Standard] |",
            "| Accuracy | [Rate] | [Rates] | [Benchmark] |",
            "| Unique Feature | [Feature] | [Features] | N/A |",
            "",
            "- **Advantages:** [What gives vendor an edge]",
            "- **Gaps:** [Where competitors are superior]",
            "- **Innovation Level:** [Cutting-edge/Competitive/Behind]",
            "",
            "**Limitations & Constraints:**",
            "",
            "1. **[Limitation]:** [Description and impact]",
            "2. **[Limitation]:** [Description and impact]",
            "",
            "- **Data Privacy:** [How AI handles sensitive data]",
            "- **Language Support:** [For NLP/LLM capabilities]",
            "- **Edge Cases:** [Where AI underperforms]",
            "- **Failure Handling:** [Fallback mechanisms]",
            "",
            "**Evolution & Roadmap:**",
            "",
            "- **Historical Milestones:**",
            "  - [Version X] - [AI capability added] - [Date]",
            "- **Recent Updates:** [From latest release notes]",
            "- **Maturity:** [Beta/GA/Mature]",
            "- **Future Plans:** [If publicly disclosed]",
            "- **Research Publications:** [Papers, conferences]",
            "- **Open Source:** [GitHub contributions]",
            "",
            "---",
            "",
        ])

        # AI/ML Summary Section
        lines.extend([
            "### AI/ML Technology Stack Summary",
            "",
        ])

        headers = [
            "Technology", "Type", "Primary Use Case",
            "Maturity", "Competitive Edge", "Main Limitation",
        ]
        rows = [["[Tech]", "[Type]", "[Use case]", "[Status]", "[Level]", "[Limitation]"]]
        lines.append(format_table(headers, rows))

        lines.extend([
            "",
            "*To be populated during orchestration from AI/ML analysis.*",
            "",
            "### Overall AI/ML Assessment",
            "",
            "**AI/ML Strengths:**",
            "1. [To be identified]",
            "",
            "**AI/ML Weaknesses:**",
            "1. [To be identified]",
            "",
            "**Strategic AI Assessment:**",
            "- **AI Implementation Philosophy:** [AI-First vs AI-Enhanced]",
            "- **Market Position (AI Capabilities):** [Leader/Strong/Average/Behind]",
            "- **Innovation Level:** [Cutting-edge/Competitive/Fast Follower/Behind]",
            "- **AI Differentiation:** [Unique value proposition from AI]",
            "",
            "**Customer Perception of AI (Cross-reference with Agent 2):**",
            "- **Positive Mentions:** [To be cross-referenced]",
            "- **Negative Mentions:** [To be cross-referenced]",
            "- **Feature Requests:** [AI capabilities customers want]",
            "",
            "### AI/ML Competitive Landscape",
            "",
            "*Comparison with competitors from Agent 1 data - to be completed during orchestration.*",
            "",
        ])

        # Release Notes Section
        lines.extend([
            "---",
            "",
            "## Latest Release Notes Summary",
            "",
            "### Version [X.X] - Released [Date]",
            "",
            "#### New Features",
            "- [To be populated from latest release notes]",
            "",
            "#### Improvements",
            "- [To be populated]",
            "",
            "#### AI/ML Updates",
            "- [AI-specific enhancements to be highlighted]",
            "",
            "#### Bug Fixes",
            "- [Major fixes only]",
            "",
            "#### Deprecated Features",
            "- [If applicable]",
            "",
        ])

        # API Section
        lines.extend([
            "---",
            "",
            "## API & Developer Resources",
            "",
            "### API Overview",
            "- **API Type:** [REST/SOAP/GraphQL]",
            "- **Authentication:** [OAuth/API Key/etc.]",
            "- **Documentation Quality:** [Assessment]",
            "- **SDK Availability:** [Languages]",
            "",
            "### AI/ML API Endpoints",
            "- [To be identified from API documentation]",
            "",
        ])

        # Security & Compliance
        lines.extend([
            "---",
            "",
            "## Security & Compliance Certifications",
            "",
            "### Security Certifications",
            "- [To be populated from documentation]",
            "",
            "### Compliance Frameworks Supported",
            "- [To be populated from documentation]",
            "",
            "### Data Residency",
            "- [To be populated from documentation]",
            "- **AI Training/Inference Data Location:** [Where AI processes data]",
            "",
        ])

        # Documentation Quality
        lines.extend([
            "---",
            "",
            "## Documentation Quality Assessment",
            "",
            "### Coverage",
            "- **Completeness:** [To be assessed]",
            "- **AI/ML Documentation Quality:** [To be assessed]",
            "- **Gaps Identified:** [To be listed]",
            "",
            "### Accuracy",
            "- **Validation Status:** [Cross-referenced with other sources]",
            "",
            "### Usability",
            "- **Organization:** [Assessment]",
            "- **Search Functionality:** [Assessment]",
            "- **Examples/Tutorials:** [Quality]",
            "",
        ])

        # Search Queries
        lines.extend([
            "---",
            "",
            "## Search Queries for Enrichment",
            "",
            "### Product Documentation Queries",
            "",
        ])
        for query in data["doc_search_queries"]:
            lines.append(f"- `{query}`")

        lines.extend(["", "### AI/ML-Specific Queries", ""])
        for query in data["ai_ml_search_queries"]:
            lines.append(f"- `{query}`")

        # Sources
        lines.extend([
            "",
            "---",
            "",
            "## Sources",
            "",
            "### Official Documentation",
            "*To be populated during orchestration.*",
            "",
            "### GitHub Repositories",
            "*To be populated during orchestration.*",
            "",
            "### Validated Third-Party Sources",
            "*To be populated during orchestration.*",
        ])

        return "\n".join(lines)
