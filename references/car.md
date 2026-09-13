# 第一辆车、二手车与租车

## 最少输入

- ZIP/城市、年龄、驾照状态、驾驶历史
- OTD 上限、月现金流上限、现金或 financing、预计持有年限
- 通勤里程、年里程、用途、停车/toll、雪地或恶劣天气需求
- 不可接受 title/事故/里程/车型条件
- 是否已有保险 quote；不要收驾照号或保单完整号码

## 硬筛选

1. OTD 与预计持有期 all-in 不超过预算。
2. 可获得且可承担保险；先 quote 后选车。
3. VIN、title、recall、里程和卖方身份可核验。
4. 拒绝独立 PPI、要求异常付款、title 不在卖方名下或无法完成州规定过户时淘汰。
5. salvage/rebuilt/flood/lemon/buyback 等若在用户禁区直接淘汰，不靠低价补分。

## 搜索顺序

1. 州 DMV/DPS：title、registration、税费、临牌和 private-party/dealer 过户。
2. NHTSA：VIN recall 与安全信息。
3. 保险公司官方 quote；统一 liability limits、deductible 和 coverage。
4. Dealer/卖方书面 listing、VIN、buyer order 和 itemized OTD。
5. KBB/Edmunds/CarGurus 等用于行情区间，不替代车况或 PPI。

## 总成本公式

`持有期总成本 = OTD + total interest + insurance + fuel/charging + maintenance/repairs + parking/toll + inspection/registration renewals - expected resale value`

`月均 all-in = 持有期总成本 ÷ 持有月数`

financing 同时报 APR、term、amount financed、total of payments；不以月供单独比较。

## 单车核验顺序

1. VIN 与卖方/产权身份。
2. title/history、事故、里程、recall、盗抢与 lien。
3. 冷车启动和试驾：警示灯、刹车、轮胎、空调、异响、高速稳定。
4. 独立技师 PPI，获取书面问题和维修估价。
5. 同 coverage 保险 quote。
6. itemized written OTD，删除未同意 add-on 后重打印。
7. 按州官方流程付款、签字、过户和留存文件。

## 证据冲突

- Vehicle history 与 PPI 冲突：两者都保留，机械现状以独立 PPI 为核心，产权/事故仍需官方或可信记录核验。
- 广告价与 buyer order 不同：只用最终 itemized OTD 排名。
- Dealer 说某 add-on “必须”：要求指出书面法律或贷款要求；否则单列为可拒绝项。

## 输出结构

1. 核验日期、预算和硬约束。
2. 淘汰清单与具体原因。
3. 正式候选：OTD、保险、预计维修、持有期 all-in、证据状态。
4. 最省钱 / 最均衡 / 最省心与明确首选。
5. 发给 dealer/卖方、技师、保险公司的可复制话术。
6. Human gate：付定金、签 buyer order/loan、转账或接车前停下确认。

## 失败回退

- 拿不到 VIN/OTD/PPI：不排名或淘汰。
- 保险超预算：换车型/coverage 参数重新 quote，不削减到不理解的保障。
- 市场无匹配：比较短期租车、公交/骑行、延后购买的 all-in，不急买问题车。
- 私人卖家流程不明：回到州 DMV 官方 checklist。

## 租车

核验 underage fee、押金、保险覆盖、additional driver、toll、里程、跨州、还车油量和 damage claim 流程。

## Eval 映射

`car-otd-trap`、`car-no-vin`、`car-salvage-budget`、`car-insurance-first`、`car-private-payment-scam`。
