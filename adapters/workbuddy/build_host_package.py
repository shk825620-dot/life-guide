"""按 WorkBuddy 开放平台字段要求，从标准包生成宿主包。

标准包不动；宿主包输出到 dist/workbuddy/，不进入版本库。
字段依据：https://open.workbuddy.cn/docs/skill
未实测：assets/ 是否被平台接受、@references 引用语法、上传参数校验。
"""

from __future__ import annotations

import argparse
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "skills" / "life-guide"

DISPLAY_NAME = "减少信息差"
DISPLAY_NAME_EN = "Life Guide"
DESCRIPTION_ZH = "先查清关键条件与现成路径，再给有来源、有取舍、有下一步的判断。"
DESCRIPTION_EN = (
    "Research options, rules and evidence before giving a personalized recommendation "
    "with trade-offs and a lowest-cost next step."
)
AUTHOR = "life-guide contributors"
EXAMPLES_ZH = [
    "我想做点小生意，但只想到奶茶店，有什么建议？",
    "Python 进阶之后学什么？",
    "网上说这款保健品能降血脂，可信吗？",
]
EXAMPLES_EN = [
    "I want to start a small business but can only think of a milk tea shop.",
    "What should I learn after intermediate Python?",
    "Is this supplement claim about lowering blood lipids credible?",
]


def rewrite_frontmatter(text: str) -> str:
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise SystemExit("SKILL.md frontmatter not found")
    body = parts[2].lstrip("\n")
    description_match = None
    for line in parts[1].splitlines():
        if line.startswith("description:"):
            description_match = line.split(":", 1)[1].strip().strip('"')
            break
    description = description_match or DESCRIPTION_ZH
    zh_lines = "\n".join(f'  - "{x}"' for x in EXAMPLES_ZH)
    en_lines = "\n".join(f'  - "{x}"' for x in EXAMPLES_EN)
    front = f"""---
name: life-guide
display_name: {DISPLAY_NAME}
display_name_en: {DISPLAY_NAME_EN}
description: {description}
description_zh: {DESCRIPTION_ZH}
description_en: {DESCRIPTION_EN}
version: 6.0.6
author: "{AUTHOR}"
examples_zh:
{zh_lines}
examples_en:
{en_lines}
---
"""
    return front + body


def rewrite_refs(text: str) -> str:
    for name in [
        "capability-check", "decision-framework", "emotion-and-bias", "examples",
        "gap-map", "needs-clarification", "option-expansion", "output-contract",
        "persistent-mode", "progressive-delivery", "quick-mode",
        "research-specialists", "search-playbook", "supervision-protocol", "tool-access",
    ]:
        text = text.replace(f"`references/{name}.md`", f"@references/{name}.md")
    text = text.replace("`assets/decision-log.md`", "@assets/decision-log.md")
    return text


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "dist" / "workbuddy"))
    ap.add_argument("--zip", action="store_true", help="同时生成上传用 zip")
    args = ap.parse_args()

    out_root = Path(args.out)
    target = out_root / "life-guide"
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(SRC, target)

    skill_md = target / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    text = rewrite_frontmatter(text)
    text = rewrite_refs(text)
    skill_md.write_text(text, encoding="utf-8")

    print(f"宿主包已生成: {target}")
    print("字段: display_name / display_name_en / description / description_zh / "
          "description_en / version / author / examples_zh / examples_en")
    print("引用已改写为 @references/…（按官方文档映射，未实测）")

    if args.zip:
        zip_path = out_root / "life-guide-workbuddy-6.0.6.zip"
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(target.rglob("*")):
                if f.is_file():
                    z.write(f, Path("life-guide") / f.relative_to(target))
        print(f"zip: {zip_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
