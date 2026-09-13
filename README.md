<div align="center">

# 🇺🇸 Liuzi Skill

### 中国留学生在美国的 AI 生存副驾驶

**不是美国生活百科。是“我现在该怎么办？”执行器。**

[![Version](https://img.shields.io/badge/version-v3.1.0-111111)](./SKILL.md)
[![Playbooks](https://img.shields.io/badge/playbooks-30%2B-2563eb)](./references/query-map.md)
[![Language](https://img.shields.io/badge/language-中文-ef4444)](./SKILL.md)
[![License](https://img.shields.io/badge/license-MIT-black)](./LICENSE)

`实时搜索` · `官方核验` · `总成本计算` · `风险排雷` · `直接给下一步`

</div>

---

## 你可以直接这样问

- 🛬 我刚落地美国，没有手机号，今天先做什么？
- 🏠 帮我选学校附近的公寓
- 🚗 预算 $10k，帮我买第一辆二手车
- ✈️ 12 月回长沙，最多转一次，怎么最便宜？
- 💳 没 SSN，帮我办第一张信用卡
- 🍜 告诉我附近中国人爱吃什么
- 🛋️ 帮我收一套二手家具
- 👯 这周末怎么认识一些美国人？
- ❤️ 帮我找适合认真约会的平台
- 📦 帮我比较从中国寄东西到美国的报价
- 🏥 我发烧了，该去校医院、Urgent Care 还是 ER？
- 💼 帮我找实习，并检查 CPT / OPT 风险
- 🇺🇸 做自媒体收钱会不会影响 F-1？
- 💰 帮我把每月生活费降下来

## 它怎么回答

不会给你一大段“美国生活常识”。默认给能直接照着做的步骤：

```text
问题：在美国学校旁边租房，我最应该注意什么？

1. 安全
   → 官方 crime data
   → 最近 6–12 个月评论
   → 晚上从车站回家的路线

2. 通勤
   → 到校车站步行多久
   → 班次 / 末班车
   → 下雨和夜间替代方案

3. 真实房租
   → base rent
   → mandatory fees
   → utilities / parking / renters insurance

4. 没信用记录怎么申请
   → I-20 / bank statement
   → guarantor
   → higher deposit / prepay

5. 最后给你
   → 最省钱 / 最均衡 / 最省心
   → 明确推荐哪一个
   → tour 和申请的下一步
```

## 核心能力

| 场景 | Skill 会做什么 |
|---|---|
| 🏠 租房 | 通勤圈 → 实时房源 → all-in → no-credit packet → 安全/评论 → lease checklist |
| 🚗 买车 | VIN → title/history → recall → insurance → PPI → written OTD → 决策 |
| ✈️ 回国机票 | 日期网格 → 多机场 → 行李 → self-transfer 风险 → 真实总成本 |
| 💳 信用 | SSN/ITIN/信用历史路由 → starter cards → 建信用步骤 |
| 🍜 吃饭 | 定位 → 最近评论 → 中国胃适配 → 距离/价格 → shortlist |
| 🛋️ 二手 | listing → 估价 → 防骗 → 验货 → 议价 → 搬运 |
| 👯 社交 | 学校/城市/兴趣 → recurring 活动 → 本周 1–3 个可执行入口 |
| ❤️ 约会 | 渠道选择 → profile → first date → intent/safety filtering |
| 📦 海运 | 禁限运 → 同口径报价 → 体积重 → 清关 → 附加费 → 赔付 |
| 🏥 医疗 | PCP / Urgent Care / ER → network → EOB → bill audit |
| 💼 求职 | Handshake / LinkedIn / alumni → outreach → CPT/OPT guardrails |
| 🇺🇸 身份 | 当前 status → 官方规则 → 风险分级 → DSO/律师升级边界 |

## 工作流

```mermaid
flowchart LR
    A[用户问题] --> B[识别场景]
    B --> C[实时搜索与官方核验]
    C --> D[算总成本与风险]
    D --> E[三档方案]
    E --> F[明确推荐与下一步]
```

## 项目结构

```text
liuzi-skill/
├── SKILL.md                 # 主路由、回答风格、决策规则
├── agents/openai.yaml       # Agent 展示与调用信息
├── references/              # 30+ 场景 playbooks
├── templates/               # 可复制 checklist / quote / decision table
├── examples/                # 真实问题的完整回答示例
└── LICENSE
```

## 安装

### Codex / ChatGPT Work

```bash
git clone https://github.com/qianquandong/liuzi-skill.git
cp -R liuzi-skill ~/.codex/skills/liuzi-skill
```

新对话里直接说：

```text
Use $liuzi-skill 帮我选学校附近的公寓
```

### Claude Code

```bash
git clone https://github.com/qianquandong/liuzi-skill.git ~/.claude/skills/liuzi-skill
```

至少保留 `SKILL.md`、`references/`、`templates/` 和 `examples/`。

### 其他 Agent

将 `SKILL.md` 作为主操作说明；按路由加载对应 `references/*.md`。涉及价格、库存、地图、政策或时限时，必须使用运行时的搜索/浏览工具重新核验。

## 研究原则

1. 身份 / 税务 / 法律 / 医疗 / 安全 → 官方来源优先。
2. 公寓体验 / 餐馆 / 社群 → 实时地图 + 最近评论 + 社区体验。
3. 机票 / 房租 / DMV / 政策 / 优惠 → 运行时重新查询，不硬编码。
4. 比价格时算 all-in，不只看广告价。
5. 付钱、签约、提交、取消、发送等不可逆动作前设置 human gate。

## Disclaimer

本 Skill 不替代律师、DSO、医生、CPA、保险经纪等专业人士。高风险问题的目标是找到当前权威规则、整理事实、标出风险边界，并明确什么时候升级给专业人士。

---

<div align="center">

**从刚下飞机，到毕业离开美国。**

MIT © Jack Qian

</div>
