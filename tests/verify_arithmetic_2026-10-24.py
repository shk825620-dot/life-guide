# -*- coding: utf-8 -*-
"""第二轮独立算术复核（2026-10-24）。

复核对象：tests/runs-2026-10-22/ 四轮运行 + 两个迁移案例中出现的计算结果，
以及 round-2026-10-22.md 第六节声称由"独立脚本复算"的数字（该脚本未随仓库留档，
本脚本为第二轮重新编写的独立复算，不声称复现原脚本）。

输入数值均来自 2026-10-18 更正报告 1.1/2.1 节的输入归属表（用户提供/用户暂估/情景假设）。
"""

from decimal import Decimal as D

results = []


def check(name, actual, claimed, tol=D("0.05")):
    actual = D(actual)
    claimed = D(claimed)
    ok = abs(actual - claimed) <= tol
    results.append((name, actual, claimed, ok))


# ---------- 奶茶店（永康） ----------
fixed = D(5000) + D(3500) + D(1200) + D(2000)
check("奶茶-月固定支出", fixed, 11700, 0)

price, margin, target, days = D(16), D("0.65"), D(8000), D(30)

# 成本覆盖线：11,700/0.65 = 18,000 元/月
cov_rev = fixed / margin
check("奶茶-成本覆盖营业额(元/月)", cov_rev, 18000, D("0.01"))
check("奶茶-成本覆盖单数(单/天)", cov_rev / price / days, D("37.5"), D("0.5"))  # 输出写"约38单"

# 目标达成线：(11,700+8,000)/0.65 = 30,307.7
tgt_rev = (fixed + target) / margin
check("奶茶-目标营业额(元/月)", tgt_rev, D("30307.69"), D("0.5"))  # 输出写"≈30,300"；10-18 报告写 30,308
check("奶茶-目标单数(单/天)", tgt_rev / price / days, D("63.1"), D("0.1"))

# 情形 B：25% 营业额走外卖、该部分综合费率 20% → 有效贡献率 0.60
eff = margin - D("0.25") * D("0.20")
check("奶茶-有效贡献率", eff, D("0.60"), 0)
check("奶茶-情形B营业额(元/月)", (fixed + target) / eff, D("32833.33"), D("0.5"))
check("奶茶-情形B单数(单/天)", (fixed + target) / eff / price / days, D("68.4"), D("0.1"))

# 情形 C：另计折旧 1,800（情景假设）
dep = D(1800)
check("奶茶-情形C营业额(元/月)", (fixed + target + dep) / eff, D("35833.33"), D("0.5"))
check("奶茶-情形C单数(单/天)", (fixed + target + dep) / eff / price / days, D("74.7"), D("0.1"))

# 情形 D：45 单/天
rev_d = D(45) * price * days
contrib_d = rev_d * margin - rev_d * D("0.25") * D("0.20")
check("奶茶-45单月营业额", rev_d, 21600, 0)
check("奶茶-45单贡献(元)", contrib_d, 12960, D("0.01"))
check("奶茶-45单结余(元)", contrib_d - fixed, 1260, D("0.01"))
check("奶茶-45单结余扣折旧(元)", contrib_d - fixed - dep, D("-540"), D("0.01"))

# milktea-s2 补充：原料率 35%→38%
check("奶茶-38%原料率目标营业额", (fixed + target) / (1 - D("0.38")), D("31800"), D("50"))  # 输出写"≈31,800"
check("奶茶-38%原料率单数", (fixed + target) / (1 - D("0.38")) / price / days, D("66"), D("0.5"))

# 迁移案例一（t1）：18 元每杯 vs 每单（60 杯/天，30 天，固定 11,700，原料 35%）
check("t1-每杯口径结余(元)", D(60) * 18 * days * margin - fixed, 9360, D("40"))  # 输出写"约+9400"
check("t1-每单口径(一单两杯)结余(元)", D(30) * 18 * days * margin - fixed, D("-1170"), D("30"))  # 输出写"约-1200"
check("t1-一单1.5杯结余(元)", D(40) * 18 * days * margin - fixed, 2340, D("40"))  # 输出写"约+2300"
check("t1-保本日营收(元)", fixed / margin / days, 600, D("0.01"))
check("t1-保本杯数(杯价口径)", fixed / margin / days / 18, D("33.3"), D("0.1"))
check("t1-保本杯数(一单两杯口径)", fixed / margin / days / 18 * 2, D("66.7"), D("0.1"))

# ---------- 儿童体能馆（成都） ----------
g_fixed = D(22000) + D(36000) + D(12000)
check("体能馆-月固定支出", g_fixed, 70000, 0)
check("体能馆-日固定支出", g_fixed / D(30), D("2333.33"), D("33"))  # 输出写"约2,300"

per_session = D(1200) / D(12)
capacity = D(5) * D(10) * D(26)
check("体能馆-单节价格", per_session, 100, 0)
check("体能馆-满负荷节数", capacity, 1300, 0)
check("体能馆-满负荷月收入", capacity * per_session, 130000, 0)
check("体能馆-现金盈亏平衡节数", g_fixed / per_session, 700, 0)
check("体能馆-平衡座位利用率", g_fixed / per_session / capacity, D("0.5385"), D("0.001"))  # 输出写54%

check("体能馆-签约即付(押金+装修)", D(44000) + D(180000), 224000, 0)
check("体能馆-押一付一总支出", D(44000) + D(180000) + D(22000), 246000, 0)
check("体能馆-押一付一剩余", D(300000) - D(246000), 54000, 0)
check("体能馆-押一付三总支出", D(44000) + D(180000) + D(66000), 290000, 0)
check("体能馆-押一付三剩余", D(300000) - D(290000), 10000, 0)

