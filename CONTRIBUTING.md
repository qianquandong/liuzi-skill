# Contributing

欢迎提交真实问题、失效来源、错误结论和更好的执行路径。本项目优先提高现有核心路线的可靠性，而不是单纯增加场景数量。

## 提交前

1. 不要提交 SSN、护照号、账户号、完整医疗记录、精确住址或其他个人敏感信息。
2. 规则、资格、费用、时限和权利义务尽量给直接官方页面。
3. 区分“官方直接确认、第一方自述、第三方支持、合理推测、无法验证”。
4. 高风险主张没有直接官方来源时，只能标为待确认。
5. 新行为必须至少增加或更新一条 `evals/evals.json` 用例。

## 本地验证

需要 Python 3.10+，无第三方 Python 依赖。

```bash
python3 -m unittest discover -s tests -v
python3 scripts/check_source_links.py .
```

可选网络链接探测：

```bash
python3 scripts/check_source_links.py . --network
```

## Pull request checklist

- [ ] 只改了与问题相关的文件
- [ ] 高风险结论有直接官方来源与核验日期要求
- [ ] 动态价格/库存/规则没有硬编码成永久事实
- [ ] 更新了对应 eval
- [ ] 本地测试全部通过

