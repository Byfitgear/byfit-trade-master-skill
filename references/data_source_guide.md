# BYFIT 外贸调查数据源完整指南

## 使用说明

本指南涵盖外贸客户背景调查所需的所有数据源，按用途分类，每个数据源标注：URL、可获取数据、免费/付费、以及如何配合 WebSearch/WebFetch 工具使用。

---

## 一、海关数据平台

### 1. 52wmb.com（外贸邦）

| 项目 | 详情 |
|------|------|
| **URL** | https://www.52wmb.com |
| **可获取数据** | 中国海关进出口记录、采购商/供应商名称、产品描述、数量、金额、日期 |
| **免费内容** | 部分提单摘要、公司名称搜索、月度数据趋势 |
| **付费内容** | 完整提单详情、联系方式、深度分析报告 |
| **免费额度** | 注册后每月可查3-5条完整记录 |
| **使用技巧** | 搜索"rubber flooring"可找到进口该产品的海外买家列表 |
| **WebSearch** | `site:52wmb.com "rubber flooring" importer` |
| **BYFIT应用** | 搜索HS编码4016.99（硫化橡胶制品）找到进口gym flooring的买家 |

### 2. ImportGenius

| 项目 | 详情 |
|------|------|
| **URL** | https://www.importgenius.com |
| **可获取数据** | 美国海关提单数据、采购商、供应商、产品、数量、重量 |
| **免费内容** | 有限搜索预览、行业报告摘要 |
| **付费内容** | 完整提单、供应商关系图、采购趋势 |
| **免费额度** | 注册可预览3-5条记录的摘要 |
| **使用技巧** | 可查看某公司的全部进口记录和供应商关系 |
| **WebSearch** | `site:importgenius.com "[company name]" import` |
| **BYFIT应用** | 追踪美国健身连锁的rubber flooring进口记录和供应商切换 |

### 3. Panjiva（S&P Global旗下）

| 项目 | 详情 |
|------|------|
| **URL** | https://panjiva.com |
| **可获取数据** | 全球贸易数据、提单、采购关系、供应链映射 |
| **免费内容** | 基础搜索、供应商/采购商概览 |
| **付费内容** | 完整提单、趋势分析、供应链映射 |
| **免费额度** | 搜索可见前5-10条记录摘要 |
| **使用技巧** | 输入公司名可看其供应商/客户列表概览 |
| **WebSearch** | `site:panjiva.com "[company name]" shipment` |
| **BYFIT应用** | 映射竞争对手的出口客户网络 |

### 4. TradeImeX

| 项目 | 详情 |
|------|------|
| **URL** | https://www.tradeimex.in |
| **可获取数据** | 70+国家进出口数据、HS编码搜索、采购商供应商数据 |
| **免费内容** | 样本数据报告、HS编码搜索预览 |
| **付费内容** | 完整数据集、定制报告 |
| **免费额度** | 免费样本报告下载 |
| **使用技巧** | 按HS编码搜索可获取某产品的全球贸易流向 |
| **WebSearch** | `site:tradeimex.in "rubber flooring" import data` |
| **BYFIT应用** | 了解gym flooring全球贸易流向，识别增长市场 |

### 5. Zauba

| 项目 | 详情 |
|------|------|
| **URL** | https://www.zauba.com |
| **可获取数据** | 印度进出口数据、提单详情、HS编码搜索 |
| **免费内容** | 基础搜索、部分提单预览 |
| **付费内容** | 完整提单、联系方式 |
| **免费额度** | 搜索可见前几条记录 |
| **使用技巧** | 专注印度市场，搜索特定产品的印度进口商 |
| **WebSearch** | `site:zauba.com "gym equipment" import` |
| **BYFIT应用** | 挖掘印度健身市场进口商（印度是增长最快的健身市场之一） |

### 海关数据搜索通用策略

```
WebSearch查询模板：
1. "[公司名] import records rubber flooring"
2. "[公司名] supplier China gym equipment"
3. "HS code 950691 import [国家]" （健身器材）
4. "HS code 401699 import [国家]" （硫化橡胶地板）
5. "[公司名] bill of lading flooring"
```

---

## 二、公司注册查询（按国家）

### 美国 — SEC EDGAR

