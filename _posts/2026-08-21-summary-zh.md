---
layout: default
title: "Horizon Summary: 2026-08-21 (ZH)"
date: 2026-08-21
lang: zh
---

> 从 349 条内容中筛选出 28 条重要资讯。

---

1. [恶意 Rust crate arrayref 在构建时执行载荷](#item-1) ⭐️ 9.0/10
2. [中国 40 天内实现首次陆地火箭回收](#item-2) ⭐️ 8.0/10
3. [Waymo 首次公开自研 5nm ASIC 芯片，用于 Robotaxi 计算](#item-3) ⭐️ 8.0/10
4. [我国科学家合成微米级单原子金属线](#item-4) ⭐️ 8.0/10
5. [中国团队发现毛细血管是心脏修复关键，而非已有动脉](#item-5) ⭐️ 8.0/10
6. [特斯拉 Robotaxi 在奥斯汀实现完全无监督运行](#item-6) ⭐️ 8.0/10
7. [内华达州批准特斯拉、优步、Waymo 机器人出租车许可](#item-7) ⭐️ 8.0/10
8. [智谱发布 GLM 5.3 引发 API 抢购，展现中国 AI 竞赛中的崛起](#item-8) ⭐️ 7.0/10
9. [中科第五纪融资超 10 亿元，加速全球化布局](#item-9) ⭐️ 7.0/10
10. [机器人竞争焦点从硬件转向 AI 模型与数据](#item-10) ⭐️ 7.0/10
11. [微软将于 2026 年 9 月更新中彻底移除 Windows 11 的 WMIC](#item-11) ⭐️ 7.0/10
12. [英伟达年底前向中国出货专用 AI 芯片](#item-12) ⭐️ 7.0/10
13. [《麻省理工科技评论》称 AI 意识辩论是种干扰](#item-13) ⭐️ 7.0/10
14. [地质氢：清洁能源的下一个前沿](#item-14) ⭐️ 7.0/10
15. [中国为 AI 陪伴服务划定安全边界](#item-15) ⭐️ 6.0/10
16. [中船七〇四所台风中测试新型旋筒风帆](#item-16) ⭐️ 6.0/10
17. [恒大创始人许家印被判终身监禁](#item-17) ⭐️ 6.0/10
18. [专家撤回对第四频道 ADHD 纪录片的支持，称其存在偏见](#item-18) ⭐️ 6.0/10
19. [AI 数据标注为印度城市卡鲁尔创造就业机会](#item-19) ⭐️ 6.0/10
20. [印度工人佩戴摄像头为 AI 采集数据](#item-20) ⭐️ 6.0/10
21. [中国第 16 次北冰洋考察部署无人冰站与浮标组网](#item-21) ⭐️ 5.0/10
22. [上海将在“十五五”期间推动数智赋能教育变革](#item-22) ⭐️ 5.0/10
23. [中国交付新一代深水多功能工程船“海洋石油 292”](#item-23) ⭐️ 4.0/10
24. [广州知识产权法院 2025 年先行调解成功超三千件](#item-24) ⭐️ 4.0/10
25. [中法青年向湖南芷江捐赠解密二战档案](#item-25) ⭐️ 4.0/10
26. [中国“十五五”医保规划回应民生关切](#item-26) ⭐️ 4.0/10
27. [第四届广东建筑业高质量发展大会在广州开幕](#item-27) ⭐️ 3.0/10
28. [中国军事纪录片《制胜》展示新武器](#item-28) ⭐️ 3.0/10

---

<a id="item-1"></a>
## [恶意 Rust crate arrayref 在构建时执行载荷](https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/) ⭐️ 9.0/10

流行的 Rust crate 'arrayref' 的一个恶意版本被发布到 crates.io，在编译期间执行构建时载荷，下载并运行远程恶意软件。Rust 团队已移除恶意版本并发布安全公告。 此事件凸显了 Rust 生态系统对供应链攻击的脆弱性，尤其是通过构建脚本进行的攻击。它影响了数千个依赖 arrayref 的项目，可能危及 CI/CD 管道并泄露机密。 攻击涉及被入侵的维护者账户，并使用 proc-macro1 构建脚本下载并执行跨平台载荷。恶意版本在约两小时后被移除，事件还影响了 'internment' 和 'append-only-vec' 这两个 crate。

hackernews · abhisek · 8月20日 13:23 · [社区讨论](https://news.ycombinator.com/item?id=49374269)

**背景**: Rust crate 通常包含在编译期间运行的构建脚本（build.rs），这些脚本可能被滥用来执行任意代码。针对 crates.io 等包注册表的供应链攻击日益受到关注，正如 JavaScript 生态系统中类似事件所示。Rust 团队一直在努力对构建脚本进行沙箱化以降低此类风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/08/rust-supply-chain-attack-puts-build.html">Rust Supply Chain Attack Puts Build-Time Malware in Crates with 245 Million Downloads</a></li>
<li><a href="https://socket.dev/blog/popular-rust-crates-compromised">Popular Rust Crates Compromised in Build-Time Supply Chain Attack - Socket</a></li>
<li><a href="https://www.stepsecurity.io/blog/arrayref-rust-crate-supply-chain-attack">Rust Supply-Chain Attack: arrayref, internment, and append-only-vec Poisoned by the proc-macro1 Build-Time Dropper - StepSecurity</a></li>

</ul>
</details>

**社区讨论**: 社区评论对 crates.io 的事件响应表示不满，指出缺乏明确的 yank 指示和安全公告。一些人呼吁对构建脚本进行更好的沙箱化，并采取“内置电池”的方法来减少依赖数量，而另一些人则强调 AI 辅助攻击维护者的更广泛风险。

**标签**: `#security`, `#supply-chain`, `#rust`, `#malware`, `#crates.io`

---

<a id="item-2"></a>
## [中国 40 天内实现首次陆地火箭回收](https://www.chinanews.com.cn/gn/2026/08-21/10681409.shtml) ⭐️ 8.0/10

中国在海上回收成功仅 40 天后，实现了首次陆地火箭回收。这标志着该国可重复使用火箭技术发展的重要里程碑。 这一快速进展表明中国在可重复使用火箭技术方面的能力正在加速提升，可能大幅降低发射成本，并增强其在全球航天产业中的竞争力。这也使中国成为低成本进入太空竞赛中的关键参与者。 此次陆地回收是在长征十号乙火箭助推器实现开创性海上回收（采用网捕技术）之后进行的。陆地回收可能采用了类似的回收机制，但具体技术细节尚未完全公开。

rss · China News Service China · 8月21日 00:37

**背景**: 火箭回收是可重复使用运载火箭的关键技术，使火箭在发射后能够重复使用，从而降低成本。中国一直在开发多种回收方式，包括海上平台和陆地着陆，类似于 SpaceX 的猎鹰 9 号。2026 年 7 月长征十号乙的海上回收因其网捕技术而引人注目，这与 SpaceX 使用的推进着陆方式不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ourchinastory.com/en/17154/How-are-rockets-recovered?-China-pioneers-">How are rockets recovered ? China pioneers... | Our China Story</a></li>
<li><a href="https://tacticsinstitute.com/analysis/china-tests-sea-based-reusable-rocket/">China Tests Sea - Based Reusable Rocket</a></li>

</ul>
</details>

**标签**: `#aerospace`, `#rocket recovery`, `#China`, `#space technology`, `#reusable rockets`

---

<a id="item-3"></a>
## [Waymo 首次公开自研 5nm ASIC 芯片，用于 Robotaxi 计算](https://www.ithome.com/0/992/451.htm) ⭐️ 8.0/10

Waymo 首次公开了其自动驾驶计算系统的细节，其中包括一颗定制的 5nm ASIC 芯片。该芯片提供超过 1000 TOPS 的机器学习算力，且系统原始计算性能在过去八年中提升了 20 倍。 这一披露凸显了 Waymo 在硬件上走向垂直整合的趋势，减少了对英伟达和 AMD 等公司现成组件的依赖。这强调了定制芯片在自动驾驶领域日益增长的重要性，可能影响行业趋势和竞争格局。 这款 5nm ASIC 是专为实时处理、传感器数据融合和高级神经网络设计的专用机器学习引擎。它能即时从激光雷达、雷达和摄像头的原始数据流中提取关键信息，为传感器融合模型提供推理引擎素材。该系统还配备双计算引擎实现并行冗余，并采用超低延迟软件栈。

rss · ITHome Feed · 8月21日 01:41

**背景**: 自动驾驶汽车依赖高性能计算来实时处理海量传感器数据。TOPS（每秒万亿次操作）是衡量 AI 加速器性能的常用指标。Waymo 的定制 ASIC 采用台积电 5nm 工艺制造，是科技公司为特定工作负载设计专用芯片、减少对通用处理器依赖这一更广泛趋势的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/transportation/982653/waymo-brain-computer-chip-robotaxi-hardware-suppliers">Waymo lifts the lid on the ‘brain’ powering its robotaxis | The Verge</a></li>
<li><a href="https://blockonomi.com/alphabets-googl-waymo-debuts-custom-chip-and-ojai-robotaxi-fleet/">Alphabet's (GOOGL) Waymo Debuts Custom Chip and Ojai Robotaxi Fleet - Blockonomi</a></li>
<li><a href="https://seekingalpha.com/news/4635507-waymo-built-a-data-center-on-wheels-to-power-its-driverless-cars">Waymo built a 'data center on wheels' to power its driverless cars (WAYMO:Private) | Seeking Alpha</a></li>

</ul>
</details>

**标签**: `#自动驾驶`, `#ASIC`, `#Waymo`, `#芯片设计`, `#机器学习`

---

<a id="item-4"></a>
## [我国科学家合成微米级单原子金属线](https://www.ithome.com/0/992/448.htm) ⭐️ 8.0/10

我国科学家首次将单原子直径的“金属线”的合成长度突破微米级。该研究由北京高压科学研究中心李阔团队领导，成果发表于《科学》期刊。 这一突破有望为下一代纳米电路和柔性穿戴电子器件提供全新材料选项，为我国新型低维功能材料的研发开辟新路径。 团队采用高压固相拓扑聚合新策略，以β-酞菁铜晶体为原料，制备出碳包裹的铜单原子链，单根长度突破 1 微米，可连续串联 4000 个以上铜原子，比过去样品链长提升两个数量级以上。该方法还可推广至钴、镍、锌等多种金属。

rss · ITHome Feed · 8月21日 01:28

**背景**: 单原子金属线是理论上最细的一维金属结构，是研究低维物理的理想对象。以往制备方法要么需要超高真空条件且易损毁，要么链长有限，难以兼顾稳定性与批量制备。新方法利用高压压缩分子间距，触发拓扑聚合，形成碳质保护鞘，解决了这一难题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pubs.cstam.org.cn/article/doi/10.11858/gywlxb.20230749">高压固相拓扑聚合合成纳米碳材料</a></li>
<li><a href="https://www.emtscience.com/jiayabengzhan">emtscience.com/jiayabengzhan</a></li>
<li><a href="http://school.freekaoyan.com/bj/iphy/2021/12-29/16407863441510437.shtml">基于 巴 黎 - 爱 丁 堡 压 机 的高 压 中子衍射技术 - 中科院物理研究所 - Free...</a></li>

</ul>
</details>

**标签**: `#materials science`, `#nanotechnology`, `#single-atom wire`, `#high-pressure synthesis`, `#scientific breakthrough`

---

<a id="item-5"></a>
## [中国团队发现毛细血管是心脏修复关键，而非已有动脉](https://www.ithome.com/0/992/418.htm) ⭐️ 8.0/10

中国科学院分子细胞科学卓越创新中心的研究团队发现，毛细血管而非已有动脉会转变为侧支动脉以修复心脏损伤。该成果于 8 月 21 日发表在《科学》杂志上。 这一发现挑战了侧支动脉来源于已有动脉的传统观点，为缺血性心脏病提供了新的机制和潜在治疗靶点。它可能催生增强心脏自我修复能力的新疗法，惠及全球数百万患者。 研究团队利用邻近细胞遗传学技术和双重组酶追踪系统，永久标记动脉内皮细胞并捕捉毛细血管向动脉的转变。他们发现 VEGFA 分子起关键作用；在受损小鼠心脏中短暂提高 VEGFA 水平可显著提升毛细血管向动脉的转化效率，减少心肌缺血面积并改善心功能。

rss · ITHome Feed · 8月20日 23:14

**背景**: 缺血性心脏病是由于冠状动脉堵塞导致心肌缺氧和营养不足。部分人群会形成侧支动脉以绕过堵塞区域，但其来源此前并不清楚。研究团队设计的“细胞接触历史记录仪”和高精度追踪系统使他们能够追踪这些新动脉的真正来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cemcs.cas.cn/kyjz/202211/t20221130_6557663.html">Science...</a></li>
<li><a href="https://m.thepaper.cn/newsDetail_forward_33819483">科学家解密心脏的天然“搭桥”，有望为心梗患者提供温和疗法</a></li>

</ul>
</details>

**标签**: `#cardiovascular research`, `#ischemic heart disease`, `#capillary-to-artery transformation`, `#Science publication`, `#VEGFA`

---

<a id="item-6"></a>
## [特斯拉 Robotaxi 在奥斯汀实现完全无监督运行](https://www.ithome.com/0/992/396.htm) ⭐️ 8.0/10

根据 Robotaxi Tracker 的数据，过去两周在奥斯汀监测到的 170 次特斯拉 Robotaxi 行程全部没有安全员，涉及 54 辆车。达拉斯和休斯敦也出现类似趋势，过去一周约有 30 辆无人驾驶特斯拉投入运营。 这标志着特斯拉 Robotaxi 服务的一个重要里程碑，表明完全无监督的自动驾驶在奥斯汀已成为现实。这可能加速自动驾驶网约车的普及，并对 Waymo 等竞争对手构成压力，同时也引发监管和安全方面的讨论。 无安全员车辆数量的增加部分归因于 Robotaxi Tracker 的数据修正，此前其指标存在滞后。特斯拉不公布详细车队数据，因此该追踪器成为少数能观察车队变化的渠道之一。目前服务主要使用 Model Y，而专门设计的 Cybercab 预计最快本月在奥斯汀推出。

rss · ITHome Feed · 8月20日 14:32

**背景**: 特斯拉在奥斯汀的 Robotaxi 服务始于 2025 年 6 月 22 日，最初为有安全员的监督运营。2026 年 1 月，埃隆·马斯克宣布取消车内安全员，而近期数据表明已完全过渡到无人驾驶。Robotaxi Tracker 依靠应用用户的众包数据和公开信息来监测车队。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://robotaxitracker.com/">Robotaxi Tracker - Tesla & Waymo Fleet Dashboard</a></li>
<li><a href="https://cryptobriefing.com/tesla-unsupervised-robotaxis-austin/">Tesla rolls out unsupervised robotaxis across entire Austin metro area</a></li>
<li><a href="https://www.lambham.com/post/tesla-launches-unsupervised-robotaxis-in-austin-without-safety-drivers/">Tesla Launches Unsupervised Robotaxis in Austin Without Safety...</a></li>

</ul>
</details>

**社区讨论**: Reddit 和 X 上的社区反馈与追踪器数据一致，用户报告在奥斯汀乘坐了无人驾驶车辆。一些人对进展表示兴奋，而另一些人则对安全性以及特斯拉缺乏官方数据表示担忧。

**标签**: `#Tesla`, `#Robotaxi`, `#autonomous driving`, `#AI`, `#transportation`

---

<a id="item-7"></a>
## [内华达州批准特斯拉、优步、Waymo 机器人出租车许可](https://techcrunch.com/2026/08/20/tesla-uber-and-waymo-all-get-the-ok-to-operate-thousands-of-robotaxis-in-nevada/) ⭐️ 8.0/10

内华达州已向特斯拉、优步和 Waymo 颁发许可，允许它们在接下来 12 个月内部署多达 8000 辆机器人出租车。这标志着大规模自动驾驶汽车运营获得重大监管批准。 这一批准是自动驾驶汽车商业化的重要一步，涉及主要参与者和大规模部署。它可能为其他州树立先例，并加速全国范围内机器人出租车的采用。 这些许可总共允许在未来一年内部署多达 8000 辆机器人出租车。内华达州是 2011 年首个将自动驾驶汽车合法化的州，拉斯维加斯仍是测试和部署的主要中心。

rss · TechCrunch · 8月21日 00:23

**背景**: 机器人出租车是一种提供按需交通服务的自动驾驶车辆，配备传感器、摄像头、雷达和激光雷达。内华达州一直是自动驾驶汽车监管的先驱，为自动驾驶车辆设计了带有无限符号的独特红色牌照。此次批准基于该州早期的合法化和持续的测试工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://builtin.com/articles/robotaxi">What Is a Robotaxi ? | Built In</a></li>
<li><a href="https://dmv.nv.gov/autonomous.htm">Nevada DMV - Autonomous Vehicles</a></li>
<li><a href="https://www.corenalaw.com/legal-procedures/nevada-self-driving-laws/">Nevada Autonomous Vehicle Laws 2026 | Corena Law</a></li>

</ul>
</details>

**标签**: `#autonomous vehicles`, `#robotaxis`, `#regulation`, `#Nevada`, `#transportation`

---

<a id="item-8"></a>
## [智谱发布 GLM 5.3 引发 API 抢购，展现中国 AI 竞赛中的崛起](https://36kr.com/p/3947451908357257?f=rss) ⭐️ 7.0/10

2026 年 8 月 14 日，智谱 AI 发布了新一代模型 GLM 5.3，在国产模型 Coding 测评中登顶，与 Kimi K3 并列开源第一，达到与 Claude Fable 5、GPT-5.6 Sol 等闭源旗舰模型同一水平。发布后引发客户抢购 API，甚至有客户提前锁定推理算力。 此次发布巩固了智谱作为中国领先 AI 公司的地位，展示了其在编程能力上与国际前沿竞争的实力。API 抢购表明市场需求强劲，可能加剧中国大模型领域的竞争，重塑“六小虎”之间的格局。 GLM 5.3 基于 743B 参数的基座模型，在 CyberGym 上获得 84.5 分，超过 Anthropic Mythos 5 和 GPT-5.6 Sol。该模型的 API 原定于 8 月 18 日上线，但被推迟，引发已分配预算和开发资源的客户不满。

rss · 36Kr Feed · 8月20日 07:12

**背景**: 智谱 AI 成立于 2019 年，脱胎于清华大学，最初专注于 B 端定制化模型部署。2025 年 5 月，面对 DeepSeek R1 的竞争，智谱做出战略转向，开发融合推理、编程和智能体能力的“三合一”模型，并于 2025 年 7 月发布 GLM 4.5，成为其首个在编程领域获得口碑的模型。这一转向源于用户对提升研发效率的需求，为后续 GLM 5、5.1、5.2 及现在的 5.3 奠定了基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GLM-5.3">GLM-5.3</a></li>
<li><a href="https://aihot.virxact.com/story/377f652d-2a7e-4376-bbf9-429cf111d5ed">智谱发布 GLM - 5 . 3 · AIHOT</a></li>
<li><a href="https://seo.whoops.com.tw/glm-5-3/">GLM - 5 . 3 是什麼？ 只靠後訓練衝高的 Z.ai... - Whoops SEO</a></li>

</ul>
</details>

**标签**: `#AI`, `#大模型`, `#智谱`, `#GLM`, `#开源模型`

---

<a id="item-9"></a>
## [中科第五纪融资超 10 亿元，加速全球化布局](https://36kr.com/p/3947288204770693?f=rss) ⭐️ 7.0/10

中国具身智能企业中科第五纪已完成 A1 轮和 A2 轮融资，总金额超过 10 亿元人民币。公司已获得数亿元海外订单，并计划在未来六个月内拓展欧洲、澳大利亚、新西兰、日本和韩国等海外市场。 这笔重大融资凸显了中国具身智能日益增长的商业可行性，以及向全球市场拓展的战略转变。它也强调了行业从硬件出口向软硬一体化解决方案的转变，可能重塑全球工业自动化格局。 该公司的 FAM 系列具身操作大模型采用独创的“热力图对齐”技术，保留三维空间结构，仅需 3 至 5 条示范即可学习新任务，基础任务成功率高达 97%，数据需求量仅为传统方法的 1%。其轮式机器人拥有 28 个自由度，已在物流、柔性制造和能源巡检等场景实现规模化落地。

rss · 36Kr Feed · 8月20日 03:10

**背景**: 具身智能是指通过身体（如机器人）与物理世界交互的人工智能系统。目前行业正在探索不同的技术路线，一些公司如 Figure 和 1X Technologies 遵循 Scaling Law，使用海量数据，而中科第五纪等公司则专注于数据效率和少样本学习。VLA（视觉-语言-动作）架构是常见方法，但在特征压缩过程中常丢失空间信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://juejin.cn/post/7486670839923359796">什么是 具 身 智 能 ？ 具 身 智 能 （Embodied Intelligence...</a></li>
<li><a href="https://damodev.csdn.net/694ff3e3bf6b0e4b285ed86d.html">VLA 架 构 细节分析（2025 年 11 月现状）_ 架 构 _jzwspace-DAMO...</a></li>
<li><a href="https://m.leiphone.com/category/ai/ABnmB3o4JHMsiCmW.html">独家｜北大董豪：「仅停留在数据层面的 Scaling Law ...</a></li>

</ul>
</details>

**标签**: `#embodied intelligence`, `#funding`, `#robotics`, `#AI`, `#China`

---

<a id="item-10"></a>
## [机器人竞争焦点从硬件转向 AI 模型与数据](https://36kr.com/newsflashes/3948570144914565?f=rss) ⭐️ 7.0/10

在 2026 世界机器人大会上，企业越来越多地展示具身智能模型、世界模型、数据采集和仿真训练等能力，而不仅仅是行走、抓取等硬件技能。这标志着机器人产业的竞争焦点从硬件性能转向“模型+数据”的综合能力。 这一转变表明，机器人创新的下一阶段将由 AI 和数据驱动，可能加速机器人在现实生产和日常生活中的部署。同时，它也凸显了科技公司和初创企业的新战场，数据采集和模型开发成为关键差异化因素。 文章指出，机器人不仅需要执行任务的能力，还需要对物理世界的理解能力，因此模型和数据正成为核心。会议上的具体例子包括世界模型和仿真训练的演示，但文章缺乏技术深度和具体产品名称。

rss · 36Kr Feed · 8月21日 01:03

**背景**: 具身智能是指通过身体与物理世界交互的 AI 系统，例如机器人。世界模型是能够预测环境未来状态的 AI 系统，使机器人能够规划行动。数据采集和仿真训练对于开发这些模型至关重要，因为真实世界的数据稀缺且获取成本高。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://juejin.cn/post/7486670839923359796">什 么 是 具 身 智 能 ？ 具 身 智 能 （Embodied Intelligence...</a></li>
<li><a href="https://matt33.com/2026/07/21/embodied-intelligence-overview/">具 身 智 能 （一）：物理世界中的 智 能 闭环 | Matt's Blog</a></li>
<li><a href="https://www.ofweek.com/ai/2025-07/ART-201717-8110-30666688.html">一文读懂：到底 什 么 是 “ 具 身 智 能 ” ？ - OFweek 人工 智 能 网</a></li>

</ul>
</details>

**标签**: `#robotics`, `#AI`, `#embodied intelligence`, `#industry trends`, `#data`

---

<a id="item-11"></a>
## [微软将于 2026 年 9 月更新中彻底移除 Windows 11 的 WMIC](https://www.ithome.com/0/992/453.htm) ⭐️ 7.0/10

微软将在 2026 年 9 月的累积更新中彻底移除 Windows 11 中的 WMIC（Windows Management Instrumentation Command-line）工具，此前已在预览版 26220.9202（25H2）和 28020.2731（26H1）中移除。用户在命令提示符中运行“wmic”将收到“命令无法识别”的错误，且无法通过“可选功能”或任何终端命令重新启用该工具。 这一变化影响了依赖 WMIC 进行脚本编写和系统管理工作的 Windows 管理员和安全专业人员。这反映了微软持续的安全推动，旨在减少攻击面，因为 WMIC 曾被攻击者滥用于侦察和恶意软件部署。 WMIC 自 Windows 10 21H1 起已被弃用，微软建议使用 PowerShell 作为替代。此次移除是 2026 年 9 月补丁星期二的一部分，在预览版中，该工具已从 Windows 搜索、系统分区和命令提示符中消失。

rss · ITHome Feed · 8月21日 01:45

**背景**: WMIC 是一个命令行工具，为 Windows Management Instrumentation（WMI）提供用户友好的界面，允许管理员通过脚本查询系统硬件、软件和配置。自 Windows XP 以来它一直是标准工具，但其强大的功能也使其成为攻击者的目标。出于安全原因，微软一直在逐步淘汰它，此次移除标志着最后一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmic">WMI command - line ( WMIC ) utility - Win32 apps | Microsoft Learn</a></li>
<li><a href="https://pureinfotech.com/windows-11-removes-wmic-command-line-tool/">Microsoft is killing WMIC after years of warnings, and some Windows ...</a></li>
<li><a href="https://support.microsoft.com/en-us/servicing/os/windows/docs/2025/09/windows-management-instrumentation-command-line-wmic-removal-from-windows">Windows Management Instrumentation Command-line ( WMIC )...</a></li>

</ul>
</details>

**标签**: `#Windows 11`, `#WMIC`, `#Security`, `#System Administration`

---

<a id="item-12"></a>
## [英伟达年底前向中国出货专用 AI 芯片](https://www.rfi.fr/cn/%E4%B8%AD%E5%9B%BD/20260820-%E8%8B%B1%E4%BC%9F%E8%BE%BE%E5%B9%B4%E5%BA%95%E5%89%8D%E5%87%BA%E8%B4%A7%E4%B8%AD%E5%9B%BD%E4%B8%93%E7%94%A8ai%E8%8A%AF%E7%89%87-%E4%BA%89%E5%A4%BA%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E5%BA%94%E7%94%A8%E5%B8%82%E5%9C%BA) ⭐️ 7.0/10

据《The Information》报道，英伟达计划在今年年底前开始向中国客户小批量供应一款专为中国市场设计的 AI 芯片。该报道援引两名英伟达员工的话，并指出该芯片旨在符合美国出口管制要求。 此举意义重大，因为它使英伟达能够在出口管制下继续在中国这个利润丰厚的人工智能市场保持存在。这也可能影响竞争格局，因为中国企业可能更倾向于英伟达的生态系统而非国产替代品。 这款新芯片预计将符合美国出口管制，限制 HBM 容量和 CoWoS 等先进封装技术。它可能是此前为中国市场开发的性能缩减版 H20 的继任者。

rss · RFI Chinese · 8月20日 21:30

**背景**: 美国对向中国出口先进 AI 芯片实施了管制，限制了英伟达最强大 GPU 的销售。作为回应，英伟达开发了针对中国的变体，如 H20，通过降低性能来满足监管要求。中国市场对英伟达仍然重要，但华为等国内竞争对手正在崛起。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/technology/exclusive-nvidia-offers-new-advanced-chip-china-that-meets-us-export-controls-2022-11-08/">reuters.com/technology/exclusive- nvidia -offers-new-advanced- chip ...</a></li>
<li><a href="https://wccftech.com/nvidia-is-plotting-its-china-comeback-via-a-new-lpu-based-inference-chip-as-smic-rides-us-export-controls-to-a-virtual-china-monopoly/">NVIDIA Is Plotting Its China Comeback Via A New LPU-Based...</a></li>
<li><a href="https://spoonai.me/posts/2026-07-13-china-nvidia-h200-purchase-approval-jul2026-en">China Will Let Its AI Giants Buy Nvidia H200s — With a Ton... | spoonai</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#AI chips`, `#China`, `#semiconductors`, `#export controls`

---

<a id="item-13"></a>
## [《麻省理工科技评论》称 AI 意识辩论是种干扰](https://www.technologyreview.com/2026/08/20/1142571/ai-consciousness-debate-trap/) ⭐️ 7.0/10

在 2026 年 8 月的一篇评论文章中，《麻省理工科技评论》认为，关于 AI 意识的辩论是一个陷阱，分散了人们对 AI 监管和伦理中更紧迫问题的注意力。作者批评了 Demis Hassabis、Dario Amodei 和 Sam Altman 等科技领袖所宣扬的“失控”AI 和“叛逆”智能体的言论。 这一观点挑战了 AI 系统接近意识且超人的主流叙事，这种叙事曾被用来为某些监管方式辩护。通过重新聚焦于具体危害和治理，这篇文章可能影响政策制定者和公众对 AI 风险的优先级排序。 文章特别点名了 Demis Hassabis、Dario Amodei 和 Sam Altman 等知名人物，他们推动对“超人”系统的监管。文章将这与由政策组织领导的另一派别进行对比，后者主张对 AI 的实际影响进行更接地气的讨论。

rss · MIT Technology Review · 8月20日 15:42

**背景**: AI 意识辩论常常将拟人化语言与机器实际感知混为一谈，导致投机性恐惧。科技领袖呼吁全球监管，例如 Hassabis 提议建立美国主导的 AI 监管机构，而其他人则认为关注意识会分散对偏见、失业和滥用等实际问题的注意力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.axios.com/2026/07/14/demis-hassabis-ai-regulation-google-deepmind">Exclusive: Google's Hassabis calls for U.S.-led global AI watchdog</a></li>
<li><a href="https://cryptobriefing.com/altman-ai-safety-bill-ted-cruz/">OpenAI CEO Sam Altman backs 'light-touch' AI safety bill after Senate....</a></li>
<li><a href="https://www.therundown.ai/p/dario-amodei-logs-on-to-answer-the-critics">Dario Amodei logs on to answer the critics</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#AI policy`, `#AI consciousness`, `#regulation`

---

<a id="item-14"></a>
## [地质氢：清洁能源的下一个前沿](https://www.technologyreview.com/2026/08/20/1142512/geologic-hydrogen-hunt/) ⭐️ 7.0/10

文章重点介绍了对天然地质氢的探索热潮，这是一种潜在的清洁燃料来源，并讨论了相关科学、挑战以及地下氢储量勘探日益增长的商业兴趣。 地质氢可为重型运输和钢铁制造等难以脱碳的行业提供低碳燃料替代品，并可能补充通过电解生产的绿氢。其发现和开采可能对清洁能源转型产生重大影响，并减少对化石燃料的依赖。 文章指出，氢可用于卡车、飞机和炼钢，燃烧时产生水。然而，文章未提供勘探方法或商业项目的具体技术细节，但搜索结果指出，地质氢通过水岩反应（如蛇纹石化）形成，并可采用类似于天然气勘探的技术进行勘探。

rss · MIT Technology Review · 8月20日 10:00

**背景**: 地质氢，也称为天然氢或白氢，是通过水岩反应（如蛇纹石化）和地核脱气等过程在地壳中自然产生的。它被认为是一种有前景的清洁能源，因为其燃烧只产生水，并且可以像天然气一样开采。然而，勘探仍处于早期阶段，在寻找可行矿藏和开发经济有效的开采方法方面存在挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gtk.fi/en/current/geology-in-the-hydrogen-era/">Geology in the Hydrogen Era | GTK</a></li>
<li><a href="https://www.blackridgeresearch.com/blog/geological-hydrogen-production-storage">All You Need to Know About Geologic Hydrogen</a></li>
<li><a href="https://deltahydrogeninc.com/natural-hydrogen">Natural Hydrogen | Explore Natural ... — Delta Hydrogen Inc.</a></li>

</ul>
</details>

**标签**: `#hydrogen`, `#clean energy`, `#geology`, `#climate tech`, `#energy storage`

---

<a id="item-15"></a>
## [中国为 AI 陪伴服务划定安全边界](https://www.chinanews.com.cn/sh/2026/08-21/10681433.shtml) ⭐️ 6.0/10

中国新规《人工智能拟人化互动服务管理暂行办法》于 2026 年 7 月 15 日起施行，为 AI 陪伴服务划定安全边界。该办法要求服务在公开发布前进行安全评估，并对可能产生不可接受风险的服务施加限制。 该法规意义重大，因为它直接针对日益增长的 AI 陪伴情感依赖问题，这些服务模拟恋人、朋友或逝去的亲人。它为中国 AI 治理树立了先例，在创新与用户保护之间取得平衡，并可能影响全球类似政策。 该办法明确禁止向未成年人提供虚拟伴侣等服务，并包含服务限制、身份识别和监护管控等条款。AI 陪伴服务在公开发布前必须进行安全评估，若监管机构认定其行为产生不可接受的风险，则可能面临限制。

rss · China News Service Scroll · 8月21日 01:28

**背景**: AI 陪伴服务在中国日益流行，通过模拟关系为用户提供情感支持。然而，情感依赖、隐私以及对未成年人的影响等问题引发担忧。新规是中国在 AI 发展中预防潜在问题的更广泛努力的一部分，体现了家长式的治理方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://www.legaldaily.com.cn/video/content/2026-04/13/content_9372340.html">《 人 工 智 能 拟 人 化 互 动 服 务 管 理 暂 行 办 法 》 7月15...</a></li>
<li><a href="https://m.mp.oeeee.com/a/BAAFRD0000202607151626500.html">今起施 行 ， 拟 人 不替代 人 ！ 创意海报带你读懂AI 拟 人 化 新规 | 南都N视频</a></li>
<li><a href="https://news.bjd.com.cn/2026/04/12/11683566.shtml">严禁向未成年 人 提供虚 拟 伴侣等 服 务 ，新规今年7月施 行 _京报网</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#AI companion`, `#policy`, `#China`

---

<a id="item-16"></a>
## [中船七〇四所台风中测试新型旋筒风帆](https://www.chinanews.com.cn/gn/2026/08-20/10681293.shtml) ⭐️ 6.0/10

在 2026 年第 13 号台风“白海豚”影响上海期间，中船七〇四所在长兴岛园区对新一代船用旋筒风帆成功进行了实景综合性能测试验证。 此次极端天气测试的成功验证了旋筒风帆的坚固性和可靠性，支持其在航运业中减少燃料消耗和排放的潜力。这标志着中国绿色海事技术和可再生能源应用向前迈进了一步。 测试利用台风窗口期，提供了实验室难以复制的极端风力条件。旋筒风帆旨在利用风能辅助船舶推进，从而提高能源效率。

rss · China News Service China · 8月20日 12:15

**背景**: 旋筒风帆，又称弗莱特纳转子，是垂直圆柱体，通过旋转在风中产生升力，推动船舶前进。它们作为减少航运温室气体排放的手段正受到关注。中船七〇四所隶属于中国船舶集团，专注于船舶设备研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.bjx.com.cn/topics/xuantongfengfan/">旋 筒 风 帆 -北极星电力新闻网</a></li>
<li><a href="http://www.csic.com.cn/n5/n18/c34052/content.html">集团新闻_ 中 国 船 舶集团有限公司</a></li>
<li><a href="https://www.workercn.cn/c/2026-05-06/8794687.shtml">探访全球第一｜给 船 舶装上“绿色翅膀” - 经济 - 中 工网</a></li>

</ul>
</details>

**标签**: `#marine engineering`, `#renewable energy`, `#rotor sail`, `#extreme weather testing`, `#China`

---

<a id="item-17"></a>
## [恒大创始人许家印被判终身监禁](https://www.rfi.fr/cn/%E4%B8%93%E6%A0%8F%E6%A3%80%E7%B4%A2/%E8%A6%81%E9%97%BB%E8%A7%A3%E8%AF%B4/20260820-%E4%BB%8E%E4%BA%9A%E6%B4%B2%E9%A6%96%E5%AF%8C%E5%88%B0%E7%BB%88%E8%BA%AB%E7%9B%91%E7%A6%81-%E6%81%92%E5%A4%A7%E8%AE%B8%E5%AE%B6%E5%8D%B0-%E4%BC%A0%E5%A5%87-%E8%90%BD%E5%B9%95) ⭐️ 6.0/10

2026 年 8 月 20 日，深圳法院判处恒大创始人许家印无期徒刑，并没收其全部个人财产。恒大集团及恒大地产合计被罚款 158.2 亿元人民币（超过 20 亿欧元）。 这一判决标志着全球负债最重的房地产开发商恒大倒闭进程中的一个里程碑，也象征着中国房地产行业更广泛的危机。它凸显了在市场动荡中高管面临的法律和经济后果。 67 岁的许家印于 4 月对八项指控认罪，包括伪造财务报表、虚增资产、隐瞒负债、欺诈性集资、贿赂和挪用资金等。法院还判处没收其全部个人财产，并对恒大集团处以总计 158.2 亿元的罚款。

rss · RFI Chinese · 8月20日 13:17

**背景**: 恒大曾是中国房地产繁荣的象征，积累了超过 3000 亿美元的债务，并于 2021 年违约，引发了中国经济长期危机。该公司于 2024 年 1 月被法院勒令清算，并从香港证券交易所退市。许家印曾于 2017 年被福布斯评为中国首富，净资产达 425 亿美元，如今面临终身监禁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/business-58985757">Evergrande $2.6bn property unit deal collapses</a></li>
<li><a href="https://www.linkedin.com/pulse/evergrande-anatomy-corporate-collapse-lessons-global-investors-prag-ohagc">Evergrande Collapse : Key Lessons for Investors</a></li>
<li><a href="https://bruinpoliticalreview.org/articles?post-slug=concrete-jungles-china-s-property-crisis">Concrete Jungles: China ’s Property Crisis | Bruin Political Review</a></li>

</ul>
</details>

**标签**: `#business`, `#legal`, `#real estate`, `#China`

---

<a id="item-18"></a>
## [专家撤回对第四频道 ADHD 纪录片的支持，称其存在偏见](https://www.theguardian.com/society/2026/aug/20/the-great-adhd-myth-channel-4-programme-contributor-expert-criticism) ⭐️ 6.0/10

伦敦国王学院认知神经科学教授 Katya Rubia 撤回了对第四频道纪录片《伟大的 ADHD 神话？》的支持，称该片存在偏见并歪曲了她的观点。她警告该节目可能鼓励家长让孩子停药，从而增加自杀风险。 这一争议凸显了媒体呈现对公众认知和医疗决策的重大影响，尤其是在心理健康治疗方面。误导性的描述可能阻碍循证医疗，危及弱势儿童，强调了健康报道中负责任新闻的重要性。 Rubia 是精神病学、心理学和神经科学研究所的教授，她的撤回是在其他权威人士提出批评之后。该纪录片被《卫报》称为“年度最具争议的节目”，争论焦点在于对 ADHD 药物及其风险的呈现。

rss · The Guardian World · 8月20日 17:54

**背景**: ADHD 是一种神经发育障碍，通常使用兴奋剂药物治疗，这些药物已被证明能减轻症状，并且根据一些研究，还能降低自杀企图的风险。然而，对副作用和过度诊断的担忧引发了公众辩论。认知神经科学研究大脑过程如何支撑心理功能，像 Rubia 这样的专家为这类讨论提供了科学背景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7292769/">Medication for Attention - Deficit / Hyperactivity Disorder and Risk for...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cognitive_neuroscience">Cognitive neuroscience</a></li>

</ul>
</details>

**标签**: `#ADHD`, `#media ethics`, `#mental health`, `#documentary`, `#controversy`

---

<a id="item-19"></a>
## [AI 数据标注为印度城市卡鲁尔创造就业机会](https://www.nytimes.com/2026/08/20/world/asia/ai-jobs-data-annotation-india-karur.html) ⭐️ 6.0/10

《纽约时报》的一篇文章报道称，印度卡鲁尔市的数据标注工作正在为训练 AI 系统的人类创造就业机会。这突显了印度小城市中与 AI 相关的就业实例。 这很重要，因为它表明 AI 发展可以创造本地就业机会，从而反驳了大规模失业的担忧。同时，它也强调了人类劳动在 AI 供应链中的重要性，尤其是在数据标注领域。 文章聚焦于印度南部城市卡鲁尔，那里的工人参与数据标注以提升 AI 性能。数据标注涉及对数据进行结构化处理，使机器能够理解，这对于训练机器学习模型至关重要。

rss · The New York Times World · 8月20日 12:03

**背景**: 数据标注是为训练 AI 模型而给数据打标签的过程，是机器学习的基础步骤，使 AI 系统能够识别模式并执行任务。随着 AI 应用的扩展，数据标注的需求不断增长，在印度等国家创造了新的就业市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cvat.ai/academy/introduction-to-data-annotation">What is Data Annotation ? Definition , Use Cases... | CVAT Academy</a></li>
<li><a href="https://www.dataannotation.tech/">DataAnnotation | Future-Proof Your Career With AI Training Work</a></li>

</ul>
</details>

**标签**: `#AI`, `#data annotation`, `#employment`, `#India`, `#labor`

---

<a id="item-20"></a>
## [印度工人佩戴摄像头为 AI 采集数据](https://www.nytimes.com/video/world/asia/100000011091777/india-ai-robots-human-movement.html) ⭐️ 6.0/10

在印度，工人们将摄像头绑在身上，收集人体运动数据，用于训练机器人领域的 AI 系统。这凸显了人类在 AI 数据流水线中一个细分但至关重要的角色。 这种人在回路的数据采集对于开发能在现实环境中运行的机器人至关重要，因为它提供了训练所需的结构化、高质量运动数据。同时，它也凸显了即使在自动化不断进步的情况下，AI 训练中对人类劳动力的需求仍在增长。 所采集的数据用于训练物理 AI 系统，需要结构化、可重复且可扩展的人体运动数据，这与电影动作捕捉不同。这项工作是人机协同标注大趋势的一部分，人类在其中验证和完善 AI 生成的标签，以用于安全关键的机器人应用。

rss · The New York Times World · 8月20日 13:19

**背景**: AI 系统，尤其是机器人领域的 AI，需要大量真实世界数据来学习如何执行任务。人在回路的数据采集涉及人类演示动作或提供标注，供 AI 模型训练使用，这对于处理自动化无法单独解决的模糊或安全关键场景至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thefuturismtoday.com/startups/mecka-helps-robots-learn-from-humans/">Meet Mecka AI : The Startup Helping Robots Learn From Humans</a></li>
<li><a href="https://humaid.co/blog/what-is-human-in-the-loop-robotics-data-collection">Human - in - the - Loop Robotics Data Collection Guide | Humaid</a></li>
<li><a href="https://www.sapien.io/blog/why-robots-need-humans-in-the-loop-to-walk-and-talk">Why Robots need Humans - in - the - Loop to Walk and Talk</a></li>

</ul>
</details>

**标签**: `#AI`, `#robotics`, `#data collection`, `#human-in-the-loop`, `#India`

---

<a id="item-21"></a>
## [中国第 16 次北冰洋考察部署无人冰站与浮标组网](https://www.chinanews.com.cn/gn/2026/08-21/10681404.shtml) ⭐️ 5.0/10

中国第 16 次北冰洋考察已在“雪龙”号上完成冰站作业，并正在“雪龙 2”号上继续，部署了生态无人冰站和冰基浮标，形成观测网。该网络旨在研究北冰洋中央区大气-海冰-海洋相互作用及生态系统耦合。 此次考察增进了对北极快速变化及其全球气候影响的理解。无人观测系统的部署提升了偏远极地地区的监测能力，有助于气候建模和生态系统研究。 “雪龙”号完成了 12 个冰站作业，为历次北冰洋考察单船之最，而“雪龙 2”号正在进行 7 个冰站。共布放 30 余套冰基浮标，其中部分浮标类型的国产化率平均超过 90%。

rss · China News Service China · 8月21日 00:09

**背景**: 由于气候变化，北极海冰正在迅速减少，影响全球天气模式和生态系统。冰站和浮标提供了关于大气-海冰-海洋耦合系统的关键数据，这对于改进气候模型和预测未来变化至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.news.cn/tech/20251017/8fd84d43c6c44d258f036bfac4b41c8e/c.html">冰 上攻坚战——北极27个 冰 基 浮 标 布放记-新华 网</a></li>
<li><a href="https://cn.chinadaily.com.cn/a/202608/11/WS6a7aca58a310d709c2fc29df.html">“雪龙”号顺利完成12个 冰 站作业任务 - 中国日报 网</a></li>
<li><a href="https://news.youth.cn/gn/202608/t20260811_16810078.htm">“雪龙”号顺利完成12个 冰 站作业任务_新闻频道_中国青年 网</a></li>

</ul>
</details>

**标签**: `#Arctic research`, `#climate science`, `#oceanography`, `#expedition`

---

<a id="item-22"></a>
## [上海将在“十五五”期间推动数智赋能教育变革](https://www.chinanews.com.cn/gn/2026/08-20/10681291.shtml) ⭐️ 5.0/10

上海市教委 8 月 20 日披露，“十五五”时期上海将促进数智赋能教育变革，推动人工智能赋能学科和科研发展，建设新兴学科、交叉学科，并探索人工智能拔尖创新人才培养新模式。 该计划包括利用智能技术促进学科跃升，根据产业结构智能升级衍生新学科增长点，并建设一批新兴学科和交叉学科。公告未透露实施、资金或时间表的具体细节。

rss · China News Service China · 8月20日 12:16

**背景**: “十五五”规划（2026-2030 年）是中国国家发展蓝图。近年来，中国强调教育数字化转型，许多省份正在探索人工智能赋能教学和人才培养。上海作为重要的经济和教育中心，经常试点创新政策，这些政策随后会在全国推广。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://epaper.hubeidaily.net/pc/content/202505/14/content_314392.html">湖北 数 字 教 育 ：筑基强 能 构生态 数 智 赋 能 育 未来 湖北日报 数 字报</a></li>
<li><a href="https://m.jfdaily.com/wx/detail.do?id=841358">数 智 融合，多元案例勾勒未来 教 育 图景</a></li>
<li><a href="http://www.jyb.cn/rmtzgjyb/202604/t20260425_2111471774.html">敢向无 人 区挺进，探索 拔 尖 创 新 人 才 培 养 新 模 式 -中国教育 新 闻网</a></li>

</ul>
</details>

**标签**: `#AI in Education`, `#Education Policy`, `#Shanghai`, `#Digital Transformation`

---

<a id="item-23"></a>
## [中国交付新一代深水多功能工程船“海洋石油 292”](https://www.chinanews.com.cn/cj/2026/08-21/10681456.shtml) ⭐️ 4.0/10

此次交付标志着中国在高端海洋工程装备自主化方面迈出重要一步，减少了对国外船舶的依赖。它为加快深海能源资源开发提供了关键装备保障，对保障国家能源安全和推动海洋产业发展具有重要意义。 该船具备水下管缆及结构物安装、海底调查、运输保障等能力，覆盖海洋工程全流程作业。该船由上海振华重工为中国海油深圳海洋工程技术服务有限公司建造。

rss · China News Service Scroll · 8月21日 01:50

**背景**: 深水多功能海洋工程船是用于海上油气田水下施工、维护和调查作业的专用船舶。中国一直在发展此类船舶，以支持其日益增长的深海勘探和生产活动，此前“海洋石油 286”等船型已成为标杆。“海洋石油 292”的交付标志着该领域的持续进步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.seafarer.love/industry_news/8721.html">seafarer.love/industry_news/8721.html</a></li>
<li><a href="https://sdxw.iqilu.com/w/article/YS0yMS0xNzA3NDI4Mg.html">我国自主研发新一代 深 水 多 功 能 海 洋 工 程 船 今日下 水</a></li>

</ul>
</details>

**标签**: `#maritime engineering`, `#deep-sea vessel`, `#China`, `#industry news`

---

<a id="item-24"></a>
## [广州知识产权法院 2025 年先行调解成功超三千件](https://www.chinanews.com.cn/gn/2026/08-20/10681344.shtml) ⭐️ 4.0/10

广州知识产权法院于 2026 年 8 月 20 日召开调解工作座谈会，通报 2025 年成功调解知识产权纠纷超过 3000 件。 这一里程碑凸显了中国知识产权体系中替代性纠纷解决机制的有效性，可能减轻法院案件负担，并为当事人提供更快、对抗性更低的解决方案。它反映了法律实践中向调解发展的趋势，可能对构建案件管理工具的法律科技和软件开发者具有参考意义。 座谈会于广州举行，法院官员和调解员参加。报道称成功调解案件数“超过 3000 件”，但未提供按案件类型或成功率的详细分类。

rss · China News Service China · 8月20日 13:47

**背景**: 随着技术创新，中国的知识产权纠纷不断增加，法院因此推广调解作为诉讼的节约成本的替代方案。广州知识产权法院是为高效处理此类案件而设立的专门法院之一。调解可在正式诉讼前（先行调解）或诉讼过程中进行，旨在友好解决争议。

**标签**: `#intellectual property`, `#legal news`, `#China`

---

<a id="item-25"></a>
## [中法青年向湖南芷江捐赠解密二战档案](https://www.chinanews.com.cn/gn/2026/08-20/10681339.shtml) ⭐️ 4.0/10

2026 年 8 月 20 日，法国青年马库斯、白士杰与中国青年钟灏松一行，向位于湖南芷江的中国人民抗日战争胜利受降纪念馆捐赠了法国官方解密的日本侵华档案扫描件。这批档案以第三方国际视角丰富了该馆的馆藏。 此次捐赠有助于从外部视角补齐湖南抗战域外史证链条，强化日本侵华历史的证据链。同时，它体现了国际社会在保存二战历史方面的持续合作，对历史研究和公众教育具有重要意义。 这些档案是在法国南特外交部档案馆查档收集的，属于马库斯和白士杰团队更广泛努力的一部分。此前，2026 年 5 月 4 日，他们已向侵华日军南京大屠杀遇难同胞纪念馆移交了类似资料，用于学术研究。

rss · China News Service China · 8月20日 13:46

**背景**: 芷江受降纪念馆位于 1945 年 8 月 21 日中国接受日军投降的旧址，是全国唯一全面反映抗战胜利受降的专题性纪念馆。此次捐赠的法国解密档案提供了关于日本战时行为的独立第三方视角，补充了中日两国的记录。此类国际档案交流是保存和记录二战历史的更广泛努力的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.qq.com/rain/a/20260504V06FNK00">法 国 友人向南京移交 日 本 侵 华 档 案 _腾讯新闻</a></li>
<li><a href="https://m.voc.com.cn/xhn/news/202605/32583450.html">法 国 友人移交的1993...</a></li>
<li><a href="https://www.stnn.cc/c/2026-05-04/4073446.shtml">stnn.cc/c/2026-05-04/4073446.shtml</a></li>

</ul>
</details>

**标签**: `#history`, `#archives`, `#WWII`, `#China-France`

---

<a id="item-26"></a>
## [中国“十五五”医保规划回应民生关切](https://www.chinanews.com.cn/gn/2026/08-20/10681347.shtml) ⭐️ 4.0/10

《全民医疗保障“十五五”规划》于 2026 年 8 月 19 日正式发布，描绘了未来五年医保事业发展的蓝图。规划中专门设置了 5 个民生实事专栏，涵盖灵活就业者参保、药店购药等实际问题。 该规划直接回应了公众的日常关切，如灵活就业者参保和药店购药问题，使医疗服务更加可及和贴心。这标志着政策向务实、以人民为中心的实施方向转变，有望提升公众对医疗体系的满意度和信任度。 规划中设置了 5 个民生实事专栏，涵盖灵活就业者参保、24 小时药店购药、手机查看就诊排队情况等具体问题。这些细节被纳入顶层设计，体现了解决实际问题的决心。

rss · China News Service China · 8月20日 13:22

**背景**: 中国的五年规划是指导经济社会发展的综合性国家战略。《全民医疗保障“十五五”规划》是这一框架的一部分，聚焦于医保改革。以往的规划已建立了覆盖绝大多数人口的基本医疗保险制度，而新规划旨在对其进行完善和提升。

**标签**: `#healthcare`, `#policy`, `#China`

---

<a id="item-27"></a>
## [第四届广东建筑业高质量发展大会在广州开幕](https://www.chinanews.com.cn/dwq/2026/08-21/10681441.shtml) ⭐️ 3.0/10

2026 年 8 月 20 日，第四届广东建筑业高质量发展大会在广州开幕，主题为“智造赋能 全链协同——新型建筑工业化与建筑全生命周期管理协同发展”。来自全省住房和城乡建设部门、建筑业协会、专家学者及企业代表近 350 人参加，共话广东培育建筑业新质生产力的实践路径。 此次大会标志着广东通过智能制造和全链协同推动建筑业现代化，可能为中国其他地区树立标杆。它凸显了新质生产力在传统行业中的重要性，有望推动建筑业的创新和效率提升。 大会聚焦新型建筑工业化和建筑全生命周期管理，探讨设计、生产、施工等环节的整合。会议由相关部门组织，吸引了近 350 名官员、学者和企业代表参加。

rss · China News Service Scroll · 8月21日 01:56

**背景**: 新型建筑工业化以设计标准化、生产工厂化、现场装配化、主体装饰机电一体化、全过程管理信息化为特征。建筑全生命周期管理（BLM）将规划、设计、招投标、施工、竣工验收及物业管理等环节作为一个整体。这些概念是中国建筑业现代化和提升效率与可持续性的核心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.buildenvi.com/zhuanti/lj/m8z0r">“未来 建 筑 ”啥样？ 带你从8个角度去领略 - 建 环视界</a></li>
<li><a href="https://www.baike.com/wikiid/2913660566377994151">建 筑 全 生 命 周 期 -快懂百科</a></li>

</ul>
</details>

**标签**: `#construction`, `#conference`, `#industry`, `#China`

---

<a id="item-28"></a>
## [中国军事纪录片《制胜》展示新武器](https://www.chinanews.com.cn/sh/2026/08-21/10681429.shtml) ⭐️ 3.0/10

中国军事纪录片《制胜》近期播出，展示了大量新型武器装备，令人目不暇接。观众被建议一帧一帧观看，以免错过隐藏细节。 这部纪录片展现了中国军事现代化的成就，可能增强民族自豪感和公众对国防技术的兴趣。同时，它也向国际社会传递了中国军事能力不断增强的信号。 该纪录片是一部“融媒体”作品，表明其设计用于多平台分发。文章提到，观众开玩笑说需要暂停并仔细审视每一帧，以捕捉“彩蛋”（隐藏细节）。

rss · China News Service Scroll · 8月21日 01:43

**背景**: 中国军队一直在推进现代化建设，重点发展先进武器系统。像《制胜》这样的纪录片作为宣传工具，向公众展示这些进步，增强民族自豪感。

**标签**: `#military`, `#documentary`, `#China`, `#promotional`

---