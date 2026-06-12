# BYFIT Evolution Rules

> 定义自动进化的触发条件和执行逻辑。Phase 8 Auto-Learning 的决策引擎。

---

## 1. FAQ Auto-Expansion Rules

### Rule: NEW_FAQ_PATTERN
- **Trigger:** 同一类型问题在不同客户中出现 3+ 次
- **Detection:** 在 `learning/inquiry_log.md` 中搜索 `Pattern Note:`
- **Action:** 新增一条 FAQ 到对应的 FAQ 文件中
- **Template:**

```
### Q: "[New Question]"
- **场景**: [when this arises]
- **根因**: [root cause]
- **调查信号**: [clues]
- **回复策略**: [strategy]
- **回复模板**:
  > [English template with placeholders]
- **CTA**: [action call]
```

### Rule: UNCOVERED_QUESTION
- **Trigger:** 客户提出某个具体问题，现有 8 个 FAQ 模块都没有覆盖
- **Detection:** 在 Phase 0-4 分析中，发现询盘核心问题无法匹配任何现有 FAQ
- **Action:** 新增一条 FAQ 到最相关的 FAQ 文件
- **Note:** 新 FAQ 至少 15 天后再检查是否已有覆盖，避免重复

---

## 2. Scoring Calibration Rules

### Rule: SCORE_MISMATCH
- **Trigger:** 某个 Tier 1 客户（90+分）超过 30 天无回应，或某个 Tier 3 客户（30-59分）快速成交
- **Detection:** 对比 `inquiry_log.md` 中的评分与实际结果反馈
- **Action:** 在 `client_scoring_framework.md` 中加入校准注释，说明该维度可能的偏差

### Rule: NEW_SCORING_SIGNAL
- **Trigger:** 发现新的有效区分信号（如 "客户问展会参与情况" 是高意向新信号）
- **Detection:** 在回盘过程中注意到新的高频信号模式
- **Action:** 将新信号加入 Phase 5 的评分指南

---

## 3. Buyer Archetype Evolution Rules

### Rule: NOVEL_CLIENT_TYPE
- **Trigger:** 遇到现有 8 种买家原型无法完全匹配的客户
- **Detection:** Phase 4.2 匹配时匹配度 < 60%
- **Action:** 在 `references/buyer_archetype_guide.md` 中添加新原型或子类型

### Rule: ARCHETYPE_SIGNAL_REFINEMENT
- **Trigger:** 某个买家原型的匹配信号在 5+ 个客户中被证实为误判
- **Detection:** 回查 inquiry_log 中的 archetype 匹配记录
- **Action:** 更新匹配信号描述，增加/删除特征信号

---

## 4. Email Group Refinement Rules

### Rule: SUBJECT_LINE_PERFORMANCE
- **Trigger:** 某种 Subject 模式连续 3+ 次获得客户回复
- **Detection:** 在 inquiry_log 中比对 Subject 模式与客户反馈
- **Action:** 将该 Subject 模式提升为"推荐"并加入模板注释

### Rule: CTA_OPTIMIZATION
- **Trigger:** 某个 CTA 类型（如 "call me" vs "send samples"）在多个案例中有效率差异
- **Detection:** 模式识别
- **Action:** 在相关 Email Group 模板中调整 CTA 建议顺序

---

## 5. Case Library Expansion Rules

### Rule: NEW_REAL_CASE
- **Trigger:** 成功成交的新客户（不论大小）
- **Detection:** 用户反馈 "成交了" / "客户下单了" / "样品确认了" 等信号
- **Action:** 将客户案例匿名化后加入 `products/[product]/real_world_cases.md`
- **Template:**

```
### Case #[N]: [Anonymized Title]
- Client Profile: [Country, Company Type]
- Pain Point: [痛点]
- Solution: [BYFIT方案]
- Process: [关键步骤]
- Outcome: [结果]
- Key Learning: [经验总结]
```

### Rule: FAQ_TO_CASE
- **Trigger:** 某个 FAQ 被高频查询（Phase 0 识别为"核心痛点"的 3+ 次）
- **Detection:** 在 inquiry_log 中统计 Pain Point 出现频次
- **Action:** 将该痛点对应的处理经验整理成 case 加入 real_world_cases

---

## 6. Market Intelligence Evolution Rules

### Rule: NEW_COUNTRY_INSIGHT
- **Trigger:** 某国家的询盘出现 3+ 次，且触发新的市场模式
- **Detection:** inquiry_log 中 Country 字段统计
- **Action:** 在对应产品的 `market_intelligence.md` 中加入新洞察

### Rule: NEW_CERT_REQUIREMENT
- **Trigger:** 1+ 客户提出市场特定的认证要求，当前未在文档中覆盖
- **Detection:** 询盘中出现新认证名称
- **Action:** 在 `market_intelligence.md` 的对应国家添加认证要求

---

## 7. Supply Chain Role Evolution Rules

### Rule: NOVEL_SUPPLY_CHAIN_ROLE
- **Trigger:** 遇到现有 8 种供应链角色无法完全匹配的客户
- **Detection:** Phase 1.5 分类时匹配度 < 60%
- **Action:** 在 SKILL.md Phase 1.5 的角色表中添加新角色定义

---

## 规则优先级

| 优先级 | 规则 | 原因 |
|--------|------|------|
| P0 | NEW_REAL_CASE | 真实成交案例价值最高 |
| P0 | NEW_FAQ_PATTERN | 提升下次回复效率 |
| P1 | SCORE_MISMATCH | 评分准确性影响所有后续判断 |
| P1 | SUBJECT_LINE_PERFORMANCE | 直接提升回复率 |
| P2 | CTA_OPTIMIZATION | 渐进优化 |
| P2 | ARCHETYPE_SIGNAL_REFINEMENT | 提升原型匹配精度 |
| P3 | NOVEL_CLIENT_TYPE | 扩展边界场景 |
| P3 | NEW_COUNTRY_INSIGHT | 丰富市场情报 |
| P3 | NEW_CERT_REQUIREMENT | 更新合规信息 |

## 规则执行总原则

1. **Append only.** 永不删除已有内容。进化 = 新增 + 注释，不重写
2. **One change per inquiry.** 每次询盘最多触发 1 次进化，避免批量修改的混乱
3. **Traceable.** 每次修改必须注明依据（Inquiry Log #编号）
4. **Review before push to GitHub.** 进化后的文件变更会累积在本地，推送到 GitHub 前用户可以 review
