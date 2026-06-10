---
name: byfit-trade-master
description: "BYFIT外贸全流程大师Skill — 整合毅冰Email Group、外土司、料神Sam三大方法论。支持：外贸市场调研→客户背景调查→社媒信息调查→采购行为分析→核心需求调查→痛点挖掘→客户分级→多渠道回复（Email/WeChat/WhatsApp）。Auto-Mode: 用户发送客户name+email+message自动调查回复。覆盖三大产品线(Gym Rubber Flooring/Gym Equipment/Pilates Equipment)，每种产品独立文件夹。综合运用海关数据、银行信息、社媒数据等进行深度背调。谈判策略采用毅冰Email Group模式，跟进开发采用外土司方法论，背调开发采用料神Sam谷歌技巧。触发词：调查客户背景/分析这个客户/帮我写跟进邮件/客户痛点分析/邮件组/毅冰/Email Group/谈判策略/报价邮件组/FAQ/客户砍价怎么回/外土司/询盘分析/客户社媒/海关数据/客户分级/市场调研/料神/谷歌开发/draft a reply to this buyer/client background check/social media investigation/customs data lookup/client grading/market research/自动背调回复"
agent_created: true
---

# BYFIT Trade Master — 外贸全流程大师

> **核心管道：料神找到他们 → 外土司分级他们 → 毅冰拿下他们**

本 Skill 是 BYFIT 品牌专属的 B2B 外贸全流程处理引擎。当收到客户询盘（name + email + message），自动执行三段式硬管道：
- **料神段**（Phase 1-2）：6步背景调查 + 供应链角色分类 + 客户裂变
- **外土司段**（Phase 0 + 3-5）：询盘分级 + 7维评分 + 采购行为分析 + 痛点挖掘 + 买家原型匹配
- **毅冰段**（Phase 6-7）：Email Group 全序列生成 + 5步谈判框架 + 多渠道回复

---

## Seller Profile

```yaml
seller:
  name: Eric
  email: sales@sdbyfit.com
  websites: [https://byfitgear.com, https://shandongbyfit.com]
  brand: BYFIT
  country: China
  products: [Gym Rubber Flooring, Gym Equipment, Pilates Equipment]
  business_model: B2B Wholesale Only
  facility: Factory with 20 production lines
  port: FOB Qingdao
  export_countries: [US, Germany, UK, France, Italy, UAE, Saudi Arabia, Japan, South Korea, Australia]
  target_buyers: [Large company buyers, Gym Flooring Importers/Distributors, Gym Owners/Operators, Sporting Goods Retailers, E-commerce Retailers]
  features: [Diverse Products, Top Quality, Customizable Logo, Durability, High Value for Money, Eco-Friendly, Shock Absorption, Anti-Slip]
  promotion: [Exhibitions, Google Ads, Customer Referral]
```

---

## Trigger Words

| Category | Triggers (Chinese + English) |
|---|---|
| **Auto Intake** | 发客户信息自动调查回复 / 自动背调回复 / 帮我查这个客户并回复 / auto investigate and reply / drop client info |
| Market Research | 外贸市场调研 / 市场调查 / 目标市场分析 / market research / target market analysis |
| Background Investigation | 调查客户背景 / 客户背调 / 背景调查 / client background check / investigate buyer / company verification |
| Social Media | 客户社媒调查 / 社媒信息 / LinkedIn调查 / social media investigation / buyer social profiles |
| Purchasing Behavior | 客户采购调查 / 海关数据查客户 / 进口记录 / purchasing behavior / customs data lookup |
| Core Needs | 核心需求调查 / 客户需求分析 / core needs analysis / buyer needs |
| Pain Points | 痛点挖掘 / 客户痛点分析 / pain point mining / buyer pain analysis |
| Client Grading | 客户分级 / 客户评分 / 客户等级 / client grading / lead scoring |
| Message Drafting | 帮我写邮件 / 写跟进 / 邮件组 / 谈判策略 / 报价邮件组 / 催单 / draft reply / follow up email / Email Group |
| 毅冰 Method | 毅冰 / Email Group / 邮件组 / 谈判邮件组 / 报价邮件组 / 跟进邮件组 / 催单邮件组 |
| 外土司 Method | 外土司 / 询盘分析 / 网红标题 / 催款 / 客户管理 / 展会跟进 |
| 料神 Method | 料神 / 谷歌开发 / Google搜索开发 / 背调技巧 / Liaoshen / Google development |
| Product Routing | 橡胶地垫 / gym flooring / 健身器材 / gym equipment / 普拉提 / pilates |

**Auto-trigger:** When user drops raw client details (name + email + message in any format), activate the full pipeline immediately. Do NOT ask "Do you want me to investigate?" — just do it.

---

## 三段式硬管道

