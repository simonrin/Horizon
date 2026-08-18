---
layout: default
title: "Horizon Summary: 2026-08-18 (ZH)"
date: 2026-08-18
lang: zh
---

> 从 347 条内容中筛选出 28 条重要资讯。

---

1. [DuckDB v2.0 预览版推出 VARIANT 和 Quack](#item-1) ⭐️ 8.0/10
2. [三结太阳电池效率达 32.22%，成果发表于《自然》](#item-2) ⭐️ 8.0/10
3. [英伟达将为 OpenAI 俄亥俄数据中心提供最高 1050 亿美元担保](#item-3) ⭐️ 8.0/10
4. [苹果用户收到间谍软件警报数量空前](#item-4) ⭐️ 8.0/10
5. [世界最长海底高铁隧道完成带压盾构换刀](#item-5) ⭐️ 7.0/10
6. [机器人力传感器企业蓝点触控完成数亿元 D 轮融资](#item-6) ⭐️ 7.0/10
7. [苹果带摄像头 AirPods 演示视频在 macOS Tahoe 中曝光](#item-7) ⭐️ 7.0/10
8. [Groq 转型 Neocloud，以 35 亿美元估值融资 3.5 亿美元](#item-8) ⭐️ 7.0/10
9. [美国数据中心建设热潮每年或排放超亿吨二氧化碳](#item-9) ⭐️ 7.0/10
10. [特斯拉最快本月在奥斯汀推出 Cybercab 自动驾驶出租车服务](#item-10) ⭐️ 7.0/10
11. [Anthropic 年化营收突破 650 亿美元，引发 IPO 猜测](#item-11) ⭐️ 7.0/10
12. [Meta 面临美国 30 州就青少年安全提起的里程碑式诉讼](#item-12) ⭐️ 7.0/10
13. [乌克兰卫星以实时数据增强无人机作战](#item-13) ⭐️ 7.0/10
14. [中国欲出口数据以影响全球 AI 聊天机器人](#item-14) ⭐️ 7.0/10
15. [Higgsfield 完成 4 亿美元 B 轮融资，估值翻两番达 54 亿美元](#item-15) ⭐️ 7.0/10
16. [亚马逊销毁稀有书籍训练 AI 引发伦理担忧](#item-16) ⭐️ 7.0/10
17. [中国移动离岸 95 公里开通 5G 基站创全国纪录](#item-17) ⭐️ 6.0/10
18. [全球航运成本飙升至历史新高，工厂面临停工威胁](#item-18) ⭐️ 6.0/10
19. [中美 AI 竞赛：突破创新与低成本普及的对决](#item-19) ⭐️ 6.0/10
20. [SHEIN 香港上市估值降至 250 亿美元，较 2021 年峰值缩水 75%](#item-20) ⭐️ 6.0/10
21. [山西高校团队研发 100 余种铝镁合金产品](#item-21) ⭐️ 5.0/10
22. [全球粮食安全初见成效，零饥饿目标仍遥远](#item-22) ⭐️ 4.0/10
23. [7 月工业增加值增长 4.5%，集成电路大幅增长](#item-23) ⭐️ 4.0/10
24. [蒙古国前总理：中国经济从基建转向数智动力](#item-24) ⭐️ 4.0/10
25. [田湾核电 7 号机组完成装料，进入带核调试阶段](#item-25) ⭐️ 4.0/10
26. [中国警方公布 14 起涉企网络谣言典型案例](#item-26) ⭐️ 4.0/10
27. [银发私教：为老年人打造客厅健身房](#item-27) ⭐️ 4.0/10
28. [广东高院出台 15 条举措护航绿色低碳发展](#item-28) ⭐️ 4.0/10

---

<a id="item-1"></a>
## [DuckDB v2.0 预览版推出 VARIANT 和 Quack](https://duckdb.org/2026/08/17/duckdb-20-highlights) ⭐️ 8.0/10

DuckDB v2.0 预览版引入了主要功能，包括用于半结构化数据的 VARIANT 数据类型和用于运行时使用的客户端-服务器协议 Quack。该预览版引发了社区的高度关注，获得了 538 个点赞和 96 条评论。 此次发布对数据工程社区意义重大，因为它增强了 DuckDB 高效处理半结构化数据的能力，并将其用例扩展到客户端-服务器部署。它可能影响开发者构建分析管道和运行时应用的方式，从而可能减少某些工作负载对传统数据库的依赖。 VARIANT 类型受 Snowflake 的 VARIANT 启发，支持“shredding”技术，将常见字段提取到列式存储中，以获得更好的压缩和性能。Quack 作为扩展提供，允许 DuckDB 通过 HTTP 同时充当服务器和客户端，支持多写入者和远程访问，同时保持进程内模式作为一等公民。

hackernews · ibotty · 8月17日 13:46 · [社区讨论](https://news.ycombinator.com/item?id=49330781)

**背景**: DuckDB 是一种进程内分析数据库，以其速度和易用性著称，常用于数据分析和 ETL。VARIANT 类型专为 JSON 等半结构化数据设计，这类数据在现代数据管道中很常见，但存储和查询效率往往较低。Quack 将 DuckDB 的能力扩展到客户端-服务器模型，这是对其传统嵌入式特性的转变，可能拓宽其适用性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://duckdb.org/docs/current/sql/data_types/variant">Variant Type - DuckDB</a></li>
<li><a href="https://duckdb.org/quack/">Quack Remote Protocol – DuckDB</a></li>
<li><a href="https://github.com/duckdb/duckdb-quack">The Quack Client/Server Protocol for DuckDB</a></li>

</ul>
</details>

**社区讨论**: 社区情绪普遍积极，用户对 VARIANT 的压缩优势和 Quack 的运行时能力表示兴奋。一些用户分享了实际经验，例如使用 DuckDB 进行实时分析以及在其上构建流处理引擎。一位用户对不到 6 个月内 10,000 次提交的高数量表示担忧，质疑 AI 是否加速了开发，这可能成为争论点。

**标签**: `#DuckDB`, `#database`, `#analytics`, `#data engineering`, `#release`

---

<a id="item-2"></a>
## [三结太阳电池效率达 32.22%，成果发表于《自然》](https://www.ithome.com/0/990/905.htm) ⭐️ 8.0/10

东南大学团队与天合光能、复旦大学合作，在钙钛矿/钙钛矿/晶体硅三结太阳电池中实现了 32.22%的认证稳态光电转换效率。该成果于 2026 年 8 月 17 日发表在《自然》上，引入了一种新型界面钝化材料 4F-POEABr，可抑制表面缺陷和非辐射复合。 这一突破展示了超越单结太阳电池 Shockley-Queisser 极限的可行途径，可能加速高效光伏技术的应用。该界面钝化的分子设计策略可广泛应用于多结太阳电池的性能和稳定性提升，惠及可再生能源产业。 4F-POEABr 分子将全氟芳香共轭骨架与铵盐钝化基团集成，实现化学钝化和场效应钝化的协同。修饰后，1.95 eV 宽带隙子电池获得了 1.413 V 的开路电压，并通过 SnOx/IZO 中间层的光学管理优化了光场分布和电流匹配。

rss · ITHome Feed · 8月18日 00:59

**背景**: 三结太阳电池通过堆叠不同带隙的吸收材料来更高效地利用太阳光谱，有望超越单结电池的效率极限。然而，宽带隙钙钛矿顶电池存在表面缺陷和非辐射复合，导致电压损失。像 4F-POEABr 这样的界面钝化材料旨在化学中和缺陷并调节局域电场，从而减少这些损失并提升器件性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-026-11010-8">Defect passivation and optical management of triple-junction solar cells | Nature</a></li>
<li><a href="https://bioengineer.org/researchers-improve-triple-junction-solar-cells-through-defect-passivation-and-optical-management/">Researchers improve triple-junction solar cells through defect passivation</a></li>

</ul>
</details>

**标签**: `#solar cells`, `#perovskite`, `#photovoltaics`, `#materials science`, `#Nature`

---

<a id="item-3"></a>
## [英伟达将为 OpenAI 俄亥俄数据中心提供最高 1050 亿美元担保](https://www.ithome.com/0/990/890.htm) ⭐️ 8.0/10

英伟达同意为 OpenAI 在俄亥俄州的数据中心提供最高 1050 亿美元的担保，该数据中心由软银旗下的 SB Energy 开发，英伟达还将向 SB Energy 投资 15 亿美元。这是英伟达迄今规模最大的基础设施融资承诺。 这笔交易凸显了英伟达通过融资 AI 基础设施来推动其芯片需求的战略转变，可能为类似安排开创先例。同时，它也引发了对循环融资的担忧，即资本在少数公司之间流动，如果 AI 收入未能实现，可能带来系统性风险。 该数据中心位于俄亥俄州派克县，总计算能力最高可达 8 吉瓦，首期 800 兆瓦预计于 2028 年投入使用。OpenAI 计划租用该设施 20 年，英伟达将成为独家芯片供应商。担保仅覆盖租赁和电力费用的一部分，若 OpenAI 违约，英伟达需承担差额。

rss · ITHome Feed · 8月17日 23:57

**背景**: AI 基础设施需要大量资金用于数据中心和能源，往往超出单个公司的资产负债表。英伟达作为 AI 芯片主导者，越来越多地参与项目融资以确保其产品需求。循环融资指的是资本在少数交易对手之间流动的安排，如芯片供应商、模型实验室和基础设施开发商，这可能产生相互关联的金融风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/08/17/nvidia-financing-open-ai-data-center-ohio.html">Nvidia backs financing for OpenAI data center in Ohio</a></li>
<li><a href="https://cryptobriefing.com/nvidia-reduces-guarantee-openai-data-center/">Nvidia scales back financial guarantee to under $120B for ...</a></li>
<li><a href="https://sbenergy.com/openai-and-softbank-group-partner-with-sb-energy/">OpenAI and SoftBank Group Partner with SB Energy</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#OpenAI`, `#AI infrastructure`, `#data center`, `#financing`

---

<a id="item-4"></a>
## [苹果用户收到间谍软件警报数量空前](https://techcrunch.com/2026/08/17/unprecedented-number-of-apple-users-received-recent-spyware-alert-say-investigators/) ⭐️ 8.0/10

调查人员报告称，收到关于雇佣间谍软件的威胁通知的苹果用户数量异常之多，标志着针对性攻击显著增加。据《福布斯》报道，这些警报已发送给 110 个国家的用户。 这种升级表明国家支持的监控活动范围更广、更具攻击性，影响到记者、活动人士、政治家和外交官。这凸显了雇佣间谍软件日益增长的威胁，以及苹果威胁通知系统在保护高风险个人方面的重要性。 苹果的威胁通知通过横幅、电子邮件和 iMessage 发送，警告用户可能遭受雇佣间谍软件攻击。这些警报是苹果正式安全计划的一部分，调查人员认为最近的激增是前所未有的。

rss · TechCrunch · 8月17日 20:18

**背景**: 雇佣间谍软件（如 Pegasus）是复杂的监控软件，常被政府用于针对特定个人。这些攻击成本高昂且有效期短，难以检测。苹果的威胁通知系统旨在告知可能被单独针对的用户，并提供自我保护指导。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.apple.com/en-us/102174">About Apple threat notifications and protecting against mercenary spyware</a></li>
<li><a href="https://www.forbes.com/sites/kateoflahertyuk/2026/08/14/apple-issues-new-spyware-warning-to-iphone-users-in-110-countries/">Apple Issues New Spyware Warning To iPhone Users In 110 Countries - Forbes</a></li>
<li><a href="https://www.zdnet.com/article/apple-warns-targetted-spyware-attacks-what-to-do/">Apple is warning users of new spyware attacks - what to do if... | ZDNET</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#spyware`, `#Apple`, `#privacy`, `#threat notification`

---

<a id="item-5"></a>
## [世界最长海底高铁隧道完成带压盾构换刀](https://www.chinanews.com.cn/gn/2026/08-18/10679361.shtml) ⭐️ 7.0/10

2026 年 8 月 17 日，建设者在甬舟铁路金塘海底隧道宁波侧 80 米深处，于 7.8 巴水压下历时 21 天完成 104 把盾构刀具的检查和更换，标志着我国自主研发的饱和带压进仓技术首次成功通过长时间、超高压实战检验。 这一里程碑展示了我国在极端深海条件下安全高效更换刀具的能力，提升了在深埋跨海隧道建设领域的竞争力。该饱和带压技术的成功验证减少了对国外方法的依赖，为未来更具雄心的海底基础设施项目铺平了道路。 此次作业位于甬舟铁路金塘海底隧道，水深 80 米，水压 7.8 巴，历时 21 天完成 104 把刀具的检查与更换，验证了“深海空间站”设备的可靠性。该设备于 2026 年 2 月首次投入使用。

rss · China News Service China · 8月17日 23:33

**背景**: 盾构机利用旋转刀盘挖掘隧道，刀具会随时间磨损，尤其是在磨蚀性或混合地层中。水下换刀通常需要带压作业（压缩空气）或预先加固地层以便常压进仓。饱和带压技术是将工人送入充满饱和空气的加压舱内进行维护，相比传统压缩空气方法，可在更深、更高水压下实现更长的工作时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.news.cn/politics/20260206/261fb55e38814c4f98898a353bced5d9/c.html">我国自主研发盾构饱和带压进仓技术成功应用-新华网</a></li>
<li><a href="http://www.zj.xinhuanet.com/20260207/8981cf07002e4834b6532497fdd96889/c.html">我国自主研发盾构饱和带压进仓技术成功应用-新华网</a></li>
<li><a href="https://www.toutiao.com/article/7615058589509583403/">我国自主研发盾构饱和带压进仓技术成功应用 - 今日头条</a></li>

</ul>
</details>

**标签**: `#engineering`, `#tunnel construction`, `#deep-sea`, `#technology`, `#infrastructure`

---

<a id="item-6"></a>
## [机器人力传感器企业蓝点触控完成数亿元 D 轮融资](https://36kr.com/p/3943183864560776?f=rss) ⭐️ 7.0/10

本轮融资凸显了力传感器在人形机器人供应链中的战略重要性，尤其是在人形机器人从展示走向实际应用之际。蓝点触控在人形机器人六维力传感器市场占据 72.6%的份额，其发展标志着行业的高度认可，并可能影响整个生态。 蓝点触控的六维力传感器实现 0.1%FS 精度、10kHz 以上高频响应、500%抗过载能力，体积缩减 90%、重量降低 80%。公司在广东建立了国内首条机器人力传感器全自动产线，设计年产能达关节力传感器 100 万套、末端六维力传感器 20 万套，交付周期从 6-8 周缩短至 2-3 周。

rss · 36Kr Feed · 8月17日 05:38

**背景**: 六维力传感器是一种精密传感器，能够同时测量三个力分量（Fx, Fy, Fz）和三个力矩分量（Mx, My, Mz），提供物体在三维空间中所受全部力和力矩的完整信息。它们对于机器人感知和与环境交互至关重要，可实现精确、安全的运动控制，尤其在人形机器人中用于平衡、装配和抓取等任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/1921137128483577871">六维力传感器是什么？工作原理是什么？有哪些具体应用、注意事项</a></li>
<li><a href="https://baike.baidu.com/item/六维力传感器/66982815">六维力传感器 - 百度百科</a></li>
<li><a href="https://blog.csdn.net/2301_79503228/article/details/138118817">六维力传感器的介绍 - CSDN博客</a></li>

</ul>
</details>

**标签**: `#robotics`, `#funding`, `#force sensors`, `#humanoid robots`, `#supply chain`

---

<a id="item-7"></a>
## [苹果带摄像头 AirPods 演示视频在 macOS Tahoe 中曝光](https://www.ithome.com/0/990/919.htm) ⭐️ 7.0/10

在 macOS Tahoe 26.7 RC 中发现的一段演示视频证实苹果正在研发配备摄像头的 AirPods（代号 B790），视频中用户拍摄书名并通过视觉智能保存。系统代码还包含设置提示以及头发遮挡摄像头的警告。 这表明苹果带摄像头的 AirPods 已接近发布，最早可能在 2026 年 9 月与 iPhone 18 系列一同亮相。这标志着苹果将 AI 驱动的视觉智能集成到可穿戴设备中的重要一步，扩展了其生态系统并增强了在 AI 领域的竞争力。 AirPods 的摄像头将把信息提供给苹果的视觉智能，使 Siri 能够回答有关周围环境的问题并记录相关信息。内部代号 B790 此前曾被彭博社记者 Mark Gurman 提及，他暗示可能在 9 月发布。

rss · ITHome Feed · 8月18日 01:33

**背景**: macOS Tahoe 是苹果最新的 macOS 大版本，于 2025 年 WWDC 上发布。视觉智能是 Apple Intelligence 的一部分，后者是苹果的 AI 功能套件，提供屏幕感知和上下文理解。带摄像头的 AirPods 预计不会用于拍照，而是让 Siri 具备视觉感知能力，实现物体识别和环境理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.macrumors.com/2026/08/17/camera-equipped-airpods-macos-26-7/">Apple's Camera-Equipped AirPods Confirmed: See Them in ...</a></li>
<li><a href="https://www.macrumors.com/2026/08/03/airpods-with-cameras-could-arrive-sooner/">AirPods With Cameras Could Arrive Sooner Than Expected</a></li>
<li><a href="https://en.wikipedia.org/wiki/MacOS_Tahoe">macOS Tahoe - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Apple`, `#AirPods`, `#Visual Intelligence`, `#Wearables`, `#AI`

---

<a id="item-8"></a>
## [Groq 转型 Neocloud，以 35 亿美元估值融资 3.5 亿美元](https://www.ithome.com/0/990/912.htm) ⭐️ 7.0/10

8 月 17 日，Groq 宣布完成 3.5 亿美元 A 轮融资，估值达 35 亿美元，由 Disruptive 领投，NVIDIA 计划参与。此前 6 月已融资 6.5 亿美元，近期累计融资达 10 亿美元，公司正从 AI 芯片开发商转型为 Neocloud 服务提供商。 这一转型标志着 AI 基础设施领域的重大战略转变，Groq 利用与 NVIDIA 的 LPU 技术许可协议，转型为云服务提供商。NVIDIA 的参与凸显了专业 AI 云服务提供商的兴起趋势，以及 AI 计算资源的整合。 Groq 于去年 12 月与 NVIDIA 签署了价值 200 亿美元的非独家技术许可协议，授权 NVIDIA 使用其 LPU 推理加速 ASIC。8 月 12 日，Groq 宣布成为 NVIDIA 云合作伙伴，提供基于 NVIDIA 加速计算集群的训练和推理服务，并计划将算力容量从当前的 54MW 提升至 2027 年的 200MW 以上。

rss · ITHome Feed · 8月18日 01:19

**背景**: Groq 以其语言处理单元（LPU）闻名，这是一种专为推理设计的 ASIC，使用片上 SRAM 而非 HBM，为大型语言模型提供确定性延迟和高吞吐量。Neocloud 是一种新型云服务提供商，专注于面向 AI 工作负载的 GPU 优化基础设施，相比传统超大规模云服务商提供更快的访问速度和更低的成本。Groq 从芯片制造商向 Neocloud 的转型反映了对专业 AI 计算服务日益增长的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Groq">Groq - Wikipedia</a></li>
<li><a href="https://dnyuz.com/2026/08/14/nvidia-got-groqs-technology-and-talent-now-its-turning-the-rest-of-its-former-rival-into-a-customer/">Nvidia got Groq ’s technology and talent. Now it’s turning the rest of its...</a></li>
<li><a href="https://theempiremagazine.com/groq-nvidia-agreement/">Groq Raises $650M to Scale AI Cloud After Nvidia Agreement AI Infra...</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#Groq`, `#funding`, `#NVIDIA`, `#cloud computing`

---

<a id="item-9"></a>
## [美国数据中心建设热潮每年或排放超亿吨二氧化碳](https://www.ithome.com/0/990/903.htm) ⭐️ 7.0/10

一项新分析显示，亚马逊、谷歌、Meta 和微软在美国建设的 60 座大型数据中心全面投入运营后，每年可能合计排放约 1.015 亿吨二氧化碳，相当于 27 座燃煤电厂或 2400 万辆燃油汽车的排放量。 这凸显了一个重大的环境矛盾：科技巨头的人工智能扩张正推动化石燃料使用激增，削弱了他们早先的气候承诺。这加剧了人工智能基础设施增长与可持续发展目标之间的紧张关系，影响社区、公用事业公司和政策制定者。 分析发现，在这些数据中心所在地区，约四分之三的电力运营商正在建设或规划新的燃气发电能力，而仍在运营燃煤电厂的电力企业中约三分之一正在推迟退役计划。亚马逊 2025 年排放量同比增长 16%，微软增长 25%，Alphabet（调整后）增长 18%。

rss · ITHome Feed · 8月18日 00:51

**背景**: 数据中心是能源密集型设施，为云计算和人工智能服务提供动力。其快速增长引发了对电力需求、用水和碳排放的担忧。美国正经历数据中心建设热潮，尤其是为了人工智能，导致对天然气和煤炭的依赖增加，以满足全天候电力需求，因为可再生能源和储能尚不充足。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theregister.com/2025/01/22/datacenter_emissions_not_accurate/?ref=biztoc.com">Analysts say real datacenter emissions are a dirty secret • The Register</a></li>
<li><a href="https://www.dw.com/en/pushback-on-data-centers-artificial-intelligence-water-drought-environmental-problems/a-78064418">US citizens are ramping up pressure on data centers - dw.com</a></li>
<li><a href="https://buildenergyhub.com/why-ai-is-increasing-electricity-demand/">Why AI Is Increasing Electricity Demand - Build Energy Hub</a></li>

</ul>
</details>

**标签**: `#data centers`, `#carbon emissions`, `#AI infrastructure`, `#environmental impact`, `#US energy`

---

<a id="item-10"></a>
## [特斯拉最快本月在奥斯汀推出 Cybercab 自动驾驶出租车服务](https://www.ithome.com/0/990/899.htm) ⭐️ 7.0/10

据 The Information 报道，特斯拉已通知员工，正准备推出 Cybercab 自动驾驶出租车服务，最快将于本月在得克萨斯州奥斯汀市上线。公司计划先让员工在公共道路上体验车辆，随后几天内正式将其纳入 Robotaxi 服务。 这标志着特斯拉在自动驾驶领域迈出重要一步，因为 Cybercab 是一款专为自动驾驶设计的车型，没有方向盘和踏板。如果成功，可能加速自动驾驶出租车的普及，重塑城市交通，同时加剧自动驾驶网约车市场的竞争。 Cybercab 是一款双座电动车，没有方向盘和踏板，专为完全自动驾驶设计。特斯拉一直在为推出做准备，包括进行道路测试、让员工在封闭道路上体验车辆，以及与当地急救人员开展培训。自 6 月以来，量产版已在公共道路上测试，预计今年晚些时候将扩大产量。

rss · ITHome Feed · 8月18日 00:41

**背景**: 特斯拉多年来一直在开发自动驾驶技术，包括其完全自动驾驶（FSD）系统和 Robotaxi 服务。Cybercab 于 2024 年 10 月作为概念车亮相，特斯拉已在包括奥斯汀在内的多个城市推出了基于 Model Y 的 Robotaxi 服务。Cybercab 旨在成为该服务的专用车辆，提供更低的每英里成本和更高的安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Cybercab">Tesla Cybercab - Wikipedia</a></li>
<li><a href="https://www.tesla.com/robotaxi">Robotaxi - Tesla</a></li>
<li><a href="https://builtin.com/articles/tesla-robotaxis">What Is the Tesla Robotaxi Service ? | Built In</a></li>

</ul>
</details>

**标签**: `#Tesla`, `#Autonomous Driving`, `#Robotaxi`, `#Cybercab`, `#Electric Vehicles`

---

<a id="item-11"></a>
## [Anthropic 年化营收突破 650 亿美元，引发 IPO 猜测](https://www.ithome.com/0/990/887.htm) ⭐️ 7.0/10

截至 7 月底，Anthropic 的年化收入运行率已超过 650 亿美元，高于 5 月份的 470 亿美元和 2025 年底的约 90 亿美元。这一快速增长加剧了市场对其可能在今年晚些时候进行 IPO 的猜测。 这一里程碑凸显了 Anthropic 在人工智能行业的爆炸性增长，主要得益于其 Claude 编程智能体的广泛采用。这也使该公司成为 AI 市场的主要竞争者，潜在的 IPO 可能重塑投资者情绪和竞争格局。 年化收入运行率是根据当前销售水平推算未来 12 个月营收的指标。Anthropic 已秘密提交 IPO 申请，路透社报道该公司预计 2028 年营收将达到约 1900 亿至 2000 亿美元，这将成为其 IPO 估值的重要依据。

rss · ITHome Feed · 8月17日 23:53

**背景**: 年化收入运行率是一种基于当前收入趋势推算公司年度收益的指标，常用于高增长初创企业。Anthropic 是一家以 Claude 模型闻名的领先 AI 公司，其在软件开发领域的广泛应用推动了营收激增。该公司在 5 月完成了 650 亿美元的 H 轮融资，估值达到 9650 亿美元，是 2 月份 3800 亿美元估值的两倍多。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.shopify.com/blog/run-rate">Run Rate : Definition , Formula, and How to Calculate It (2025) - Shopify</a></li>
<li><a href="https://www.investopedia.com/terms/r/runrate.asp">investopedia.com/terms/r/runrate.asp</a></li>
<li><a href="https://www.cnbc.com/2026/08/13/anthropic-cfo-early-ipo-meetings-valuation.html">Anthropic CFO Krishna Rao is leading early IPO meetings with investors and has not discussed valuation, sources say</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI`, `#revenue`, `#IPO`, `#Claude`

---

<a id="item-12"></a>
## [Meta 面临美国 30 州就青少年安全提起的里程碑式诉讼](https://www.bbc.com/zhongwen/articles/c4g33g9red9o/trad?at_medium=RSS&at_campaign=rss) ⭐️ 7.0/10

美国 30 个州已对 Meta 提起诉讼，要求对其社交媒体平台 Instagram 和 Facebook 进行重大改革，以保护年轻用户。该诉讼要求改变据称对未成年人有害的平台设计和做法。 这起诉讼可能从根本上改变 Meta 为年轻用户运营其平台的方式，并可能为整个行业的社交媒体监管树立先例。如果成功，可能会导致更严格的安全措施、年龄验证和设计变更，影响数百万用户并重塑科技政策。 该诉讼得到 30 个州的两党联盟支持，表明具有广泛的政治支持。具体要求可能包括限制成瘾性功能、增强家长控制以及解决针对未成年人的数据收集做法，但摘要中未详细说明具体条款。

rss · BBC Chinese · 8月17日 12:16

**背景**: 像 Instagram 和 Facebook 这样的社交媒体平台因其对年轻用户心理健康的影响而面临越来越多的审查，包括成瘾、网络欺凌和接触有害内容等问题。这起诉讼是针对科技公司的更广泛监管和法律行动趋势的一部分，此前已有类似案件和旨在保护儿童在线的立法努力。

**标签**: `#Meta`, `#lawsuit`, `#social media`, `#tech policy`, `#youth safety`

---

<a id="item-13"></a>
## [乌克兰卫星以实时数据增强无人机作战](https://www.nytimes.com/2026/08/17/world/europe/from-the-sky-to-the-battlefield.html) ⭐️ 7.0/10

乌克兰无人机团队现在利用近实时的卫星数据来追踪部队动向，将卫星图像送达前线部队的时间从数天缩短至近乎即时。这种整合使无人机飞行员能够获得最新的远程打击目标信息。 这一进展显著增强了战场态势感知和打击精度，可能改变现代战争的平衡。它展示了整合卫星与无人机技术以获取军事优势的重要性日益增长，影响全球防御战略。 一年前，卫星图像需要数天才能到达前线部队，而现在支援团队可以为无人机飞行员提供最新数据。该系统利用实时 C2 数据融合平台，将卫星图像、声学特征和无人机视频源整合到统一的作战画面中。

rss · The New York Times World · 8月17日 20:38

**背景**: 在现代战争中，无人机用于侦察、目标指示和打击。卫星图像提供广泛的态势感知，但数据传输延迟历来限制其战术效用。卫星技术和数据融合的进步现在实现了近实时更新，使无人机能够根据最新情报采取行动。这种整合是使用 AI 和机器学习更快处理和传播战场数据的更广泛趋势的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/08/17/world/europe/from-the-sky-to-the-battlefield.html">How Ukraine’s Satellites Help Drive Its War Drones</a></li>
<li><a href="https://blog.roninsgrips.com/sitrep-military-drones-august-8-2026-to-august-15-2026/">SITREP Military Drones - August 8, 2026 to August 15... - Ronin's Grips</a></li>

</ul>
</details>

**标签**: `#defense`, `#satellites`, `#drones`, `#military technology`, `#real-time data`

---

<a id="item-14"></a>
## [中国欲出口数据以影响全球 AI 聊天机器人](https://www.nytimes.com/2026/08/17/world/asia/china-ai-data-chatbots.html) ⭐️ 7.0/10

中国正在扩大其 AI 影响力，不仅出口模型，还出口数据，旨在塑造全球聊天机器人的叙事。此举引发担忧，即北京的观点可能通过广泛使用的 AI 系统传播。 这一发展意义重大，因为它可能为中国在全球 AI 生态系统中提供软实力杠杆，潜在地影响数十亿用户对地缘政治问题的看法。这也凸显了数据主权的重要性以及 AI 训练数据的地缘政治影响。 该新闻基于《纽约时报》2026 年 8 月的报道，指出中国的战略包括出口数据以影响聊天机器人。与此同时，关于中国 AI 出口管制的讨论也在进行，这些管制可能限制海外获取先进 AI 模型、数据和算法。

rss · The New York Times World · 8月17日 11:10

**背景**: AI 聊天机器人基于大型数据集进行训练，这些数据塑造了它们的回应和潜在偏见。各国和公司日益认识到，控制训练数据可以影响这些系统传播的叙事和观点。中国出口数据的举措是其更广泛战略的一部分，旨在全球扩展其技术和意识形态影响力，类似于美国和其他国家利用 AI 投射力量的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.explainx.ai/blog/china-overseas-ai-model-restrictions-reuters-july-2026">China AI Export Restrictions: Reuters Report Explained ...</a></li>
<li><a href="https://thesiliconreview.com/2026/07/china-ai-export-controls-strategy">China AI Export Controls Reshape AI Race | TSR</a></li>
<li><a href="https://www.techrepublic.com/article/news-apac-china-ai-model-export-controls/">China Considers Export Controls on AI Models, Data and Chips</a></li>

</ul>
</details>

**标签**: `#AI`, `#China`, `#data`, `#geopolitics`, `#policy`

---

<a id="item-15"></a>
## [Higgsfield 完成 4 亿美元 B 轮融资，估值翻两番达 54 亿美元](https://techcrunch.com/2026/08/17/higgsfield-raises-400m-series-b-quadrupling-its-valuation-in-8-months-to-5-4b/) ⭐️ 7.0/10

由前 Snap 高管 Alex Mashrabov 创立的 AI 图像和视频创作初创公司 Higgsfield 完成了 4 亿美元的 B 轮融资，在短短八个月内估值翻了两番，达到 54 亿美元。 这轮重大融资凸显了投资者对 AI 内容创作工具的浓厚兴趣，使 Higgsfield 成为快速增长的生成式媒体市场中的主要参与者。估值的飙升反映了竞争格局以及 AI 驱动创造力颠覆传统内容生产的潜力。 该公司由前 Snap 高管 Alex Mashrabov 创立，专注于让用户创建 AI 生成的图像和视频。这轮融资发生在 2026 年 8 月，估值在八个月内从约 13.5 亿美元增至 54 亿美元，表明其快速增长和市场信心。

rss · TechCrunch · 8月17日 19:04

**背景**: AI 内容创作工具已获得显著关注，像 Higgsfield 这样的初创公司利用生成模型，让用户无需传统技能即可制作媒体内容。该公司估值的快速增长反映了 AI 投资的更广泛趋势，投资者正在押注下一个创意表达的大平台。

**标签**: `#AI`, `#funding`, `#startup`, `#valuation`

---

<a id="item-16"></a>
## [亚马逊销毁稀有书籍训练 AI 引发伦理担忧](https://techcrunch.com/2026/08/17/amazon-once-an-online-bookseller-is-destroying-rare-books-to-train-ai-models/) ⭐️ 7.0/10

据 404 Media 调查，亚马逊据称购买稀有书籍，切掉书脊进行扫描以用于 AI 训练，甚至对极其稀有的书籍也在数字化后销毁实体副本。 这凸显了 AI 发展中的一个重大伦理困境：在推进 AI 能力与保护文化遗产之间的权衡。它影响作者、收藏家和更广泛的文学界，并对当前数据获取方式的可持续性和伦理提出质疑。 调查人员在稀有书籍中放置追踪设备，最终发现该书到达亚马逊设施。该做法包括购买书籍、切掉书脊以便高效扫描，然后丢弃实体副本，即使这些书是独一无二的。

rss · TechCrunch · 8月17日 16:38

**背景**: 大型语言模型（LLM）需要大量高质量文本数据进行训练。虽然许多数据来自网络抓取，但稀有书籍包含网上无法获得的独特内容，因此对提升模型性能很有价值。然而，数字化这些书籍往往涉及销毁实体副本，引发对文化遗产损失的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/17/amazon-once-an-online-bookseller-is-destroying-rare-books-to-train-ai-models/">Amazon, which started off selling books, is destroying rare ...</a></li>
<li><a href="https://www.theliteraturetimes.com/millions-of-books-are-being-destroyed-to-train-ai-rare-titles-could-be-lost-forever/">Millions of Books Are Being Destroyed to Train AI. Rare ...</a></li>
<li><a href="https://futurism.com/artificial-intelligence/ai-companies-destroying-rare-books">AI Companies Are Buying Antique Books, Ingesting Their ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#ethics`, `#Amazon`, `#training data`, `#rare books`

---

<a id="item-17"></a>
## [中国移动离岸 95 公里开通 5G 基站创全国纪录](https://www.chinanews.com.cn/dwq/2026/08-18/10679391.shtml) ⭐️ 6.0/10

中国移动在离岸 95 公里的阳江三山岛换流站开通了 5G 基站，刷新了全国离岸最远海上通信基站的纪录。该消息于 2026 年 8 月 18 日公布。 这一成就证明了将可靠 5G 覆盖扩展到偏远海上基础设施的可行性，这对于深海风电场的运维以及可再生能源并网至关重要。同时，它也凸显了中国在推动绿色发展过程中，电信与能源行业之间日益增强的协同效应。 该换流站是阳江三山岛海上风电柔直输电工程的一部分，这是中国首个海陆一体柔性直流输电工程。5G 基站将为换流站提供实时监控、远程控制和数据传输支持，该工程预计每年向粤港澳大湾区输送约 60 亿千瓦时的清洁电能。

rss · China News Service Scroll · 8月18日 01:33

**背景**: 阳江三山岛换流站被称为“海上电力心脏”，是中国首个海陆一体柔性直流输电工程的核心枢纽。它汇集深远海风电场的电能并输送至陆地。该项目于 2025 年 4 月开工，计划 2026 年 10 月投产，包括±500 千伏海上换流站、115 公里海底直流电缆和 178 公里陆上输电线路。5G 基站将为换流站的自动化运行提供先进的通信能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sohu.com/a/1047933403_121948416">千亿产业链！“海上电力心脏”，破解世界级难题→_工程_换流站_三山岛</a></li>
<li><a href="https://baike.baidu.com/item/阳江三山岛海上风电柔直输电工程/65568421">阳江三山岛海上风电柔直输电工程_百度百科</a></li>
<li><a href="https://cpnn.com.cn/news/hy/202607/t20260708_1900494.html">我国首个海陆一体“超级心脏”启运阳江--中国能源新闻网</a></li>

</ul>
</details>

**标签**: `#5G`, `#offshore communication`, `#infrastructure`, `#China`, `#renewable energy`

---

<a id="item-18"></a>
## [全球航运成本飙升至历史新高，工厂面临停工威胁](https://www.chinanews.com.cn/cj/2026/08-18/10679389.shtml) ⭐️ 6.0/10

据全球能源和大宗商品价格评估机构 Argus 的数据，过去一个月，巴拿马运河、莱茵河、红海和黑海等关键航线的运费创下历史新高。这一飙升是由持续的地缘政治冲突以及欧洲和拉丁美洲长期干旱导致的水位下降和航行中断共同推动的。 此次运费飙升凸显了全球供应链的脆弱性，可能导致全球工厂因生产成本飙升而停工。它强调了地缘政治不稳定和气候变化对国际贸易的叠加影响，波及全球企业和消费者。 创纪录的运费归因于多种因素：红海和黑海地区的地缘政治冲突，以及巴拿马运河和莱茵河因干旱导致的水位下降。这些情况迫使船只绕行或受到限制，降低了运力，推高了成本。

rss · China News Service Scroll · 8月18日 01:16

**背景**: 全球航运路线是国际贸易的生命线，巴拿马运河和苏伊士运河等关键咽喉要道承担着全球大量货物运输。地缘政治冲突，如红海船只遇袭，曾迫使船只绕行好望角，增加了运输时间和成本。同样，气候变化加剧的干旱导致巴拿马运河水位下降，促使当局限制船只通行。这些中断凸显了海上物流对人为和自然事件的脆弱性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Argus_Media">Argus Media - Wikipedia</a></li>
<li><a href="https://www.woodwellclimate.org/drought-panama-canal-7-graphics/">Drought , Climate, and the Panama Canal - Woodwell Climate</a></li>
<li><a href="https://epostglobalshipping.com/shipping-intelligence/intelligence/international-shipping-disruptions">Five years of international shipping disruptions exposed</a></li>

</ul>
</details>

**标签**: `#supply chain`, `#shipping`, `#geopolitics`, `#climate change`, `#economics`

---

<a id="item-19"></a>
## [中美 AI 竞赛：突破创新与低成本普及的对决](https://www.bbc.com/zhongwen/articles/cn5n9kqd5vvo/trad?at_medium=RSS&at_campaign=rss) ⭐️ 6.0/10

文章分析了中美 AI 竞赛，对比了美国追求技术突破与中国注重低成本普及的不同策略，并预测了三种可能的结果。 这一分析凸显了不同战略方法如何塑造全球 AI 格局并影响技术领导地位。理解这些动态对于政策制定者、企业和研究人员应对不断演变的 AI 生态系统至关重要。 文章指出，美国优先追求下一代技术突破，而中国则注重广泛且低成本的普及。文章还提到中国 2017 年《新一代人工智能发展规划》旨在 2030 年成为全球领导者，以及开源战略在强化工业主导地位中的作用。

rss · BBC Chinese · 8月18日 00:01

**背景**: 中美 AI 竞赛是一场涉及计算、模型、采用和部署的多维度竞争。美国在前沿研究和创新方面领先，而中国则利用其制造规模和开源方法实现快速迭代和低成本部署。这些对比鲜明的策略反映了两国之间更广泛的地缘政治和经济紧张关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.brookings.edu/articles/competing-ai-strategies-for-the-us-and-china/">Competing AI strategies for the US and China - Brookings</a></li>
<li><a href="https://www.cfr.org/articles/china-united-states-and-ai-race">China, the United States, and the AI Race | Council on ...</a></li>
<li><a href="https://www.uscc.gov/research/two-loops-how-chinas-open-ai-strategy-reinforces-its-industrial-dominance">Two Loops: How China ’s Open AI Strategy Reinforces Its Industrial...</a></li>

</ul>
</details>

**标签**: `#AI`, `#geopolitics`, `#US-China`, `#technology policy`

---

<a id="item-20"></a>
## [SHEIN 香港上市估值降至 250 亿美元，较 2021 年峰值缩水 75%](https://www.rfi.fr/cn/%E4%B8%AD%E5%9B%BD/20260817-shein%E9%A6%99%E6%B8%AF%E4%B8%8A%E5%B8%82%E4%BC%B0%E5%80%BC%E9%99%8D%E8%87%B3%E7%BA%A6250%E4%BA%BF%E7%BE%8E%E5%85%83-%E8%BE%83%E5%9B%9B%E5%B9%B4%E5%89%8D%E4%BC%B0%E5%80%BC%E5%A4%A7%E5%B9%85%E7%BC%A9%E6%B0%B4%E5%9B%9B%E5%88%86%E4%B9%8B%E4%B8%89) ⭐️ 6.0/10

SHEIN 最快本周在香港开始接受 IPO 认购，估值约为 250 亿美元，仅为四年前私募融资时 1000 亿美元估值的四分之一。 这一大幅估值缩水反映了跨境电子商务领域日益增加的监管压力和不断变化的市场环境，可能重塑投资者对该行业的预期。这也标志着这家全球最大的快时尚企业之一在更具挑战性的 IPO 环境中进行重大调整。 250 亿美元的估值较 2021 年 1000 亿美元的私募估值下降了 75%。报道显示，SHEIN 的利润下降了近 40%，并且在美国和欧洲失去了小额包裹免税政策，这些因素共同导致了估值下降。

rss · RFI Chinese · 8月17日 15:35

**背景**: SHEIN 是一家中国快时尚电商巨头，以超低价服装和数据驱动的供应链闻名。该公司此前曾寻求在美国上市，但因监管障碍和地缘政治紧张局势转而选择香港。小额免税政策允许低价值包裹免税入境，是 SHEIN 商业模式的关键优势，而该政策在主要市场的取消对其增长和盈利能力造成了压力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cxnetwork.com/cx-retail/news/shein-ipo-hits-another-hurdle-as-company-value-slides">Shein IPO hits another hurdle</a></li>
<li><a href="https://worldef.com/2026/07/17/shein-ipo-lower-valuation-eu-ecommerce/">Shein IPO Valuation Slips as Regulatory Pressure... - WORLDEF</a></li>
<li><a href="https://theopenletter.io/p/shein-ipo-valuation">Shein IPO Valuation Targets $40bn, Down From $98bn Peak</a></li>

</ul>
</details>

**标签**: `#SHEIN`, `#IPO`, `#e-commerce`, `#valuation`, `#business`

---

<a id="item-21"></a>
## [山西高校团队研发 100 余种铝镁合金产品](https://www.chinanews.com.cn/cj/2026/08-18/10679406.shtml) ⭐️ 5.0/10

中北大学材料科学与工程学院院长王强带领的团队研发出了 100 余种铝镁合金产品，可用于卫星、飞机、高铁和汽车。该消息于 2026 年 8 月 17 日在太原宣布。 这一进展可能减少中国对国外高端材料的依赖，因为中国是铝镁生产和消费大国，但部分高端产品仍依赖进口。这可能加强国内供应链，并促进山西地区的制造业发展。 该团队已研发出 100 余种合金产品，但简报中未披露具体的合金成分、性能指标或应用细节。声明强调部分高端材料和产品仍“受制于人”，表明该领域仍面临挑战。

rss · China News Service Scroll · 8月18日 01:40

**背景**: 铝镁合金是轻质结构材料，结合了镁的低密度（约 1.8 g/cm³）和铝的强化效果，具有高比强度。它们广泛应用于航空航天、汽车和轨道交通行业，以减轻重量并提高燃油效率。中国是铝镁生产大国，但由于加工复杂和质量控制要求高，高端合金制造仍面临挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2213956723002281">Applications of magnesium alloys for aerospace: A review</a></li>
<li><a href="https://eureka.patsnap.com/materials/mg-al-alloy-aerospace">Magnesium Aluminium Alloy Aerospace Material: Comprehensive ...</a></li>

</ul>
</details>

**标签**: `#materials science`, `#aluminum-magnesium alloys`, `#China`, `#manufacturing`, `#research`

---

<a id="item-22"></a>
## [全球粮食安全初见成效，零饥饿目标仍遥远](https://www.chinanews.com.cn/gj/2026/08-18/10679386.shtml) ⭐️ 4.0/10

2026 年《世界粮食安全和营养状况》报告显示，全球粮食安全治理取得初步进展，但到 2030 年实现联合国“零饥饿”目标依然十分艰难。 该报告为全球抗击饥饿的努力提供了重要基准，影响各国政府和国际组织的政策决策与资源分配。实现“零饥饿”目标的持续困难凸显了加强行动和创新粮食体系的必要性。 该报告可能包含关于营养不足、粮食不安全以及可持续发展目标 2（零饥饿）进展的最新统计数据。它还可能强调区域差异，以及冲突、气候变化和经济衰退对粮食安全的影响。

rss · China News Service Scroll · 8月18日 01:44

**背景**: 《世界粮食安全和营养状况》是由联合国粮农组织、国际农业发展基金、联合国儿童基金会、世界粮食计划署和世界卫生组织等机构联合发布的年度报告。它跟踪全球饥饿和营养不良状况，提供数据和分析以指导政策。零饥饿目标是联合国 2030 年可持续发展议程的一部分。

**标签**: `#food security`, `#global issues`, `#UN report`

---

<a id="item-23"></a>
## [7 月工业增加值增长 4.5%，集成电路大幅增长](https://www.chinanews.com.cn/cj/2026/08-18/10679410.shtml) ⭐️ 4.0/10

7 月份，全国规模以上工业增加值同比增长 4.5%，高技术制造业和数字产品制造业增长亮眼。集成电路实现了三位数增长，但摘要中未给出具体数字。 该数据凸显了新动能，尤其是半导体和高技术产业对中国工业经济的贡献不断增强。这表明经济持续向先进制造业转型，对经济结构升级和技术自主具有重要意义。 国家统计局 8 月 17 日发布的报告涵盖年营业收入 2000 万元以上的工业企业。4.5%的同比增长是 7 月份的数据，其中装备制造业、高技术制造业和数字产品制造业是主要增长点。

rss · China News Service Scroll · 8月18日 01:38

**背景**: 规模以上工业增加值是监测工业经济短期运行的核心指标，反映年营业收入 2000 万元以上的工业企业的新增价值。高技术制造业包括医药、航空航天、电子等行业，而数字产品制造业涵盖计算机、通信和其他电子设备制造等，是数字经济核心产业的重要组成部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/规模以上工业增加值/2775757">规模以上工业增加值_百度百科</a></li>
<li><a href="https://baike.baidu.com/item/高技术制造业/60192049">高技术制造业_百度百科</a></li>
<li><a href="https://baike.baidu.com/item/数字产品制造业/62893619">数字产品制造业_百度百科</a></li>

</ul>
</details>

**标签**: `#China`, `#industrial data`, `#integrated circuits`, `#semiconductors`, `#economics`

---

<a id="item-24"></a>
## [蒙古国前总理：中国经济从基建转向数智动力](https://www.chinanews.com.cn/gj/2026/08-18/10679395.shtml) ⭐️ 4.0/10

2026 年 8 月 17 日，蒙古国前总理林钦尼亚木·阿玛尔扎尔嘎勒在《中国日报》撰文称，中国经济增长动力正从传统基础设施投资转向数智新动力，并将通过扩大国际科技合作推动新一轮经济发展。 这一评论反映了国际社会对中国经济转型的广泛认可，对国际观察者和政策制定者具有重要意义。它凸显了从实体基础设施向数字和智能技术的转变，这一趋势可能重塑全球经济伙伴关系和技术合作。 该文章于 2026 年 8 月 17 日发表在《中国日报》上，作者为蒙古国前总理林钦尼亚木·阿玛尔扎尔嘎勒。文章强调了国际科技合作在推动中国下一阶段经济增长中的作用，但未提供具体政策细节。

rss · China News Service Scroll · 8月18日 01:32

**背景**: 中国经济长期以来由大规模基础设施投资驱动，如公路、铁路和港口。近年来，政府推动“数智化”转型，整合人工智能、大数据和云计算以提升生产力和创新。这一转变是实现高质量发展、减少对传统建设项目依赖的更广泛努力的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://theory.people.com.cn/n1/2025/1023/c40531-40587470.html">加快推动经济社会数智化转型--理论-中国共产党新闻网</a></li>
<li><a href="https://www.qstheory.cn/20251023/725c39f6afb746888087fec917790b07/c.html">加快推动经济社会数智化转型 - 求是网</a></li>
<li><a href="http://theory.people.com.cn/n1/2025/1222/c40531-40629075.html">全面推进数智化是促进实体经济发展的关键举措--理论-中国共产党新闻网</a></li>

</ul>
</details>

**标签**: `#China economy`, `#digital transformation`, `#economic policy`

---

<a id="item-25"></a>
## [田湾核电 7 号机组完成装料，进入带核调试阶段](https://www.chinanews.com.cn/cj/2026/08-18/10679394.shtml) ⭐️ 4.0/10

这一里程碑使中国首台 VVER-1200 机组更接近商业运行，有助于提升国家核电装机容量和实现碳减排目标。同时，它也展示了中俄核能合作的进展，以及全球最大核电基地（按装机容量计）的扩建。 装料工作于 8 月 12 日开始，至 18 日结束，包括燃料组件转运、装载入堆和正确性核查三个阶段。装载过程采用全自动远程控制系统，该机组计划于 2026 年投入商业运行。

rss · China News Service Scroll · 8月18日 01:19

**背景**: VVER-1200 是俄罗斯设计的第三代压水堆，装机容量 126.5 万千瓦，设计寿命 60 年。装料是核电站建设中的关键里程碑，标志着转入带核运行阶段。装料后，反应堆将经历临界、并网和商业运行等阶段。田湾核电站规划建设 8 台机组，其中 1-6 号机组已投运，7、8 号机组在建。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VVER">VVER - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Criticality_(status)">Criticality (status) - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S245230381730095X">New generation first-of-the kind unit – VVER-1200 design ...</a></li>

</ul>
</details>

**标签**: `#nuclear energy`, `#China`, `#infrastructure`, `#energy`

---

<a id="item-26"></a>
## [中国警方公布 14 起涉企网络谣言典型案例](https://www.chinanews.com.cn/gn/2026/08-18/10679374.shtml) ⭐️ 4.0/10

2026 年 8 月 18 日，中国公安部网络安全保卫局公布了 14 起涉企网络谣言典型案例，作为“净网 2026”专项行动的一部分。这些案件涉及个人编造虚假信息，包括利用人工智能生成的假车祸视频，以诋毁企业。 这一公告凸显了中国政府加大对损害企业声誉的网络谣言的打击力度，反映了更广泛的监管推动以维护清朗网络空间。它向企业和个人发出信号，传播涉企虚假信息将面临法律后果，可能影响网络言论和企业传播。 这 14 起案例通过公安部网安局微信公众号发布，所有涉案者均为男性，年龄在 26 岁至 44 岁之间。具体案例包括内蒙古呼和浩特一名男子在抖音上编造谣言以博取关注和吸粉引流，以及其他涉及 AI 生成假车祸视频的案件。

rss · China News Service Scroll · 8月18日 00:05

**背景**: “净网 2026”专项行动是中国公安机关打击网络违法犯罪的一项特别行动，重点打击网络谣言。该行动持续进行，全国各地公安部门针对各类谣言相关违法行为采取行动，包括涉企谣言。公布典型案例既是对潜在违法者的警示，也展示了政府保护企业在数字空间合法权益的决心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mps.gov.cn/n2254098/n4904352/c10582774/content.html">公安部网安局公布14起涉企网络谣言典型案例-公安部网站</a></li>
<li><a href="https://www.zaobao.com.sg/news/china/story20260818-9534392">中国警方公布涉企网络谣言典型案例 包含编造智驾事故 | 联合早报</a></li>
<li><a href="https://www.news.cn/legal/20260818/0d1c2235eec64168b8b88f5e345d39da/c.html">公安部网安局公布14起涉企网络谣言典型案例-新华网</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#law enforcement`, `#online rumors`, `#China`

---

<a id="item-27"></a>
## [银发私教：为老年人打造客厅健身房](https://www.chinanews.com.cn/sh/2026/08-18/10679371.shtml) ⭐️ 4.0/10

北京一位 95 后教练李轩为老年客户提供上门健身服务，并根据现场情况灵活调整训练方案——当 77 岁的客户刘士让表示腰部不适时，他将原定的下肢力量平衡练习改为腰部拉伸和放松训练。 这一趋势凸显了老龄化人口对个性化、上门健身服务日益增长的需求，这有助于改善老年人的身体健康和生活质量，同时为年轻教练创造新的就业机会。它也反映了社会向居家照护和预防性健康的转变。 教练携带便携式血压仪、弹力带和波速球等设备。客户刘士让 77 岁，长期服用肿瘤药物，但看起来精神矍铄；教练的快速调整体现了老年健身中灵活性和健康监测的重要性。

rss · China News Service Scroll · 8月17日 23:56

**背景**: 随着中国人口老龄化，许多老年人面临慢性疾病和行动不便的问题，传统健身房对他们来说不太方便。上门私教提供了一种便捷、安全的选择，使教练能够根据个人健康状况定制锻炼方案。使用波速球和弹力带等工具有助于在不需重型设备的情况下改善平衡和力量。

**标签**: `#elderly fitness`, `#personal training`, `#health`, `#aging`, `#home care`

---

<a id="item-28"></a>
## [广东高院出台 15 条举措护航绿色低碳发展](https://www.chinanews.com.cn/gn/2026/08-17/10679322.shtml) ⭐️ 4.0/10

2026 年 8 月 17 日，广东省高级人民法院发布《关于司法服务保障绿色低碳发展的工作意见》，围绕理念引领、审判履职、产业护航、机制建设四个维度推出 15 条举措，将生态环境法典精神融入司法实践。 此举标志着司法服务与中国绿色低碳转型目标对齐的重要一步，可能为其他省份树立先例。它有望加强对环境案件的法律保护，并支持广东乃至更广泛地区的可持续经济发展。 15 条举措分为理念引领、审判履职、产业护航、机制建设四个维度。意见强调将生态环境法典精神融入司法实践，旨在为经济社会发展全面绿色转型提供全链条司法保障。

rss · China News Service China · 8月17日 13:53

**背景**: 中国一直在推进“双碳”目标（2030 年前碳达峰、2060 年前碳中和），促使法律体系相应调整。生态环境法典作为综合性法律框架，正被融入司法实践以加强环境保护。广东作为经济大省，正积极采取措施使其司法体系与国家绿色发展政策保持一致。

**标签**: `#policy`, `#environment`, `#law`, `#green development`

---