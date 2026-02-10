# CLAUDE.md

## Project Overview
Python 3.10+ multi-agent system for automated competitive intelligence analysis of Data Security vendors. Uses async/await orchestration with 7 specialized agents running in coordinated phases. Zero required external dependencies (standard library only); optional deps in `requirements.txt`.

## Build & Install
```bash
pip install -e .
```

## Running
```bash
python -m vendor_intelligence --vendor "VendorName"
python -m vendor_intelligence --vendor "VendorName" --product "ProductName" --competitors "A,B,C" --output ./reports --json-output results.json
python -m vendor_intelligence --help
```

## Testing
No formal test framework. Validate changes with a functional test run:
```bash
python -m vendor_intelligence --vendor "TestVendor" --output /tmp/test
```

## Code Style
- Python 3.10+ with type hints required on all functions
- Async-first: use `async/await` for agent methods
- All agents inherit from `BaseAgent` (`vendor_intelligence/agents/base.py`)
- Single responsibility per agent
- Reports use Markdown formatting via `utils/report_writer.py`

## Architecture
Three-phase orchestration managed by `vendor_intelligence/orchestrator.py`:

- **Phase 1 (Sequential):** Agent 3 creates output folder structure
- **Phase 2 (Parallel):** Agents 1, 2, 4 gather intelligence concurrently
- **Phase 3 (Sequential):** Agents 5, 6, 7 perform QA, gap analysis, executive summary

### Key Files
| File | Purpose |
|------|---------|
| `vendor_intelligence/__main__.py` | CLI entry point (argparse) |
| `vendor_intelligence/orchestrator.py` | Master orchestrator, 3-phase execution |
| `vendor_intelligence/config.py` | Constants, thresholds, category definitions |
| `vendor_intelligence/agents/base.py` | Abstract base class for all agents |
| `vendor_intelligence/agents/agent_*.py` | 7 specialized agents |
| `vendor_intelligence/utils/web_search.py` | Async web search client |
| `vendor_intelligence/utils/report_writer.py` | Markdown report generator |

## Sensitive Files — Do Not Commit
`.env`, `service_account.json`, `credentials.json`, `token.json`, `*.key.json`