```
┌──────────────────────────────────────────────────────────────────┐
│                     THREE-SEGMENT PIPELINE                        │
├────────────┬───────────────────┬─────────────────────────────────┤
│ 料神段      │ 外土司段           │ 毅冰段                           │
│ Phase 0-2  │ Phase 3-5         │ Phase 6-7                       │
├────────────┼───────────────────┼─────────────────────────────────┤
│ 6步背调    │ 7维评分→分级       │ Email Group类型选择              │
│ 供应链角色  │ 采购行为分析        │ 全序列生成（5封/4封）            │
│ 客户裂变    │ 痛点6层挖掘        │ 5步谈判框架                     │
│ 社媒深度    │ 买家原型匹配        │ 条件性让步+三层报价              │
│            │                   │ 多渠道（Email/WA/WeChat）        │
└────────────┴───────────────────┴─────────────────────────────────┘
```

**任何询盘处理都必须跑完三段管道。不允许跳过任何一段。**

---

## Phase 0: 外土司询盘分级（入口）

### 0.1 解析输入

自动提取：客户姓名、公司名、邮箱域名、国家/地区、网站URL、产品关键词、询盘正文。

### 0.2 外土司3步分析（强制）

**Step 1 — 身份检查 (Identity Check):**
- 公司域名邮箱 → +20分；Gmail/Yahoo/Hotmail → +0分
- 签名含电话/地址/职位 → +10分；无签名 → +0分
- 是否能搜到 LinkedIn 个人资料 → +5分

**Step 2 — 意图诊断 (Intent Diagnosis):**
- 有具体规格（厚度/数量/型号）→ 高意向
- 有产品线提及但无规格 → 中意向
- "send catalog" / "what's your price" 一句 → 低意向
- 有技术问题 → 超高意向（比报价需求更强）

**Step 3 — 质量评级:**

| Grade | 条件 | 策略 |
|---|---|---|
| **A级** | 公司域名 + 具体询盘 + 量/时间提及 | 全管道（Phase 1-7），100%火力 |
| **B级** | 公司邮箱 + 模糊询盘，或个人邮箱 + 具体询盘 | 全管道但可缩检测深度，60%火力 |
| **C级** | 通用邮箱 + 一行询盘 / 无公司信息 | 模板回复，不跑管道 |

### 0.3 产品路由

匹配询盘关键词到产品文件夹：

| Product | Keywords | Folder |
|---|---|---|
| Gym Rubber Flooring | rubber floor, gym mat, rubber tile, rubber roll, EPDM, stall mat, anti-slip, 橡胶地垫 | `products/gym-rubber-flooring/` |
| Gym Equipment | gym equipment, strength, cardio, treadmill, dumbbell, power rack, functional trainer, 健身器材 | `products/gym-equipment/` |
| Pilates Equipment | pilates, reformer, Cadillac, barrel, 普拉提 | `products/pilates-equipment/` |

默认 → `products/gym-rubber-flooring/`

---

## Phase 1: 料神Sam 6步背景调查（强制）

> **料神原则：调查深度决定了回复的质量。没有调查就没有发言权。**

**MUST 执行以下全部 6 步，不可跳过。**

### Step 1 — About Us 深度分析

**操作指令（强制执行）：**

1. 使用 WebFetch 抓取 `https://[公司域名]/about-us`（尝试 `/about`, `/company`, `/our-story`, `/who-we-are`）
2. **必须提取以下信息：**
   - 公司成立年份（<5年 = 新公司风险；>10年 = 稳定）
   - 公司规模（员工数、仓库面积、年营收区间）
   - 使命/价值观描述 → 用于对齐回复中的价值主张
   - 关键人物姓名（CEO、采购负责人、创始人）
   - 发展历程（收购、扩张、新品线 → 采购需求变化信号）
   - 公司性质描述中的关键词（"we are a leading distributor of..." → 供应链角色信号）

3. **输出格式（强制）：**
```
## 料神 Step 1 — About Us 分析
- 成立年份: [year] → [信号解读]
- 规模: [employees/warehouse] → [匹配MOQ判断]
- 公司性质: [原文关键句] → [供应链角色推测]
- 关键人物: [name, title]
- 发展动态: [expansion/merger/new line] → [需求信号]
```

### Step 2 — 首页&产品导航分析

**操作指令（强制执行）：**

1. 使用 WebFetch 抓取公司首页
2. **必须分析：**
   - 导航栏产品分类（哪些是核心品类=排前面？哪些是附属？）
   - 是否有与 BYFIT 产品重叠的品类？
   - 是否有 BYFIT 能填补的空白品类？（这是黄金切入点）
   - 产品描述中的品牌名——是他们自己的品牌还是代理品牌？
   - 是否有 "New Products" / "Coming Soon" 栏目？
   - 价格显示方式——零售价？批发询价？→ 判断 B2B vs B2C

3. **输出格式（强制）：**
```
## 料神 Step 2 — 产品导航分析
- 核心品类: [list]
- 重叠品类: [BYFIT能供应的部分]
- 空白品类: [BYFIT可切入的缺失部分] ← 黄金切入点
- 品牌信号: [自有品牌/代理品牌/混合]
- 价格模式: [零售价/批发询价/无价格] → [B2B vs B2C判断]
```

