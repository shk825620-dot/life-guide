"""Check that known local/generated artifacts are excluded from a public repo."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    text = (ROOT / ".gitignore").read_text(encoding="utf-8")
    required = ["/_ppt_render/", "/--name/", "/build/"]
    missing = [entry for entry in required if entry not in text]
    if missing:
        print("RED/FAIL: generated artifact patterns missing: " + ", ".join(missing))
        return 1
    print("GREEN/PASS: known generated artifacts are ignored")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
