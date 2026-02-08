"""
Agent modules for the Vendor Intelligence System.

Agents:
    Agent 1: Market Research & Competitive Analysis
    Agent 2: Review Intelligence Scanner
    Agent 3: Folder Structure Creator
    Agent 4: Product Documentation Analyzer (with AI/ML Deep Dive)
    Agent 5: Quality Assurance & Validation Engine
    Agent 6: Product Gap Analysis
    Agent 7: Executive Summary Generator
"""

from vendor_intelligence.agents.base import BaseAgent, AgentResult
from vendor_intelligence.agents.agent_1_market_research import MarketResearchAgent
from vendor_intelligence.agents.agent_2_review_scanner import ReviewScannerAgent
from vendor_intelligence.agents.agent_3_folder_creator import FolderCreatorAgent
from vendor_intelligence.agents.agent_4_product_docs import ProductDocsAgent
from vendor_intelligence.agents.agent_5_qa_validation import QAValidationAgent
from vendor_intelligence.agents.agent_6_gap_analysis import GapAnalysisAgent
from vendor_intelligence.agents.agent_7_executive_summary import ExecutiveSummaryAgent

__all__ = [
    "BaseAgent",
    "AgentResult",
    "MarketResearchAgent",
    "ReviewScannerAgent",
    "FolderCreatorAgent",
    "ProductDocsAgent",
    "QAValidationAgent",
    "GapAnalysisAgent",
    "ExecutiveSummaryAgent",
]