| 项目 | 详情 |
|------|------|
| **URL** | https://www.sec.gov/cgi-bin/browse-edgar |
| **可获取数据** | 上市公司年报(10-K)、季报(10-Q)、重大事件(8-K)、股东信息、高管薪酬 |
| **费用** | 完全免费 |
| **使用方式** | 输入公司名或CIK编号搜索 |
| **WebSearch** | `site:sec.gov "[company name]" 10-K` |
| **BYFIT应用** | 查看上市健身连锁（如Planet Fitness PLNT）的年报，了解扩张计划和采购预算 |

### 美国 — 州务卿注册查询

| 项目 | 详情 |
|------|------|
| **各州URL** | Delaware: https://icis.corp.delaware.gov/ecorp/EntitySearch/nbsearch.aspx |
| | California: https://bizfileonline.sos.ca.gov/search/business |
| | Texas: https://direct.sos.state.tx.us/acct/acct-search.asp |
| **可获取数据** | 公司注册状态、注册日期、注册代理人、办公地址 |
| **费用** | 免费基础查询 |
| **使用技巧** | 先查Delaware（多数美国公司注册于此），再查经营所在州 |
| **WebSearch** | `"[company name] site:sos.[state].gov" business search` |
| **BYFIT应用** | 验证美国买家公司真实性和经营年限 |

### 英国 — Companies House

| 项目 | 详情 |
|------|------|
| **URL** | https://find-and-update.company-information.service.gov.uk |
| **可获取数据** | 公司注册信息、年报、董事信息、股东结构、抵押登记、变更历史 |
| **费用** | 免费查看基本信息和文件 |
| **使用方式** | 输入公司名或注册号搜索 |
| **WebSearch** | `site:find-and-update.company-information.service.gov.uk "[company name]"` |
| **BYFIT应用** | 调查英国健身器材经销商的公司规模和财务健康状况 |

### 德国 — Handelsregister

| 项目 | 详情 |
|------|------|
| **URL** | https://www.handelsregister.de （统一入口） |
| **各州法院** | Bayern: https://www.handelsregisterbayern.de |
| | Berlin: https://www.handelsregisterberlin.de |
| **可获取数据** | 公司注册信息、董事/总经理、注册资本、公司类型 |
| **费用** | 基础搜索免费，完整文件付费 |
| **使用方式** | 输入公司名或注册号 |
| **WebSearch** | `"[company name] Handelsregister" site:handelsregister.de` |
| **BYFIT应用** | 验证德国健身设备采购商的公司资质 |

### 法国 — SIRENE

| 项目 | 详情 |
|------|------|
| **URL** | https://avis-situation-sirene.inpi.fr |
| **可获取数据** | SIREN/SIRET号码、公司地址、法律形式、注册资本、经营类别(NAF) |
| **费用** | 免费 |
| **使用方式** | 输入公司名或SIREN号码 |
| **WebSearch** | `"[company name] SIREN" site:inpi.fr` |
| **BYFIT应用** | 确认法国买家是否为合法注册企业 |

### 阿联酋 — DED（经济发展部）

| 项目 | 详情 |
|------|------|
| **URL** | https://www.det.gov.ae （Dubai）|
| | https://www.abudhabibusinesscentre.gov.ae （Abu Dhabi）|
| **可获取数据** | 贸易许可证信息、公司名称、活动类别、许可证状态 |
| **费用** | 免费基础查询 |
| **使用方式** | 输入公司名或许可证号 |
| **WebSearch** | `"[company name] trade license Dubai"` |
| **BYFIT应用** | 验证迪拜健身设备进口商的贸易许可证 |

### 沙特 — MCI（商工部）

| 项目 | 详情 |
|------|------|
| **URL** | https://mci.gov.sa （搜索CR - Commercial Registration）|
| **可获取数据** | 商业注册号、公司名称、活动类别、注册日期 |
| **费用** | 免费基础查询 |
| **使用方式** | 输入CR号或公司名 |
| **WebSearch** | `"[company name] commercial registration Saudi Arabia"` |
| **BYFIT应用** | 验证沙特健身市场买家的合法性 |

### 日本 — 法人登記情報