### Step 3 — 品牌网站陷阱识别

**操作指令（强制执行）：**

1. **检查以下信号：**
   - 网站有 ® 或 ™ 标志？→ 品牌商，可能不采购竞品
   - 只卖一个品牌的产品？→ 独家代理或自有品牌
   - "Where to buy" 而非 "Contact us for wholesale"？→ B2C，不是采购方
   - 没有 wholesale / distributor / trade 页面？→ 可能不对外采购
   - Footer 的版权公司名 ≠ 网站品牌名？→ 品牌≠公司，需进一步追

2. **输出：**
```
## 料神 Step 3 — 品牌陷阱
- 品牌信号: [无 / 有®标志 / 单品牌 / 多品牌]
- B2B信号: [有wholesale页面 / 有trade account / 无]
- 结论: [真实采购方 / 品牌零售站 / 需OEM切入 / 不适合]
- 切入策略: [直接联系采购 / OEM角度切入 / 放弃]
```

### Step 4 — 母公司追溯

**操作指令（强制执行）：**

1. 在 About Us 页面搜索关键短语："part of", "a subsidiary of", "owned by", "a division of", "member of"
2. Google 搜索：`"[Company Name]" parent company` 和 `"[Company Name]" subsidiary`
3. LinkedIn 搜索公司页面 → 查看 "Parent Company" 字段
4. 对比网站 Footer 版权公司名 vs 品牌名——如果不一致，Footer 里的公司才是母公司

**输出：**
```
## 料神 Step 4 — 母公司追溯
- 母公司: [name / 无]
- 关联公司: [sister companies]
- 母公司规模: [if found]
- 采购决策层级: [母公司集团采购 / 子公司独立采购 / 无法确定]
```

### Step 5 — 锁定决策公司

**操作指令（强制执行）：**

基于 Step 4 的结果，判断真正的采购决策实体：
- 独立公司 → 直接联系该公司
- 子公司（独立采购权）→ 联系子公司采购
- 子公司（采购归母公司）→ 联系母公司采购部
- 集团采购中心 → 联系采购中心负责人
- 加盟/特许经营 → 联系总部供应链

### Step 6 — 邮箱破解

**操作指令（强制执行）：**

1. `site:[公司域名] email` / `site:[公司域名] contact`
2. `site:[公司域名] "@[公司域名]"` — 搜内部邮箱
3. `"@[公司域名]" "purchasing" OR "buyer" OR "procurement" OR "sourcing"` — 搜采购人员
4. `site:linkedin.com/in "[公司名]" "purchasing manager"` — LinkedIn 采购负责人
5. 邮箱格式猜测：firstname@ / firstname.lastname@ / f.lastname@ / firstname_lastname@
6. 使用 WHOIS 查域名注册邮箱

---

## Phase 1.5: 料神 供应链角色分类 + 客户裂变（强制）

### 1.5.1 供应链角色分类

**MUST 使用料神的供应链角色词系统对客户进行分类：**

| 角色 | 关键词 | 特征 | BYFIT策略 |
|---|---|---|---|
| **分销商 (Distributor)** | distributor, distribution partner | 批量采购，区域分销，多品类 | 推组合产品+区域保护 |
| **进口商 (Importer)** | importer, import, importation | 有进口能力，通常中型 | 推FOB条款+MOQ灵活 |
| **批发商 (Wholesaler)** | wholesaler, wholesale dealer | 大批量，价格敏感 | 推量大折扣+标准品 |
| **代理商 (Agent)** | agent, representative, exclusive agent | 区域代表，品牌代理 | 推独家代理条件 |
| **经销商 (Dealer)** | dealer, authorized dealer | 品牌授权销售 | 推品牌定制方案 |
| **零售商 (Retailer)** | retailer, retail chain, specialty store | 终端零售，量小 | MOQ低+包装方案 |
| **项目承包商 (Contractor)** | contractor, fit-out, installation | 项目驱动，单次量大 | 推全案供应+技术支持 |
| **品牌商 (Brand Owner)** | brand, private label, OEM | 自有品牌生产 | 推OEM/ODM方案 |

**输出分类 + 对应的 BYFIT 切入策略。**

### 1.5.2 客户裂变（料神核心技术）

**MUST 从 Step 1 的 About Us 描述中提取特征句子，生成裂变搜索词：**

格式：
```
原始句子: "[从About Us提取的描述句]"
特征短语1: "[phrase]" → 搜索: "[phrase] distributor [country]"
特征短语2: "[phrase]" → 搜索: "[phrase] importer [country]"
```

记录输出但不执行搜索（供用户后续开发使用）。

---

## Phase 2: 社媒信息调查

### 平台调查（强制执行）

