# 银行、首张信用卡与信用记录

这是高风险金钱路由。目标不是列“热门卡”，而是先确认用户能申请什么，再评估获批可能，最后比较是否值得申请。所有资格与费用信息必须实时查发卡行官方页面并标注核验日期。

文末的 [2026 卡片快照](#2026-卡片快照) 只提供候选池与已知变化，用于缩短搜索范围和排除已停用产品，不替代上述流程，也不构成排名。

## 最少输入

- 年龄是否满 21 岁；所在州和学校
- 是否有 SSN、ITIN；不要索取号码本身
- 美国信用档案长度、已持卡、近 6–12 个月申请次数
- 是否已有 checking/deposit relationship
- 可证明的个人收入来源；不替用户定义法律意义上的可用收入
- 主要消费、是否出境、能否每月全额还 statement balance

缺少年龄、SSN/ITIN、信用档案或收入时，不直接给“可申请排名”；先给条件分支。

## 硬筛选

1. 官方申请页是否明确接受用户具备的身份识别材料。
2. 年龄、居住地址、学生状态、收入声明等资格是否满足。
3. 年费、押金、foreign transaction fee 是否触碰硬约束。
4. 用户能否全额还款；不能时不以奖励诱导申请。
5. 最近 hard inquiries 或新账户过多时，优先无 hard pull 的 pre-qualification。

无法从官方页面确认 SSN/ITIN 路径的产品标为 `无法验证`，不得进入正式排名。客服口头答复记录时间与 case/reference number，但仍标为第一方确认而非公开条款。

## 搜索顺序

1. 当前银行/信用合作社官方账户关系与 pre-qualification。
2. 发卡行官方学生卡、secured card、身份材料、费率与奖励条款。
3. CFPB/FTC/AnnualCreditReport 等官方消费者规则与信用报告渠道。
4. 信用局官方渠道核验 credit file/freeze。
5. 第三方社区只用于发现候选和常见失败点，不用于证明资格。

## 三层结论

对每张卡分别写：

- **能申请**：官方资格是否直接覆盖；不确定就写待确认。
- **可能获批**：高/中/低或未知，并列出依据；不能承诺。
- **值得申请**：年费、奖励、使用场景、hard pull、毕业路径和替代方案。

## 评分口径

先硬淘汰，再评分：

`总分 = 资格确定性 30 + 获批路径 20 + 长期价值 20 + 费用 15 + 境外适用 10 + 申请可逆性 5`

资格为 `合理推测` 或 `无法验证` 时不得进入前三名。

## 输出结构

1. 核验日期、用户条件与未知项。
2. 正式排名表：卡名、能否申请、获批判断、年费/押金、FTF、证据状态、官方链接。
3. 未验证候选：为什么暂不排名、应向谁确认。
4. 明确首选和申请顺序；同一轮不要鼓励多张盲申。
5. 申请后设置 autopay statement balance、提醒 due date、查看官方 credit report。
6. Human gate：点击提交申请前确认条款、hard pull 与声明信息。

## 失败回退

- 无 SSN/ITIN 且官方路径不明：先查现有银行人工开户/产品政策、secured 路径或建立银行关系；不借用他人身份。
- 无信用档案：不要制造“必须付利息养分”的误区；按时全额还款即可。
- 被拒：保存 adverse action notice，按其列出的原因修复；不要当天连续申请。
- 无法承担：优先 debit/checking 与预算方案，不用循环利息换积分。

## 2026 卡片快照

**核验日期：2026-09-13。超过 90 天必须整节重查后再用。**

这一节是候选池与已知变化，不是排名。任何一张卡进入正式推荐前，仍要按上面的硬筛选和评分口径跑一遍，并重新打开官方页面确认当前条款。奖励与年费是变化最快的部分，过期风险最高。

### 2026 年必须知道的变化

- **Deserve EDU 已彻底停用。** 2023-09 停止新申请，2025-08 发卡方通知关闭全部存量账户并停止交易。中文社区里仍在推荐它的攻略都已过期。对老用户还有一层伤害：它常是用户最老的账户，关闭会缩短平均账龄。证据状态：第三方支持（多家独立媒体与发卡方 FAQ 页一致），不作为资格依据，仅用于排除候选。
- **无 SSN 的无抵押卡基本消失。** Deserve 退出后，剩下的护照路径以 secured 或 fintech 产品为主。把"先拿 ITIN"当作主路径，而不是继续找免 SSN 的捷径。

### 无 SSN / ITIN 路径

| 产品 | 身份材料 | 类型 | 年费 | 证据状态 |
|---|---|---|---|---|
| Capital One Platinum Secured / Quicksilver Secured | 接受 ITIN 代替 SSN | 押金 | $0 | 官方直接确认 |
| Chase Freedom Rise | 需 SSN 或 ITIN | 无抵押 | $0 | 官方直接确认 |
| Firstcard | 护照 + I-20，无需 SSN/ITIN/信用检查 | 押金 | $0 | 第一方自述 |
| Zolve | 护照 + F-1 + I-20，无需 SSN | 无抵押 | $0 | 第一方自述 |
| Deserve EDU | — | — | — | 已停用，不可选 |

Firstcard 与 Zolve 的条款目前只有厂商自己的页面支撑，按证据契约属第一方自述：可以进入候选并标明局限，但不能当作官方资格保证。这两家的对比文章多为自家营销内容，不用于证明资格。

### 学生卡

| 产品 | 年费 | FTF | 奖励 | 开卡奖励 |
|---|---|---|---|---|
| Discover it Student Cash Back | $0 | 发卡行称无 | 5% 轮换季度类别（需激活，有上限）+ 1% | 首年 Cashback Match，无最低消费 |
| Capital One Savor Student | $0 | $0 | 3% 餐饮/娱乐/流媒体/超市（不含 Walmart、Target）+ 1% | $100 消费得 $50，限 3 个月内 |
| Capital One Quicksilver Student | $0 | $0 | 1.5% 全场 | 同上 |
| BoA Travel Rewards for Students | $0 | 无 | 1.5x 全场 | 90 天内消费 $1,000 得 20,000 分（约 $200），部分版本为 25,000 分 |

在读认定：Capital One 把"已录取且 3 个月内入学"也算学生。Discover 要求 18 岁以上、在读、有收入来源，提供不影响信用的 pre-approval 预查。Chase 没有学生卡品牌，Freedom Rise 不要求在读证明。

Capital One 同一产品 48 个月内拿过新卡奖励则不再合资格。BoA 的 bonus 每个新账户限一次，余额代偿和取现不计入。

### Secured 押金卡

| 产品 | 押金 | 起始额度 | 年费 | FTF | 奖励 | 毕业路径 |
|---|---|---|---|---|---|---|
| Capital One Platinum Secured | $49 / $99 / $200，按资质定 | $200 起，激活前可加存至 $1,000 | $0 | $0 | 无 | 最快 6 个月自动复审提额；转无抵押或销户还清后退押金 |
| Capital One Quicksilver Secured | $200 起 | $200 起，上限通常 $1,000–$3,000 | $0 | $0 | 1.5% 全场 | 良好用卡可退押金为 statement credit 并升级为无抵押 Quicksilver |

押金可一次付清或在 35 天内分次付，不计利息。押金卡的作用是建立档案，不要为了额度超额存钱。

### 无 FTF 出境适用

- Capital One 全线产品无 foreign transaction fee，含学生卡与 secured 卡，官方直接确认。
- BoA Travel Rewards for Students 无 FTF；但**同系列的 Customized Cash Rewards for Students 收 FTF**，回国或旅行场景下不要混用。
- Discover 宣称无 FTF，但境外受理网络明显窄于 Visa/Mastercard，其 99% 受理率是美国境内口径。出境不要只带 Discover。

### 用这节时的强制动作

1. 打开官方 pricing/terms 页面确认年费、FTF、APR 与当前奖励，写下新的核验日期。
2. 21 岁以下必须出示独立收入。父母汇款和直接抵扣学费的助学金不算；校内工作、stipend、助教助研收入算。
3. 本国信用记录不会转入美国信用局，不要把国内评分当作获批依据。
4. 优先用无 hard pull 的 pre-qualification 判断匹配度，不要同轮盲申多张。

## 官方入口

CFPB、FTC、AnnualCreditReport、各信用局官方渠道、目标银行的申请资格与 pricing/terms 页面。使用 [evidence-contract.md](evidence-contract.md) 校验证据。

## Eval 映射

`credit-no-ssn`、`credit-under-21`、`credit-no-browser`、`credit-third-party-conflict`、`credit-multiple-hard-pulls`。
