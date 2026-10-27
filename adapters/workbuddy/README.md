# WorkBuddy 适配状态

核心包 `skills/life-guide/` 使用 Agent Skills 标准字段。WorkBuddy Open Platform 官方技能文档示例还使用展示名、中文/英文描述、版本和作者等宿主字段，因此不能把宿主字段塞进标准核心的顶层 frontmatter，再声称所有 Agent 都接受同一份元数据。

## 当前判断

- 这份仓库文档只记录适配边界，**不是可导入的发行包或自动转换器**。
- 标准包的 `name`、`description` 和 `metadata.version` 可以提供转换输入；宿主展示名和本地化描述需要按当前 WorkBuddy 文档生成。
- `author` 是对外身份信息，当前没有在本项目中确认，不能由维护者猜填。
- WorkBuddy 本地安装、Open Platform 导入、工具调用、自动触发和子 Agent 能力需分别实测；其中任一项不能由格式校验替代。
- 当前候选 5.1.12 已复制到用户现有 WorkBuddy 安装目录；目标目录仍残留 6 个旧参考文件，尚未完成干净替换。自动触发、参考文件读取和工具行为仍未实测，未实测的能力一律标为未验证。

实现适配时先确认目标是本地个人安装还是 Open Platform 发布，再按官方最新字段单独生成发行包，并保留从标准核心到宿主包的可复现映射。

## Windows 编码注意事项（2026-10-24 实测记录）

- 本仓库自带脚本（`tests/validate_package.py`、`tests/verify_arithmetic_2026-10-24.py`）显式使用 UTF-8 读取，Windows 默认环境实测通过，不依赖环境变量。
- 官方 Skill Creator 随附的 `quick_validate.py` 以 `read_text()` 无 encoding 参数读取 `SKILL.md`：在 GBK 区域设置且 Python ≤3.13 的机器上会因 UTF-8 中文内容抛 UnicodeDecodeError。本机 Python 3.14.7 默认首选编码已是 UTF-8，两种环境实测均通过——**该缺陷被本机 Python 版本掩盖，在旧版 Python 的 GBK 机器上运行官方校验器需设 `PYTHONUTF8=1`**。这是官方第三方工具的限制，本仓库无法代为修复；WorkBuddy 内置的另一份副本对目录与文件两种参数均报 "SKILL.md not found"，记录为该副本的参数处理问题。

参考：[WorkBuddy 官方 Skill 文档](https://open.workbuddy.cn/docs/skill)；[Agent Skills 标准](https://agentskills.io/specification)。