| 平台 | 搜索内容 | 工具 |
|---|---|---|
| **LinkedIn** | 公司主页（规模、动态、招聘）；联系人（职位、活跃度、人脉） | WebSearch: `site:linkedin.com/company "[公司名]"` |
| **Facebook** | 商业页（评价、活动、促销）；行业群组 | WebSearch: `"[公司名]" Facebook` |
| **Instagram** | 产品展示、用户标签、品牌合作 | WebSearch: `"[公司名]" Instagram` |
| **YouTube** | 产品视频、开箱评测 | WebSearch: `"[公司名]" YouTube` |
| **Trustpilot/Google Reviews** | 客户满意度、常见投诉 | WebFetch |
| **Reddit/Quora** | 行业讨论、品牌提及 | WebSearch |

**必须提取的关键信号：**
- 🟢 招聘信号 → 公司扩张，可能需新供应商
- 🟢 新品发布 → 新品类，新采购需求
- 🔴 投诉现有供应商 → 切换窗口打开
- 🟢 展会动态 → 活跃采购，接触时机好
- 🟡 高管变动 → 新采购领导，供应商重审

---

## Phase 3: 海关数据 + 采购行为分析

### 3.1 海关数据搜索（执行指令）

```
"[公司名]" import records
"[公司名]" customs data
"[公司名]" shipping records
site:importgenius.com "[公司名]"
site:panjiva.com "[公司名]"
"[产品关键词]" importer of record "[国家]"
```

**提取：** HS编码、进口量、进口频次、来源国、供应商模式。

### 3.2 采购周期推断

- 高峰期（健身行业：年初、夏季前、返校季）
- 预估年采购量（基于进口频次×单次量）
- 订单模式（整柜/LCL/混装）

### 3.3 决策链分析

```
决策者（谁签字）→ 影响者（谁建议）→ 使用者（谁用产品）
```

---

## Phase 4: 痛点6层挖掘 + 买家原型匹配

### 4.1 痛点6层金字塔（强制逐层分析）

| Layer | 深度 | 示例 |
|---|---|---|
| **Layer 0: 行业结构性痛点** | 行业普遍 | "EU橡胶地板市场被3家分销商垄断" |
| **Layer 1: 表面声称** | 买家说的 | "Your price is too high" |
| **Layer 2: 业务影响** | 如何影响生意 | "Margins squeezed, can't compete with chains" |
| **Layer 3: 根因** | 真正原因 | "Current supplier no volume discount, quality inconsistent" |
| **Layer 4: 情绪** | 感受 | "Frustrated choosing between quality and price" |
| **Layer 5: 未说出口** | 不敢说 | "Afraid of making a bad decision and losing my job" |

**必须对每个询盘逐层分析，至少覆盖 Layer 0-3。**

### 4.2 买家原型匹配（8选1）

| Archetype | Key Trait | 匹配信号 | 毅冰Email Group |
|---|---|---|---|
| Price Hunter | 最低价 | 只谈价格、不关心规格 | Negotiation Group（三层报价） |
| Quality Seeker | 品质第一 | 问认证、材料、检测报告 | Quotation Group（价值锚定） |
| Brand Builder | 建自有品牌 | 问OEM/ODM、包装定制 | Quotation + OEM展示 |
| Volume Buyer | 大规模系统采购 | 提年用量、多品类 | Order Push Group |
| Innovation Pioneer | 要最新 | 问新品、新技术 | Quotation Group（产品亮点） |
| Risk Avoider | 需保证 | 问质保、退货政策、案例 | Follow-Up Group（案例佐证） |
| Relationship Driven | 个人信任 | 频繁非正式沟通、WhatsApp | 长期培育 |
| Efficiency First | 快简单 | 直接问交期、下单流程 | Order Push Group（快速成交） |

---

## Phase 5: 7维客户评分（强制）

| Dimension | Max | Scoring |
|---|---|---|
| 1. 采购意向 | 25 | 具体规格+数量+时间线=20-25；有规格无数量=12-19；模糊=5-11；一行="price?"=0-4 |
| 2. 公司质量 | 20 | 知名企业=18-20；可查证中小企=12-17；能查到但信息少=6-11；查不到=0-5 |
| 3. 采购潜力 | 20 | 整柜/长期合同=16-20；LCL/季度=10-15；小批量=5-9；无法判断=0-4 |
| 4. 市场匹配 | 20 | BYFIT产品完美匹配=16-20；大部分匹配=10-15；部分匹配=5-9；不匹配=0-4 |
| 5. 沟通质量 | 15 | 快速+专业+详细=12-15；正常=7-11；慢+简短=3-6；不回复=0-2 |
| 6. 社媒活跃度 | 10 | LinkedIn活跃+公司页面更新=8-10；有账号但不活跃=4-7；无线索=0-3 |
| 7. 采购行为匹配 | 10 | 有进口记录+周期对齐+切换信号=8-10；有进口记录=5-7；无线索=0-4 |

| Total | Tier | Label | 策略 |
|---|---|---|---|
| 90-120 | 🔴 Tier 1 | Priority | 全火力。毅冰完整Email Group。当日回复。 |
| 60-89 | 🟡 Tier 2 | Active | 标准Email Group。24h回复。推样品。 |
| 30-59 | 🟢 Tier 3 | Nurture | Follow-Up Group。周度触达。价值内容。 |
| 0-29 | ⚪ Tier 4 | Monitor | 一封模板回复，不跟进。 |

