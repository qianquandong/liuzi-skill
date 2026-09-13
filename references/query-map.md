# 问题路由地图

先匹配用户真正要完成的动作；一句话包含多个动作时，按依赖顺序串联 playbook。

| 用户说法 | 主路由 | 常见联动 |
|---|---|---|
| 刚下飞机、SIM、接机、临时住处 | `arrival.md` | apps、bank、housing |
| 找房、sublease、签 lease、押金 | `housing.md` | roommates、utilities、safety |
| 买车、lease、dealer 报价 | `car.md` | insurance、DMV、driving |
| 驾照、路考、车牌、registration | `dmv.md` | car、insurance |
| 银行账户、信用卡、信用分 | `money-credit.md` | identity-security、saving |
| 回国机票、转机、行李 | `flights.md` | travel、immigration-school |
| 生病、保险、账单 | `healthcare.md` | insurance、emergency |
| CPT、OPT、兼职、1099、创业 | `immigration-school.md` | jobs、taxes |
| 找实习、network、面试 | `jobs.md` | community、immigration-school |
| 饭店、奶茶、超市、外卖 | `food.md` | grocery-shopping、saving |
| 华人群、活动、交朋友 | `community.md` | social-dating、90-day-plan |
| 找对象、约会软件、第一次见面 | `social-dating.md` | safety、etiquette |
| 海运、寄回国、清关 | `shipping.md` | shopping-returns |
| 二手、搬家、卖家具 | `secondhand-moving.md` | safety、address-mail |
| 美国为什么这样 | `unwritten-america.md` | etiquette、对应业务 playbook |

歧义时最多问 3 个问题：位置/日期、预算、不可妥协条件。若能先做出有用结果，就标明假设后直接做。
