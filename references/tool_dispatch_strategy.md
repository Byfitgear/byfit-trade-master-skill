# 工具调度策略 (Tool Dispatch Strategy)

> 核心原则：不同的调查任务需要不同的工具。用搜索引擎查趋势，用WebFetch提取页面内容，用stealth-browser突破反爬，用海关数据验证采购记录。选错工具 = 浪费时间 = 信息不全。

---

## 目录

1. [工具概览](#工具概览)
2. [核心工具详解](#核心工具详解)
3. [海关数据查询调度](#海关数据查询调度)
4. [银行/征信查询调度](#银行征信查询调度)
5. [公司注册信息查询调度](#公司注册信息查询调度)
6. [社交媒体调查调度](#社交媒体调查调度)
7. [完整决策树](#完整决策树)
8. [场景化调度方案](#场景化调度方案)

---

## 工具概览

### 五大核心工具

| 工具 | 定位 | 最佳场景 | 速度 | 深度 | 反爬能力 |
|------|------|----------|------|------|----------|
| **WebSearch** | 通用搜索引擎 | 快速查询公司信息、行业趋势 | ★★★★★ | ★★☆☆☆ | ★☆☆☆☆ |
| **WebFetch** | 页面内容提取 | 从已知URL提取结构化信息 | ★★★★☆ | ★★★★☆ | ★☆☆☆☆ |
| **web-access (CDP)** | 浏览器自动化 | LinkedIn、B2B平台、需登录网站 | ★★☆☆☆ | ★★★★★ | ★★★★☆ |
| **multi-search-engine** | 多引擎搜索 | 跨16引擎广覆盖搜索 | ★★★☆☆ | ★★★☆☆ | ★★☆☆☆ |
| **stealth-browser** | 隐身浏览器 | 反爬网站、CAPTCHA、需要隐藏身份 | ★★☆☆☆ | ★★★★★ | ★★★★★ |

### 辅助工具

| 工具 | 用途 | 触发场景 |
|------|------|----------|
| **LinkedIn** (via web-access) | 客户身份和关系网络调查 | 需要了解采购负责人 |
| **Hunter.io / Snov.io** | 邮箱查找和验证 | 找不到客户邮箱 |
| **Google Maps** | 客户实体地址和规模验证 | 确认客户是否真实 |
| **YouTube** | 客户产品视频和展会记录 | 了解客户的产品和市场 |

---

## 核心工具详解

### 1. WebSearch — 快速情报收集

**适用场景**：
- 初步了解一家公司
- 查询行业趋势和数据
- 验证客户提到的信息
- 搜索竞品信息

**查询模式**：

| 任务 | 查询模板 | BYFIT 示例 |
|------|----------|-----------|
| 公司基本信息 | `[Company Name] + [industry] + [country]` | `"ABC Fitness" gym distributor UK` |
| 公司新闻 | `[Company Name] + news OR announcement` | `"ABC Fitness" news OR expansion OR new` |
| 行业趋势 | `[product] + market trend + [year]` | `rubber flooring market trend 2025` |
| 竞品分析 | `[product] + manufacturer + China + [spec]` | `gym rubber flooring manufacturer China EN14904` |
| 客户口碑 | `[Company Name] + review OR complaint` | `"ABC Fitness" review OR complaint` |

**BYFIT 实战示例**：

```
任务：快速了解一家英国gym equipment分销商

Step 1: WebSearch "ABC Fitness Distribution UK"
→ 获取公司官网URL、基本描述

Step 2: WebSearch "ABC Fitness Distribution" news
→ 获取最新动态（扩张、新品、收购等）

Step 3: WebSearch "ABC Fitness Distribution" review
→ 获取客户评价和行业口碑

输出：3分钟内获得公司基本画像
```

**限制**：
- 不能访问需要登录的页面
- 不能处理CAPTCHA
- 搜索结果可能不够精准（需要人工筛选）
- 不能做深度页面交互

---

### 2. WebFetch — 精准内容提取

**适用场景**：
- 从客户网站提取特定信息（About Us、产品列表、联系方式）
- 读取行业报告或新闻文章
- 提取页面中的邮箱、电话等联系信息

**查询模式**：

| 任务 | URL来源 | 提取指令 |
|------|---------|----------|
| 提取About Us | 客户官网/about-us | "提取公司历史、规模、关键人物、使命" |
| 提取产品列表 | 客户官网/products | "列出所有产品类别和子类别" |
| 提取联系方式 | 客户官网/contact | "提取所有邮箱、电话、地址" |
| 提取新闻 | 客户官网/news | "提取最近6个月的重要新闻" |

**BYFIT 实战示例**：

```
任务：提取英国分销商的产品信息和联系方式

Step 1: WebFetch https://www.abc-fitness.co.uk/about-us
  Prompt: "提取公司成立年份、员工数、年营收、母公司、关键人物名字和职位"

Step 2: WebFetch https://www.abc-fitness.co.uk/products
  Prompt: "列出所有产品类别，特别关注是否有rubber flooring和gym equipment"

Step 3: WebFetch https://www.abc-fitness.co.uk/contact
  Prompt: "提取所有邮箱地址、电话号码和办公地址"

输出：10分钟内完成6步背景调查的Step 1+2+6
```

**限制**：
- 需要知道目标URL
- 无法处理JavaScript渲染的页面
- 无法绕过反爬机制
- 部分网站会阻止爬取

---

### 3. web-access (CDP) — 深度浏览器自动化

**适用场景**：
- LinkedIn个人和公司页面调查
- B2B平台（Alibaba、Made-in-China等）深度搜索
- 需要登录的网站
- 需要翻页、点击、滚动等交互的页面

**查询模式**：

| 任务 | 操作流程 | 输出 |
|------|----------|------|
| LinkedIn公司页 | 打开公司页 → 截图 → 提取信息 | 公司规模、员工列表、最近动态 |
| LinkedIn个人页 | 打开个人页 → 提取profile | 职位、联系方式、工作经历 |
| B2B平台搜索 | 搜索关键词 → 筛选结果 → 提取供应商信息 | 竞品列表、价格参考 |
| 需登录网站 | 登录 → 导航 → 提取 | 受保护的内容 |

**BYFIT 实战示例**：

```
任务：在LinkedIn上找到ABC Fitness的采购负责人

Step 1: web-access 打开LinkedIn
Step 2: 搜索 "ABC Fitness Distribution"
Step 3: 进入公司页面，查看员工列表
Step 4: 筛选职位包含 "purchasing" / "buying" / "procurement" / "sourcing"
Step 5: 打开目标人物的profile，提取联系信息
Step 6: 如果有共同连接，考虑通过介绍联系

输出：采购负责人姓名、职位、邮箱（如果可见）
```

**限制**：
- 速度较慢（需要模拟真实浏览器行为）
- LinkedIn有频率限制，过度使用会被限制
- 需要LinkedIn账号
- 操作复杂，需要明确指令

---

### 4. multi-search-engine — 广覆盖搜索

**适用场景**：
- 单一搜索引擎结果不够全面
- 需要覆盖中文和英文搜索结果
- 搜索冷门信息（Google可能没有）
- 需要对比不同搜索引擎的结果

**支持的16个引擎**：

| 类别 | 引擎 |
|------|------|
| 中国引擎（7个） | 百度、搜狗、360搜索、头条搜索、必应中国、神马、夸克 |
| 国际引擎（9个） | Google、Bing、DuckDuckGo、Yandex、Naver、Daum、Qwant、Startpage、Brave |

**BYFIT 实战示例**：

```
任务：搜索一家俄罗斯gym equipment进口商的信息

Google可能结果有限（俄语内容），使用multi-search-engine：

Step 1: 搜索 "фитнес оборудование дистрибьютор" (俄语：fitness equipment distributor)
  → Yandex（俄罗斯搜索引擎）可能有更多本地结果

Step 2: 搜索 "ABC Fitness" Russia
  → 同时在Google和Bing上搜索，对比结果

Step 3: 如果目标市场是俄罗斯，Yandex的结果比Google更有价值
```

**限制**：
- 速度中等（需要查询多个引擎）
- 结果可能有大量重复
- 不同引擎的结果质量差异大
- 适合广覆盖，不适合深度提取

---

### 5. stealth-browser — 隐身浏览器

**适用场景**：
- 目标网站有反爬机制（Cloudflare、PerimeterX等）
- 需要解决CAPTCHA
- 需要隐藏身份访问（竞争对手调查）
- 需要保持登录状态进行深度操作

**查询模式**：

| 任务 | 场景 | 操作 |
|------|------|------|
| 突破Cloudflare | 目标网站有5秒盾 | 使用stealth-browser自动等待和验证 |
| CAPTCHA解决 | 搜索或登录时遇到验证码 | 自动识别和填写 |
| 竞品网站深度调查 | 竞品网站限制访问频率 | 使用代理IP+指纹伪装 |
| 批量页面抓取 | 需要抓取多个页面 | 自动翻页+提取 |

**BYFIT 实战示例**：

```
任务：从受Cloudflare保护的B2B目录网站提取gym equipment分销商列表

Step 1: stealth-browser 打开目标URL
Step 2: 自动等待Cloudflare验证通过
Step 3: 搜索 "gym equipment distributor"
Step 4: 提取搜索结果中的公司名称、网站URL、联系方式
Step 5: 自动翻页，提取多页结果
Step 6: 汇总输出分销商列表

输出：20-50家分销商的名称和联系方式
```

**限制**：
- 速度最慢
- 消耗资源最多
- 需要明确操作指令
- 不应过度使用（尊重网站政策）

---

## 海关数据查询调度

### 海关数据的价值

海关数据是验证客户真实性的"黄金证据"：
- 确认客户是否真的在进口你的产品
- 了解客户的采购频次和采购量
- 发现客户的现有供应商（你的竞争对手）
- 判断客户的采购趋势（增长/减少/稳定）

### 海关数据平台调度

| 平台 | 覆盖范围 | 优势 | 限制 | 调度场景 |
|------|----------|------|------|----------|
| **52wmb.com** (外贸邦) | 中国海关数据为主 | 中文界面、免费基础查询、数据更新快 | 深度数据需付费 | 中国出口数据查询 |
| **ImportGenius** | 美国为主，部分拉美 | 美国海关数据最全、提单详情 | 费用高($300+/月) | 美国进口商调查 |
| **Panjiva** (S&P Global) | 全球 | 数据质量高、关联分析强 | 费用高 | 大客户深度调查 |
| **TradeImeX** | 全球70+国家 | 覆盖广、价格适中 | 数据深度不如ImportGenius | 中小客户调查 |
| **Seair Exim Solutions** | 印度为主，全球 | 印度数据详细 | 其他国家数据一般 | 印度市场调查 |
| **Descartes Datamyne** | 亚洲为主 | 日韩东南亚数据强 | 欧美数据弱 | 亚洲市场调查 |

### BYFIT 海关数据查询SOP

```
Step 1: 确定查询目标
  → 客户公司名（英文名 + 当地语言名）
  → 产品HS Code（rubber flooring: 401699, gym equipment: 950691）

Step 2: 选择平台
  → 客户在美国？→ ImportGenius
  → 客户在亚洲？→ Descartes Datamyne
  → 快速免费查询？→ 52wmb.com
  → 需要全球覆盖？→ Panjiva 或 TradeImeX

Step 3: 查询关键词
  → 用公司名搜索（注意拼写变体）
  → 用HS Code搜索（看同类产品的进口商）
  → 组合搜索（公司名 + HS Code）

Step 4: 分析结果
  → 采购频次：月度/季度/年度
  → 采购量：TEU数量或重量
  → 供应商：现有供应商是谁？来自哪个国家？
  → 采购趋势：增长/下降/稳定
  → 品类范围：只买flooring？还是也买equipment？

Step 5: 制定策略
  → 如果客户采购量增长 → 主动出击，提供扩展方案
  → 如果客户采购量下降 → 了解原因，可能是换供应商的窗口期
  → 如果客户现有供应商是中国贸易公司 → 强调你是工厂直供
  → 如果客户现有供应商是当地品牌商 → 从OEM/性价比角度切入
```

### BYFIT 海关数据查询示例

```
目标：调查 "ABC Fitness Distribution" 的采购情况

52wmb.com 查询：
  关键词：ABC Fitness
  结果：
  - 2024年共进口6批次橡胶地板（HS 401699）
  - 供应商：XYZ Trading Co., Ltd. (中国青岛)
  - 平均每批：1x20'集装箱
  - 采购趋势：2023年4批 → 2024年6批（增长50%）

分析：
1. ABC Fitness 正在增长采购量 → 积极信号
2. 当前供应商是贸易公司（XYZ Trading）→ BYFIT工厂直供有优势
3. 每批1x20' → 中型客户，适合Standard产品线

策略：
- 开发信重点：工厂直供 vs 贸易公司优势
- 提出：相同品质更低价格，或相同价格更高品质
- 提供：3次连续采购后从1x20'升级到1x40'HQ的折扣方案
```

---

## 银行/征信查询调度

### 为什么需要征信查询

- 避免与财务不健康的客户合作
- 了解客户的信用等级和付款习惯
- 为付款条件谈判提供依据
- 预防坏账风险

### 征信平台调度

| 平台 | 覆盖范围 | 优势 | 限制 | 调度场景 |
|------|----------|------|------|----------|
| **D&B (Dun & Bradstreet)** | 全球 | 最全面的商业信用数据库、D-U-N-S编号 | 报告费用高($100-500/份) | 大客户深度信用调查 |
| **Experian** | 全球（英美为主） | 信用评分体系成熟 | 欧洲以外数据较弱 | 英美客户信用调查 |
| **Creditsafe** | 全球 | 性价比高、界面友好 | 数据深度不如D&B | 中小客户信用快查 |
| **Kompass** | 全球 | 公司基础信息+行业分类 | 信用数据较少 | 快速公司信息查询 |
| **各国本地征信机构** | 特定国家 | 本地数据最准确 | 需要逐国查询 | 特定市场深度调查 |

### 各国征信机构参考

| 国家/地区 | 征信机构 | 网站 |
|-----------|----------|------|
| 英国 | Companies House | companieshouse.gov.uk |
| 美国 | SEC EDGAR + D&B | sec.gov/edgar |
| 德国 | Bundesanzeiger | bundesanzeiger.de |
| 法国 | Societe.com | societe.com |
| 澳大利亚 | ASIC | asic.gov.au |
| 阿联酋 | DED (Department of Economic Development) | 各酋长国DED网站 |
| 印度 | Ministry of Corporate Affairs | mca.gov.in |
| 巴西 | Receita Federal | receita.economia.gov.br |

### BYFIT 征信查询SOP

```
Step 1: 确定查询优先级
  → 首次合作 + 大额订单？→ 必须查
  → 首次合作 + 小额试单？→ 基础查询即可
  → 老客户 + 请求账期？→ 查付款记录

Step 2: 选择工具
  → 快速基础查询：Companies House / 免费征信网站
  → 深度信用调查：D&B / Creditsafe
  → 特定国家：各国本地征信机构

Step 3: 查询内容
  → 公司注册信息：成立年份、注册地址、注册资本
  → 财务健康：年营收、利润率、资产负债率
  → 信用评分：D&B评分 / Experian评分
  → 法律风险：是否有诉讼/欠款/破产记录
  → 关联公司：母公司、子公司、关联企业

Step 4: 结果解读
  → 信用评分 > 80：安全，可正常合作
  → 信用评分 60-80：谨慎，要求预付款或L/C
  → 信用评分 < 60：高风险，坚持100%预付款或拒绝合作
  → 有诉讼/欠款记录：了解具体情况，可能需要额外保障

Step 5: 制定付款策略
  → 高信用客户：可提供30%+70%标准条件
  → 中等信用：50%+50%或L/C at sight
  → 低信用：100%预付款或L/C at sight
  → 无信用记录（新公司）：小额试单+100%预付款
```

### BYFIT 征信查询示例

```
目标：调查 "ABC Fitness Distribution Ltd"（英国）的信用状况

Step 1: Companies House 查询（免费）
  → 公司注册号：12345678
  → 成立日期：2008-03-15（17年历史）
  → 注册资本：£100,000
  → 董事：John Smith, Managing Director
  → 年度报表：已提交（最新2024年3月）

Step 2: Creditsafe 查询（付费）
  → 信用评分：72/100（中等偏上）
  → 年营收：£2.5M
  → 建议信用额度：£15,000
  → 付款习惯：平均58天（略慢于标准30天）
  → 法律风险：无诉讼记录

Step 3: 结论
  → 信用状况中等偏上，可以合作
  → 建议付款条件：30% T/T deposit + 70% against B/L copy
  → 不建议提供超过£15K的信用额度
  → 注意其付款习惯偏慢，需要在PI中明确付款期限
```

---

## 公司注册信息查询调度

### 各国公司注册查询入口

| 地区 | 查询平台 | URL模式 | 可获取信息 |
|------|----------|---------|-----------|
| 英国 | Companies House | find-and-update.company-information.service.gov.uk | 注册号、董事、年报、注册资本 |
| 美国 | 各州Secretary of State | 州政府网站 | 注册信息、年报、注册代理 |
| 欧盟 | 各国商业注册局 | 各国网站 | 注册信息、年报、董事 |
| 澳大利亚 | ABN Lookup | abr.business.gov.au | ABN、注册地址、实体类型 |
| 加拿大 | Corporations Canada | ic.gc.ca | 注册信息、董事 |
| 印度 | MCA | mca.gov.in | 注册信息、董事、年报 |
| 阿联酋 | DED各酋长国 | 各酋长国DED网站 | 注册信息、营业执照 |
| 新加坡 | ACRA | bizfile.gov.sg | 注册信息、年报 |
| 香港 | Companies Registry | icris.cr.gov.hk | 注册信息、年报、董事 |
| 德国 | Handelsregister | handelsregister.de | 注册信息、年报 |
| 法国 | Societe.com | societe.com | 注册信息、年报、财务 |
| 巴西 | Receita Federal | receita.economia.gov.br | CNPJ信息 |

### BYFIT 公司注册查询SOP

```
Step 1: 确认客户所在国家
Step 2: 访问对应国家公司注册网站
Step 3: 输入公司名或注册号搜索
Step 4: 重点查看：
  → 公司是否真实存在
  → 成立年份（<2年要谨慎）
  → 注册资本（判断规模）
  → 董事信息（确认联系人的身份）
  → 年报是否按时提交（经营是否正常）
  → 是否有注销/清算/破产记录
Step 5: 交叉验证：
  → 注册地址 vs 网站地址（是否一致）
  → 董事名 vs 联系人名（是否匹配）
  → 注册资本 vs 采购规模（是否匹配）
```

---

## 社交媒体调查调度

### 各平台调查策略

| 平台 | 调查目的 | 操作方法 | 工具 |
|------|----------|----------|------|
| **LinkedIn** | 找关键人物、了解组织架构 | 搜索公司名 → 查看员工列表 → 筛选采购/管理层 | web-access (CDP) |
| **Facebook** | 了解品牌形象、客户互动 | 搜索公司页 → 查看帖子、评论、评分 | WebFetch / web-access |
| **Instagram** | 了解产品展示、品牌调性 | 搜索公司账号 → 查看帖子内容 | WebFetch / web-access |
| **YouTube** | 了解产品视频、展会记录 | 搜索公司名 + product | WebSearch |
| **Twitter/X** | 了解公司动态、客户服务 | 搜索公司账号 → 查看推文和互动 | WebSearch / WebFetch |
| **TikTok** | 了解面向C端的内容营销 | 搜索公司名 | WebSearch |

### LinkedIn 深度调查SOP

```
Step 1: 公司页面调查
  → 员工规模（LinkedIn显示的员工数 vs 网站 vs 注册信息）
  → 最近动态（新产品、扩张、招聘）
  → 类似公司（LinkedIn推荐的"Similar Pages"）

Step 2: 关键人物识别
  → 搜索职位关键词：
    "purchasing manager" / "procurement" / "buyer" / "sourcing"
    "CEO" / "managing director" / "owner"
    "product manager" / "category manager" (有采购建议权的人)
  → 记录姓名、职位、在岗时间

Step 3: 关系网络分析
  → 关键人物的connections（是否有共同联系）
  → 关键人物是否关注BYFIT竞品
  → 关键人物的activity（发帖、评论、分享的内容）

Step 4: 间接信息收集
  → 公司的LinkedIn帖子 → 了解业务方向
  → 员工的角色变化 → 组织变动信号
  → 招聘信息 → 扩张/调整信号
```

### 社交媒体信息验证矩阵

| 信息类型 | LinkedIn | Facebook | Instagram | YouTube |
|----------|----------|----------|-----------|---------|
| 公司规模 | ★★★★☆ | ★★☆☆☆ | ★☆☆☆☆ | ★★☆☆☆ |
| 关键人物 | ★★★★★ | ★★☆☆☆ | ★☆☆☆☆ | ★☆☆☆☆ |
| 产品线 | ★★★☆☆ | ★★★☆☆ | ★★★★☆ | ★★★★★ |
| 客户口碑 | ★★☆☆☆ | ★★★★★ | ★★★☆☆ | ★★★☆☆ |
| 品牌调性 | ★★★☆☆ | ★★★☆☆ | ★★★★★ | ★★★★☆ |
| 业务动态 | ★★★★★ | ★★★☆☆ | ★★☆☆☆ | ★★☆☆☆ |

---

## 完整决策树

```
你要做什么？
│
├─ 快速了解一家公司
│   ├─ 知道公司名 → WebSearch → 获取官网URL
│   ├─ 有官网URL → WebFetch → 提取About Us + 产品 + 联系方式
│   └─ 需要更多 → web-access → LinkedIn公司页
│
├─ 找采购负责人
│   ├─ LinkedIn → web-access → 搜索公司+筛选职位
│   ├─ 找到名字但没邮箱 → Hunter.io / Snov.io → 验证邮箱
│   └─ 找不到人 → Google site:linkedin.com/in + 公司名 + 职位
│
├─ 验证客户真实性
│   ├─ 公司注册信息 → 各国注册网站 → 确认公司存在
│   ├─ 海关数据 → 52wmb / ImportGenius → 确认采购记录
│   ├─ 信用查询 → D&B / Creditsafe → 确认财务健康
│   └─ 社交媒体 → Facebook / LinkedIn → 确认活跃度
│
├─ 调查竞品供应商
│   ├─ 海关数据 → 查看客户的供应商是谁
│   ├─ Google搜索 → 竞品网站和产品信息
│   └─ B2B平台 → web-access → 竞品在平台上的展示
│
├─ 突破反爬网站
│   ├─ Cloudflare保护 → stealth-browser
│   ├─ CAPTCHA → stealth-browser
│   └─ 需要登录 → web-access (CDP)
│
├─ 搜索冷门/多语言信息
│   ├─ 俄语市场 → multi-search-engine (Yandex)
│   ├─ 韩国市场 → multi-search-engine (Naver)
│   ├─ 中国市场 → multi-search-engine (百度)
│   └─ 全球覆盖 → multi-search-engine (全引擎)
│
├─ 行业趋势调研
│   ├─ 快速概览 → WebSearch + 行业关键词
│   ├─ 深度报告 → WebFetch + 行业报告URL
│   └─ 多角度 → multi-search-engine
│
└─ 客户深度画像
    ├─ Step 1: WebSearch → 公司基本信息
    ├─ Step 2: WebFetch → 网站详细内容
    ├─ Step 3: web-access → LinkedIn人物信息
    ├─ Step 4: 海关数据 → 采购验证
    ├─ Step 5: 征信查询 → 财务验证
    └─ Step 6: 社交媒体 → 品牌和口碑验证
```

---

## 场景化调度方案

### 场景1：新询盘客户快速评估（10分钟内完成）

```
任务：收到一个新询盘，快速评估客户价值

Step 1: WebSearch "[Company Name]" + industry + country
  → 确认公司是否存在、基本规模
  → 工具：WebSearch
  → 时间：2分钟

Step 2: WebFetch 公司官网 → 提取About Us和产品信息
  → 了解公司定位和产品线
  → 工具：WebFetch
  → 时间：3分钟

Step 3: WebSearch "[Company Name]" + review OR complaint
  → 快速检查是否有负面信息
  → 工具：WebSearch
  → 时间：2分钟

Step 4: 判断客户等级（A/B/C/D）并决定投入精力
  → 基于收集的信息做判断
  → 时间：3分钟

总耗时：~10分钟
```

### 场景2：深度客户调查（30-60分钟完成）

```
任务：对A级客户做全面深度调查

Phase 1: 基础信息（10分钟）
  → WebSearch: 公司基本信息
  → WebFetch: 网站About Us + Products + Contact
  → WebFetch: 新闻/博客页面

Phase 2: 人物调查（15分钟）
  → web-access: LinkedIn公司页
  → web-access: 采购负责人profile
  → Hunter.io: 验证邮箱

Phase 3: 贸易验证（10分钟）
  → 52wmb.com: 海关数据查询
  → 分析采购频次、量、供应商

Phase 4: 信用验证（10分钟）
  → Companies House（或对应国家）: 注册信息
  → Creditsafe / D&B: 信用评分

Phase 5: 社交验证（10分钟）
  → Facebook: 品牌和口碑
  → Instagram: 产品展示
  → YouTube: 产品视频

Phase 6: 整理画像
  → 汇总所有信息
  → 制定开发策略

总耗时：~60分钟
```

### 场景3：竞品供应商调查（20分钟完成）

```
任务：了解客户的现有供应商是谁

Step 1: 海关数据查询
  → 平台：ImportGenius（美国客户）或52wmb（通用）
  → 搜索客户公司名 + HS Code
  → 提取供应商名称和地址

Step 2: WebSearch 供应商公司名
  → 确认是工厂还是贸易公司
  → 了解其产品线和定位

Step 3: 对比分析
  → 工厂 vs 贸易公司 → BYFIT差异化策略
  → 产品线差异 → BYFIT产品线优势
  → 价格参考（如果可获取）→ BYFIT定价策略

总耗时：~20分钟
```

### 场景4：市场进入调研（2-4小时完成）

```
任务：评估BYFIT是否应该进入某个新市场

Phase 1: 市场规模和趋势（30分钟）
  → WebSearch: rubber flooring market [country] size trend
  → WebFetch: IHRSA/Euromonitor报告摘要
  → multi-search-engine: 多角度搜索

Phase 2: 竞争格局（30分钟）
  → WebSearch: rubber flooring distributor [country]
  → 统计主要竞争对手数量和类型
  → 分析竞争密度

Phase 3: 关税和认证（30分钟）
  → WebSearch: HS 401699 import duty [country]
  → WebSearch: rubber flooring certification requirements [country]
  → 确认进入壁垒

Phase 4: 潜在客户搜索（60分钟）
  → Google高级搜索 + B2B过滤
  → 筛选30-50家潜在分销商
  → 6步背景调查前10家

Phase 5: 决策建议（30分钟）
  → 汇总所有信息
  → 给出Go/No-Go建议
  → 如果Go，制定进入策略

总耗时：~3小时
```

### 场景5：客户信用风险预警（15分钟完成）

```
任务：老客户突然请求大幅延长账期，需要快速评估风险

Step 1: 征信快查
  → Creditsafe / D&B → 最新信用评分
  → 时间：5分钟

Step 2: 海关数据查趋势
  → 52wmb → 最近12个月采购量趋势
  → 采购量下降 = 可能经营困难
  → 时间：5分钟

Step 3: 社交媒体查动态
  → LinkedIn → 是否有裁员/高管离职消息
  → Facebook → 是否有关店/负面评价
  → 时间：5分钟

决策：
  → 信用评分下降 + 采购量下降 + 负面消息 → 拒绝延长账期
  → 信用评分稳定 + 采购量稳定 + 无负面消息 → 可适度延长
  → 信息不足 → 维持现有条件
```

---

## 工具使用注意事项

### 1. 合规优先

- 所有调查活动必须合法合规
- 不要使用非法手段获取信息（如黑客攻击、社会工程学）
- 尊重数据保护法规（GDPR、CCPA等）
- 不要在未经授权的情况下访问受保护的信息

### 2. 效率原则

- 先快后深——先用WebSearch快速了解，再决定是否需要深度调查
- 不是所有客户都需要完整调查——根据客户等级分配调查精力
- 避免重复劳动——记录调查结果，团队成员共享

### 3. 信息交叉验证

- 单一信息源不可靠——至少2个来源交叉验证
- 网站信息可能过时——检查最后更新日期
- 海关数据可能有延迟——通常滞后2-3个月
- LinkedIn信息可能不完整——不是所有员工都有profile

### 4. BYFIT 工具使用精力分配

| 客户等级 | 建议调查时间 | 推荐工具组合 |
|----------|-------------|-------------|
| A级（Top 20%） | 60分钟 | 全部工具：WebSearch + WebFetch + web-access + 海关数据 + 征信 |
| B级（Top 50%） | 20分钟 | WebSearch + WebFetch + 海关数据 |
| C级（其余） | 10分钟 | WebSearch + WebFetch |
| D级（低价值） | 5分钟 | WebSearch |

---

## 核心金句

> "WebSearch是望远镜——看得远但不细。WebFetch是放大镜——看得细但需要知道看哪里。web-access是显微镜——看得最深但最慢最贵。选对工具，事半功倍。"

> "海关数据不会说谎——客户说他每年采购100万，海关数据显示他只进口了30万。信谁？"

> "征信查询不是不信任客户，是保护你自己。10分钟的查询可以避免10万美元的坏账。"

> "LinkedIn是客户的'公开日记'——他在哪里工作过、关注什么、和谁互动——这些信息比任何公司官网都真实。"

> "工具是手段，不是目的。调查的目的是理解客户，不是为了收集数据而收集数据。"