---

## Phase 6: 毅冰 Email Group 回复生成（核心输出）

> **毅冰原则：谈判是一个过程，不是一封邮件。永远不要在一封邮件中亮出所有底牌。控制节奏，构建沉没成本。**

**这是整个 Skill 的核心输出阶段。必须生成完整的 Email Group 序列，不是一封邮件。**

### 6.1 Email Group 类型选择矩阵（强制）

| 场景 | Email Group | 封数 | 周期 |
|---|---|---|---|
| 收到新询盘，需报价 | **Quotation Group** | 5封 | 8天 |
| 对方对报价提异议（价格高） | **Negotiation Group** | 5封 | 8天 |
| 报价后对方沉默不回复 | **Follow-Up Group** | 4封 | 18天 |
| 对方表达购买意向但不下单 | **Order Push Group** | 4封 | 7天 |
| 展会接触后 | **展会跟进序列（外土司）** | 5封 | 12天 |

**首次询盘默认使用 Quotation Group。**

### 6.2 Quotation Email Group — 强制模板结构（5封/8天）

**MUST 按以下结构生成全部 5 封邮件，不要只生成第一封。**

---

#### Q1 (Day 1): 确认需求 — NOT 报价

**毅冰原则：不直接报价，先确认需求。这让你显得专业，同时争取时间了解对方预算水平。**

```
Subject: Re: [原邮件主题] — BYFIT

Hi [Name],

[感谢询盘 — 1句]

Before I prepare a precise quotation, let me confirm your requirements:

- Application: [Commercial gym / Home gym / Other]?
- Product type: [Tiles (interlocking) / Rolls (glue-down)]?
- Thickness: [常见厚度选项]?
- Quantity: [Approximate sqm or container load]?
- Destination port: [Port, Country]?

This helps me recommend the right product grade and give you an accurate
price — rather than a generic quote.

I'll send the quotation within 24 hours once confirmed.

Best regards,
Eric
BYFIT | Gym Flooring & Equipment Manufacturer
WhatsApp: +86-XXX-XXXX-XXXX
Email: sales@sdbyfit.com
Web: www.byfitgear.com
```

---

#### Q2 (Day 2 or 客户回复后): 报价 + 价值框架

**毅冰原则：报价不只报数字，要附带"价值语境"。用精确数字（$13.80而非$14），显得经过认真计算。**

**MUST 嵌入 BYFIT 6大差异化：**

```
Subject: BYFIT [product] quotation for [Company Name]

Hi [Name],

As discussed, here's our quotation:

| Item | Spec | MOQ | FOB Qingdao Price |
|------|------|-----|-------------------|
| [产品名1] | [规格] | [MOQ] | $XX.XX/[unit] |
| [产品名2] | [规格] | [MOQ] | $XX.XX/[unit] |
| [产品名3] | [规格] | [MOQ] | $XX.XX/[unit] |

WHAT'S INCLUDED (不只是价格):
- [认证] certified quality — [具体认证名称]
- Batch QC report shipped with every container
- Standard export pallet packaging
- Free replacement for defective pieces (rate >2%)
- [BYFIT独有优势 — 从product_knowledge.md提取1个]

Valid for 30 days.
Production lead time: [X] days. Shipping to [Port]: [Y] days.

Would you like to adjust any specs or quantities?

Best regards,
Eric
```

---

#### Q3 (Day 4): 技术深度补充

**毅冰原则：证明你值这个价格。每次邮件只讲一个价值点。**

```
Subject: Technical note — [一个核心卖点]

Hi [Name],

Following the quotation — here's one technical detail that matters:

[选一个BYFIT产品核心技术优势，深度展开]:
- 原材料差异（Virgin SBR vs Recycled → 为什么我们的密度更稳定）
- 生产工艺差异（硫化时间/压力/温度 → 为什么我们的更耐用）
- 品控差异（检测点数/公差 → 为什么我们的退货率<0.3%）
- 认证差异（通过XX标准 → 为什么能进入你们市场）

[技术对比数据，用数字说话]

This directly affects installation quality and end-user experience.

Happy to share the full lab test report.

Best regards,
Eric
```

---

#### Q4 (Day 6): 案例佐证（Social Proof）

**毅冰原则：用"类似客户的成功故事"降低对方感知风险。**

**MUST 从 `products/[product]/real_world_cases.md` 提取一个最匹配的案例：**

```
Subject: How [similar company type] solved [pain point] with BYFIT

Hi [Name],

A quick case that might be relevant:

[从 real_world_cases.md 提取或构造]:
- Client profile: [匿名化的客户类型，如 "a distributor in Germany"]
- Challenge: [痛点，必须与 Phase 4 的痛点分析对齐]
- Our solution: [BYFIT如何解决]
- Result after 12 months: [量化结果]

This is similar to the situation we've been discussing.

Best regards,
Eric
```

