# 银行、首张信用卡与信用记录

这是高风险金钱路由。目标不是列“热门卡”，而是先确认用户能申请什么，再评估获批可能，最后比较是否值得申请。所有资格与费用信息必须实时查发卡行官方页面并标注核验日期。

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

## 官方入口

CFPB、FTC、AnnualCreditReport、各信用局官方渠道、目标银行的申请资格与 pricing/terms 页面。使用 [evidence-contract.md](evidence-contract.md) 校验证据。

## Eval 映射

`credit-no-ssn`、`credit-under-21`、`credit-no-browser`、`credit-third-party-conflict`、`credit-multiple-hard-pulls`。
