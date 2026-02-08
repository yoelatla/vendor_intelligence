"""
CLI entry point for the Multi-Agent Vendor Intelligence System.

Usage:
    python -m vendor_intelligence --vendor "Zscaler"
    python -m vendor_intelligence --vendor "Netskope" --product "Netskope One"
    python -m vendor_intelligence --vendor "Varonis" --competitors "BigID,Cyera,Securiti"
"""

import argparse
import asyncio
import json
import logging
import sys
from pathlib import Path

from vendor_intelligence.config import AnalysisConfig
from vendor_intelligence.orchestrator import VendorIntelligenceOrchestrator


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        prog="vendor_intelligence",
        description=(
            "Multi-Agent Vendor Intelligence System - "
            "Comprehensive competitive intelligence analysis for "
            "Data Security vendors"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --vendor "Zscaler"
  %(prog)s --vendor "Netskope" --product "Netskope One"
  %(prog)s --vendor "Varonis" --competitors "BigID,Cyera,Securiti"
  %(prog)s --vendor "Proofpoint" --output ./reports --verbose

        """,
    )

    parser.add_argument(
        "--vendor",
        required=True,
        help="Name of the vendor to analyze",
    )

    parser.add_argument(
        "--product",
        default=None,
        help="Specific product to focus on (default: all products)",
    )

    parser.add_argument(
        "--competitors",
        default=None,
        help=(
            "Comma-separated list of competitor names "
            "(default: auto-detect)"
        ),
    )

    parser.add_argument(
        "--output",
        default="output",
        help="Output directory for reports (default: ./output)",
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging",
    )

    parser.add_argument(
        "--json-output",
        default=None,
        help="Path to write JSON results summary",
    )

    return parser.parse_args()


def setup_logging(verbose: bool = False) -> None:
    """Configure logging."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )


async def main_async(args: argparse.Namespace) -> int:
    """Async main entry point."""
    # Parse competitors list
    competitors = None
    if args.competitors:
        competitors = [c.strip() for c in args.competitors.split(",") if c.strip()]

    # Create configuration
    config = AnalysisConfig(
        vendor_name=args.vendor,
        product_name=args.product,
        user_provided_competitors=competitors,
        auto_detect_competitors=competitors is None,
        output_dir=args.output,
    )

    # Create and run orchestrator
    orchestrator = VendorIntelligenceOrchestrator(config)
    result = await orchestrator.run()

    # Write JSON output if requested
    if args.json_output:
        json_path = Path(args.json_output)
        json_path.parent.mkdir(parents=True, exist_ok=True)
        with open(json_path, "w") as f:
            json.dump(result, f, indent=2, default=str)
        print(f"\nJSON results written to: {json_path}")

    # Return exit code based on status
    if result.get("status") == "success":
        return 0
    elif result.get("status") == "partial":
        return 1
    else:
        return 2


def main() -> None:
    """Main entry point."""
    args = parse_args()
    setup_logging(args.verbose)

    exit_code = asyncio.run(main_async(args))
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