| 项目 | 详情 |
|------|------|
| **URL** | https://www1.touki.or.jp/gateway.html |
| **可获取数据** | 公司注册信息、代表取締役、资本金、所在地 |
| **费用** | 基础搜索免费，详细证明付费 |
| **使用方式** | 输入公司名或登記号 |
| **WebSearch** | `"[会社名] 登記情報" OR "[company name] Japan corporate registry"` |
| **BYFIT应用** | 调查日本高端健身设备采购商 |

### 韩国 — DART（金融监督院电子公示系统）

| 项目 | 详情 |
|------|------|
| **URL** | https://dart.fss.or.kr |
| **可获取数据** | 上市公司公示信息、年报、重大事项 |
| **费用** | 免费 |
| **使用方式** | 输入公司名搜索 |
| **WebSearch** | `site:dart.fss.or.kr "[회사명]" OR "[company name]"` |
| **BYFIT应用** | 查看韩国健身连锁上市公司（如VFitness）的经营数据 |

### 澳大利亚 — ASIC

| 项目 | 详情 |
|------|------|
| **URL** | https://connectonline.asic.gov.au |
| **可获取数据** | ABN/ACN、公司注册信息、董事、注册地址 |
| **费用** | 基础ABN查询免费 |
| **使用方式** | 输入ABN或公司名 |
| **WebSearch** | `"[company name] ABN" site:abr.business.gov.au` |
| **BYFIT应用** | 验证澳大利亚健身设备买家的注册状态 |

---

## 三、信用/财务评估

### Dun & Bradstreet（D&B）

| 项目 | 详情 |
|------|------|
| **URL** | https://www.dnb.com |
| **可获取数据** | D-U-N-S编号、信用评分、付款历史、财务压力指数、公司族谱 |
| **免费内容** | D-U-N-S编号查询、基础公司概要 |
| **付费内容** | 完整信用报告、财务分析、风险监测 |
| **WebSearch** | `"[company name] D&B credit report" OR "D-U-N-S [company name]"` |
| **BYFIT应用** | 评估大型采购商的信用风险，决定付款条件 |

### Experian Business

| 项目 | 详情 |
|------|------|
| **URL** | https://www.experian.com/business |
| **可获取数据** | 商业信用评分、付款趋势、公共记录（破产、诉讼）|
| **免费内容** | 有限预览 |
| **付费内容** | 完整商业信用报告 |
| **WebSearch** | `"[company name] business credit score Experian"` |

### Creditsafe

| 项目 | 详情 |
|------|------|
| **URL** | https://www.creditsafe.com |
| **可获取数据** | 全球200+国家公司信用报告、信用评分、财务数据 |
| **免费内容** | 基础搜索预览 |
| **付费内容** | 完整信用报告 |
| **优势** | 覆盖范围广，特别是欧洲中小企业 |
| **WebSearch** | `"[company name] Creditsafe credit rating"` |

### 各国本地信用评估机构

| 国家/地区 | 机构 | URL |
|-----------|------|-----|
| 中国 | 企查查 | https://www.qcc.com |
| 中国 | 天眼查 | https://www.tianyancha.com |
| 德国 | Creditreform | https://www.creditreform.com |
| 法国 | Altares | https://www.altares.com |
| 日本 | 帝国データバンク | https://www.tdb.co.jp |
| 韩国 | KIS (Korea Investors Service) | https://www.kisrating.com |
| 印度 | CIBIL | https://www.cibil.com |
| 巴西 | Serasa | https://www.serasaexperian.com.br |
| 南非 | TransUnion | https://www.transunion.co.za |

### 信用评估搜索策略

```
WebSearch查询模板：
1. "[公司名] credit rating" OR "credit score"
2. "[公司名] financial statements" OR "annual report"
3. "[公司名] bankruptcy" OR "insolvency" OR "liquidation"
4. "[公司名] payment terms" OR "payment history"
5. "[公司名] litigation" OR "lawsuit"
```

---

## 四、银行/金融验证

### 基本验证方法

| 方法 | 操作 | 适用场景 |
|------|------|----------|
| **银行参考信** | 请客户提供其银行出具的参考信 | 大额订单验证 |
| **SWIFT代码查询** | https://www.swift.com/standards/data-standards/bic-directory 查询银行BIC代码有效性 | 验证客户提供的银行信息 |
| **银行对账单验证** | 要求近3个月银行对账单（可遮挡敏感信息） | 评估付款能力 |
| **信用证开立能力** | 要求客户提供其银行可开L/C的证明 | L/C付款条件 |
| **贸易融资记录** | 通过银行了解客户的贸易融资历史 | 长期合作评估 |