---

#### Q5 (Day 8): 行动邀请（The Close）

**毅冰原则：给出明确的下一步，不给开放式结尾。**

```
Subject: Next step for [Company Name] — [Option A] or [Option B]?

Hi [Name],

Over the past week, I've shared:
1. Product specs and pricing tailored to your requirements
2. Technical details on [core differentiator]
3. A real case from [similar client situation]

Two options to move forward:

Option A: Sample evaluation
Send you [X] samples via DHL. You'll receive in 5-7 days.
Sample cost: $XX (refundable against first order).

Option B: Quick call
15 minutes to discuss your timeline and specifics.
[Suggest 2-3 time slots]

Which works better for you?

Best regards,
Eric
```

---

### 6.3 Negotiation Email Group — 强制模板结构（5封/8天）

**当对方对价格提出异议时，MUST 使用此序列。**

> **毅冰5步谈判框架：Anchor First → Listen & Classify → Conditional Concession → Tiered Offer → The Close**

#### N1 (Day 1): 确认异议 — NOT 急于降价

```
Subject: Re: Price feedback — let me understand better

Hi [Name],

Thank you for sharing your price expectation.

Before I explore solutions:
- Is your target based on a specific competitor's offer, or a budget ceiling?
- Are we comparing same specs? (Virgin SBR vs recycled can be 15-20% apart)
- Besides price, are there other terms to adjust? (MOQ, payment, lead time)

This helps me find a real solution, not just a number.

Best regards,
Eric
```

#### N2 (Day 2): 价值重申 — Total Cost of Ownership

**毅冰原则：不要直接降价。先让客户理解"为什么值这个价"。**

```
Subject: The real cost of "cheap" flooring

Hi [Name],

I understand price is important. Let me share a quick comparison:

Cheap flooring costs:
- Return rate: 10-15% → Replacement logistics: $5-8/sqm
- Inconsistent quality → Brand reputation damage: immeasurable
- No warranty → You bear all risk

BYFIT flooring:
- Return rate: <0.3%
- Batch QC report per shipment
- 2-year warranty + free defect replacement

The invoice price is not the real cost. Total cost of ownership is.

Best regards,
Eric
```

#### N3 (Day 4): 条件性让步

> **毅冰铁律：每一个降价都必须有对方的让步。永远不要无条件降价。**

```
Subject: A possible solution for both sides

Hi [Name],

I discussed with our team. Here's what we can explore:

If you can commit to:
- [我方要求1: e.g., 40'HQ container instead of 20']
- [我方要求2: e.g., 50% deposit instead of 30%]

We can offer:
- [让步1: e.g., 5% discount]
- [让步2: e.g., Priority production slot — lead time reduced to 18 days]
- [让步3: e.g., Free sample shipment]

This is a partnership model — both sides invest.

Would these terms work?

Best regards,
Eric
```

#### N4 (Day 6): 三层报价（Decoy Effect）

> **毅冰原则：永远给三个选项。Premium让Standard看起来性价比高。Economy的存在让客户觉得有选择。**

```
Subject: Three options for your project

Hi [Name],

Here are three tiers for maximum flexibility:

╔══════════════╦══════════════╦══════════════╦══════════════╗
║              ║ PREMIUM      ║ STANDARD ⬅   ║ ECONOMY      ║
╠══════════════╬══════════════╬══════════════╬══════════════╣
║ Material     ║ [最高配]     ║ [推荐配置]   ║ [基础配置]   ║
║ Certification║ [最多认证]   ║ [核心认证]   ║ [基础认证]   ║
║ Warranty     ║ 5 years      ║ 3 years      ║ 1 year       ║
║ FOB Price    ║ $XX.XX       ║ $XX.XX       ║ $XX.XX       ║
║ Best for     ║ Premium gyms ║ Standard gyms║ Budget projects║
╚══════════════╩══════════════╩══════════════╩══════════════╝

Most of our distributors start with Standard and add Premium later.

Which tier fits your market?

Best regards,
Eric
```

#### N5 (Day 8): 最终方案 + 紧迫感

```
Subject: Final offer — valid until [Date: 7天后]

Hi [Name],

Here's my best proposal after our discussions:

[总结已达成的内容]
- Product: [spec]
- Price: $XX.XX FOB Qingdao
- MOQ: [agreed]
- Payment: [agreed]
- Bonus: [额外赠品]

Valid until [Date] due to:
- Production slots filling for [Month]
- Raw material price trending up

Can we move forward?

Best regards,
Eric
```

---

### 6.4 Follow-Up Email Group — 强制模板结构（4封/18天）

**毅冰原则：每封邮件必须有新价值。禁止 "Just checking in"。**

| 邮件 | 时间 | 角度 | 新价值 |
|---|---|---|---|
| F1 | Day 3 | 温和提醒 | "有没有需要调整的地方？" |
| F2 | Day 7 | 价值追加 | **新品/新认证/市场趋势报告** |
| F3 | Day 12 | 关怀角度 | 行业洞察 + 原材料价格提醒（紧迫感） |
| F4 | Day 18 | 优雅退出 | "关档" + 留 WhatsApp + "随时可以重新开始" |

