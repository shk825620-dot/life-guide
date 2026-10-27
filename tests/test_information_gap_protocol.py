"""Static acceptance probes for the 5.1.8 information-gap protocol additions.

These probes check that the generic package contains the public rules requested
for source signals, tool authorization, two investigation modes, and decision
comparison. They do not treat a keyword match as proof of runtime behavior.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "life-guide"


def read(name: str) -> str:
    return (SKILL / "references" / name).read_text(encoding="utf-8")


def main() -> int:
    search = read("search-playbook.md")
    access = read("tool-access.md")
    decision = read("decision-framework.md")
    quick = read("quick-mode.md")
    persistent = read("persistent-mode.md")
    emotion = read("emotion-and-bias.md")
    supervision = read("supervision-protocol.md")

    required = {
        "search:weibo": ("微博", search),
        "search:tutorial-rubric": ("教程质量", search),
        "access:explicit-install-approval": ("明确批准", access),
        "access:no-virus-guarantee": ("不能保证无病毒", access),
        "access:account-safety": ("封号", access),
        "decision:opportunity-cost": ("机会成本", decision),
        "decision:relative-time": ("相对耗时", decision),
        "decision:robustness": ("稳健性", decision),
        "quick:user-selectable": ("用户选择", quick),
        "quick:30-minute-checkpoint": ("30 分钟", quick),
        "major:three-hour-target": ("3 小时", persistent),
        "major:user-selectable": ("用户选择", persistent),
        "emotion:observable-signals": ("可观察的决策信号", emotion),
        "emotion:no-diagnosis": ("不是心理诊断", emotion),
        "emotion:outside-view": ("外部视角", emotion),
        "emotion:sunk-cost": ("沉没成本", emotion),
        "emotion:stop-condition": ("继续、调整或停止的条件", emotion),
        "emotion:deadline-not-exemption": ("截止时间不豁免高风险核验", emotion),
        "search:atomic-claim-evidence": ("逐项对应证据", search),
        "search:scope-match": ("适用范围", search),
        "search:partial-support": ("部分支持", search),
        "supervision:claim-scope": ("逐项核对原文和适用范围", supervision),
    }
    missing = [name for name, (needle, text) in required.items() if needle not in text]
    safety_rules = [
        ("access:no-captcha-bypass", "不自动绕过验证码"),
        ("access:no-auto-install", "不自行下载、安装、升级或启用"),
        ("access:explicit-approval", "明确批准"),
        ("access:no-security-guarantee", "不能保证无病毒"),
    ]
    missing.extend(name for name, needle in safety_rules if needle not in access)
    if missing:
        print("RED/FAIL: missing protocol markers: " + ", ".join(missing))
        return 1
    print("GREEN/PASS: information-gap protocol markers present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