### 反欺诈验证清单

```
✓ 公司注册地址是否与银行地址一致
✓ 公司名称拼写是否与注册名完全一致
✓ 联系人职位是否与LinkedIn信息匹配
✓ 邮箱域名是否为公司官网域名（非gmail/hotmail）
✓ 电话号码区号是否与公司注册地匹配
✓ 公司网站是否真实可访问且内容充实
✓ 采购量是否与公司规模匹配
✓ 付款条件要求是否合理
```

---

## 五、社交媒体搜索技术

### LinkedIn 高级搜索语法

#### 基础搜索

```
搜索模板：
1. "purchasing manager" "fitness" OR "gym" OR "wellness"
2. "procurement" "rubber flooring" OR "gym equipment"
3. "buying" "exercise equipment" company:"Planet Fitness"
4. "sourcing" "pilates" OR "yoga equipment"
```

#### 高级运算符

| 运算符 | 用法 | 示例 |
|--------|------|------|
| `""` | 精确匹配 | `"rubber flooring"` |
| `OR` | 或运算 | `"gym" OR "fitness"` |
| `()` | 分组 | `("purchasing manager" OR "buyer") "fitness"` |
| `company:` | 指定公司 | `company:"Anytime Fitness"` |
| `title:` | 指定职位 | `title:"procurement"` |
| `industry:` | 指定行业 | `industry:"health fitness"` |

#### BYFIT专用搜索组合

```
1. 找采购决策人：
   title:("purchasing" OR "procurement" OR "buyer" OR "sourcing")
   "fitness" OR "gym" OR "health club" OR "wellness"

2. 找健身连锁高管：
   title:("VP" OR "director" OR "head")
   ("operations" OR "facilities" OR "procurement")
   company:("fitness" OR "gym" OR "health club")

3. 找设备经销商：
   title:("owner" OR "president" OR "buyer")
   "fitness equipment" OR "gym equipment" OR "exercise equipment"
   "distributor" OR "dealer" OR "wholesaler"

4. 找Pilates工作室主：
   title:("owner" OR "founder" OR "studio manager")
   "pilates" OR "reformer"
```

### Facebook 搜索策略

| 方法 | 操作 | BYFIT应用 |
|------|------|-----------|
| **Graph Search替代** | 搜索栏输入 "People who work at [公司名]" | 找到目标公司员工 |
| **公司页面** | 搜索公司名查看官方页面 | 了解公司规模、活动、评价 |
| **群组搜索** | "gym owners" "fitness business" "gym equipment" | 找到潜在买家聚集的群组 |
| **评论挖掘** | 查看健身设备品牌的用户评论 | 找到正在比较产品的买家 |
| ** Marketplace** | 搜索 "commercial gym equipment" | 发现正在采购的健身房 |

### Instagram 搜索策略

| 方法 | 操作 | BYFIT应用 |
|------|------|-----------|
| **Hashtag搜索** | #gymowner #gymbuild #commercialgym #gymflooring #pilatesstudio | 找到正在建/翻新健身房的业主 |
| **位置标签** | 搜索特定城市的健身相关标签 | 区域化客户开发 |
| **竞品标签** | #regupol #ecofit #mondoflooring | 找到使用竞品产品的场馆 |
| **Reels/Story** | 搜索 "gym tour" "gym renovation" | 发现新建/翻新中的健身房 |
| **关注列表** | 查看竞品的关注者和粉丝 | 找到潜在客户 |

#### BYFIT核心Hashtag列表

```
产品相关：
#gymflooring #rubberflooring #gymmats #gymtiles #plyometricflooring
#pilatesreformer #pilatesequipment #gymequipment #commercialgym

目标客户相关：
#gymowner #gymbuild #gymrenovation #gymsetup #fitnessbusiness
#gymdesign #studiodesign #fitout #gymfitout #commercialfitout

场景相关：
#crossfitbox #functionalfitness #personaltrainingstudio
#boutiquefitness #hotelgym #homegym #corporatewellness
```

### Twitter/X 搜索策略

```
高级搜索语法：
1. "looking for" "gym flooring" OR "rubber flooring"
2. "need" "pilates equipment" supplier OR manufacturer
3. "gym renovation" OR "gym build" from:[城市]
4. "requesting quote" OR "RFQ" "fitness equipment"
```