**F2 必须包含一个确实新的价值点（新产品、新认证、新市场数据、新案例），不能是重复信息。**

**F4 的关键技巧：说 "I'm closing the file" 反而经常收到回复——给对方一个安全退出通道。**

---

### 6.5 Order Push Email Group — 强制模板结构（4封/7天）

**适用于 Tier 1 客户已表达明确意向但迟迟不下单。**

| 邮件 | 时间 | 角度 |
|---|---|---|
| P1 | Day 1 | 逐条确认订单细节 → 发 PI |
| P2 | Day 3 | 真实紧迫感（排产、原材料、船期） |
| P3 | Day 5 | 风险翻转（等待的成本 > 下单的成本） |
| P4 | Day 7 | 假设成交（直接发 PI，语气是"已决定"） |

---

### 6.6 毅冰高级策略（必须应用）

**在任何 Email Group 中，MUST 遵循以下规则：**

1. **沉没成本原则：** 每封邮件要求一个小行动（回复确认、提供信息、选择方案），让对方持续投入。不要一封邮件解决所有问题。

2. **条件性让步铁律：** 每一次降价，必须换取对方一个让步（量、预付款、排他性、交期）。绝不允许无条件降价。

3. **Decoy Effect：** 任何报价场景都给出 3 个选项（Premium/Standard/Economy），Standard 是目标成交层。

4. **Anchoring：** 首次报价留 8-15% 让步空间。用精确数字（$13.80 而非 $14）增加可信度。

5. **Friday Send：** 逼单邮件（P2-P4）和最终报价（N5）在周五发送——决策者周末前倾向于"清收"待办。

6. **Spoken Word：** 4封以上邮件沟通后，必须推电话/视频通话。"We've exchanged quite a few emails — a 10-minute call might be more efficient."

7. **Subject Line 铁律：** 永远不要用 "Re: Your Inquiry" 或 "Following Up"。每封邮件主题必须传达新价值。

---

### 6.7 多渠道适配

| Channel | Tone | Length | Signature |
|---|---|---|---|
| **Email** | 专业、结构化 | 150-300 words | 全签名 |
| **WhatsApp** | 直接、友好、移动优先 | 60-120 words | 名字+公司 |
| **WeChat** | 温暖、简洁、可用表情 | 80-150 words | 名字+公司 |

**对于 WhatsApp/WeChat，必须将 Email Group 内容压缩为单条消息的简洁版本，同时保留核心价值点。**

---

### 6.8 产品知识嵌入（强制）

**MUST 从 `products/[product]/product_knowledge.md` 提取以下内容嵌入回复：**
- 6大差异化（至少用1个）
- 具体认证名称
- MOQ/交期/价格区间
- OEM能力描述

**MUST 从 `products/[product]/market_intelligence.md` 提取：**
- 目标市场的认证要求
- 目标市场的竞争格局
- 目标市场价格区间参考

---

## Phase 7: 最终交付格式（强制）

```
═══════════════════════════════════════════
  BYFIT Trade Master — 全流程分析报告
  客户: [Name] | [Company] | [Country]
  产品: [Product] | 分级: [Tier] | 评分: [Score]/120
═══════════════════════════════════════════

━━━ 料神段 ━━━

📊 6步背调结果
  Step 1 About Us: [关键发现]
  Step 2 产品导航: [重叠/空白品类]
  Step 3 品牌陷阱: [结论]
  Step 4 母公司: [结果]
  Step 5 决策公司: [结论]
  Step 6 邮箱: [结果]

🏷 供应链角色: [Distributor/Importer/...] → [切入策略]

🔍 客户裂变词:
  "[特征短语1]" → "[搜索词]"
  "[特征短语2]" → "[搜索词]"

📱 社媒信号:
  LinkedIn: [发现]
  FB/IG/YT: [发现]
  🟢 [正面信号] / 🔴 [负面信号]

━━━ 外土司段 ━━━

📋 询盘分析: [外土司3步评级理由]

💰 采购行为:
  海关数据: [进口记录/无]
  采购周期: [预估]
  年采购量: [预估区间]
  决策链: [Decision Maker → Influencer → End User]

🎯 痛点分析:
  Layer 0 行业: [行业结构性痛点]
  Layer 1 表层: [买家说了什么]
  Layer 2 业务: [如何影响生意]
  Layer 3 根因: [真正原因]
  Layer 4 情绪: [感受]
  Layer 5 未说: [不敢说]

👤 买家原型: [Archetype] — [匹配依据]

📊 7维评分:
  1.采购意向[xx/25] 2.公司[xx/20] 3.潜力[xx/20] 4.匹配[xx/20]
  5.沟通[xx/15] 6.社媒[xx/10] 7.采购行为[xx/10]
  → 总分: [xx]/120 → Tier [1/2/3/4] → 跟进节奏: [frequency]

━━━ 毅冰段 ━━━

📧 Email Group: [Quotation/Negotiation/Follow-Up/Order Push] Group
   序列: [X]封 / [Y]天

✉️ Email 1 (Day X): [Subject]
[完整邮件正文]

✉️ Email 2 (Day X): [Subject]
[完整邮件正文]

... [全部序列邮件]

📱 WhatsApp版:
[压缩版]

💬 WeChat版:
[压缩版]

═══════════════════════════════════════════
```

