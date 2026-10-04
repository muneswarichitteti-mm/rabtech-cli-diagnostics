import argparse
import json
import os
import sys


def check_config():
    """Check the DIAG_CONFIG environment variable."""
    value = os.getenv("DIAG_CONFIG")

    return {
        "name": "DIAG_CONFIG",
        "configured": value is not None,
        "value": value if value is not None else None,
    }


def main():
    parser = argparse.ArgumentParser(
        description="RabTech CLI Diagnostics Tool"
    )

    parser.add_argument(
        "--json",
        metavar="FILE",
        help="Save the diagnostic report to a JSON file",
    )

    args = parser.parse_args()

    config_check = check_config()

    report = {
        "status": "success" if config_check["configured"] else "failure",
        "checks": {
            "environment": config_check
        }
    }

    # Save report to JSON file
    if args.json:
        with open(args.json, "w", encoding="utf-8") as file:
            json.dump(report, file, indent=2)
    else:
        print(json.dumps(report, indent=2))

    # Exit codes
    if config_check["configured"]:
        return 0
    else:
        return 1


if __name__ == "_main_":
    sys.exit(main())