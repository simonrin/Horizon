---
layout: default
title: "Horizon Summary: 2026-09-05 (ZH)"
date: 2026-09-05
lang: zh
---

> 从 350 条内容中筛选出 28 条重要资讯。

---

1. [所有 Chromium 版本中正在被利用的沙箱远程代码执行漏洞](#item-1) ⭐️ 9.0/10
2. [谷歌最强音乐 AI Lyria 3.5 现已集成至 Gemini 和 API](#item-2) ⭐️ 8.0/10
3. [猪肾在人体内运作 271 天创纪录](#item-3) ⭐️ 8.0/10
4. [幸存者就 Tumbler Ridge 枪击案对 OpenAI 提起 30 起诉讼](#item-4) ⭐️ 8.0/10
5. [美国监管机构对特斯拉 Cybercab 部署展开调查](#item-5) ⭐️ 8.0/10
6. [研究识别出 1000 多个与五大人格相关的遗传变异](#item-6) ⭐️ 7.0/10
7. [AI 智能体成为医学影像“首席助理”：速度快，但人机协作更优](#item-7) ⭐️ 7.0/10
8. [微软预览 Excel 的 Copilot Canvas，将数据转化为交互式仪表板](#item-8) ⭐️ 7.0/10
9. [小米开源表格基础模型 TabLDM，登顶 OpenML-CTR23](#item-9) ⭐️ 7.0/10
10. [美中拟于 9 月中旬举行首次 AI 安全对话](#item-10) ⭐️ 7.0/10
11. [美军因位置数据被利用而禁用部队设备上的广告追踪](#item-11) ⭐️ 7.0/10
12. [Audacity 4 全面改版：流行音频编辑器迎来新界面与新功能](#item-12) ⭐️ 7.0/10
13. [AI 初创公司 Gimlet 融资 3 亿美元，估值达 30 亿美元](#item-13) ⭐️ 6.0/10
14. [长安副总裁预测智驾行业 2028 年洗牌，称将留存](#item-14) ⭐️ 6.0/10
15. [星际争霸官网故障暗示新作，剧情推进约 67 年](#item-15) ⭐️ 6.0/10
16. [加州登山者轻信谷歌 Gemini 路线建议被困](#item-16) ⭐️ 6.0/10
17. [纽约市禁止中小学生使用生成式人工智能](#item-17) ⭐️ 6.0/10
18. [美国汽车制造商敦促国会永久禁止中国网联汽车](#item-18) ⭐️ 6.0/10
19. [全国首个 AI 服务一条街在深圳龙岗开放](#item-19) ⭐️ 5.0/10
20. [海南率先出台城镇开发边界管理细则](#item-20) ⭐️ 3.0/10
21. [中国—东盟运河报道媒体倡议发布](#item-21) ⭐️ 2.0/10
22. [武汉文化节在德国架起友好城市桥梁](#item-22) ⭐️ 2.0/10
23. [中国交响乐团演绎神话主题组曲](#item-23) ⭐️ 2.0/10
24. [习近平致贺信祝贺《小喇叭》开播 70 周年](#item-24) ⭐️ 2.0/10
25. [中国以科技创新推动高质量发展，阜阳展示新成果](#item-25) ⭐️ 2.0/10
26. [专家：9 至 10 月接种流感疫苗对冬季高峰仍有效](#item-26) ⭐️ 2.0/10
27. [西藏边境银行确保涉外金融服务不间断](#item-27) ⭐️ 2.0/10
28. [中加举行第五次国防部工作会晤](#item-28) ⭐️ 2.0/10

---

<a id="item-1"></a>
## [所有 Chromium 版本中正在被利用的沙箱远程代码执行漏洞](https://nvd.nist.gov/vuln/detail/cve-2026-85046) ⭐️ 9.0/10

一个严重漏洞 CVE-2026-85046 正在野外被积极利用，影响所有 Chromium 版本。谷歌已确认该漏洞被利用，并在 Chrome 152.0.7977.82 版本中发布了紧急补丁。 该漏洞允许远程攻击者通过精心构造的 HTML 页面在沙箱内执行任意代码，对所有基于 Chromium 的浏览器构成重大安全风险。积极利用的情况凸显了用户和组织立即更新的紧迫性，以防止潜在的数据泄露或系统受损。 该漏洞是 V8 JavaScript 引擎中的类型混淆，可被利用在沙箱内实现任意代码执行。修复包含在 Chrome 152.0.7977.82 及更高版本中，建议同时更新 V8 引擎。

hackernews · negura · 9月4日 21:52 · [社区讨论](https://news.ycombinator.com/item?id=49570669)

**背景**: Chromium 是支撑 Google Chrome 及许多其他浏览器的开源浏览器项目。沙箱是一种安全机制，用于隔离网页内容以限制漏洞的影响。V8 是 Chromium 的 JavaScript 引擎，类型混淆漏洞可能导致内存损坏和代码执行。该 CVE 是近期 Chromium 中一系列沙箱逃逸漏洞的一部分，凸显了持续存在的安全挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://feedly.com/cve/CVE-2026-85046">CVE - 2026 - 85046 - Exploits & Severity - Feedly</a></li>
<li><a href="https://cvefeed.io/vuln/detail/CVE-2026-85046">CVE - 2026 - 85046 - Google Chrome V8 Type Confusion Vulnerability</a></li>
<li><a href="https://issues.chromium.org/issues/412075782">Google Chrome Sandbox Escape Vulnerability [412075782] - Chromium</a></li>

</ul>
</details>

**社区讨论**: 社区评论讨论了该漏洞的金钱价值，一位用户指出谷歌为报告支付了 1000 美元，并质疑其实际价值。其他人对不断出现的安全问题表示沮丧，并比较了 Brave 和 GrapheneOS 等浏览器的更新及时性。还有用户询问攻击者在沙箱内能做什么，因为沙箱本应提供隔离。

**标签**: `#security`, `#chromium`, `#CVE`, `#RCE`, `#browser`

---

<a id="item-2"></a>
## [谷歌最强音乐 AI Lyria 3.5 现已集成至 Gemini 和 API](https://www.ithome.com/0/998/647.htm) ⭐️ 8.0/10

9 月 5 日，谷歌宣布在 Gemini 应用和 Gemini API 中发布其最新音乐生成模型 Lyria 3.5，向消费者和开发者开放。该模型可生成时长数分钟的完整歌曲，支持图像提示和 SynthID 水印。 这标志着先进的 AI 音乐生成技术向主流用户和开发者生态迈出了重要一步，可能改变音乐制作的创意流程。同时，它也巩固了谷歌在竞争激烈的 AI 音乐领域的地位，对艺术家、制作人和应用开发者产生影响。 提供两种模型：Lyria 3 Clip（模型 ID 为 lyria-3-clip-preview）用于 30 秒循环和预览，以及 Lyria 3.5（模型 ID 为 lyria-3.5）用于生成包含副歌、桥段等多个部分的完整歌曲。开发者可在文本提示外提供最多 10 张图像，输出支持 MP3（默认）和 WAV（Lyria 3.5）；所有输出均嵌入 SynthID 水印。

rss · ITHome Feed · 9月4日 23:53

**背景**: Lyria 是谷歌的 AI 音乐生成模型，此前用于 Google Flow Music 等实验性工具。SynthID 是一种水印技术，可将隐形且稳健的标识嵌入 AI 生成的内容中，以帮助追踪和验证其来源。此次集成至 Gemini 和 API 标志着其从研究走向商业部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/lyria/">Lyria 3.5 — Google DeepMind</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-labs/lyria-3-5/">We’re launching Lyria 3.5 in Google Flow Music, with advances across musicality, lyrics, vocals, and creative control.</a></li>
<li><a href="https://deepmind.google/models/synthid/">SynthID — Google DeepMind</a></li>

</ul>
</details>

**标签**: `#AI music generation`, `#Google Gemini`, `#Lyria 3.5`, `#API`, `#creative AI`

---

<a id="item-3"></a>
## [猪肾在人体内运作 271 天创纪录](https://www.bbc.com/zhongwen/articles/c1dlr007vkgo/trad?at_medium=RSS&at_campaign=rss) ⭐️ 8.0/10

一名等待人体肾脏移植的男子依靠基因编辑猪肾在体内运作创纪录的九个月（271 天）存活，标志着异种移植领域的重大里程碑。 这一突破展示了猪器官在缓解器官短缺方面为患者争取时间的潜力，有望减少等待名单上的死亡人数，并为人类捐献器官提供可行的替代方案。 猪肾经过基因编辑以提高兼容性并降低排斥风险。该患者后来成功接受了人类肾脏移植，成为在长期猪肾支持后完成这一过渡的首例。

rss · BBC Chinese · 9月4日 05:57

**背景**: 异种移植涉及将其他物种（如猪）的器官移植到人体内。基因编辑技术的进步帮助克服了超急性排斥反应，美国已启动猪肾移植的临床试验，专家预计 5 至 10 年内有望获批。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hms.harvard.edu/news/patient-who-received-pig-kidney-becomes-first-progress-human-kidney-transplant">Patient Who Received Pig Kidney Becomes First To Progress to Human ...</a></li>
<li><a href="https://www.kidney.org/news-stories/pig-kidney-transplants-humans-xenotransplantation-explained-experts">Pig Kidney Transplants in Humans: Xenotransplantation Explained by Experts</a></li>
<li><a href="https://www.scientificamerican.com/article/transplant-rejection-is-a-major-hurdle-for-pig-organs-scientists-are-solving/">Transplant Rejection Is a Major Hurdle for Pig Organs. Scientists Are Solving the Problem | Scientific American</a></li>

</ul>
</details>

**标签**: `#xenotransplantation`, `#organ transplant`, `#medical breakthrough`, `#biotechnology`, `#health`

---

<a id="item-4"></a>
## [幸存者就 Tumbler Ridge 枪击案对 OpenAI 提起 30 起诉讼](https://www.nytimes.com/2026/09/04/world/canada/openai-lawsuits-tumbler-ridge-shooting.html) ⭐️ 8.0/10

不列颠哥伦比亚省 Tumbler Ridge 枪击案的幸存者已对 OpenAI 提起 30 起诉讼，指控该公司未能在 2 月袭击前就枪手令人不安的 ChatGPT 账户提醒警方。诉讼称，OpenAI 在八个月前关闭该账户时就应通知当局。 此案可能为 AI 公司对用户生成内容的责任以及其向当局警告潜在威胁的义务树立法律先例。它引发了关于平台责任、内容审核和 AI 安全的关键问题，可能影响 AI 提供商处理有害内容及与执法部门互动的方式。 诉讼称，OpenAI 在 2 月袭击前八个月关闭了枪手的 ChatGPT 账户，但未通知警方。法律行动聚焦于 AI 公司是否有义务报告令人担忧的用户活动，而现有法律尚未明确解决这一问题。

rss · The New York Times World · 9月4日 17:19

**背景**: OpenAI 有内容审核政策和工具，如审核 API，用于检测有害内容，但这些主要用于过滤输出，而非触发执法通知。AI 生成内容责任的法律环境仍在演变，关于用户滥用 AI 系统时谁应负责的问题尚存争议。此案凸显了用户隐私、平台安全以及主动威胁报告潜在需求之间的紧张关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/transparency-and-content-moderation/">Transparency & content moderation | OpenAI</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/moderation">Moderation | OpenAI API</a></li>
<li><a href="https://www.rock.law/liability-ai-model-providers-user-generated-harms-platform-responsibility/">What Liability Do AI Model Providers Face for User-Generated ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#legal`, `#OpenAI`, `#content moderation`, `#liability`

---

<a id="item-5"></a>
## [美国监管机构对特斯拉 Cybercab 部署展开调查](https://techcrunch.com/2026/09/04/feds-launch-investigation-into-teslas-cybercab-deployment/) ⭐️ 8.0/10

美国国家公路交通安全管理局（NHTSA）已对特斯拉 Cybercab 的部署展开调查，就在 2026 年 9 月 4 日首批量产车在德克萨斯州奥斯汀开始向公众提供付费乘车服务几小时后。 此次调查是一个重大的监管事件，可能影响未来自动驾驶汽车政策，并冲击特斯拉的运营和声誉。它凸显了自动驾驶技术在从测试走向商业部署过程中面临的严格审查。 Cybercab 是一款双座纯电动汽车，没有方向盘、踏板或后视镜，专为特斯拉 Robotaxi 服务设计。调查在车辆公开亮相后数小时内启动，表明监管机构急于快速解决潜在的安全问题。

rss · TechCrunch · 9月4日 12:01

**背景**: 特斯拉 Cybercab 于 2024 年 10 月首次以概念车形式亮相，2026 年 2 月开始试生产。NHTSA 通常采用基于风险的流程调查潜在安全缺陷，通过审查数据和投诉来确定是否存在缺陷。此次调查是在该车首次商业部署后进行的，标志着特斯拉自动驾驶汽车雄心面临关键时刻。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Cybercab">Tesla Cybercab</a></li>
<li><a href="https://www.nhtsa.gov/resources-investigations-recalls">Resources Related to Investigations and Recalls | NHTSA</a></li>

</ul>
</details>

**标签**: `#Tesla`, `#autonomous vehicles`, `#regulation`, `#Cybercab`, `#investigation`

---

<a id="item-6"></a>
## [研究识别出 1000 多个与五大人格相关的遗传变异](https://www.chinanews.com.cn/gj/2026/09-05/10690824.shtml) ⭐️ 7.0/10

2026 年 9 月 2 日发表在《自然》杂志上的一项荟萃分析，利用来自 46 个队列、多达 114 万名参与者的数据，识别出 1260 个与五大人格特质相关的先导遗传变异。这是迄今为止规模最大的人格遗传研究之一。 这项研究极大地推进了我们对人格遗传基础的理解，可能为心理学、精神病学和个人化医疗的未来研究提供信息。它也强调了遗传与环境之间的复杂相互作用，因为所识别的变异仅解释了人格差异的一小部分。 该研究识别出 1260 个先导变异，其中 824 个位于此前未关联的基因组区域，并发现这些常见遗传变异仅解释了约 5%至 10%的人格差异。研究使用了 46 个队列的数据，不同特质的样本量从 611,037 到 114 万不等。

rss · China News Service Scroll · 9月5日 04:05

**背景**: 五大人格特质——外向性、宜人性、尽责性、神经质和经验开放性——是心理学中广泛使用的描述人格的框架。全基因组关联研究（GWAS）通过扫描许多个体的基因组来寻找与特质相关的遗传变异。这项荟萃分析结合了多个 GWAS 数据集，以增加统计功效并识别出比以往研究更多的变异。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Big_Five_personality_traits">Big Five personality traits - Wikipedia</a></li>
<li><a href="https://www.nature.com/articles/s41586-026-10992-9">Robust inference and correlates from genetic associations with personality | Nature</a></li>
<li><a href="https://www.news-medical.net/news/20260903/What-your-genes-can-and-cannot-tell-us-about-your-personality.aspx">What your genes can, and cannot, tell us about your personality</a></li>

</ul>
</details>

**标签**: `#genetics`, `#personality`, `#Nature`, `#meta-analysis`, `#Big Five`

---

<a id="item-7"></a>
## [AI 智能体成为医学影像“首席助理”：速度快，但人机协作更优](https://36kr.com/p/3968685170700801?f=rss) ⭐️ 7.0/10

在上海举行的第五届医学影像 AI 学术会议上，举办了一场公开的“人机读片大赛”，AI 智能体与医生竞争撰写诊断报告。结果显示，高年资医生搭配多任务智能体得分最高（85.2 分），而独立工作的 AI 智能体得分 66.2 分，但用时最短，仅 20 分 32 秒。 这一发现强调，尽管 AI 智能体速度快，但人机协作能产生更优质的诊断报告，凸显了当前 AI 在医学影像中的最佳应用方式。这也反映了行业从单任务垂直模型向集成到放射科工作流程的多智能体系统的转变。 比赛使用了来自顶级医院的 10 个真实疑难病例，设置了 7 个组别，包括低/高年资医生与 AI 智能体的不同组合。AI 智能体会产生假阳性结果，需要医生复核；专家有时误将 AI 生成的报告判断为人类撰写，表明人机边界逐渐模糊。

rss · 36Kr Feed · 9月4日 08:18

**背景**: 医学影像 AI 已从单任务垂直模型（如检测肺结节）发展到模拟放射科医生阅片逻辑并生成完整报告初稿的多智能体系统。这一转变旨在减少医生的重复性工作，但在临床验证、监管和报销方面仍存在挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://digiqt.com/blog/ai-agents-in-medical-imaging-and-radiology/">AI Agents in Medical Imaging: 20 Use Cases (2026) | Digiqt Blog</a></li>
<li><a href="https://healthmanagement.org/c/decision-support/News/human-ai-collaboration-lifts-diagnostic-decisions">Human–AI Collaboration Lifts Diagnostic Decisions</a></li>
<li><a href="https://dirjournal.org/articles/human-ai-interaction-and-collaboration-in-radiology-from-conceptual-frameworks-to-responsible-implementation/dir.2026.263780">Human–AI interaction and collaboration in radiology: from ...</a></li>

</ul>
</details>

**标签**: `#AI in healthcare`, `#medical imaging`, `#human-AI collaboration`, `#AI agents`

---

<a id="item-8"></a>
## [微软预览 Excel 的 Copilot Canvas，将数据转化为交互式仪表板](https://www.ithome.com/0/998/693.htm) ⭐️ 7.0/10

微软宣布为 Excel 推出 Copilot Canvas，这是一项新的人工智能功能，可将工作簿数据转化为包含关键可视化、指标和洞察的交互式画布。该功能将在未来几周内逐步推送，预计于 10 月初完成部署。 该功能通过提供整合的交互式视图，减少了在多个图表和工作表之间切换的需求，从而增强了 Excel 的 Copilot 能力。这标志着向更直观、AI 驱动的数据分析迈出了重要一步，可能提升商业用户和分析师的生产力。 Copilot Canvas 与原始工作簿保持实时连接，因此手动数据编辑或来自外部来源的更新都会自动刷新仪表板。用户还可以通过与 Copilot 的自然语言对话来修改画布内容，这建立在现有创建模板和仪表板的能力之上。

rss · ITHome Feed · 9月5日 03:00

**背景**: Excel 是一款广泛使用的电子表格应用程序，微软一直在集成其 AI 助手 Copilot，以帮助用户分析数据和创建可视化。此前，Copilot 可以根据提示生成模板和仪表板，但用户仍需在不同元素之间导航。Copilot Canvas 旨在将这些整合到一个交互式视图中，利用 AI 简化数据探索和展示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.windowslatest.com/2026/09/05/microsoft-is-adding-an-ai-powered-canvas-to-excel-that-turns-workbook-data-into-interactive-dashboards/">Microsoft is adding an AI-powered Canvas to Excel that turns ...</a></li>
<li><a href="https://windowsforum.com/windows-news.4/excel-canvas-what-microsofts-2026-roadmap-promises.443985/">Excel Canvas: What Microsoft’s 2026 Roadmap Promises</a></li>
<li><a href="https://letsdatascience.com/news/microsoft-is-adding-copilot-canvas-to-excel-784be390">Microsoft Is Adding Copilot Canvas to Excel | Let's Data Science</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#Excel`, `#AI`, `#Data Visualization`, `#Copilot`

---

<a id="item-9"></a>
## [小米开源表格基础模型 TabLDM，登顶 OpenML-CTR23](https://www.ithome.com/0/998/683.htm) ⭐️ 7.0/10

小米于 2026 年 9 月 5 日正式发布并开源了通用表格数据基础模型 Xiaomi-TabLDM。该模型在四大公开基准测试中均进入第一梯队，在 OpenML-CTR23 回归榜上排名第一，并在 TALENT 二分类任务中同样排名第一。 此次发布将“一次预训练、跨任务使用”的范式引入结构化数据领域，有望降低传统表格机器学习繁重的部署成本。这可能对金融、医疗、制造、物流等严重依赖表格数据的行业产生重要影响。 Xiaomi-TabLDM 完全基于结构因果模型（SCM）生成的大规模合成数据进行预训练，其架构引入了双流特征分组、轻量级注意力残差和稀疏混合专家。该模型还探索了 Test-Time Scaling，在不改变预训练参数的情况下，通过增加推理阶段计算量来持续提升预测性能。

rss · ITHome Feed · 9月5日 02:31

**背景**: 表格数据在许多行业中普遍存在，但传统的机器学习模型通常需要针对每个新数据集进行重新训练和调参。基础模型在大规模数据上预训练并可适应多种任务，已在文本和图像领域取得成功，Xiaomi-TabLDM 旨在将这一范式引入表格数据。该模型提供 scikit-learn 兼容接口，可通过 pip 安装使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.03880">Xiaomi - TabLDM : A Tabular Foundation Model Technical Report</a></li>
<li><a href="https://post.smzdm.com/p/a4qdoplw/">小米发布并开源结构化数据大模型 Xiaomi - TabLDM ...</a></li>

</ul>
</details>

**标签**: `#AI/ML`, `#Foundation Models`, `#Structured Data`, `#Tabular Data`, `#Xiaomi`

---

<a id="item-10"></a>
## [美中拟于 9 月中旬举行首次 AI 安全对话](https://www.rfi.fr/cn/%E4%B8%AD%E5%9B%BD/20260904-%E7%BE%8E%E4%B8%AD%E6%8B%9F9%E6%9C%88%E4%B8%AD%E6%97%AC%E9%A6%96%E6%AC%A1%E4%B8%BE%E8%A1%8Cai%E5%AE%89%E5%85%A8%E5%AF%B9%E8%AF%9D) ⭐️ 7.0/10

据知情人士透露，美国和中国正筹备于 2026 年 9 月中旬举行首次正式的 AI 安全对话。会谈将重点讨论如何监测 AI 引发的网络攻击，以及建立机制防止先进 AI 系统被滥用。 此次对话是当前美国政府任期内美中首次专门聚焦 AI 安全的双边讨论，在更广泛的地缘政治紧张局势中标志着罕见的合作领域。对话结果可能为国际 AI 治理树立先例，并影响全球应对 AI 相关风险的努力。 对话预计将讨论如何监测 AI 引发的网络攻击，并建立机制防止先进 AI 系统被滥用。会谈定于 9 月中旬举行，但具体日期和地点尚未公开。

rss · RFI Chinese · 9月4日 20:20

**背景**: AI 安全是指旨在确保人工智能系统安全运行且不造成伤害的实践和政策。随着 AI 能力快速发展，人们对其在网络攻击和其他恶意活动中被滥用的担忧日益增加，促使国际社会就治理和安全措施展开讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.usnews.com/news/world/articles/2026-09-04/exclusive-us-china-gear-up-for-mid-september-ai-safety-dialogue">Exclusive-US, China Gear up for Mid-September AI Safety Dialogue</a></li>
<li><a href="https://www.reuters.com/legal/litigation/us-china-gear-up-mid-september-ai-safety-dialogue-2026-09-04/">EXCLUSIVE: US, China gear up for mid-September AI safety ...</a></li>
<li><a href="https://cryptobriefing.com/us-china-ai-safety-dialogue-september/">US and China prepare for mid-September AI safety dialogue</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#US-China relations`, `#AI governance`, `#cybersecurity`

---

<a id="item-11"></a>
## [美军因位置数据被利用而禁用部队设备上的广告追踪](https://techcrunch.com/2026/09/04/us-military-disabled-ad-tracking-on-troops-devices-following-reports-of-targeted-attacks/) ⭐️ 7.0/10

据报道，外国对手利用位置数据对美军人员实施针对性攻击，美军随后禁用了部队设备上的广告追踪。一位参议员的信件证实了这一行动，该行动旨在保护军人免受针对性攻击。 此举凸显了广告追踪和位置数据带来的日益增长的安全风险，这些数据可能被对手武器化。它为其他组织，尤其是敏感行业的组织，重新考虑其数据收集做法树立了先例。 该行动通过参议员的信件得到确认，但有关如何禁用追踪或哪些设备受影响的具体技术细节并未披露。此前有报道称外国对手利用位置数据瞄准部队，凸显了数据隐私漏洞的现实影响。

rss · TechCrunch · 9月4日 13:21

**背景**: 移动设备上的广告追踪依赖于广告标识符（如 iOS 上的 IDFA 和 Android 上的 AAID），这些标识符允许广告商跨应用和网站追踪用户行为。位置数据通常通过这些追踪机制收集，可能揭示个人活动和习惯的敏感信息。当此类数据落入不当之手时，可能被用于恶意目的，包括针对军事人员。禁用广告追踪是减少此类风险暴露的直接措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.adtaxi.com/blog/mobile-id-tracking-what-is-it-and-why-does-it-work/">Mobile ID Tracking : What Is it, and Why Does it Work ? | Adtaxi</a></li>
<li><a href="https://froggyads.com/blog/how-does-ad-tracking-work/">Best How Does Ad Tracking Work ? - [2026] Froggy Ads</a></li>
<li><a href="https://www.groovypost.com/howto/reset-your-ad-tracking-id-on-your-android-or-ios-device/">Limit Ad Tracking and Reset Your Advertising ID on Android or iOS</a></li>

</ul>
</details>

**标签**: `#privacy`, `#security`, `#military`, `#location tracking`

---

<a id="item-12"></a>
## [Audacity 4 全面改版：流行音频编辑器迎来新界面与新功能](https://www.theverge.com/tech/990658/audacity-4-update-audio-editing) ⭐️ 7.0/10

Audacity 4 已作为开源音频编辑器的全面改版发布，采用了重新设计的界面和新标志。此次更新承诺在先前版本基础上进行重大改进，回应了用户长期以来的反馈。 此次重大更新对音频制作社区意义重大，因为 Audacity 是全球最广泛使用的音频编辑器之一。这次改版可能吸引新用户并改善现有用户的体验，有可能重塑开源音频编辑的格局。 新标志的最终版本比去年十月流传的早期版本争议性更小。文章提到了承诺的改进，但现有内容中未提供具体的技术细节。

rss · The Verge · 9月4日 21:23

**背景**: Audacity 是一款免费开源的数字音频编辑器，因其强大的功能和跨平台可用性而流行数十年。像这样的全面改版通常涉及用户界面的现代化、性能提升以及添加新工具，以保持与商业软件的竞争力。

**标签**: `#Audacity`, `#audio editing`, `#open source`, `#software update`

---

<a id="item-13"></a>
## [AI 初创公司 Gimlet 融资 3 亿美元，估值达 30 亿美元](https://36kr.com/newsflashes/3969862414266633?f=rss) ⭐️ 6.0/10

AI 初创公司 Gimlet 完成了由 Andreessen Horowitz 领投的 3 亿美元融资，估值达到 30 亿美元。 这笔重大投资凸显了市场对 AI 初创公司持续的高度关注和资金流入，可能加速 Gimlet 的产品开发和市场扩张。这也反映了顶级风投机构正在支持有前景的 AI 企业的竞争格局。 本轮融资由知名风投机构 Andreessen Horowitz 领投。资金的具体用途尚未披露，但此类投资通常用于扩大运营、研发和人才招聘。

rss · 36Kr Feed · 9月5日 01:52

**背景**: Gimlet 是一家在快速增长的人工智能领域运营的 AI 初创公司。近期，风险投资在 AI 领域的投资激增，投资者押注于变革性技术。Andreessen Horowitz 是一家领先的风投公司，以支持科技公司而闻名。

**标签**: `#AI`, `#funding`, `#startup`, `#venture capital`

---

<a id="item-14"></a>
## [长安副总裁预测智驾行业 2028 年洗牌，称将留存](https://www.ithome.com/0/998/728.htm) ⭐️ 6.0/10

长安汽车副总裁贺刚预测，智能驾驶行业将在 2028 年左右完成首轮洗牌，届时中国市场上可能仅剩五六家具备竞争力的解决方案商。他表示“我们和引望会留下来”，并透露天枢领航技术总投入已超 600 亿元，研发团队达 7500 人。 这一预测凸显了中国自动驾驶领域日益激烈的竞争和预期的行业整合，可能重塑市场格局。长安宣称将留存，并投入巨资推进技术落地，标志着传统车企在智能驾驶领域与科技巨头展开正面竞争的重大举措。 长安“天枢领航”系统提供 Pro、Max、Ultra、Ultimate 四个梯度，算力从超过 100 TOPS 到最高 1000 TOPS，全系标配激光雷达并采用一段式端到端架构。首款车型长安启源 Q06 预售 2 小时内订单突破 11079 台，其中 Ultra 版本占比达 53%。长安计划明年在海外落地高速 NCA 方案，并已与多家外部车厂完成路测。

rss · ITHome Feed · 9月5日 04:12

**背景**: 智能驾驶系统如 NCA（导航巡航辅助）可在高速和城市道路提供辅助驾驶功能。“一段式端到端”架构通过单一 AI 模型将传感器数据直接映射为控制指令，区别于模块化或两段式方法。中国近期批准了强制性国家标准《智能网联汽车自动驾驶系统安全要求》（GB 44721—2026），将于 2027 年 7 月实施，但 L3 级面向消费者的安全标准仍在制定中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.qq.com/rain/a/20260905A04MK200">首个央企自研智能驾驶辅助方案，长安“天枢领航”来了_腾讯新闻</a></li>
<li><a href="https://www.sohu.com/a/1072128504_161795">首个央企自研智能驾驶辅助方案，长安“天枢领航”来了_技术_Ultra_搭载</a></li>
<li><a href="https://k.sina.cn/article_2131593523_7f0d893302001ozo4.html">长安发布天枢领航自研智驾技术，启源Q06同步开启预售|长安汽车|长安启...</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#Changan Auto`, `#intelligent driving`, `#automotive technology`, `#industry consolidation`

---

<a id="item-15"></a>
## [星际争霸官网故障暗示新作，剧情推进约 67 年](https://www.ithome.com/0/998/723.htm) ⭐️ 6.0/10

暴雪《星际争霸》官网出现故障效果和隐藏信息，粉丝发现这些线索指向一款设定在 2575 年、即《星际争霸 II：虚空之遗》剧情约 67 年后的新作。该预告出现在 2026 年暴雪嘉年华（9 月 12-13 日）前夕。 这是自《虚空之遗》（2015 年）以来首个暗示《星际争霸》新作的重要线索，可能标志着该系列的复兴。这种 ARG 式营销表明暴雪正以互动方式吸引社区参与，为 2026 年暴雪嘉年华的官方公告造势。 隐藏信息包括时间戳为 2575 年 8 月至 9 月的通讯记录，提及罗克萨拉的一处月球采矿设施、正在靠近的 Theta 中队，以及自动炮、重型设备、电子设备和机密研究箱等货物。记录还显示电网波动、系统登记的在场生还者为 0 人，但传感器探测到 14 个未识别的移动或生命信号。

rss · ITHome Feed · 9月5日 03:51

**背景**: 替代现实游戏（ARG）是一种以现实世界为平台的互动叙事，通常包含隐藏线索和谜题。《星际争霸 II：虚空之遗》于 2015 年 11 月 10 日发布，是《星际争霸》系列最后一部主线作品，结束了始于《自由之翼》（2010 年）和《虫群之心》（2013 年）的三部曲。暴雪嘉年华是暴雪每年举办的展会，通常在此发布重大公告。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Alternate_reality_game">Alternate reality game - Wikipedia</a></li>
<li><a href="https://starcraft.fandom.com/wiki/StarCraft_II:_Legacy_of_the_Void">StarCraft II: Legacy of the Void | StarCraft Wiki | Fandom</a></li>
<li><a href="https://blizzardwatch.com/2026/09/01/watch-blizzcon-2026-schedule-livestream-coverage/">How to watch BlizzCon 2026, with full convention schedule</a></li>

</ul>
</details>

**标签**: `#StarCraft`, `#Blizzard`, `#ARG`, `#Gaming`, `#Teaser`

---

<a id="item-16"></a>
## [加州登山者轻信谷歌 Gemini 路线建议被困](https://www.ithome.com/0/998/684.htm) ⭐️ 6.0/10

三名缺乏经验的登山者在沙斯塔山依赖谷歌 Gemini 的路线建议，但该建议低估了攀登时间和难度，导致夜间救援行动。他们凌晨 3 点出发，预计上午 11 点登顶，但直到晚上 7 点才到达山顶，耗时约 16 小时。 这一事件凸显了 AI 在高风险场景中的现实局限性，强调 AI 生成的建议不应成为安全关键决策的唯一依据。它提醒用户，尤其是在户外活动中，应将 AI 信息与权威来源进行交叉验证。 其中一名登山者手机中安装了 AllTrails 导航应用，但手机没电导致无法使用。事后，他们向救援人员承认“过于依赖 AI，而没有进行自己的判断”。Gemini 还建议携带碳水化合物而非脂肪，称脂肪“消化时间太长”，这可能影响了他们的体力。

rss · ITHome Feed · 9月5日 02:32

**背景**: 沙斯塔山是一座具有挑战性的山峰，坡陡、天气多变、海拔高，需要充分的准备和登山技能。像谷歌 Gemini 这样的 AI 工具可以快速整合公开信息，但缺乏实际经验，无法评估当前的天气、雪况或个人体能。这一事件为 AI 在户外导航和安全方面的局限性提供了警示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mountshastamagic.com/what-is-the-difficulty-level-of-climbing-mount-shasta/">What Is The Difficulty Level Of Climbing Mount Shasta?</a></li>
<li><a href="https://globalsummitguide.com/mountains-mount-shasta-california-usa-difficulty-safety/">Mount Shasta Difficulty & Safety: Essential Climbing Tips ...</a></li>
<li><a href="https://www.alltrails.com/">AllTrails : Trail Guides & Maps for Hiking, Camping, and Running</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#Gemini`, `#real-world AI`, `#limitations`, `#outdoor navigation`

---

<a id="item-17"></a>
## [纽约市禁止中小学生使用生成式人工智能](https://www.dw.com/zh/%E7%BA%BD%E7%BA%A6%E5%B8%82%E9%95%BF%E9%A9%AC%E5%A7%86%E8%BE%BE%E5%B0%BC%EF%BC%9A%E5%B0%8F%E5%AD%A6%E5%88%9D%E4%B8%AD%E7%A6%81%E7%94%A8%E7%94%9F%E6%88%90%E5%BC%8Fai%E4%B8%80%E5%B9%B4/a-78946149?maca=chi-rss-chi-all-1127-rdf) ⭐️ 6.0/10

纽约市市长佐兰·马姆达尼于 2026 年 9 月 2 日宣布，公立学校将在 2026-2027 学年禁止学前班至八年级学生使用生成式人工智能工具。该禁令影响约 60 万名学生，而高中生在特定条件下仍可使用 AI。 这是美国教育领域最严格的 AI 政策之一，为大型学区如何处理生成式 AI 对儿童发展和学术诚信的风险树立了先例。它凸显了在拥抱 AI 教育潜力与保护低龄学生免受潜在危害之间的日益紧张关系。 教师仍可使用 AI 进行备课和日程安排。该禁令为期一年，同时该市将为高中生推出 AI 教育培训项目。此前，在 ChatGPT 于 2022 年发布后不久，该市曾实施过临时禁令。

rss · DW Chinese · 9月4日 10:01

**背景**: 像 ChatGPT 这样的生成式 AI 工具可以生成类似人类的文本、图像和其他内容，引发了对抄袭、错误信息以及对儿童发展影响的担忧。全球各地的学区都在努力解决如何负责任地整合这些工具的问题。纽约市公立学校系统是美国最大的学区，其政策具有影响力。新禁令反映了一种谨慎的态度，在创新与儿童安全和教育诚信之间寻求平衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://global.hk01.com/即时国际/60386287/纽约市新学年推新规-拟禁止公立学校中三以下学生用ai">纽约市新学年推新规 拟禁止公立学校中三以下学生用AI</a></li>
<li><a href="https://news.qq.com/rain/a/20260904A03RJ000">纽约市长发布全美最严课堂AI禁令，60万学生将受影响</a></li>
<li><a href="https://original.ifeng.com/c/8w73V6Lla5W">纽约市禁高中以下学生用AI，禁令为期1年_凤凰网</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#education`, `#generative AI`, `#regulation`

---

<a id="item-18"></a>
## [美国汽车制造商敦促国会永久禁止中国网联汽车](https://www.rfi.fr/cn/%E5%9B%BD%E9%99%85/20260904-%E6%B1%BD%E8%BD%A6%E5%88%B6%E9%80%A0%E5%95%86%E6%95%A6%E4%BF%83%E7%BE%8E%E5%9B%BD%E5%9B%BD%E4%BC%9A%E6%B0%B8%E4%B9%85%E7%A6%81%E6%AD%A2%E4%B8%AD%E5%9B%BD%E7%BD%91%E8%81%94%E6%B1%BD%E8%BD%A6%E8%BF%9B%E5%85%A5%E7%BE%8E%E5%9B%BD) ⭐️ 6.0/10

在美国运营的主要汽车制造商通过汽车创新联盟向国会施压，要求在 1 月 3 日会期结束前通过一项永久禁令，禁止在美国销售、进口和生产中国网联汽车及其软硬件。 此举可能通过限制一个主要的全球供应商，深刻重塑汽车和科技行业，可能影响供应链和网络安全标准。这也标志着美中在高科技汽车领域的贸易紧张局势升级。 汽车创新联盟代表了占美国轻型车销量 99%的汽车制造商，包括福特、通用、丰田和大众等主要品牌。拟议的禁令不仅涵盖整车，还包括其软件和硬件组件。

rss · RFI Chinese · 9月4日 17:15

**背景**: 网联汽车是指配备互联网连接和先进技术（如传感器、人工智能和通信系统）的汽车，能够实现自动驾驶和实时数据交换等功能。汽车创新联盟是一个总部位于华盛顿特区的行业协会，成立于 2020 年，代表美国的主要汽车制造商。对数据安全和国家安全的担忧导致对中国制造的汽车及其技术的审查日益严格。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Alliance_for_Automotive_Innovation">Alliance for Automotive Innovation - Wikipedia</a></li>
<li><a href="https://baike.baidu.com/item/美国汽车创新联盟/62182147">美国汽车创新联盟_百度百科</a></li>
<li><a href="https://m.tech.china.com/tech/article/20211012/20211012894333.html">重塑 汽 车 产业生态 新 技 术 筑安全底线_中华 网</a></li>

</ul>
</details>

**标签**: `#automotive`, `#policy`, `#China`, `#connected vehicles`, `#trade`

---

<a id="item-19"></a>
## [全国首个 AI 服务一条街在深圳龙岗开放](https://www.chinanews.com.cn/gn/2026/09-05/10690798.shtml) ⭐️ 5.0/10

2026 年 9 月 4 日，全国首个 AI 服务一条街在深圳龙岗正式开放，该街区串联 AI 技术研发、场景落地、产业赋能和企业服务等全链条环节。 这标志着龙岗区“All in AI”战略的重要进展，从单点 AI 应用迈向全域 AI 产业化、场景化和市民化。此举可能为中国其他地区发展 AI 产业集群和智慧城市建设提供示范。 该街区依托全国首个具身智能机器人示范街区及“机器人大道”等成熟载体，定位为龙岗区迈向全域 AI 生态的核心标杆项目。

rss · China News Service China · 9月5日 02:27

**背景**: 龙岗区一直积极推动 AI 发展，包括 2025 年 5 月启用的“机器人大道”，作为其具身智能机器人示范街区的核心场景。该区的“All in AI”战略旨在构建从技术研发到场景落地的完整生态圈，吸引全球开发者和 AI 创业者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.21jingji.com/article/20251208/herald/179092e2e42dfff9149c7c22058af889.html">这个 街 区 ，“ 机 器 人 浓度”很高 - 21经济网</a></li>
<li><a href="https://m.jiemian.com/article/14511232_sina.html">大湾 区 具 身 智 能 迎来产业爆发期，深圳通信巨头转 身 算力新贵 | 界面新闻</a></li>
<li><a href="https://m.21jingji.com/article/20260310/herald/7cd0d3932582adb93dec623ade736ad7.html">深 圳 龙 岗 “ 龙 虾十 条 ”未出先火，数百家企业连夜咨询 - 21财经</a></li>

</ul>
</details>

**标签**: `#AI`, `#China`, `#Industry`, `#Smart City`

---

<a id="item-20"></a>
## [海南率先出台城镇开发边界管理细则](https://www.chinanews.com.cn/gn/2026/09-04/10690712.shtml) ⭐️ 3.0/10

海南省近日出台《城镇开发边界管理实施细则（试行）》，在全国率先推出。该细则细化了管控标准、优化了调整规则，并引入了激励机制。 此举提升了海南的国土空间治理水平，并有助于解决规划落地难题，可能为其他省份提供借鉴。它反映了中国推进国土空间治理现代化的更广泛努力。 该细则由海南省自然资源和规划厅发布，据中新社 9 月 4 日报道。它是国家框架的一部分，遵循自然资源部《城镇开发边界管理办法（试行）》。

rss · China News Service China · 9月4日 14:25

**背景**: 城镇开发边界是在国土空间规划中划定的控制城市扩张、保护生态和农业用地的界线。2019 年，中国建立了国家空间规划体系，自然资源部发布了城镇开发边界管理办法（试行）。海南的新细则提供了更详细的地方实施指导。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gov.cn/gongbao/2026/issue_12646/202603/content_7064117.html">自然资源部关于印发《城镇开发边界管理办法（试行）》的通知 城镇开发...</a></li>
<li><a href="https://www.guoturen.com/guihua-4739.html">广东省城镇开发边界管理实施细则（试行，公开征求意见稿）</a></li>
<li><a href="https://www.chinalandscience.com.cn/zgtdkx/article/abstract/20241360">国土空间治理现代化：理论逻辑与实现路径</a></li>

</ul>
</details>

**标签**: `#urban planning`, `#policy`, `#China`, `#land management`

---

<a id="item-21"></a>
## [中国—东盟运河报道媒体倡议发布](https://www.chinanews.com.cn/aseaninfo/2026/09-05/10690858.shtml) ⭐️ 2.0/10

2026 年 9 月 4 日，在广西钦州平陆运河工程建设指挥部，中国与东盟青年代表共同发布了《中国—东盟主流媒体运河国际报道倡议书》，旨在加强运河相关报道的区域媒体合作。 该倡议标志着中国与东盟之间加强区域媒体合作的努力，可能有助于提升对平陆运河等重大基础设施项目的跨境理解。它有望促进更协调、更包容青年的区域互联互通与经济一体化叙事。 该倡议是在平陆运河项目现场举行的“我们与世界对话——中外青年共话运河时代机遇”活动期间发布的。倡议强调加强青年交流、深化运河主题合作、推动区域传播协作，共同讲好中国—东盟合作故事。

rss · China News Service Scroll · 9月5日 04:26

**背景**: 平陆运河是中国广西的一项重大内河航道工程，旨在连接西江水系与北部湾，提供新的贸易通道。中国与东盟经济联系紧密，媒体合作被视为增进相互理解、支持“一带一路”等区域倡议的途径。

**标签**: `#media`, `#ASEAN`, `#China`, `#regional cooperation`

---

<a id="item-22"></a>
## [武汉文化节在德国架起友好城市桥梁](https://www.chinanews.com.cn/cul/2026/09-05/10690852.shtml) ⭐️ 2.0/10

2026 年 9 月 4 日，德国杜伊斯堡玛丽安门剧院举办“中国节”，来自武汉的顶尖文艺院团以“白云黄鹤是故乡”为主题轮番登场。该活动庆祝了武汉与杜伊斯堡四十余年的友好城市关系。 此次文化节凸显了中德之间的文化交流，加强了国际联系，并向海外展示了武汉的文化底蕴。它体现了文化活动如何促进国家间的相互理解与友谊。 活动在德国北威州杜伊斯堡的玛丽安门剧院举行，由武汉顶尖文艺院团献上表演。主题“白云黄鹤是故乡”源自中国著名诗句，象征着武汉的文化身份。

rss · China News Service Scroll · 9月5日 04:08

**背景**: 武汉与杜伊斯堡保持友好城市关系已超过四十年，促进了经济和文化交流。“中国节”是推动中国文化海外传播、加强双边关系的持续努力的一部分。

**标签**: `#culture`, `#China`, `#Germany`, `#event`

---

<a id="item-23"></a>
## [中国交响乐团演绎神话主题组曲](https://www.chinanews.com.cn/cul/2026/09-05/10690845.shtml) ⭐️ 2.0/10

9 月 4 日晚，吉林省交响乐团在吉林省音乐厅上演了大型交响音乐套曲《中国传说》，演绎了五个乐章，灵感源自中国古代神话。 这一活动凸显了中国传统文化与西方古典音乐的融合，可能扩大两者的受众，并以现代形式促进文化遗产的传播。 该套曲包含五个乐章：《开天》《移山》《奔月》《填海》《逐日》，每个乐章对应一个著名的中国神话。演出在长春的吉林省音乐厅举行。

rss · China News Service Scroll · 9月5日 04:06

**背景**: 中国神话包括盘古开天、愚公移山、嫦娥奔月、精卫填海和夸父逐日等故事。这些故事是中国文化认同的基础，并被改编成各种艺术形式。交响乐团旨在通过西方管弦乐重新诠释这些古老叙事，创造跨文化的艺术表达。

**标签**: `#music`, `#culture`, `#China`

---

<a id="item-24"></a>
## [习近平致贺信祝贺《小喇叭》开播 70 周年](https://www.chinanews.com.cn/ll/2026/09-05/10690854.shtml) ⭐️ 2.0/10

中国国家主席习近平在中央广播电视总台《小喇叭》儿童广播节目开播 70 周年之际致贺信，肯定其贡献，并鼓励创作更多优质儿童作品。 这体现了中国政府对儿童文化教育的高度重视及其软实力战略。它表明国家将继续支持塑造青少年价值观的媒体，可能影响中国儿童内容的资金和政策。 贺信强调“立德树人”的根本任务，并呼吁创作传播真善美的作品。同时指出该节目在培养德智体美劳全面发展的社会主义建设者和接班人中的作用。

rss · China News Service Scroll · 9月5日 03:53

**背景**: 《小喇叭》是中国一档历史悠久的儿童广播节目，自 1956 年开播以来，以故事、歌曲和教育内容著称。它是中国利用媒体进行青少年教育和思想引导的更广泛努力的一部分。

**标签**: `#politics`, `#children's media`, `#China`

---

<a id="item-25"></a>
## [中国以科技创新推动高质量发展，阜阳展示新成果](https://www.chinanews.com.cn/ll/2026/09-05/10690842.shtml) ⭐️ 2.0/10

一篇宣传性新闻文章重点介绍了安徽阜阳的技术创新，包括用于家电的磁共振无线供电、功能性纺织材料，以及每天超过 10 亿只的芯片电阻高效生产。 这篇文章强调了中国将科技创新融入产业发展的努力，可能促进经济增长和技术自主。它反映了国家高质量发展的战略，但缺乏技术深度。 文章提到了具体例子：用于破壁机和风扇的磁共振无线供电、用于极地和消防的功能性纺织品，以及每天超过 10 亿只的芯片电阻生产。这些被作为创新推动产业进步的证据。

rss · China News Service Scroll · 9月5日 03:28

**背景**: 磁共振无线供电利用谐振耦合实现无接触电能传输，可隔空供电。芯片电阻，也称为贴片电阻，是用于手机和 5G 基站等电子设备中的微型元件。该文章是高质量发展宣传系列的一部分，高质量发展是中国的重要政策主题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://patents.google.com/patent/CN201742173U/zh">CN201742173U - 磁共振式无线供电电路 - Google Patents</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/555881806">什么是芯片电阻，其标准规格如何 - 知乎</a></li>

</ul>
</details>

**标签**: `#China`, `#technology`, `#promotional`

---

<a id="item-26"></a>
## [专家：9 至 10 月接种流感疫苗对冬季高峰仍有效](https://www.chinanews.com.cn/jk/2026/09-05/10690840.shtml) ⭐️ 2.0/10

中国卫生部门发布了 2026-2027 年度流感疫苗接种技术指南，建议公众在 9 至 10 月完成接种，因为冬春季流感流行季通常在 11 月左右开始。 该指南帮助公众了解流感疫苗的最佳接种时机，确保在流行高峰获得保护，同时支持公共卫生工作，减少流感相关疾病和医院负担。 指南指出，2026-2027 年度中国上市的三价流感疫苗包括三价灭活疫苗和三价减毒活疫苗，并强调 9 至 10 月接种可在 11 月高峰来临前产生足够免疫力。

rss · China News Service Scroll · 9月5日 03:22

**背景**: 流感是一种季节性呼吸道疾病，在中国北方和南方地区冬季达到高峰。由于流感病毒变异且疫苗效力随时间减弱，建议每年接种。中国疾控中心每年发布技术指南以规范接种实践。

**标签**: `#public health`, `#vaccination`, `#flu season`

---

<a id="item-27"></a>
## [西藏边境银行确保涉外金融服务不间断](https://www.chinanews.com.cn/cj/2026/09-05/10690838.shtml) ⭐️ 2.0/10

2026 年 9 月 4 日，在中国农业银行西藏吉隆口岸支行，一名商户将 1 万美元兑换成崭新的人民币现钞，凸显了该行在边境地区持续提供涉外金融服务。 这一日常交易凸显了该行在偏远边境地区持续提供跨境金融服务的承诺，对当地贸易和经济稳定至关重要。它反映了支持边境社区和促进西藏跨境业务的更广泛努力。 此次兑换发生在西藏日喀则市吉隆县吉隆镇的中国农业银行吉隆口岸支行，商户将 1 万美元兑换成崭新的人民币现钞。新闻简报强调此类服务不间断提供，确保跨境业务及时办理。

rss · China News Service Scroll · 9月5日 03:14

**背景**: 吉隆是西藏的一个边境县，设有与尼泊尔贸易的口岸。此类地区的银行通常提供外汇服务，以支持当地商户和跨境经济活动。中国农业银行在偏远地区设有分支机构，服务当地社区并促进贸易。

**标签**: `#news`, `#finance`, `#Tibet`

---

<a id="item-28"></a>
## [中加举行第五次国防部工作会晤](https://www.chinanews.com.cn/gn/2026/09-05/10690829.shtml) ⭐️ 2.0/10

2026 年 9 月 4 日，中加两国在加拿大举行了第五次国防部工作会晤，双方就共同关心的国际和地区问题交换了意见，并表示愿意加强军事合作。 此次会晤表明，尽管地缘政治局势紧张，中加两国仍保持外交和军事对话。这有助于管控双边关系，促进两军务实合作。 会晤于 2026 年 9 月 4 日举行，中国国防部网站于 9 月 5 日发布了相关消息。双方进行了坦诚深入的交流，聚焦共同关心的问题，增进了相互理解和信任。

rss · China News Service Scroll · 9月5日 03:08

**背景**: 中加两国在国防领域有交流历史，但近年来关系面临挑战。此次工作会晤是两国国防部保持沟通的持续机制的一部分。

**标签**: `#defense`, `#diplomacy`, `#China`, `#Canada`

---