---

## FAQ 快速查找

当买家的问题不是完整询盘而是具体问题时，跳过管道，直接从对应的 FAQ 文件查找：

| 问题类型 | FAQ 文件 |
|---|---|
| 市场/行业问题 | `faq/faq_market_research.md` |
| 公司背景验证 | `faq/faq_background_investigation.md` |
| 社媒查询 | `faq/faq_social_media_investigation.md` |
| 采购/进口行为 | `faq/faq_purchasing_behavior.md` |
| 需求/要求 | `faq/faq_core_needs.md` |
| 痛点/异议处理 | `faq/faq_pain_points.md` |
| 客户分类 | `faq/faq_client_grading.md` |
| 回复起草 | `faq/faq_reply_drafting.md` |
| 产品特定问题 | `products/[product]/faq_product_specific.md` |

**FAQ 回复也必须诊断根因后给回复，不能照搬模板。**

---

## Reference File Index

| File | 用途 | 加载时机 |
|---|---|---|
| `references/methodology_integration.md` | 三法整合框架 | 全流程开始时 |
| `references/yibing_email_group_strategy.md` | 毅冰 Email Group 详细方法论 | Phase 6 补充参考 |
| `references/waitsui_methodology.md` | 外土司7模块 | Phase 0 补充参考 |
| `references/liaoshensam_google_method.md` | 料神Sam谷歌开发详细方法 | Phase 1 补充参考 |
| `references/client_scoring_framework.md` | 7维评分详细标准 | Phase 5 补充参考 |
| `references/pain_point_deep_dive.md` | 痛点6层金字塔 | Phase 4 补充参考 |
| `references/buyer_archetype_guide.md` | 8种买家原型 | Phase 4.2 补充参考 |
| `references/data_source_guide.md` | 海关/银行/注册数据源 | Phase 3 补充参考 |
| `references/tool_dispatch_strategy.md` | 工具选择决策树 | 研究阶段参考 |
| `references/message_style_guide.md` | 多渠道风格规则 | Phase 6 参考 |
| `references/negotiation_strategy_matrix.md` | 买家原型×场景矩阵 | Phase 6 补充参考 |
| `faq/faq_*.md` (8 files) | 通用 FAQ | FAQ 查找时 |
| `products/[product]/product_knowledge.md` | 产品知识 | 产品相关内容 |
| `products/[product]/market_intelligence.md` | 市场情报 | 市场相关内容 |
| `products/[product]/faq_product_specific.md` | 产品特定 FAQ | 产品问题 |
| `products/[product]/email_templates.md` | 产品邮件模板 | Phase 6 补充 |
| `products/[product]/wechat_whatsapp_templates.md` | IM模板 | Phase 6 补充 |
| `products/[product]/real_world_cases.md` | 真实案例 | Phase 6 Q4 案例 |

---

## 执行规则总结

```
料神段 (Phase 1-2):
  ✅ MUST 执行6步背调全部步骤
  ✅ MUST 输出每步的分析结果
  ✅ MUST 进行供应链角色分类
  ✅ MUST 生成客户裂变搜索词
  ✅ MUST 覆盖所有社媒平台

外土司段 (Phase 0 + 3-5):
  ✅ MUST 进行3步询盘分析并给 A/B/C 级
  ✅ MUST 搜索海关数据
  ✅ MUST 进行6层痛点分析（至少 Layer 0-3）
  ✅ MUST 匹配8种买家原型之一
  ✅ MUST 计算7维评分

毅冰段 (Phase 6-7):
  ✅ MUST 生成完整的 Email Group 序列（所有邮件，不是一封）
  ✅ MUST 每封邮件主题传达新价值（不是 "Re: Your Inquiry"）
  ✅ MUST 每封邮件只讲一个核心价值点
  ✅ MUST 报价时给出3个选项（Premium/Standard/Economy）
  ✅ MUST 条件性让步（每次降价=对方让步）
  ✅ MUST 每封邮件有明确的 CTA
  ✅ MUST 生成 WhatsApp 和 WeChat 压缩版
  ✅ MUST 嵌入产品具体知识（认证/交期/MOQ/差异化）
```

**🚫 永远不要做的事：**
- ❌ 只生成一封邮件就结束
- ❌ 无条件降价
- ❌ 用 "Re: Your Inquiry" / "Following Up" 做主题
- ❌ 在一封邮件中列完所有优势
- ❌ 跳过料神6步背调直接回邮件
- ❌ 不给CTA
- ❌ 报价不带价值语境

---
