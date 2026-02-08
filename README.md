<div align="center">

# 🛡️ Multi-Agent Vendor Intelligence System

**Transform weeks of manual competitive research into a single automated workflow.**

A 7-agent AI orchestration system that conducts comprehensive competitive intelligence analysis for Data Security vendors — DLP, Cloud Security, SSPM, DSPM, CASB, and more.

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agents: 7](https://img.shields.io/badge/agents-7-purple.svg)](#architecture)
[![Status: Production Ready](https://img.shields.io/badge/status-production%20ready-brightgreen.svg)](#quick-start)

</div>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Guide](#usage-guide)
- [Agent Descriptions](#agent-descriptions)
- [Output Structure](#output-structure)
- [AI/ML Deep Dive Analysis](#aiml-deep-dive-analysis)
- [Configuration](#configuration)
- [Use Cases](#use-cases)
- [Performance](#performance)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [FAQ](#faq)

---

## Overview

The **Multi-Agent Vendor Intelligence System** automates the competitive intelligence lifecycle for the Data Security market. It deploys seven specialized AI agents — running in parallel where possible — to research markets, scan customer reviews, dissect product documentation, validate data quality, identify product gaps, and synthesize everything into executive-ready reports.

**Who it's for:** Senior Product Managers, CPOs, and VPs of Product who need to understand the competitive landscape quickly without spending weeks on manual research.

**What it produces:** Six structured Markdown reports covering market research, customer intelligence, product analysis (with AI/ML deep dive), QA validation, gap analysis, and a one-page executive summary — all organized in a date-stamped output folder ready for stakeholder review.

---

## Features

### Core Intelligence Capabilities

- **Market Research & Competitive Analysis** — Auto-detects vendor category, identifies 10-15 competitors, maps market positioning, and tracks 2025-2026 industry trends
- **Customer Review Intelligence** — Aggregates reviews from G2, Gartner Peer Insights, TrustRadius, Capterra, Reddit, and more with sentiment analysis and pain point identification
- **Product Documentation Analysis** — Complete feature mapping, architecture assessment, API review, and release notes analysis
- **AI/ML Technology Deep Dive** — Comprehensive analysis of vendor AI capabilities across 10 technology categories including LLMs, NLP, anomaly detection, and behavioral analytics
- **Quality Assurance & Validation** — Automated hallucination detection, source verification, cross-agent consistency checks, and 100-point quality scoring
- **Product Gap Analysis** — Feature parity comparison, AI/ML capability gaps, customer-requested features, and prioritized roadmap recommendations
- **Executive Summary** — One-page synthesis designed for < 5 minute executive reading

### Technical Capabilities

- **Async parallel execution** — Phase 2 agents run concurrently for maximum throughput
- **Configurable competitor lists** — User-provided or auto-detected from a 70+ vendor database across 6 categories
- **Cross-agent data flow** — Agent 5 validates outputs from Agents 1/2/4; Agent 6 synthesizes across all; Agent 7 distills everything
- **Structured Markdown output** — Clean reports with tables, hierarchical sections, and source citations
- **CLI interface** — Single command to launch full analysis with JSON results export
- **Zero external dependencies** — Runs on Python 3.10+ standard library only

---

## Architecture

The system executes in three phases with strict dependency ordering:

```
┌─────────────────────────────────────────────────────┐
│  PHASE 1: SETUP (Sequential)                        │
│  ┌────────────────────────────────────────────┐     │
│  │  Agent 3: Folder Structure Creator          │     │
│  │  Creates output directory hierarchy         │     │
│  └────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────┘
                        |
                        v
┌─────────────────────────────────────────────────────┐
│  PHASE 2: DATA GATHERING (Parallel)                 │
│  ┌──────────────┐ ┌───────────────┐ ┌────────────┐ │
│  │  Agent 1:     │ │  Agent 2:      │ │  Agent 4:   │ │
│  │  Market       │ │  Review        │ │  Product    │ │
│  │  Research &   │ │  Intelligence  │ │  Docs &     │ │
│  │  Competitive  │ │  Scanner       │ │  AI/ML      │ │
│  │  Analysis     │ │                │ │  Deep Dive  │ │
│  └──────────────┘ └───────────────┘ └────────────┘ │
└─────────────────────────────────────────────────────┘
                        |
                        v
┌─────────────────────────────────────────────────────┐
│  PHASE 3: ANALYSIS & SYNTHESIS (Sequential)         │
│  ┌────────────────────────────────────────────┐     │
│  │  Agent 5: QA Validation Engine              │     │
│  │  Validates all outputs, detects issues      │     │
│  └────────────────────────────────────────────┘     │
│                       |                              │
│                       v                              │
│  ┌────────────────────────────────────────────┐     │
│  │  Agent 6: Product Gap Analysis              │     │
│  │  Identifies competitive gaps & priorities   │     │
│  └────────────────────────────────────────────┘     │
│                       |                              │
│                       v                              │
│  ┌────────────────────────────────────────────┐     │
│  │  Agent 7: Executive Summary Generator       │     │
│  │  Synthesizes one-page leadership brief      │     │
│  └────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────┘
```

### Data Flow

```
Agent 1 (Market Data)  ──┐
Agent 2 (Review Data)  ──┼──> Agent 5 (Validation) ──> Agent 6 (Gap Analysis) ──> Agent 7 (Summary)
Agent 4 (Product Data) ──┘
```

---

## Prerequisites

- **Python 3.10+** — Uses `match` statements, modern type hints, and `asyncio.TaskGroup`-compatible patterns
- **No external packages required** — The base system uses only the Python standard library

### Optional (for enhanced functionality)

| Package | Purpose |
|---------|---------|
| `httpx` | Async HTTP client for live web fetching |
| `rich` | Enhanced terminal output with progress bars |
| `google-api-python-client` | Google Drive integration for direct upload |

---

## Installation

```bash
# Clone the repository
git clone https://github.com/your-org/vendor-intelligence-system.git
cd vendor-intelligence-system

# (Optional) Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Install (no external dependencies needed for base system)
pip install -e .

# Verify installation
python -m vendor_intelligence --help
```

---

## Quick Start

Run a full analysis with a single command:

```bash
# Analyze a vendor with auto-detected competitors
python -m vendor_intelligence --vendor "Zscaler"

# Focus on a specific product
python -m vendor_intelligence --vendor "Netskope" --product "Netskope One"

# Provide your own competitor list
python -m vendor_intelligence --vendor "Varonis" --competitors "BigID,Cyera,Securiti,Rubrik"

# Export JSON results summary
python -m vendor_intelligence --vendor "Proofpoint" --output ./reports --json-output results.json
```

### What Happens

1. **Agent 3** creates a date-stamped output folder with six subfolders
2. **Agents 1, 2, 4** run in parallel — market research, review scanning, and product documentation analysis (including AI/ML deep dive)
3. **Agent 5** validates all outputs against quality criteria (100-point scoring)
4. **Agent 6** identifies competitive gaps and prioritizes recommendations
5. **Agent 7** generates a one-page executive summary
6. All reports are written to the output directory as structured Markdown

---

## Usage Guide

### CLI Reference

```
python -m vendor_intelligence [OPTIONS]

Required:
  --vendor VENDOR          Name of the vendor to analyze

Optional:
  --product PRODUCT        Specific product to focus on (default: all products)
  --competitors LIST       Comma-separated competitor names (default: auto-detect)
  --output DIR             Output directory (default: ./output)
  --json-output PATH       Path to write JSON results summary
  --verbose, -v            Enable verbose logging
```

### Competitor Options

**Auto-detection (default):** The system identifies the vendor's category (DLP, DSPM, SSPM, CASB, Cloud Security, or Data Security) and selects 10-15 competitors from its built-in database.

**User-provided list:** Pass `--competitors` with a comma-separated list. If you provide fewer than 5, the system supplements with auto-detected competitors to ensure comprehensive coverage.

### Programmatic Usage

```python
import asyncio
from vendor_intelligence.orchestrator import run_analysis

result = asyncio.run(run_analysis(
    vendor_name="Zscaler",
    product_name="Data Protection",
    competitors=["Netskope", "Palo Alto Networks", "Forcepoint"],
    output_dir="./reports",
))

print(f"Status: {result['status']}")
print(f"QA Score: {result['qa_summary']['quality_score']}/100")
print(f"Output: {result['output_directory']}")
```

---

## Agent Descriptions

### Agent 3: Folder Structure Creator

**Phase:** 1 (runs first) &nbsp;|&nbsp; **Priority:** Highest

Creates the organized output directory before any other agent runs. Generates a `MANIFEST.md` with analysis metadata and agent execution tracking.

### Agent 1: Market Research & Competitive Analysis

**Phase:** 2 (parallel) &nbsp;|&nbsp; **Output:** `01_Market_Research/`

Conducts deep market research for the 2025-2026 timeframe. Auto-detects vendor category, identifies competitors (or accepts a user-provided list), maps competitive positioning, and analyzes SMB vs. Enterprise pain points and buying criteria. Includes technology landscape assessment and market trend tracking.

**Competitor database:** 70+ vendors across 6 categories (DLP, DSPM, SSPM, CASB, Cloud Security, Data Security) with market position and target segment metadata.

### Agent 2: Review Intelligence Scanner

**Phase:** 2 (parallel) &nbsp;|&nbsp; **Output:** `02_Customer_Reviews_Analysis/`

Scans customer reviews across G2, Gartner Peer Insights, TrustRadius, Capterra, PeerSpot, Reddit, Spiceworks, and LinkedIn. Categorizes issues into 12 pain point categories, tracks feature requests, identifies churn indicators, and documents competitive mentions. Uses configurable severity thresholds (critical: 10+ mentions, common: 3-9 mentions).

### Agent 4: Product Documentation Analyzer (with AI/ML Deep Dive)

**Phase:** 2 (parallel) &nbsp;|&nbsp; **Output:** `03_Product_Documentation/`

Maps the complete product portfolio, analyzes features across 7 categories (security, compliance, integration, automation, analytics, admin, UX), and reviews technical specifications. Includes a comprehensive **AI/ML technology deep dive** — see [AI/ML Deep Dive Analysis](#aiml-deep-dive-analysis).

### Agent 5: Quality Assurance & Validation Engine

**Phase:** 3 (sequential, after 1/2/4) &nbsp;|&nbsp; **Output:** `04_QA_Validation_Reports/`

Validates all agent outputs with completeness checks, hallucination detection, cross-agent consistency validation, and data quality auditing. Produces a 100-point quality score and outputs a status of APPROVED, APPROVED WITH NOTES, or REQUIRES REVISION.

### Agent 6: Product Gap Analysis

**Phase:** 3 (sequential, after 5) &nbsp;|&nbsp; **Output:** `05_Gap_Analysis/`

Cross-references Agent 1 (competitors), Agent 2 (customer requests), and Agent 4 (vendor capabilities) to identify feature parity gaps, AI/ML capability gaps, and market trend alignment gaps. Produces prioritized recommendations with an effort-vs-impact matrix and a strategic roadmap (0-3 months, 3-6 months, 6-12 months, 12+ months).

### Agent 7: Executive Summary Generator

**Phase:** 3 (runs last) &nbsp;|&nbsp; **Output:** `06_Executive_Summary/`

Synthesizes all agent outputs into a one-page executive summary optimized for < 5 minute reading. Includes situation overview, top 3 strategic highlights, competitive landscape snapshot, customer voice summary, AI/ML position, critical gaps, and recommended actions with timelines.

---

## Output Structure

Each analysis generates a date-stamped folder:

```
[Vendor]_Competitive_Intelligence_[YYYY-MM-DD]/
├── MANIFEST.md                          # Analysis metadata and agent tracking
├── 01_Market_Research/
│   └── [Vendor]_Market_Research.md      # Competitive landscape, trends, segmentation
├── 02_Customer_Reviews_Analysis/
│   └── [Vendor]_Review_Intelligence.md  # Sentiment, pain points, feature requests
├── 03_Product_Documentation/
│   └── [Vendor]_Product_Documentation.md # Features, specs, AI/ML deep dive
├── 04_QA_Validation_Reports/
│   └── [Vendor]_QA_Validation.md        # Quality score, validation results
├── 05_Gap_Analysis/
│   └── [Vendor]_Gap_Analysis.md         # Competitive gaps, prioritized roadmap
└── 06_Executive_Summary/
    └── [Vendor]_Executive_Summary.md    # One-page leadership brief
```

Reports are structured Markdown with tables, hierarchical sections, source citations, and cross-references between agents.

---

## AI/ML Deep Dive Analysis

One of the system's key differentiators is the comprehensive AI/ML technology analysis built into Agent 4. When analyzing a vendor's products, the system investigates:

### 10 AI Technology Categories

| Category | What's Analyzed |
|----------|----------------|
| Machine Learning Classification | Data classification, sensitivity labeling |
| Large Language Models (LLM) | Policy generation, investigation assistance |
| Natural Language Processing | Content inspection, context understanding |
| Computer Vision | Document/image analysis for sensitive content |
| Anomaly Detection | Behavioral baselines, deviation identification |
| Predictive Analytics | Risk scoring, threat prediction |
| Deep Learning | Neural network architectures, training approaches |
| Behavioral Analytics (UEBA) | User/entity behavior modeling |
| Generative AI | Security copilots, report generation |
| Reinforcement Learning | Adaptive policy optimization |

### For Each Technology Found

The analysis covers seven dimensions:

1. **Identification** — Type, model/framework, proprietary vs. third-party
2. **Use Case** — Problem solved, features using the technology, concrete examples
3. **Technical Implementation** — Training data, methods, update frequency, inference architecture, tech stack
4. **Performance Metrics** — Accuracy, false positive/negative rates, throughput, latency
5. **Competitive Differentiation** — Unique aspects, patents, published research, head-to-head comparison
6. **Limitations** — Known constraints, data privacy handling, language support, failure modes
7. **Evolution & Roadmap** — Historical development, maturity state, future plans, R&D indicators

The AI/ML analysis feeds directly into Agent 6's gap analysis, enabling precise identification of where a vendor's AI capabilities lag behind competitors.

---

## Configuration

### Analysis Parameters

Key thresholds are defined in `vendor_intelligence/config.py`:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `MIN_COMPETITORS` | 10 | Minimum competitors to identify |
| `MIN_REVIEWS` | 50 | Target review count for analysis |
| `MIN_SOURCES` | 15 | Minimum authoritative sources |
| `REVIEW_LOOKBACK_MONTHS` | 12 | Review analysis time window |
| `CRITICAL_MENTION_THRESHOLD` | 10 | Mentions to flag as critical issue |
| `COMMON_MENTION_THRESHOLD` | 3 | Mentions to flag as common issue |

### Vendor Category Database

The system includes pre-built competitor databases for 6 categories:

- **DLP** — 15 vendors (Symantec, Forcepoint, Netskope, Zscaler, etc.)
- **DSPM** — 14 vendors (Varonis, BigID, Cyera, Securiti, etc.)
- **SSPM** — 12 vendors (AppOmni, Adaptive Shield, Wing Security, etc.)
- **Outbound CASB** — 12 vendors (Netskope, Zscaler, Skyhigh, etc.)
- **Cloud Security** — 12 vendors (Prisma Cloud, Wiz, CrowdStrike, etc.)
- **Data Security** — 14 vendors (Varonis, Microsoft Purview, Thales, etc.)

### Programmatic Configuration

```python
from vendor_intelligence.config import AnalysisConfig

config = AnalysisConfig(
    vendor_name="Zscaler",
    product_name="Data Protection",
    user_provided_competitors=["Netskope", "Forcepoint"],
    auto_detect_competitors=False,  # Use only user-provided list
    date_range="2025-2026",
    review_months=12,
    min_competitors=10,
    output_dir="./reports",
)
```

---

## Use Cases

### Competitive Product Strategy

> "We're launching a new DLP product. What gaps do the top 10 competitors have that we can exploit?"

Run the system against a leading competitor to identify their weaknesses, then use the gap analysis to inform your feature roadmap.

### Quarterly Competitive Review

> "Our CPO wants a competitive landscape update for the board meeting."

Generate the executive summary for your top 3-5 competitors and hand the one-page briefs directly to leadership.

### AI/ML Investment Decisions

> "Should we build our own ML-based data classifier or integrate a third-party solution?"

The AI/ML deep dive shows exactly what competitors are doing — proprietary models vs. off-the-shelf, training approaches, performance benchmarks — so you can make an informed build-vs-buy decision.

### New Market Entry Assessment

> "We're expanding from DLP into DSPM. Who are the players and what do customers actually want?"

The system maps the entire DSPM competitive landscape, identifies customer pain points from reviews, and highlights the feature gaps where a new entrant could differentiate.

---

## Performance

| Metric | Value |
|--------|-------|
| Agents executed | 7 |
| Parallel agents (Phase 2) | 3 |
| Competitors analyzed | 10-15 per run |
| Review platforms scanned | 8+ (5 primary, 3+ secondary) |
| Pain point categories | 12 |
| AI/ML technology categories | 10 |
| Gap analysis categories | 8 |
| Output reports | 6 + manifest |
| Total report lines | ~1,500+ per analysis |
| QA validation points | 100-point scoring system |
| External dependencies | 0 (standard library only) |

---

## Troubleshooting

### Common Issues

**No competitors found for my vendor**

The vendor's name might not match a known category. Use `--competitors` to provide an explicit list, or check `vendor_intelligence/config.py` to see supported categories.

**QA score is low**

A score below 60 triggers "REQUIRES REVISION." This typically means data enrichment is needed during orchestration (web search results populate the templates). Check the QA report in `04_QA_Validation_Reports/` for specific issues.

**Import errors**

Ensure you're running Python 3.10+ and the package is installed:
```bash
python --version  # Should be 3.10+
pip install -e .
```

### Debug Mode

Enable verbose logging for detailed agent execution traces:

```bash
python -m vendor_intelligence --vendor "Zscaler" --verbose
```

Logs include timestamps, agent lifecycle events, and data flow details.

---

## Roadmap

### Planned Enhancements

- [ ] **Live web search integration** — Real-time data enrichment via search APIs during agent execution
- [ ] **Google Drive upload** — Direct upload of reports to Google Drive with folder sharing
- [ ] **Interactive competitor selection** — Terminal-based UI for reviewing and confirming auto-detected competitors
- [ ] **PDF export** — Generate print-ready PDF reports alongside Markdown
- [ ] **Incremental updates** — Re-run analysis against a previous baseline to track changes over time
- [ ] **Webhook notifications** — Notify Slack/Teams/email when analysis completes
- [ ] **Custom agent plugins** — Extend the system with domain-specific agents
- [ ] **Dashboard UI** — Web-based dashboard for viewing and comparing analyses

---

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Run the test suite: `python -m vendor_intelligence --vendor "TestVendor" --output /tmp/test`
5. Commit with clear messages
6. Open a pull request

### Code Standards

- Python 3.10+ with type hints
- Async-first design (use `async/await` for agent methods)
- All agents inherit from `BaseAgent`
- Reports use Markdown formatting via `utils/report_writer.py`
- Keep agents focused — each agent has a single responsibility

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## FAQ

**Q: Does this system make live web requests during analysis?**

The base system generates structured analysis frameworks with search query plans. The `WebSearchClient` in `utils/web_search.py` is designed to be extended with live search providers (e.g., Google Custom Search API, Bing API). When integrated with Claude Code's orchestration layer, agents execute web searches through Claude's built-in tools.

**Q: Can I add my own vendor categories?**

Yes. Edit `VENDOR_CATEGORIES` and `CATEGORY_KEYWORDS` in `config.py`, then add a competitor list for the new category in `agent_1_market_research.py`'s `_get_known_competitors` method.

**Q: How does the AI/ML deep dive work if a vendor doesn't use AI?**

Agent 4 searches for AI/ML capabilities across 15+ search query patterns. If no AI technologies are found, the report documents this finding with an AI maturity level of "None" — which is itself a valuable competitive intelligence data point.

**Q: Can I run just one agent instead of all seven?**

Yes. Each agent is a standalone class. Import it directly:

```python
from vendor_intelligence.agents import MarketResearchAgent
from vendor_intelligence.config import AnalysisConfig
from vendor_intelligence.utils.web_search import WebSearchClient
from vendor_intelligence.utils.report_writer import ReportWriter

config = AnalysisConfig(vendor_name="Zscaler")
agent = MarketResearchAgent(config, WebSearchClient(), ReportWriter("./output"))
result = asyncio.run(agent.execute())
```

**Q: What's the quality score based on?**

Agent 5 starts at 100 and deducts points for: missing agent results (-20), insufficient competitor count (-5), below-threshold review count (-5), missing frameworks (-2 each), and critical issues (-15 each). A score of 80+ is "High" reliability, 60-79 is "Medium," and below 60 is "Low."

---

## Acknowledgments

- Built for the [Claude Code](https://claude.ai/code) agent ecosystem by [Anthropic](https://www.anthropic.com/)
- Competitive intelligence frameworks informed by Gartner, Forrester, and IDC methodologies
- Vendor databases compiled from public market research and analyst reports