sessions_per_student = D("6.5")  # AI 假设（输出已标注"此频率你未提供，是我的假设"）
check("体能馆-平衡学员数", g_fixed / per_session / sessions_per_student, D("107.7"), D("0.5"))  # 输出写约108
check("体能馆-满负荷学员数", capacity / sessions_per_student, 200, 0)
check("体能馆-35名学员月流出", g_fixed - D(35) * sessions_per_student * per_session, 47250, D("0.01"))  # 输出写"超4.7万"

check("体能馆-月落1.5万所需节数", (g_fixed + D(15000)) / per_session, 850, 0)
check("体能馆-月落1.5万所需学员", (g_fixed + D(15000)) / per_session / sessions_per_student, D("130.8"), D("0.5"))
check("体能馆-3年回本30万月供", D(300000) / D(36), D("8333.33"), D("0.5"))
check("体能馆-3年回本所需节数(≈9.5万收入)", D(95000) / per_session, 950, 0)
check("体能馆-3年回本所需学员", D(95000) / per_session / sessions_per_student, D("146.2"), D("0.5"))
check("体能馆-回本线上座率", D(950) / capacity, D("0.731"), D("0.001"))  # 输出写73%

# ---------- 便利店转让（t2） ----------
t_out = D(80000) + D(12000) + D(18000) + D(50000)
check("便利店-签约流出", t_out, 160000, 0)
check("便利店-手边剩余", D(200000) - t_out, 40000, 0)
check("便利店-押金(押二)", D(6000) * 2, 12000, 0)
check("便利店-首期房租(付三)", D(6000) * 3, 18000, 0)
check("便利店-盈亏平衡日流水(毛利25%)", D(8000) / D(30) / D("0.25"), D("1066.67"), D("10"))  # 输出写"约1070"
check("便利店-盈亏平衡日流水(毛利20%)", D(8000) / D(30) / D("0.20"), D("1333.33"), D("10"))  # 输出写"约1330"

for daily, claimed_gross, claimed_net, label in [
    (D(2500), D("18750"), D("10750"), "2500"),
    (D(1500), D("11250"), D("3250"), "1500"),
    (D(1100), D("8250"), D("250"), "1100"),
    (D(800), D("6000"), D("-2000"), "800"),
]:
    gross = daily * D(30) * D("0.25")
    check(f"便利店-情景{label}月毛利", gross, claimed_gross, D("1"))  # 输出写约数
    check(f"便利店-情景{label}月净现金流", gross - D(8000), claimed_net, D("1"))

check("便利店-800情景含生活费月流出", D(800) * D(30) * D("0.25") - D(8000) - D(4000), D("-6000"), D("1"))
check("便利店-800情景跑道(月)", D(40000) / D(6000), D("6.67"), D("0.1"))  # 输出写"6~7个月"

# ---------- 5.0.0 后测运行（2026-10-24） ----------
# R2post（体能馆）：30−22.4=7.6 万缓冲；7 万/月固定→约 1.1 个月；20 人每周 1 节≈月 4.3 节
check("R2post-剩余现金(万)", (D(300000) - D(224000)) / D(10000), 7.6, D("0.01"))
check("R2post-缓冲月数", (D(300000) - D(224000)) / g_fixed, D("1.086"), D("0.05"))  # 输出写约1.1
check("R2post-20人口头意向月课消(人次)", D(20) * D("4.3"), 86, D("0.5"))
check("R2post-口头意向月收入(元)", D(20) * D("4.3") * per_session, 8600, D("50"))
check("R2post-每周一课平衡学员数", g_fixed / per_session / D("4.3"), D("162.8"), D("3"))  # 输出写约160

# T1post（奶茶单位陷阱）：三种口径（固定 11,700、毛利 65%、客单 18、60 杯/30 天）
check("T1post-两杯一单结余(元)", D(30) * 18 * days * margin - fixed, D("-1170"), D("1"))
check("T1post-中性1.5杯结余(元)", D(40) * 18 * days * margin - fixed, 2340, D("1"))
check("T1post-每杯口径结余(元)", D(60) * 18 * days * margin - fixed, 9360, D("40"))  # 输出写+9,400
check("T1post-两杯一单日营业额(元)", D(30) * 18, 540, D("0.01"))
check("T1post-盈亏平衡日营业额(元)", fixed / margin / days, 600, D("0.01"))
check("T1post-盈亏平衡单数(单/天)", fixed / margin / days / 18, D("33.3"), D("0.1"))

# R3post（便利店）：投入 16 万、剩 4 万；打平区间按毛利 20%–25%、月固定 7,500–8,000
check("R3post-一次性投入(万)", t_out / D(10000), 16, D("0.01"))
check("R3post-剩余周转(万)", (D(200000) - t_out) / D(10000), 4, D("0.01"))
check("R3post-打平日销下界(毛利20%,月支8000)", D(8000) / D(30) / D("0.20"), 1333, D("40"))  # 输出写区间1,100–1,800
check("R3post-打平日销上界(毛利25%,月支7500)", D(7500) / D(30) / D("0.25"), 1000, D("40"))

# ---------- 输出 ----------
passed = sum(1 for *_, ok in results if ok)
print(f"独立算术复核：{passed}/{len(results)} 项一致")
print()
for name, actual, claimed, ok in results:
    mark = "PASS" if ok else "FAIL"
    print(f"[{mark}] {name}: 计算={actual}  记录值≈{claimed}")
print()
if passed != len(results):
    raise SystemExit(1)
print("全部一致（对四舍五入容差内的记录值视为一致）。")
