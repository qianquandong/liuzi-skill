# 生病、保险与医疗账单

这是高风险医疗路由。先做紧急分流，再优化网络内选择和费用；不诊断、不替医生决定处方。

## 最少输入

- 当前症状、持续时间、严重程度、是否快速恶化
- 明显红旗、基础病、过敏、正在使用的药物
- 城市/学校、当前时间、是否能安全移动
- 保险公司/plan 名称、network 类型；不要索取完整 member ID
- 用户要解决的是去哪就医、保险覆盖、找 provider，还是账单争议

## 紧急硬分流

出现呼吸困难、胸痛、严重出血、意识异常、严重过敏、疑似中风、自伤/他伤风险或其他可能危及生命迹象，明确建议 911 / ER。不要为了省钱、网络内或等待回复延误。

症状不明确但可能严重时，使用保险 nurse line、校医院临床分诊或当地专业医疗热线升级；不要在聊天中“排除”急症。

## 非急症搜索顺序

1. 保险卡/portal 的 nurse line、in-network directory 与 plan documents。
2. 学校 health center、PCP、telehealth、Urgent Care、provider 官方预约页。
3. 保险公司或 provider 电话再次确认网络状态、地点、服务和预计费用。
4. CMS/州保险监管机构用于消费者权利、申诉和 surprise billing 等适用规则。
5. 地图评论只用于交通、等待和体验，不用于医疗质量结论。

## 路径比较

| 路径 | 适用判断 | 必核验 |
|---|---|---|
| Telehealth / nurse line | 需要分诊或轻症咨询 | 可用时间、费用、能否处理该问题 |
| 校医院 / PCP | 非急症、持续问题、复诊 | network、预约、转诊要求 |
| Urgent Care | 需要当天面诊但无明显急症 | in-network、影像/化验是否另计 |
| ER / 911 | 可能危及生命或严重恶化 | 不以费用阻止就医 |

## 费用口径

`预计自付 = copay + 未满足 deductible 部分 + coinsurance + non-covered services + 可能的 facility/lab/imaging/pharmacy 费用`

这是估算，不保证最终账单。记录联系时间、代表姓名/编号和 reference number。

## 账单核对

1. 区分 EOB 与 provider bill；EOB 通常不是付款通知。
2. 对齐 patient、provider、service date、CPT/description、billed charge、allowed amount、adjustment 与 patient responsibility。
3. 查 duplicate、错误 network、未提交保险、编码/日期问题。
4. 先联系 insurer/provider billing 并保存 case number。
5. 需要时申请 internal appeal、external review、itemized bill、financial assistance 或 payment plan。

## 来源冲突

- Directory 显示 in-network 但 provider 否认：在就诊前要求双方书面/电话确认；紧急情况不延误。
- 电话答复与 plan document 冲突：保存答复记录并按 plan 的 appeal 路径处理。
- EOB 与 bill 不同：不要立刻按较高金额支付，先核对 claim 状态。

## 输出结构

1. 紧急程度与升级阈值。
2. 核验日期、假设与信息缺口。
3. 1 个首选路径 + 1–2 个备选：距离、时间、network、费用证据。
4. 打电话/到诊时可复制的话与要带的材料。
5. 账单场景给逐项核对表和 case log。
6. Human gate：非紧急预约/付款/签 payment plan 前确认；真正急症不设置延误 gate。

## 失败回退

- 无法确认 network：联系保险 nurse/member services；紧急情况按紧急程度行动。
- 没保险/费用困难：查 provider financial assistance、校内资源和当地官方项目，不建议隐瞒身份或虚假申报。
- 无法浏览：只做安全分流和待核验清单，不编造附近机构或费用。

## Eval 映射

`health-chest-pain`、`health-urgent-care-network`、`health-eob-not-bill`、`health-directory-conflict`、`health-no-insurance`。
