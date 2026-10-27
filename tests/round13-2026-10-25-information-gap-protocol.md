# 5.1.7 信息差协议补强记录

## 目的

把用户本轮提出的通用要求合并到 Skill 本身，而不是为某一个问题写一次性回答：多平台信息线索、教程质量、插件安装授权、账号风控、机会成本、相对耗时、稳健性，以及快速/重大两档调查。

## 实际修改

- `skills/life-guide/SKILL.md`：版本升至 5.1.7，新增用户可选的快速决断/重大决策路由，并把安装前明确批准、评分不等于安全保证写入入口。
- `skills/life-guide/references/search-playbook.md`：信号雷达明确包含 X、微博、小红书；新增教程、经验帖和测评的来源、时效、可复现性、限制、交叉佐证和推广动机检查。
- `skills/life-guide/references/tool-access.md`：安装前展示候选信息并等待用户明确批准；增加来源/权限/数据流向/回退审阅、验证码与风控边界、账号封禁风险和“不能保证无病毒”口径。
- `skills/life-guide/references/decision-framework.md`：新增机会成本、相对耗时（第一反馈/有用结果/稳定结果）和稳健性（前提/依赖/脆弱点/回退/失效条件）比较行。
- `skills/life-guide/references/quick-mode.md`、`persistent-mode.md`：分别落地约 30 分钟首检点和约 3 小时分阶段目标，均声明这是投入量级而非墙上时钟保证。
- `README.md`、`adapters/`、`docs/architecture/package-boundaries.md`、`skills/life-guide/CHANGELOG.md`：同步版本与公开边界。
- `tests/test_information_gap_protocol.py`：新增静态协议探针。

## 验证

修改前先运行探针，按预期失败并报出 11 个缺口（RED）。修改后运行结果：

- `python tests/test_information_gap_protocol.py`：`GREEN/PASS`。
- `python tests/validate_package.py`：`Structural package check: PASS`。
- `python -X utf8 .../quick_validate.py skills/life-guide`：`Skill is valid!`。
- CHANGELOG 版本标题逐个计数：5.1.7 至 3.3.0 均各出现一次；无重复标题。
- 私有路径扫描：未发现本机个人路径泄漏。
- 安全边界扫描：确认存在“安装前明确批准”“不自行安装”“不自动绕过验证码”“不能保证无病毒”等规则。

## 仍未验证

- 真实宿主是否能自动触发两种模式、是否会按需读取参考文件。
- X、微博、小红书在目标宿主上的实际访问权限、登录状态、限流与平台条款适用情况。
- 任一第三方插件的实际代码安全；本 Skill 只能审阅来源和权限并要求用户批准，不能替工具做绝对无病毒保证。
- 两种模式的真实墙上时钟耗时、不同领域的多样本稳定性和跨宿主一致性。
