"""Probes for single-responsibility of runtime rules and comparison routing.

Package boundaries state each rule has one primary maintenance location. These
probes fail when the same normative block is restated in two reference files, or
when the entry point does not route the comparison rows the rest of the package
requires. They check text presence only; they do not prove runtime behavior.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "life-guide"
REFERENCES = SKILL_DIR / "references"


def files_containing(needle: str) -> list[str]:
    return [
        p.name
        for p in sorted(REFERENCES.glob("*.md"))
        if needle in p.read_text(encoding="utf-8")
    ]


def main() -> int:
    problems: list[str] = []

    staged = files_containing("首个有效检查点（约 30 分钟内的投入量级）")
    if len(staged) != 1:
        problems.append(
            "staged-delivery cadence must be defined in exactly one file, found: "
            + (", ".join(staged) or "none")
        )

    degraded = files_containing("按档给条件化结论")
    if len(degraded) > 1:
        problems.append(
            "no-multi-turn degradation rule restated in multiple files: " + ", ".join(degraded)
        )

    main_text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    start = main_text.find("### 4. 按用户条件比较并建议")
    end = main_text.find("### 5.", start)
    section = main_text[start:end] if start != -1 and end != -1 else ""
    if not section:
        problems.append("entry point has no comparison section to inspect")
    for marker in ("机会成本", "相对耗时", "稳健性"):
        if marker not in section:
            problems.append(f"comparison section does not require: {marker}")

    evidence_start = main_text.find("### 3. 核验会影响判断的信息")
    evidence_end = main_text.find("### 4.", evidence_start)
    evidence_section = main_text[evidence_start:evidence_end] if evidence_start != -1 and evidence_end != -1 else ""
    for marker in ("主张—证据对照", "适用范围", "状态", "来源名称/链接", "查询日期", "未核实"):
        if marker not in evidence_section:
            problems.append(f"evidence section does not route: {marker}")

    for marker in ("references/capability-check.md", "references/output-contract.md"):
        if marker not in main_text:
            problems.append(f"entry point does not route: {marker}")

    tier_start = main_text.find("### 1.5 选择调查档位")
    tier_end = main_text.find("### 2.", tier_start)
    tier = main_text[tier_start:tier_end] if tier_start != -1 and tier_end != -1 else ""
    if not tier:
        problems.append("entry point has no investigation-tier section to inspect")
    elif "先按 `references/needs-clarification.md` 完成首轮澄清" not in tier:
        problems.append("tier selection does not state its order against first-round clarification")

    if problems:
        print("RED/FAIL: " + "; ".join(problems))
        return 1
    print("GREEN/PASS: runtime rules have single homes and comparison rows are routed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