### YouTube 搜索策略

```
1. 搜索 "gym flooring review" → 找到正在比较产品的买家
2. 搜索 "gym tour 2024/2025" → 发现新建/翻新的健身房
3. 搜索 "pilates studio tour" → 找到Pilates工作室
4. 查看竞品视频的评论区 → 找到询价的潜在客户
```

---

## 六、新闻/诉讼搜索

### Google News 高级搜索

| 运算符 | 用法 | 示例 |
|--------|------|------|
| `intitle:` | 标题包含 | `intitle:"Planet Fitness" expansion` |
| `source:` | 指定来源 | `source:bloomberg "fitness industry"` |
| `after:` | 时间范围 | `"gym chain" expansion after:2024-01-01` |
| `before:` | 时间范围 | `"fitness industry" before:2025-01-01` |
| `OR` | 或运算 | `"gym equipment" OR "fitness equipment" lawsuit` |

#### BYFIT新闻搜索模板

```
1. 客户动态：
   "[公司名] expansion" OR "new location" OR "funding" OR "investment"
   after:2024-01-01

2. 行业趋势：
   "fitness industry" "growth" OR "trend" OR "market size"
   [目标国家] after:2024-06-01

3. 风险信号：
   "[公司名] lawsuit" OR "bankruptcy" OR "closing" OR "layoff"
   OR "fraud" OR "complaint"

4. 采购信号：
   "[公司名] contract" OR "supplier" OR "procurement" OR "tender"
   "flooring" OR "equipment"
```

### 各国法院/诉讼记录

| 国家 | 平台 | URL | 免费程度 |
|------|------|-----|----------|
| 美国（联邦） | PACER | https://pacer.uscourts.gov | 付费（$0.10/页） |
| 美国（州） | 各州法院网站 | 州法院.gov | 部分免费 |
| 英国 | The National Archives | https://www.find-case-law.service.justice.gov.uk | 免费 |
| 德国 | 各州法院 | Landesgericht网站 | 部分免费 |
| 澳大利亚 | AustLII | https://www.austlii.edu.au | 免费 |
| 加拿大 | CanLII | https://www.canlii.org | 免费 |
| 印度 | eCourts | https://ecourts.gov.in | 免费 |

### 诉讼搜索策略

```
WebSearch查询模板：
1. "[公司名] lawsuit" OR "litigation" OR "court case"
2. "[公司名] breach of contract" supplier
3. "[公司名] complaint" BBB OR "better business bureau"
4. "[公司名] fraud" OR "scam" OR "warning"
5. "[公司名] review" "scam" OR "terrible" OR "worst"
```

---

## 七、健身/体育行业专用数据库

### 行业协会

| 协会 | URL | 可获取数据 |
|------|-----|-----------|
| IHRSA（全球健身协会） | https://www.ihrsa.org | 行业报告、会员名录、市场数据 |
| FIBO（健身博览会） | https://www.fibo.com | 展商名录、行业趋势 |
| NASM（国家运动医学学院） | https://www.nasm.org | 认证教练网络（潜在客户） |
| Club Industry | https://www.clubindustry.com | 行业新闻、排名 |
| Fitness Industry Association (UK) | https://www.ukactive.com | 英国市场会员名录 |

### 健身行业排名/名录

| 资源 | URL | 内容 |
|------|-----|------|
| Club Industry Top 100 | https://www.clubindustry.com/top-clubs | 美国最大健身连锁排名 |
| IHRSA Global Report | https://www.ihrsa.org/publications | 全球健身市场报告 |
| Fitness Club Database | https://www.scrapehero.com | 健身俱乐部数据库（付费） |

### 行业展会名录

| 展会 | 地点 | 时间 | 网址 |
|------|------|------|------|
| FIBO | 德国科隆 | 每年4月 | https://www.fibo.com |
| IHRSA Convention | 美国 | 每年3月 | https://www.ihrsa.org/convention |
| Bodypower Expo | 英国伯明翰 | 每年5月 | https://www.bodypower.com |
| Asia Fitness Conference | 泰国曼谷 | 每年10月 | https://www.asiafitnessconference.com |
| China Fit | 中国北京 | 每年7月 | https://www.chinafit.com |

