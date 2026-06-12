# BYFIT Auto-Evolution Engine

> 这是 Phase 8 Auto-Learning 的完整执行指南。
> 每次处理询盘后，由 Phase 8 驱动此引擎。

---

## 核心流程

```
完成 Phase 0-7 输出
       │
       ▼
  8.1 Log Inquiry ────→ 追加到 learning/inquiry_log.md
       │
       ▼
  8.2 Check Triggers ──→ 扫描 evolution_rules.md 所有规则
       │
       ├── Trigger fired? ──→ 8.3 Apply Evolution
       │                         │
       │                         ▼
       │                    8.4 Record in evolution_journal.md
       │
       └── No trigger ──→ 完成
```

---

## 8.1 Log Inquiry (必须执行)

每次询盘处理完成后，立即在 `learning/inquiry_log.md` 末尾追加一条记录。

### 记录格式

```markdown
### Entry #[auto-increment] — [YYYY-MM-DD]
- **Client**: [Name] | [Company] | [Country]
- **Email**: [domain]
- **Product**: [product folder used]
- **Source**: [Inquiry / Proactive / Trade Show / Referral]
- **Grade**: [A/B/C by 外土司]
- **Tier**: [1/2/3/4] | **Score**: [XX]/120
- **Supply Chain Role**: [Distributor/Importer/...]
- **Buyer Archetype**: [Archetype]
- **Email Group**: [Type] — [X] emails
- **Subject Line Used**: [实际使用的主题行]
- **Pattern Note**: [新问题/新痛点/新信号/无特别]
- **Status**: [Sent / Pending Response / Converted / Silent]
- **Feedback**: [客户如回复，记录关键内容]
```

---

## 8.2 Check Evolution Triggers (触发检查)

按优先级顺序检查 `learning/evolution_rules.md` 中的所有规则。

### 检查步骤

```
1. 解析 inquiry_log 的最后一页（当前 + 历史记录）
2. 按优先级 P0→P1→P2→P3 依次检查
3. 对每个规则：
   a. 规则条件是否满足？（如：同一问题出现 3+ 次）
   b. 这个进化是否最近刚做过的？（避免重复进化）
   c. 如果满足 → 标记为待执行，停止检查更低优先级
4. 最多触发 1 个进化
```

### 检查速查表

| 检查项 | 如何查 | 是否满足 |
|--------|--------|----------|
| NEW_FAQ_PATTERN | 搜索 inquiry_log 中 Pattern Note 相同的条目 ≥ 3 条 | Yes/No |
| UNCOVERED_QUESTION | 当前询盘中是否有问题无法匹配 FAQ | Yes/No |
| SCORE_MISMATCH | 是否有历史 Tier 1 客户反馈为 Silent 或 Negative | Yes/No |
| NOVEL_CLIENT_TYPE | 买家原型匹配度是否 < 60% | Yes/No |
| SUBJECT_LINE_PERFORMANCE | 是否有相同 Subject 模式的 3+ 条记录的 Feedback 为 Positive | Yes/No |
| NEW_REAL_CASE | 用户是否反馈"成交了""下了单" | Yes/No |
| NEW_COUNTRY_INSIGHT | 当前国家的询盘总数 ≥ 3 且是第一个客户的触发词 | Yes/No |

---

## 8.3 Apply Evolution (触发执行)

根据触发的规则类型，执行对应的文件修改。

### 文件修改矩阵

| 触发规则 | 修改文件 | 修改方式 |
|----------|----------|----------|
| NEW_FAQ_PATTERN | `faq/faq_[相关模块].md` | 在末尾追加新 FAQ 条目 |
| UNCOVERED_QUESTION | `faq/faq_[最接近的模块].md` | 新增 FAQ 并标记 `[Auto-Evolved]` |
| SCORE_MISMATCH | `references/client_scoring_framework.md` | 在相关维度加校准注释 |
| NOVEL_CLIENT_TYPE | `references/buyer_archetype_guide.md` | 追加新的原型或子类型 |
| NEW_REAL_CASE | `products/[product]/real_world_cases.md` | 追加新案例 |
| SUBJECT_LINE_PERFORMANCE | SKILL.md Phase 6 的 Subject 指南 | 追加优化注释 |
| NEW_COUNTRY_INSIGHT | `products/[product]/market_intelligence.md` | 追加新洞察段落 |
| NEW_CERT_REQUIREMENT | `products/[product]/market_intelligence.md` | 追加认证要求 |

### 追加标注规范

每次进化修改后的内容必须附带以下标注：

```markdown
<!-- auto-evolved: YYYY-MM-DD | Trigger: [规则名] | Source: Entry #[编号] -->
```

这样后续可以追溯到进化来源。

---

## 8.4 Record in Evolution Journal

每次进化执行后，必须在 `learning/evolution_journal.md` 中追加一条记录。

---

## 8.5 Periodic Deep Learning (按需执行)

当用户显示触发（如 "你从这些询盘中学到了什么？" "看看有什么模式" "generate learning report"）：

1. 分析 `learning/inquiry_log.md` 的所有条目
2. 运行批量模式识别：
   - 国家分布统计（哪个国家询盘最多？）
   - 评分分布统计（Tier 1/2/3/4 各多少？）
   - Archetype 分布统计（哪种买家类型最多？）
   - 痛点模式统计（最常见的痛点是什么？）
   - 转化率统计（回复率/成交率估算）
   - Email Group 效率对比
3. 生成一份 Insight Report 呈现在回复中
4. 如果有显著的进化值得做，按 8.3 执行

---

## 防重复机制

- **进化去重：** 相同模式的问题，只在第 3 次出现时进化一次。之后即使再出现也不重复进化，除非间隔 60 天以上
- **修改去重：** 每次修改前检查目标文件是否已有相同或相似内容（新 FAQ 是否已被覆盖？新案例是否已被记录？）
- **日志去重：** 同一个客户的多封邮件处理只记录第一次完整分析，后续小更新标注在原条目
