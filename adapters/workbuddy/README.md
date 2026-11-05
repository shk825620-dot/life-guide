# WorkBuddy 适配状态

分两个目标，要求完全不同，不能混为一谈：

| 目标 | 用哪份包 | 字段要求 | 实测状态 |
|---|---|---|---|
| 本地个人安装 | 标准包 `skills/life-guide/` | 标准 `name` / `description` 即可被识别 | 元数据发现已实测；加载与触发未验证 |
| 开放平台上架 | 专用宿主包（下方脚本生成） | 8 个必填字段，见下表 | **未实测**，不能直接上传标准 zip |

## 开放平台字段要求（官方 `open.workbuddy.cn/docs/skill`）

| 官方字段 | 必填 | 标准包现状 | 宿主包处理 |
|---|---|---|---|
| `name` | 是 | 有 `life-guide` | 保留 |
| `display_name` | 是 | 在 `metadata` 下，非顶层 | 提到顶层 |
| `display_name_en` | 是 | 无 | 生成 |
| `description` | 是 | 有（中英混写） | 沿用 |
| `description_zh` | 是 | 无 | 生成 |
| `description_en` | 是 | 无 | 生成 |
| `version` | 是 | 在 `metadata` 下，非顶层 | 提到顶层 |
| `author` | 是 | 无 | 默认 `life-guide contributors`（与 LICENSE 一致，**发布前请确认是否改为个人或组织名**） |
| `examples_zh` / `examples_en` | 否 | 无 | 生成，用于详情页「试试这样用」 |

官方子资源目录为 `references/`、`scripts/`、`templates/`，并以 `@references/xxx.md` 方式引用。标准包用 `assets/` 与反引号路径，两者差异见下方「未验证」。

## 生成宿主包

```bash
python adapters/workbuddy/build_host_package.py --zip
```

产物在 `dist/workbuddy/`（已在 `.gitignore` 中，不进版本库）：

- `life-guide/`：顶层字段已改写、引用已改为 `@references/…`
- `life-guide-workbuddy-6.0.3.zip`：上传用，顶层为 `life-guide/`

标准包不受影响，宿主字段不回写 `skills/life-guide/SKILL.md`。

## 未验证（不要跳过）

- 上传后平台解析是否通过，`assets/` 目录是否被接受。
- `@references/…` 引用语法在平台侧是否按预期读取。
- 技能市场上架审核、展示效果与自动触发行为。
- 若平台拒绝 `assets/`：把 `assets/decision-log.md` 改名到 `templates/`，并同步替换正文中的 `@assets/decision-log.md` 为 `@templates/decision-log.md`。

## 本地安装

把 `skills/life-guide/` 整个目录复制到 WorkBuddy 技能目录，目录名保持 `life-guide`。当前本机副本已与 6.0.2 源包一致（`diff -rq` 为空）；6.0.3 的多渠道检索规则尚未在宿主内单独实测。此前残留的 6 个私有 / 开发文件已移出并备份，未进入运行包。

自动触发、参考文件按需读取、工具与子 Agent 行为仍未实测，未实测的能力一律标为未验证。

## Windows 编码注意事项（2026-10-24 实测记录）

- 本仓库自带脚本显式使用 UTF-8 读取，Windows 默认环境实测通过，不依赖环境变量。
- 官方 Skill Creator 随附的 `quick_validate.py` 以 `read_text()` 无 encoding 参数读取 `SKILL.md`：在 GBK 区域设置且 Python ≤3.13 的机器上会因 UTF-8 中文内容抛 UnicodeDecodeError。本机 Python 3.14.7 默认首选编码已是 UTF-8，两种环境实测均通过——**该缺陷被本机 Python 版本掩盖，在旧版 Python 的 GBK 机器上运行官方校验器需设 `PYTHONUTF8=1`**。
- WorkBuddy 内置的另一份校验副本对目录与文件两种参数均报 "SKILL.md not found"，记录为该副本的参数处理问题，不作为包缺陷。

参考：[WorkBuddy 官方 Skill 文档](https://open.workbuddy.cn/docs/skill)；[Agent Skills 标准](https://agentskills.io/specification)。
