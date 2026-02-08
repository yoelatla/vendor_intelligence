"""
Configuration for the Vendor Intelligence System.
"""

from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


# Data Security vendor categories
VENDOR_CATEGORIES = [
    "DLP",
    "Cloud Security",
    "SSPM",
    "DSPM",
    "Outbound CASB",
    "Data Security",
    "SASE",
    "Zero Trust",
    "Email Security",
    "Endpoint Security",
]

# Category keywords for auto-detection
CATEGORY_KEYWORDS = {
    "DLP": [
        "data loss prevention", "data leak", "dlp", "data protection",
        "sensitive data", "data exfiltration",
    ],
    "Cloud Security": [
        "cloud security", "cloud workload", "cwpp", "cspm",
        "cloud posture", "cloud native",
    ],
    "SSPM": [
        "saas security", "sspm", "saas posture", "saas management",
        "saas misconfiguration",
    ],
    "DSPM": [
        "data security posture", "dspm", "data discovery",
        "data classification", "shadow data",
    ],
    "Outbound CASB": [
        "casb", "cloud access security", "shadow it",
        "cloud application security", "sanctioned apps",
    ],
    "Data Security": [
        "data security", "data governance", "data privacy",
        "encryption", "tokenization",
    ],
}

# Review platforms to scan
REVIEW_PLATFORMS = [
    {"name": "G2", "search_suffix": "reviews G2", "url_pattern": "g2.com"},
    {"name": "Gartner Peer Insights", "search_suffix": "Gartner Peer Insights reviews", "url_pattern": "gartner.com/reviews"},
    {"name": "TrustRadius", "search_suffix": "reviews TrustRadius", "url_pattern": "trustradius.com"},
    {"name": "Capterra", "search_suffix": "reviews Capterra", "url_pattern": "capterra.com"},
    {"name": "PeerSpot", "search_suffix": "reviews PeerSpot", "url_pattern": "peerspot.com"},
]

# Secondary review sources
SECONDARY_REVIEW_SOURCES = [
    {"name": "Reddit", "subreddits": ["cybersecurity", "netsec", "sysadmin"]},
    {"name": "Spiceworks", "search_suffix": "Spiceworks community"},
    {"name": "LinkedIn", "search_suffix": "LinkedIn discussion"},
]

# Market research sources
MARKET_RESEARCH_SOURCES = [
    "Gartner Magic Quadrant",
    "Forrester Wave",
    "IDC MarketScape",
    "GigaOm Radar",
]

# Industry publications
INDUSTRY_PUBLICATIONS = [
    "Dark Reading",
    "CSO Online",
    "SC Magazine",
    "Cybersecurity Dive",
    "TechCrunch",
    "VentureBeat",
    "SecurityWeek",
]

# AI/ML search terms for Agent 4
AI_ML_SEARCH_TERMS = [
    "AI technology",
    "machine learning",
    "large language model LLM",
    "artificial intelligence architecture",
    "ML model",
    "AI research paper",
    "NLP natural language processing",
    "anomaly detection AI",
    "predictive analytics",
    "neural network",
    "GitHub machine learning",
    "technical whitepaper AI",
    "AI patent",
    "TensorFlow PyTorch",
    "GPT BERT transformer",
    "deep learning",
    "computer vision",
    "generative AI",
]

# Pain point categories for review analysis
PAIN_POINT_CATEGORIES = [
    "Performance/Speed",
    "Usability/UX",
    "Integration Challenges",
    "Support Quality",
    "Pricing/Value",
    "Feature Gaps",
    "Reliability/Uptime",
    "Documentation Quality",
    "Deployment Complexity",
    "Scalability",
    "False Positives",
    "Policy Management",
]

# Gap analysis categories
GAP_CATEGORIES = [
    "Security Capabilities",
    "AI/ML Capabilities",
    "Integration & Connectivity",
    "Compliance & Governance",
    "Usability & UX",
    "Automation Capabilities",
    "Reporting & Analytics",
    "Platform & Infrastructure",
]

# Minimum thresholds
MIN_COMPETITORS = 10
MIN_REVIEWS = 50
MIN_SOURCES = 15
REVIEW_LOOKBACK_MONTHS = 12

# Issue severity thresholds
CRITICAL_MENTION_THRESHOLD = 10
COMMON_MENTION_THRESHOLD = 3


@dataclass
class AnalysisConfig:
    """Configuration for a vendor analysis run."""
    vendor_name: str
    product_name: Optional[str] = None
    user_provided_competitors: Optional[list] = None
    auto_detect_competitors: bool = True
    date_range: str = "2025-2026"
    review_months: int = REVIEW_LOOKBACK_MONTHS
    min_competitors: int = MIN_COMPETITORS
    min_reviews: int = MIN_REVIEWS
    min_sources: int = MIN_SOURCES
    output_dir: str = "output"
    timestamp: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))

    # Google Drive settings
    google_drive_credentials: Optional[str] = None  # Path to credentials JSON
    google_drive_folder_id: Optional[str] = None  # Parent folder ID in Drive
    upload_to_google_drive: bool = True  # Auto-upload when credentials available

    @property
    def analysis_id(self) -> str:
        safe_name = self.vendor_name.replace(" ", "_").replace("/", "-")
        return f"{safe_name}_{self.timestamp}"
