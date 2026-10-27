"""Lightweight structural checks for the canonical life-guide Agent Skill package."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "life-guide"
MAIN = SKILL_DIR / "SKILL.md"
CHANGELOG = SKILL_DIR / "CHANGELOG.md"


def fail(message: str) -> None:
    print(f"FAIL: {message}")


def check_table_continuity(text: str, rel: str, errors: list[str]) -> None:
    """A pipe-row preceded by a non-row line is only legal as a table header
    (next line must be a delimiter row); otherwise it renders as broken text."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        s = line.strip()
        if not (s.startswith("|") and s.endswith("|") and i > 0):
            continue
        prev = lines[i - 1].strip()
        if prev.startswith("|"):
            continue
        nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
        is_delimiter = nxt.startswith("|") and set(nxt) <= set("|-: \t")
        if not is_delimiter:
            errors.append(f"table row detached from its table in {rel}: line {i + 1}")


def main() -> int:
    errors: list[str] = []
    if not MAIN.is_file():
        print(f"FAIL: missing {MAIN}")
        return 1

    raw = MAIN.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", raw, re.S)
    if not match:
        errors.append("SKILL.md has no valid YAML frontmatter block")
        frontmatter = ""
    else:
        frontmatter = match.group(1)

    top_keys = {
        line.split(":", 1)[0].strip()
        for line in frontmatter.splitlines()
        if line and not line[0].isspace() and ":" in line
    }
    if not {"name", "description"}.issubset(top_keys):
        errors.append("frontmatter must contain standard name and description")
    unsupported = top_keys - {
        "name",
        "description",
        "license",
        "compatibility",
        "metadata",
        "allowed-tools",
    }
    if unsupported:
        errors.append("non-standard top-level frontmatter fields: " + ", ".join(sorted(unsupported)))

    version = re.search(r"^\s+version:\s*[\"']?([0-9]+\.[0-9]+\.[0-9]+)", frontmatter, re.M)
    log_version = re.search(r"^##\s+\[([0-9]+\.[0-9]+\.[0-9]+)\]", CHANGELOG.read_text(encoding="utf-8"), re.M) if CHANGELOG.is_file() else None
    if not version:
        errors.append("metadata.version is missing")
    if not log_version:
        errors.append("CHANGELOG.md has no leading semantic version entry")
    if version and log_version and version.group(1) != log_version.group(1):
        errors.append(f"version mismatch: metadata {version.group(1)} vs changelog {log_version.group(1)}")

    # Package references must resolve from the file that names them.
    for md in [MAIN, *sorted((SKILL_DIR / "references").glob("*.md"))]:
        text = md.read_text(encoding="utf-8")
        check_table_continuity(text, md.relative_to(SKILL_DIR).as_posix(), errors)
        for target in re.findall(r"`([^`\n]+\.md)`", text):
            if target.startswith(("http:", "https:")):
                continue
            if target.startswith(("references/", "assets/")):
                if not (SKILL_DIR / target).is_file():
                    errors.append(f"broken package path in {md.relative_to(SKILL_DIR)}: {target}")

    forbidden_runtime_files = {
        "user-requirements.md",
        "revision-task.md",
        "overall-framework.md",
        "collaboration.md",
        "knowledge-base-protocol.md",
        "brain-trust.md",
    }
    present = forbidden_runtime_files.intersection(p.name for p in (SKILL_DIR / "references").glob("*.md"))
    if present:
        errors.append("personal/development-only files remain in runtime references: " + ", ".join(sorted(present)))

    specialist = SKILL_DIR / "references" / "research-specialists.md"
    if not specialist.is_file():
        errors.append("missing references/research-specialists.md")
    else:
        text = specialist.read_text(encoding="utf-8")
        if len(re.findall(r"^###\s+角色", text, re.M)) != 5:
            errors.append("research-specialists.md must define exactly five distinct role cards")
        if not re.search(r"简单.{0,30}(不启用|不调用|无需).{0,20}(专才|角色|Agent)", text):
            errors.append("specialist routing must say simple questions do not require specialists")

    # OpenAI/Codex UI metadata is optional in the standard, but this package
    # ships it so discovery can be configured without changing core frontmatter.
    openai_meta = SKILL_DIR / "agents" / "openai.yaml"
    if not openai_meta.is_file():
        errors.append("missing optional-but-required-for-this-package agents/openai.yaml")
    else:
        meta = openai_meta.read_text(encoding="utf-8")
        for field in ("display_name", "short_description", "default_prompt"):
            if not re.search(rf"^\s+{field}:\s+\".+\"\s*$", meta, re.M):
                errors.append(f"agents/openai.yaml missing quoted interface.{field}")
        short = re.search(r"^\s+short_description:\s+\"([^\"]+)\"", meta, re.M)
        if short and not 25 <= len(short.group(1)) <= 64:
            errors.append("agents/openai.yaml short_description must contain 25–64 characters")
        if "allow_implicit_invocation: true" not in meta:
            errors.append("agents/openai.yaml must allow implicit invocation")
        if "$life-guide" not in meta:
            errors.append("agents/openai.yaml default_prompt must mention $life-guide")

    reference_files = sorted((SKILL_DIR / "references").glob("*.md"))
    for ref in reference_files:
        route = f"references/{ref.name}"
        if f"`{route}`" not in raw:
            errors.append(f"runtime reference is not routed from SKILL.md: {route}")
    for target in re.findall(r"`((?:references|assets)/[^`\s]+)`", raw):
        if not (SKILL_DIR / target).is_file():
            errors.append(f"missing routed package resource: {target}")

    cases = ROOT / "tests" / "acceptance-cases.md"
    if cases.is_file():
        case_ids = re.findall(r"^###\s+([A-E][1-3])\.", cases.read_text(encoding="utf-8"), re.M)
        if len(case_ids) != 13 or len(set(case_ids)) != 13:
            errors.append(f"expected 13 unique frozen behavior cases, found {len(case_ids)}")
    else:
        errors.append("missing tests/acceptance-cases.md")

    ignore = ROOT / ".gitignore"
    if not ignore.is_file() or "/审查证据/" not in ignore.read_text(encoding="utf-8"):
        errors.append(".gitignore must exclude local review evidence from public publishing")

    private_patterns = (
        r"C:[/\\]+Users[/\\]+",
        r"F:[/\\]+小盛知识库",
        r"E:[/\\]+KSHGitHub",
    )
    public_roots = [ROOT / "README.md", ROOT / "CONTRIBUTING.md", ROOT / "skills", ROOT / "tests", ROOT / "docs", ROOT / "adapters"]
    public_files = [p for p in public_roots if p.is_file()]
    text_suffixes = {".md", ".py", ".txt", ".json", ".yml", ".yaml", ".toml"}
    public_files.extend(
        f for p in public_roots if p.is_dir() for f in p.rglob("*")
        if f.is_file() and f.suffix.lower() in text_suffixes
    )
    for md in public_files:
        text = md.read_text(encoding="utf-8")
        for pattern in private_patterns:
            if re.search(pattern, text, re.I):
                errors.append(f"private local path appears in public files: {md.relative_to(ROOT)}")
                break

    if errors:
        for error in errors:
            fail(error)
        print(f"Structural package check: FAIL ({len(errors)} findings)")
        return 1

    print("Structural package check: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
