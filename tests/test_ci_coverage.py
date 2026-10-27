"""Check that the repository CI runs the project's required static checks."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "validate.yml"
TESTS = ROOT / "tests"


def main() -> int:
    text = WORKFLOW.read_text(encoding="utf-8")
    required = {
        "structural": "python tests/validate_package.py",
        "protocol": "python tests/test_information_gap_protocol.py",
        "rule_singularity": "python tests/test_rule_singularity.py",
        "release_hygiene": "python tests/test_release_hygiene.py",
    }
    missing = [name for name, command in required.items() if command not in text]

    uncovered = [
        p.name
        for p in sorted(TESTS.glob("test_*.py"))
        if f"python tests/{p.name}" not in text
    ]
    missing.extend(f"not run by CI: {name}" for name in uncovered)

    if missing:
        print("RED/FAIL: CI missing checks: " + ", ".join(missing))
        return 1
    print("GREEN/PASS: CI runs every static test script")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