### 行业搜索策略

```
WebSearch查询模板：
1. "top gym chains" [国家] 2025
2. "fastest growing fitness franchises" [地区]
3. "[城市] gym opening" OR "new gym" 2025
4. "fitness industry market size" [国家] 2025
5. "commercial gym equipment suppliers" [地区]
6. "gym flooring manufacturers" ranking OR review
```

---

## 八、综合搜索流程（按步骤）

### Step 1: 初步身份验证

```
□ Google搜索公司名 → 确认公司真实存在
□ 查看官网 → 了解业务范围和规模
□ 查公司注册信息（见第二节）→ 确认合法注册
□ WHOIS查询域名注册信息 → 确认网站创建时间
```

### Step 2: 深度背景调查

```
□ 海关数据查询 → 了解采购历史和供应商
□ LinkedIn搜索 → 找到决策人和组织架构
□ 新闻搜索 → 了解近期动态和风险信号
□ 社交媒体 → 了解品牌形象和客户反馈
```

### Step 3: 信用与风险评估

```
□ D&B/Creditsafe信用报告 → 评估信用风险
□ 诉讼记录搜索 → 排除法律风险
□ 付款历史调查 → 评估付款可靠性
□ 银行验证 → 确认付款能力
```

### Step 4: 采购需求分析

```
□ 海关数据分析 → 采购周期、量级、现有供应商
□ 行业报告 → 市场地位和增长潜力
□ 社交媒体 → 新店/新项目线索
□ 竞品分析 → 可能的供应商切换信号
```

### Step 5: 整合输出

```
□ 填写client_profile_template.md
□ 完成7维评分（见client_scoring_framework.md）
□ 确定客户等级和跟进策略
□ 选择方法论组合（见methodology_integration.md）
```

---

## 九、WebSearch/WebFetch 使用速查

### WebSearch 高级语法

| 语法 | 功能 | 示例 |
|------|------|------|
| `"exact phrase"` | 精确匹配 | `"rubber flooring importer"` |
| `site:` | 限定网站 | `site:linkedin.com "gym buyer"` |
| `filetype:` | 文件类型 | `filetype:pdf "fitness industry report 2025"` |
| `intitle:` | 标题包含 | `intitle:"gym expansion" 2025` |
| `inurl:` | URL包含 | `inurl:procurement "fitness equipment"` |
| `-` | 排除 | `"gym equipment" -alibaba -amazon` |
| `OR` | 或运算 | `"gym" OR "fitness" buyer` |
| `*` | 通配符 | `"top * fitness chains"` |
| `after:YYYY-MM-DD` | 时间范围 | `"gym renovation" after:2025-01-01` |

### WebFetch 信息提取 Prompt 模板

```
从网页中提取以下信息：
1. 公司名称和地址
2. 主要业务/产品
3. 公司规模（员工数/营收）
4. 关键联系人（姓名/职位/邮箱）
5. 近期动态（扩张/采购/合作）
6. 供应商/客户关系
7. 风险信号（诉讼/投诉/财务问题）
```

---

## 十、BYFIT专用搜索清单

### 产品关键词矩阵

| 产品线 | 英文关键词 | HS编码 |
|--------|-----------|--------|
| Gym Rubber Flooring | rubber flooring, gym tiles, gym mats, rubber rolls, interlocking tiles, vulcanized rubber tiles | 4016.99, 4016.10 |
| Gym Equipment | gym equipment, fitness equipment, strength equipment, cardio machines, weight racks, power rack | 9506.91, 9506.91.20 |
| Pilates Equipment | pilates reformer, pilates cadillac, pilates chair, pilates barrel, pilates springboard | 9506.91, 9506.99 |

### 目标客户搜索组合

```
1. 健身连锁：
   "fitness chain" OR "gym chain" OR "health club chain"
   "expansion" OR "new location" OR "franchise"
   [目标国家]

2. 健身设备经销商：
   "fitness equipment distributor" OR "gym equipment wholesaler"
   [目标国家/城市]

3. 工程/装修公司：
   "gym fitout" OR "gym build" OR "fitness center design"
   "contractor" OR "builder" [目标国家]

4. Pilates工作室：
   "pilates studio" OR "pilates center"
   "opening" OR "new" OR "expanding" [目标城市]
```
