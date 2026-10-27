"""Check that shared routing rules have one maintained definition."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFS = ROOT / "skills" / "life-guide" / "references"


def main() -> int:
    quick = (REFS / "quick-mode.md").read_text(encoding="utf-8")
    persistent = (REFS / "persistent-mode.md").read_text(encoding="utf-8")
    needs = (REFS / "needs-clarification.md").read_text(encoding="utf-8")
    progressive = REFS / "progressive-delivery.md"

    missing = []
    if not progressive.exists():
        missing.append("references/progressive-delivery.md")
    if "`references/progressive-delivery.md`" not in quick:
        missing.append("quick-mode pointer")
    if "`references/progressive-delivery.md`" not in persistent:
        missing.append("persistent-mode pointer")
    if "`gap-map.md` 的“无法多轮等待时”" not in needs:
        missing.append("needs-clarification fallback pointer")
    if "首个有效检查点（约 30 分钟内的投入量级）" in persistent:
        missing.append("persistent-mode duplicated cadence")
    if missing:
        print("RED/FAIL: single-source rules incomplete: " + ", ".join(missing))
        return 1
    print("GREEN/PASS: shared rules have unique reference points")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
