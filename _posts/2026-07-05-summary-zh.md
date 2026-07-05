---
layout: default
title: "Horizon Summary: 2026-07-05 (ZH)"
date: 2026-07-05
lang: zh
---

> 从 292 条内容中筛选出 28 条重要资讯。

---

1. [提示注入泄露 YouTube 创作者的私密视频](#item-1) ⭐️ 9.0/10
2. [全球首款相变忆阻器神经芯片实现 2.12 毫秒延迟](#item-2) ⭐️ 9.0/10
3. [中国“人造太阳”计划 2030 年发出第一度核聚变电](#item-3) ⭐️ 8.0/10
4. [AI 数据中心耗水量远超披露，发电间接用水成隐形消耗](#item-4) ⭐️ 8.0/10
5. [中国团队发现中等质量黑洞最强证据](#item-5) ⭐️ 8.0/10
6. [NASA 启动紧急任务拯救斯威夫特天文台](#item-6) ⭐️ 8.0/10
7. [美光投资 93 亿美元扩建日本 HBM 工厂](#item-7) ⭐️ 7.0/10
8. [国内最大海水淡化试验场投运](#item-8) ⭐️ 7.0/10
9. [丰田计划用 AI 将 4.5 万术语精简至 5000 个](#item-9) ⭐️ 7.0/10
10. [天韵相机由神舟二十三号乘组安装至中国空间站](#item-10) ⭐️ 7.0/10
11. [澳大利亚政府警告 AI 医疗记录工具存在隐私风险](#item-11) ⭐️ 7.0/10
12. [阿里巴巴禁止员工使用 Claude Code](#item-12) ⭐️ 7.0/10
13. [白宫在热浪期间删除 6000 页节能内容](#item-13) ⭐️ 7.0/10
14. [中国发布国际科技组织成立登记指引](#item-14) ⭐️ 6.0/10
15. [中国组织器官生物制造发明专利全球第一](#item-15) ⭐️ 6.0/10
16. [我国首架大气综合航测飞机 Y-12F 首飞成功](#item-16) ⭐️ 5.0/10
17. [科技产品可能导致手部无力和视力模糊](#item-17) ⭐️ 5.0/10
18. [中国用长征六号改火箭一箭 18 星成功发射](#item-18) ⭐️ 4.0/10
19. [法国能源巨头呼吁欧中合作推进能源转型](#item-19) ⭐️ 4.0/10
20. [马斯克在 SpaceX IPO 前关于英国的帖子数量是 SpaceX 的两倍](#item-20) ⭐️ 4.0/10
21. [Schisto & Ladders：一款教孩子了解寄生虫病的棋盘游戏](#item-21) ⭐️ 4.0/10
22. [影视剧架起两岸青年文化桥梁](#item-22) ⭐️ 3.0/10
23. [成都举办科创发展活动，聚焦创新驱动](#item-23) ⭐️ 3.0/10
24. [女性影响力与人工智能峰会在斯图加特举行](#item-24) ⭐️ 3.0/10
25. [2026 港澳青年浙江行启动](#item-25) ⭐️ 3.0/10
26. [第 25 届汉语桥泰国赛区决赛举行](#item-26) ⭐️ 2.0/10
27. [贺凯琪四赴浙江带团，陪伴港澳青年](#item-27) ⭐️ 2.0/10
28. [辽台青年篮球交流活动在沈阳举行](#item-28) ⭐️ 2.0/10

---

<a id="item-1"></a>
## [提示注入泄露 YouTube 创作者的私密视频](https://javoriuski.com/post/youtube) ⭐️ 9.0/10

一名安全研究人员发现，YouTube Studio 的 AI 评论建议功能存在提示注入漏洞，可泄露创作者的私密或未公开视频。攻击者通过构造恶意评论，诱使 AI 泄露视频标题或其他敏感信息。 该漏洞影响数百万依赖 YouTube Studio AI 工具的创作者，可能泄露未发布内容。它凸显了将大语言模型集成到面向用户的应用时，缺乏针对提示注入的防护所带来的日益增长的安全风险。 攻击需要创作者点击评论标签中的建议 AI 提示，从而触发注入。研究人员演示了注入的提示可迫使 AI 在其回复中附加包含私密视频标题的通知。

hackernews · javxfps · 7月4日 16:45 · [社区讨论](https://news.ycombinator.com/item?id=48786781)

**背景**: 提示注入是一种网络安全利用方式，恶意输入导致大语言模型产生非预期行为。YouTube Studio 的 AI 评论建议功能使用大语言模型帮助创作者回复评论，但模型可能无法区分系统指令和用户提供的评论内容。这使得攻击者可以在评论中嵌入指令，AI 在生成建议时执行这些指令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://support.google.com/youtube/answer/16291691?hl=en">Learn about Ask Studio in YouTube Studio - YouTube Help - Google Help</a></li>
<li><a href="https://support.google.com/youtube/answer/10357396?hl=en-EN&co=GENIE.Platform=Desktop">Use comment reply suggestions - Computer - YouTube Help</a></li>

</ul>
</details>

**社区讨论**: 社区讨论中，一位前谷歌员工解释了 YouTube 可能因内部流程而修复缓慢的原因。一些用户尝试复现该攻击但结果不一，其他人则赞扬了研究人员清晰、不煽情的报告风格。

**标签**: `#security`, `#prompt injection`, `#YouTube`, `#vulnerability`, `#AI`

---

<a id="item-2"></a>
## [全球首款相变忆阻器神经芯片实现 2.12 毫秒延迟](https://www.ithome.com/0/972/680.htm) ⭐️ 9.0/10

中国研究团队成功研制出全球首款基于相变忆阻器的毫秒级神经动力学系统芯片，单步运算时延仅为 2.12 毫秒。该成果于 2026 年 7 月 5 日发表在《科学》杂志上。 这一突破解决了神经动力学系统半个世纪以来的瓶颈，实现了实时高保真脑建模和闭环脑机接口。在脑皮层重建任务中，该芯片比 NVIDIA A100 GPU 提速高达 478 倍。 该芯片采用 40 纳米工艺制造，存内计算与步长漂移阵列总面积仅 0.28 平方毫米。运行频率为 50 MHz，单步积分仅需 9 级流水，相比最先进的专用加速器（ASIC）实现 3.82~36.27 倍速度提升和 11.75~24.73 倍功耗降低。

rss · ITHome Feed · 7月4日 23:07

**背景**: 神经动力学系统将神经网络与微分方程相结合，用于模拟脑活动等连续时间过程。相变忆阻器通过相变改变电阻，可实现存内计算，减少数据搬运。在此之前，实现亚 10 毫秒延迟一直是该领域的重大挑战。

**标签**: `#neuromorphic computing`, `#memristor`, `#neural dynamics`, `#hardware`, `#AI chip`

---

<a id="item-3"></a>
## [中国“人造太阳”计划 2030 年发出第一度核聚变电](https://www.ithome.com/0/972/704.htm) ⭐️ 8.0/10

中国更新了核聚变时间表，计划在 2030 年前演示用核聚变发电，此前在 2026 年 6 月成功测试了 100%国产化的超导磁体。 这一里程碑展示了中国在关键聚变部件上的自给自足能力，并加速了实用聚变能源的进程，后者可提供近乎无限、清洁的能源。 测试的磁体包括环向场磁体和高温超导中心螺管线圈，线圈重量从 350 吨增加到 580 吨，可实现更高能量输出。超导材料成本从每米 400 元降至 100 元。

rss · ITHome Feed · 7月5日 01:18

**背景**: 核聚变通过极端温度下轻原子核聚变复制太阳的能量，需要强磁场约束等离子体。中国的“人造太阳”项目，包括 EAST 托卡马克装置，已在持续高温等离子体方面创造世界纪录。此次磁体突破解决了聚变反应堆建造中最难的工程挑战之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cas.cn/cm/202606/t20260629_5113869.shtml">【光明日报】我国核聚变堆超导磁体研发取得重要突破</a></li>
<li><a href="https://news.cctv.com/2026/06/27/ARTIrylGaXIl2wXuzElP1r1y260627.shtml">我国核聚变堆超导磁体研发取得重要突破_新闻频道_央视网 (cctv.com)</a></li>
<li><a href="https://news.qq.com/rain/a/20260628A040OV00">我国“人造太阳”重要突破！全球最大核聚变堆超导磁体通过验收</a></li>

</ul>
</details>

**标签**: `#nuclear fusion`, `#energy`, `#China`, `#superconducting magnet`, `#technology`

---

<a id="item-4"></a>
## [AI 数据中心耗水量远超披露，发电间接用水成隐形消耗](https://www.ithome.com/0/972/689.htm) ⭐️ 8.0/10

据《华尔街日报》报道，美国 AI 数据中心的间接耗水量（来自发电）约为直接现场耗水量的 12 倍，但微软、谷歌、亚马逊等科技巨头大多未披露这一间接用水量。 这一隐藏的水足迹引发了严重的可持续性担忧，因为 AI 基础设施投资预计将达到 1 万亿美元，可能加剧凤凰城等地区的水资源短缺——到 2031 年，数据中心用水可能超过城市供水量的 20%。 目前只有 Meta 核算了间接用水，其间接耗水量是直接耗水量的 20 倍。劳伦斯伯克利国家实验室 2024 年的分析显示，美国数据中心的间接耗水量历来约为直接耗水量的 12 倍。

rss · ITHome Feed · 7月4日 23:50

**背景**: 数据中心需要大量电力来运行服务器和冷却系统。发电过程中消耗的水——尤其是来自燃煤和核电站的水——通常不计入公司的可持续发展报告。大多数数据中心仍采用蒸发式冷却，直接消耗大量水。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eesi.org/articles/view/data-centers-and-water-consumption">Data Centers and Water Consumption | Article | EESI</a></li>
<li><a href="https://www.construction-physics.com/p/i-was-wrong-about-data-center-water">I Was Wrong About Data Center Water Consumption</a></li>

</ul>
</details>

**标签**: `#AI`, `#data centers`, `#water consumption`, `#sustainability`, `#environmental impact`

---

<a id="item-5"></a>
## [中国团队发现中等质量黑洞最强证据](https://www.ithome.com/0/972/672.htm) ⭐️ 8.0/10

一个由中国科学家领衔的研究团队基于大规模 N 体模拟，提出了银河系中心附近存在中等质量黑洞的最强动力学证据。该研究于 2026 年 6 月 29 日发表在《天体物理学报》上，解释了三组年轻星团围绕人马座 A*的异常轨道构型。 这一发现填补了黑洞演化中的关键空白，因为中等质量黑洞被认为是恒星级黑洞和超大质量黑洞之间的“缺失一环”。它还为未来的高精度观测（如中国空间站巡天望远镜 CSST）提供了可检验的预言。 研究团队使用了中山大学王龙教授开发的开源 N 体模拟软件 PeTar，并在清华大学的高性能计算平台上进行了模拟。模拟结果显示，一个质量约为太阳 1 万倍的引力源（很可能是中等质量黑洞）能在数百万年内同时复现三组星团的轨道分布特征。

rss · ITHome Feed · 7月4日 15:02

**背景**: 黑洞通常分为三类：恒星级（几到几十倍太阳质量）、超大质量（数百万到数十亿倍太阳质量）和中等质量（100 到 10 万倍太阳质量）。中等质量黑洞一直难以捉摸，仅有少数存在争议的候选体。银河系中心有一个超大质量黑洞人马座 A*，周围环绕着轨道特性令人费解的年轻星团。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Intermediate-mass_black_hole">Intermediate-mass black hole</a></li>
<li><a href="https://github.com/lwang-astro/PeTar">GitHub - lwang-astro/PeTar: PeTar is a high-performance N ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sagittarius_A*_cluster">Sagittarius A* cluster - Wikipedia</a></li>

</ul>
</details>

**标签**: `#astrophysics`, `#black holes`, `#numerical simulation`, `#Galactic center`

---

<a id="item-6"></a>
## [NASA 启动紧急任务拯救斯威夫特天文台](https://www.theverge.com/science/961459/nasa-emergency-save-swift-observatory-katalyst-space-technologies) ⭐️ 8.0/10

NASA 与 Katalyst Space Technologies 合作启动了一项紧急任务，以防止斯威夫特天文台因太阳活动增加导致的轨道衰减而在地球大气层中烧毁。Katalyst 的 LINK 航天器已于 2026 年 7 月 3 日发射，将与斯威夫特会合并提升其轨道。 这项任务意义重大，因为它旨在延长一个已运行二十多年、研究伽马射线暴及其他天体物理现象的重要科学天文台的寿命。成功将展示在轨服务和碎片减缓的关键能力，可能改变老化卫星的管理方式。 斯威夫特天文台于 2004 年发射，由于太阳风暴导致地球大气膨胀，其轨道衰减加速。Katalyst 的 LINK 航天器是一种机器人服务飞行器，旨在捕获并提升斯威夫特的轨道高度，该任务于 2026 年 7 月 3 日发射。

rss · The Verge · 7月4日 19:06

**背景**: 尼尔·格雷尔斯斯威夫特天文台是 NASA 的一个多波段太空望远镜，最初设计用于研究伽马射线暴。轨道衰减是指大气阻力使卫星减速，导致其高度下降；太阳活动增加会加热并膨胀高层大气，从而加剧这一过程。如果不进行干预，斯威夫特最早可能在 2026 年在地球大气层中烧毁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Swift_Observatory">Swift Observatory</a></li>
<li><a href="https://www.katalystspace.com/news/katalysts-link-robotic-spacecraft-integrated-with-pegasus-xl-and-ready-for-launch">Katalyst’s LINK Robotic Spacecraft Integrated with Pegasus XL ...</a></li>
<li><a href="https://www.nasa.gov/news-release/nasa-to-preview-katalyst-mission-to-boost-swift-spacecrafts-orbit/">NASA to Preview Katalyst Mission to Boost Swift Spacecraft’s ...</a></li>

</ul>
</details>

**标签**: `#space`, `#NASA`, `#satellite`, `#emergency mission`, `#Swift Observatory`

---

<a id="item-7"></a>
## [美光投资 93 亿美元扩建日本 HBM 工厂](https://36kr.com/newsflashes/3882061184413701?f=rss) ⭐️ 7.0/10

美光科技已正式启动其日本广岛工厂的扩建工程，总投资 93 亿美元，用于生产包括高带宽存储器（HBM）在内的先进存储芯片，预计 2028 年夏季左右开始出货。 这项投资凸显了 HBM 作为英伟达等 AI 处理器关键组件的旺盛需求，也反映了全球存储制造商在争夺 AI 芯片供应链方面的激烈竞争。 该项目是更广泛趋势的一部分，SK 海力士也宣布在韩国投资 514.6 亿美元新建 NAND 闪存工厂。HBM 采用 3D 堆叠技术实现高带宽，对 AI 和高性能计算至关重要。

rss · 36Kr Feed · 7月5日 01:16

**背景**: 高带宽存储器（HBM）是一种 3D 堆叠 DRAM，提供极高的带宽，用于 GPU、AI 加速器和高性能计算。它最初由 AMD 和 SK 海力士开发。美光、三星和 SK 海力士是 HBM 市场的三大主要厂商，都在竞相扩大产能以满足 AI 驱动的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/33990592">HBM火了，它到底是什么？ - 知乎</a></li>
<li><a href="https://baike.baidu.com/item/高带宽存储器/22786196">高带宽存储器 - 百度百科</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/30443031971">一文读懂 HBM：概念、架构与应用 - 知乎</a></li>

</ul>
</details>

**标签**: `#HBM`, `#美光科技`, `#AI芯片`, `#存储芯片`, `#半导体投资`

---

<a id="item-8"></a>
## [国内最大海水淡化试验场投运](https://www.ithome.com/0/972/730.htm) ⭐️ 7.0/10

位于天津的国内最大海水淡化试验场正式投运，并成功完成首批国产正位移转子式能量回收装置的测试验证。 这一里程碑减少了中国对进口海水淡化设备的依赖（此前进口设备比国产贵三成），并加速了关键组件的技术迭代，有助于保障水资源安全。 该试验场采用“超滤+反渗透”双膜法短流程工艺，单机规模达 1 万吨/日，总占地面积 2000 多平方米，可测试设备能耗、出水水质和使用寿命等指标。

rss · ITHome Feed · 7月5日 04:23

**背景**: 能量回收装置是反渗透海水淡化的关键设备，通过回收高压浓盐水的余压能降低系统能耗，约占工程总投资的 10%-15%。正位移转子式是高效类型，能量回收效率可达 90%以上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.puhonghb.com/506.html">puhonghb.com/506.html</a></li>
<li><a href="https://baike.baidu.com/item/海水淡化能量回收装置/3781190">海水淡化能量回收装置 - 百度百科</a></li>

</ul>
</details>

**标签**: `#seawater desalination`, `#energy recovery`, `#water treatment`, `#industrial technology`, `#China`

---

<a id="item-9"></a>
## [丰田计划用 AI 将 4.5 万术语精简至 5000 个](https://www.ithome.com/0/972/724.htm) ⭐️ 7.0/10

丰田宣布将利用 AI 在 2028 年前把各部门 4.5 万个专业术语精简至 5000 个通用标准术语，削减 30%的中间流程。该举措是 OMUSVI 项目的一部分，旨在统一从企划到销售的车辆规格数据。 这一标准化有望显著提升生产效率并减少供应链中的错误，每年可节省目前用于术语翻译的 31 万小时。它也为制造业中 AI 驱动的工业标准化树立了先例。 OMUSVI 系统将与年度生产计划对接，自动核算零部件需求量并推送至供应商，减少目前每家供应商高达 720 小时的手工核算工作。该项目在 2023 年遭遇内部阻力，但 2024 年获得前丰田社长佐藤恒治的支持。

rss · ITHome Feed · 7月5日 03:37

**背景**: 丰田的术语不统一问题可追溯至 1950 年，当时生产和销售分拆为两家独立公司，各自开发了不同的编码系统。即使 1982 年重新合并后，这些分散的系统仍延续至今，导致 560 个流程步骤和 800 套独立业务系统。OMUSVI 项目（全称 Organized Master Unified System for Vehicle Information）始于 2021 年。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://prtimes.jp/main/html/rd/p/000000010.000012909.html">トヨタ自動車『OMUSVI』プロジェクトで実現するクルマづくりの新常識─...</a></li>
<li><a href="https://www.talent-book.jp/toyota/stories/58967">トヨタの10年後、20年後を変える──4年目社員が「OMUSVI」でめざす変革...</a></li>
<li><a href="https://japan.cnet.com/release/31115336/">トヨタ自動車『OMUSVI』プロジェクトで実現するクルマづくりの新常識─...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Manufacturing`, `#Toyota`, `#Standardization`, `#Supply Chain`

---

<a id="item-10"></a>
## [天韵相机由神舟二十三号乘组安装至中国空间站](https://www.ithome.com/0/972/723.htm) ⭐️ 7.0/10

神舟二十三号乘组完成了天韵相机（MUSICO）的在轨组装、测试及出舱安装，这是首个登上中国空间站的香港科学载荷。 这标志着香港参与国家空间科学的重要里程碑，该相机的高分辨率温室气体监测能力有助于精确定位全球二氧化碳和甲烷排放源，支持气候行动。 天韵相机重量不超过 80 公斤，体积比家用洗衣机更小。它采用四个独立探测镜头，分别用于探测二氧化碳、甲烷、氧气和气溶胶，从而在 400 公里轨道上实现精确的点源识别。

rss · ITHome Feed · 7月5日 03:32

**背景**: 温室气体点源探测是指通过分析光谱特征，从太空识别特定排放位置（如发电厂、垃圾填埋场）。天韵相机由香港科技大学与长春光机所联合研制，随天舟十号发射，现已在中国空间站投入使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/0/972/723.htm">港科大牵头研制的“天韵相机”上岗，神舟二十三乘组在轨工作报告上新 - ...</a></li>
<li><a href="https://news.cctv.com/2026/07/05/ARTIX2OgPypCOYQwoqSvAWTS260705.shtml">组装“天韵相机”→光环境要素实验→健康管理…… | 中国空间站周记再“上”新...</a></li>
<li><a href="https://baike.baidu.com/item/天韵相机/67772175">天韵相机 - 百度百科</a></li>

</ul>
</details>

**标签**: `#space technology`, `#environmental monitoring`, `#Hong Kong`, `#greenhouse gas`, `#remote sensing`

---

<a id="item-11"></a>
## [澳大利亚政府警告 AI 医疗记录工具存在隐私风险](https://www.theguardian.com/australia-news/2026/jul/05/doctors-ai-scribes-australia-government-privacy-warning) ⭐️ 7.0/10

澳大利亚联邦卫生部对医生越来越多地使用 AI 记录工具表示担忧，这些工具会录制并转录患者问诊内容，促使监管机构考虑制定保护措施。 这标志着对 AI 在医疗领域快速应用的重要监管回应，凸显了尚未解决的隐私和数据治理问题，可能影响患者信任和临床实践。 AI 记录工具在过去 18 个月中迅速普及，但专家警告存在数据隐私、问责、偏见以及临床医生过度依赖等风险。

rss · The Guardian World · 7月4日 20:00

**背景**: AI 记录工具利用环境技术实时捕捉患者就诊过程并生成医疗文档。它们越来越多地被用于全科诊所，以减轻行政负担，但其快速部署已超过许多国家的监管框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://betakit.com/as-ai-scribes-flood-healthcare-experts-stress-need-for-responsible-adoption/">As AI scribes flood healthcare , experts stress need for... | BetaKit</a></li>
<li><a href="https://www.racgp.org.au/running-a-practice/technology/artificial-intelligence-ai/artificial-intelligence-ai-scribes">RACGP - Artificial intelligence ( AI ) scribes</a></li>

</ul>
</details>

**标签**: `#AI`, `#privacy`, `#healthcare`, `#regulation`, `#Australia`

---

<a id="item-12"></a>
## [阿里巴巴禁止员工使用 Claude Code](https://techcrunch.com/2026/07/04/alibaba-reportedly-bans-employees-from-using-claude-code/) ⭐️ 7.0/10

据报道，阿里巴巴已将 Anthropic 的 AI 编程工具 Claude Code 列为高风险软件，并禁止员工使用。 此举表明企业对 AI 编程工具（尤其是外国公司开发的工具）的监管审查日益严格，并可能影响其他科技巨头采取类似限制措施。 据报道，该禁令适用于所有阿里巴巴员工，并将 Claude Code 列为高风险软件，但未披露具体原因。

rss · TechCrunch · 7月4日 16:32

**背景**: Claude Code 是 Anthropic 开发的 AI 编程代理，能够读取代码库、编辑文件和运行命令。Anthropic 因拒绝移除禁止将 Claude 用于大规模监控和自主武器的合同条款，而面临美国政府限制，被国防部列为供应链风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**标签**: `#Alibaba`, `#Claude Code`, `#AI regulation`, `#corporate policy`, `#software security`

---

<a id="item-13"></a>
## [白宫在热浪期间删除 6000 页节能内容](https://www.theverge.com/policy/961449/white-house-mamdani-heatwave-deletion) ⭐️ 7.0/10

美国能源部在历史性热浪期间删除了约 6000 页与节能相关的网页，此前纽约市长佐兰·马姆达尼建议将空调设为 78 华氏度（约 25.6°C）的提议遭到政治反弹。 此次删除在极端高温期间削弱了公众获取节能信息的渠道，而此时此类指导对于防止停电和保护弱势群体最为关键。这也凸显了节能措施的政治化。 删除范围广泛且不加区分，移除了支持马姆达尼恒温建议的页面、节水科普、隔热材料介绍以及太阳能十项全能竞赛相关内容。互联网档案馆已保存了这些被删除的网页。

rss · The Verge · 7月4日 16:19

**背景**: 纽约市连续四天气温超过 95 华氏度（35°C），其中两天最高温超过 100 华氏度（37.8°C）。极端高温给电网带来巨大压力，尤其是在节假日居家民众增多时。将空调设为 78 华氏度有助于防止停电，避免居民失去制冷设备而面临高温健康风险。美国疾控中心和国家海洋和大气管理局的数据显示，极端高温在美国的年均致死人数超过洪水、龙卷风和飓风的总和。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/policy/961449/white-house-mamdani-heatwave-deletion">White House deletes thousands of web pages about energy ...</a></li>
<li><a href="https://www.newsweek.com/doe-deletes-webpage-instructing-people-to-lower-thermostat-to-78-12153833">DoE Deletes Webpage Instructing People To Lower... - Newsweek</a></li>
<li><a href="https://www.houstonchronicle.com/news/houston-texas/trending/article/ted-cruz-energy-recommendation-power-grid-new-york-22330358.php">Ted Cruz calls out NYC energy advice. But Texas made the same ask.</a></li>

</ul>
</details>

**标签**: `#policy`, `#energy`, `#climate`, `#politics`

---

<a id="item-14"></a>
## [中国发布国际科技组织成立登记指引](https://www.chinanews.com.cn/gn/2026/07-05/10652912.shtml) ⭐️ 6.0/10

2026 年 7 月 4 日，民政部、科技部、中国科协联合发布《国际科技组织成立登记指引》，明确了国际科技组织的成立条件和申请程序。 该政策为国际科技组织在华设立提供了明确的监管框架，可能吸引更多全球科学合作和标准制定机构落户中国。 该指引明确了注册要求，包括组织的宗旨、成员和治理结构，旨在简化审批流程，同时确保符合中国法律。

rss · China News Service China · 7月4日 22:50

**背景**: 国际科技组织在全球研究合作和标准制定中发挥关键作用。此前，中国境内的注册流程不够规范化，可能给外国实体带来不确定性。此举与中国增强其在全球科学治理中角色的更广泛战略相一致。

**标签**: `#policy`, `#science`, `#technology`, `#regulation`

---

<a id="item-15"></a>
## [中国组织器官生物制造发明专利全球第一](https://www.chinanews.com.cn/gn/2026/07-04/10652855.shtml) ⭐️ 6.0/10

据中国工程院院士杨华勇透露，中国目前在组织器官生物制造领域的发明专利数量全球第一，科研产出位居世界前列。 这一领先地位标志着中国在再生医学这一前沿领域从跟跑转向领跑，有望解决供体器官短缺问题。 该消息于 2026 年 7 月 4 日在国家科技传播中心学术发展讲堂上公布，主题为组织器官生物制造研究进展。

rss · China News Service China · 7月4日 12:51

**背景**: 组织器官生物制造利用 3D 生物打印等技术制造活体组织和器官，用于移植和药物测试。中国在该领域投入巨大，清华大学、浙江大学等机构推动创新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.me.tsinghua.edu.cn/jgsz/kyjd/zzqgswzzyxfzsbjszdsys.htm">组织器官生物智造与修复再生北京市重点实验室-清华大学机械工程系</a></li>
<li><a href="http://sklofp.zju.edu.cn/skl/">流体动力基础件与机电系统全国重点实验室</a></li>

</ul>
</details>

**标签**: `#biomanufacturing`, `#tissue engineering`, `#patents`, `#China`, `#research`

---

<a id="item-16"></a>
## [我国首架大气综合航测飞机 Y-12F 首飞成功](https://www.chinanews.com.cn/gn/2026/07-05/10652920.shtml) ⭐️ 5.0/10

2026 年 7 月 2 日，我国首架大气环境综合探测固定翼飞机——运 12F 大气综合航测飞机在哈尔滨平房机场成功完成首飞。 这一里程碑填补了国内大气综合航测能力的空白，增强了中国从空中监测空气质量、天气模式和环境变化的能力。 运 12F 是由中国航空工业集团研制的双发涡桨飞机，配备多种大气传感器，用于综合环境探测。首飞标志着国家重点研发计划飞行试验的开始。

rss · China News Service China · 7月5日 00:14

**背景**: 大气航测飞机是携带仪器测量污染物、温室气体和气象参数的专业平台。运 12F 基于广泛用于运输和监视的运 12 通用飞机改装而成，新机型专为科学研究和环境监测定制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.thepaper.cn/newsDetail_forward_33515694">运12F大气综合航测飞机首飞成功_澎湃号·政务_澎湃新闻-The Paper</a></li>
<li><a href="https://www.yicai.com/news/103260506.html">运12F大气综合航测飞机首飞成功</a></li>
<li><a href="https://finance.sina.com.cn/tech/discovery/2026-07-04/doc-inifrtka9299098.shtml">填补国内空白！运12F大气综合航测飞机首飞成功_新浪科技_新浪网</a></li>

</ul>
</details>

**标签**: `#aerospace`, `#aviation`, `#China`

---

<a id="item-17"></a>
## [科技产品可能导致手部无力和视力模糊](https://www.bbc.com/zhongwen/articles/cj0gvjp5ymlo/trad?at_medium=RSS&at_campaign=rss) ⭐️ 5.0/10

BBC 一篇文章警告，长时间使用智能手机等数字设备可能会改变颈部形态、损害视力、影响运动技能并削弱肌肉力量。 这凸显了普遍使用设备带来的日益增长的健康风险，敦促用户采取更好的人体工学习惯，以防止长期身体损伤。 文章特别提到颈椎曲度改变、视力问题和手部力量减弱是常见病症，但并未提供新的科学数据。

rss · BBC Chinese · 7月5日 01:06

**背景**: 许多人每天花费数小时使用智能手机、平板电脑和电脑，且姿势不良。这可能导致“短信颈”、数字眼疲劳和重复性劳损等问题。人们对这些问题的认识有所提高，但许多用户仍不了解其累积效应。

**标签**: `#health`, `#ergonomics`, `#mobile devices`, `#digital well-being`

---

<a id="item-18"></a>
## [中国用长征六号改火箭一箭 18 星成功发射](https://www.chinanews.com.cn/gn/2026/07-04/10652877.shtml) ⭐️ 4.0/10

2026 年 7 月 4 日，中国在太原卫星发射中心使用长征六号改运载火箭，成功将千帆极轨 13 组 18 颗卫星送入预定轨道。 此次发射标志着中国千帆星座（低轨卫星互联网巨型星座）组网进入规模化部署新阶段，展示了中国在低成本、高频次卫星部署方面的能力提升。 长征六号改运载火箭太阳同步轨道运力不小于 4.5 吨，成功将 18 颗卫星送入预定轨道。千帆星座由上海市人民政府和中国科学院支持。

rss · China News Service China · 7月4日 13:44

**背景**: 千帆星座（又称 G60 星链）是中国计划中的低地球轨道卫星互联网系统，类似于 SpaceX 的 Starlink。“一箭多星”技术允许一枚火箭部署多颗卫星，降低发射成本并提高效率。长征六号改运载火箭是由中国航天科技集团八院研制的中型运载火箭。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/wiki/千帆星座">千帆星座 - 维基百科，自由的百科全书</a></li>
<li><a href="https://zh.wikipedia.org/wiki/长征六号甲运载火箭">长征六号甲运载火箭 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.stdaily.com/web/gdxw/2026-07/04/content_542195.html">长六改火箭成功发射千帆极轨13组卫星</a></li>

</ul>
</details>

**标签**: `#space`, `#satellite`, `#China`

---

<a id="item-19"></a>
## [法国能源巨头呼吁欧中合作推进能源转型](https://www.rfi.fr/cn/%E4%B8%AD%E5%9B%BD/20260704-%E6%B3%95%E5%9B%BD%E8%83%BD%E6%BA%90%E5%B7%A8%E5%A4%B4%E5%91%BC%E5%90%81%E6%AC%A7%E6%B4%B2%E4%B8%8E%E4%B8%AD%E5%9B%BD%E5%90%88%E4%BD%9C%E6%8E%A8%E8%BF%9B%E8%83%BD%E6%BA%90%E8%BD%AC%E5%9E%8B) ⭐️ 4.0/10

这标志着行业巨头推动开放合作，可能影响欧盟能源政策，并通过中欧伙伴关系加速全球能源转型。 该言论在普罗旺斯地区艾克斯经济论坛上提出，EDF 首席执行官贝尔纳·丰塔纳和道达尔能源首席执行官帕特里克·普亚内强调工业合作而非保护主义。

rss · RFI Chinese · 7月4日 21:51

**背景**: 能源转型涉及从化石燃料转向可再生能源和核能等低碳能源。欧洲和中国是主要参与者，但贸易紧张有时阻碍合作。法国能源领导人的呼吁强调了实现气候目标的务实方法。

**标签**: `#energy`, `#policy`, `#cooperation`

---

<a id="item-20"></a>
## [马斯克在 SpaceX IPO 前关于英国的帖子数量是 SpaceX 的两倍](https://www.theguardian.com/technology/2026/jul/04/elon-musk-uk-race-immigration-spacex-ipo) ⭐️ 4.0/10

《卫报》分析发现，在 2026 年 6 月 12 日 SpaceX IPO 前的 13 天里，埃隆·马斯克在 X 上关于英国种族和移民的帖子数量是 SpaceX 的两倍。 这凸显了马斯克尽管主要居住在美国，却对英国政治高度关注，引发人们对其在自己公司关键时期干预外国政治话语的质疑。 该分析涵盖了 2026 年 5 月 31 日至 6 月 12 日期间的帖子、回复和转发。SpaceX 的 IPO 是有史以来规模最大的，公司估值达 1.77 万亿美元，使马斯克成为全球首位万亿富翁。

rss · The Guardian World · 7月4日 15:00

**背景**: 埃隆·马斯克是 SpaceX 的 CEO 和 X（原 Twitter）的所有者。SpaceX 于 2026 年 6 月 12 日上市，创下 IPO 纪录。马斯克近年来对英国政治言论日益增多，常与英国政府发生冲突。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/jul/04/elon-musk-uk-race-immigration-spacex-ipo">Elon Musk posted twice as often on UK race and... | The Guardian</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_IPO">SpaceX IPO</a></li>

</ul>
</details>

**标签**: `#Elon Musk`, `#social media`, `#politics`, `#SpaceX`

---

<a id="item-21"></a>
## [Schisto & Ladders：一款教孩子了解寄生虫病的棋盘游戏](https://www.npr.org/2026/07/04/g-s1-129679/chutes-ladders-schistosomiasis-worms-parasites) ⭐️ 4.0/10

一款名为 Schisto & Ladders 的棋盘游戏被开发出来，用于教导儿童如何预防血吸虫病，这是一种由受污染水中的寄生虫传播的疾病。 这款教育工具通过让预防知识变得有趣且易于记忆，可能有助于降低流行地区儿童的感染率。 该游戏是 Chutes & Ladders 的变体，玩家会遇到各种场景，这些场景要么有助于避免感染血吸虫病，要么增加感染风险。

rss · NPR News · 7月4日 15:51

**背景**: 血吸虫病，又称蜗牛热或裂体吸虫病，是一种由寄生扁形虫引起的热带疾病。全球超过 2 亿人受影响，主要分布在非洲、亚洲和南美洲，对儿童尤其有害，会导致生长迟缓和学习困难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Schistosomiasis">Schistosomiasis</a></li>
<li><a href="https://www.cdc.gov/schistosomiasis/index.html">Schistosomiasis | CDC</a></li>

</ul>
</details>

**标签**: `#public health`, `#education`, `#board game`

---

<a id="item-22"></a>
## [影视剧架起两岸青年文化桥梁](https://www.chinanews.com.cn/gn/2026/07-05/10653014.shtml) ⭐️ 3.0/10

一篇新闻报道指出，像《延禧攻略》和《逐玉》这样的中国电视剧正被用来促进海峡两岸青年之间的文化联系。 通过流行媒体进行的这种文化交流有助于增进海峡两岸青年的相互理解和共同文化认同，这对两岸关系具有重要意义。 文章提到，《逐玉》、《沉默的荣耀》和《延禧攻略》等剧集的海报被展示，引发了台湾青年的热烈讨论。

rss · China News Service Scroll · 7月5日 04:12

**背景**: 两岸文化交流长期以来一直是改善中国大陆与台湾关系的重点。电视剧作为一种流行的娱乐形式，是分享文化价值观和传统的便捷媒介。

**标签**: `#cultural exchange`, `#TV dramas`, `#cross-strait relations`

---

<a id="item-23"></a>
## [成都举办科创发展活动，聚焦创新驱动](https://www.chinanews.com.cn/cj/2026/07-05/10652990.shtml) ⭐️ 3.0/10

2026 年 7 月 4 日，“科创中国·天府智汇加速科创发展行动”活动在成都举行，来自全国 24 个省市、36 家头部高科技企业和投融资机构的 120 名代表齐聚一堂。 该活动凸显了中国对区域创新生态系统的持续关注，以及新社会阶层在推动技术商业化中的作用，有望促进跨区域合作与投资。 该活动由四川省新的社会阶层人士联谊会组织，吸引了来自 24 个省份的参与者，显示出广泛的全国代表性。活动未宣布具体的技术突破或产品发布。

rss · China News Service Scroll · 7月5日 03:29

**背景**: “科创中国”系列是中国科学技术协会推动创新驱动发展的全国性倡议。“天府智汇”是四川本地的创新平台。该活动面向新社会阶层人士，包括科技企业和投资机构的专业人士。

**标签**: `#tech event`, `#China`, `#innovation`, `#investment`

---

<a id="item-24"></a>
## [女性影响力与人工智能峰会在斯图加特举行](https://www.chinanews.com.cn/gj/2026/07-05/10652973.shtml) ⭐️ 3.0/10

一场女性影响力与人工智能峰会在德国斯图加特举行，汇聚了来自德国、奥地利和瑞士约 100 家企业的 120 位女性决策者。 此次峰会凸显了科技和人工智能领域对性别多样性的日益关注，旨在增强女性在塑造人工智能政策和创新中的话语权。 活动邀请了来自 DACH 地区约 100 家企业的 120 位女性领导者，聚焦人工智能与女性领导力。报道未提及具体演讲者或成果。

rss · China News Service Scroll · 7月5日 03:19

**背景**: 在全球范围内，女性在人工智能和科技领导层中的代表性仍然不足。此类峰会旨在建立人脉、提供指导，并促进人工智能行业决策角色中的性别平衡。

**标签**: `#conference`, `#women in tech`, `#AI`

---

<a id="item-25"></a>
## [2026 港澳青年浙江行启动](https://www.chinanews.com.cn/tp/2026/07-05/10652955.shtml) ⭐️ 3.0/10

2026 港澳青年浙江行在杭州正式启动，活动包括官员致辞、青年创业代表分享心得，以及之江实验室主任、阿里云创始人王坚院士的主旨演讲。 该交流活动促进跨区域文化与创业联系，有望激发港澳与浙江青年之间的科技创新与合作。 活动包括澳门 AI 企业代表向浙江科创企业提问的环节，以及内地与港澳青年共同发出倡议。

rss · China News Service Scroll · 7月5日 03:02

**背景**: 这是一次常规的文化交流活动，不涉及技术深度或对软件工程、AI 研究的影响。该新闻主要为图片报道，文字细节较少。

**标签**: `#news`, `#cultural exchange`, `#youth program`

---

<a id="item-26"></a>
## [第 25 届汉语桥泰国赛区决赛举行](https://www.chinanews.com.cn/hr/2026/07-05/10653027.shtml) ⭐️ 2.0/10

第 25 届“汉语桥”世界大学生中文比赛泰国赛区决赛于 2026 年 7 月 3 日在曼谷易三仓大学举行。 该活动促进了泰中之间的语言文化交流，增进了青年一代的相互理解。 比赛由中国驻泰国大使馆组织，来自泰国各地的大学生展示了他们的中文水平。

rss · China News Service Scroll · 7月5日 04:29

**标签**: `#cultural event`, `#language competition`, `#China`

---

<a id="item-27"></a>
## [贺凯琪四赴浙江带团，陪伴港澳青年](https://www.chinanews.com.cn/dwq/2026/07-05/10653017.shtml) ⭐️ 2.0/10

中国官员贺凯琪第四次带领港澳青年团赴浙江，表示愿陪伴他们播下梦想的种子。 这反映了中国当局持续努力加强与港澳青年的联系，可能影响他们的视野和志向。 此次行程于 2026 年 7 月 5 日在浙江杭州进行，据中新网报道。贺凯琪已四次带领此类团组，表明这是一项持续性的举措。

rss · China News Service Scroll · 7月5日 04:17

**背景**: 这是一则关于内地与港澳青年交流项目的常规政治报道。此类项目旨在加强国家认同和相互理解。

**标签**: `#politics`, `#youth`, `#China`

---

<a id="item-28"></a>
## [辽台青年篮球交流活动在沈阳举行](https://www.chinanews.com.cn/gn/2026/07-05/10653015.shtml) ⭐️ 2.0/10

7 月 4 日，作为全国台联第二十三届台胞青年千人夏令营辽宁分营系列活动之一，辽台青年篮球交流活动在沈阳举行。 该活动促进台湾与辽宁青年之间的文化交流和相互理解，增进两岸民间联系。 活动包括篮球比赛和互动，来自海峡两岸的参与者进行了友好竞争和对话。

rss · China News Service Scroll · 7月5日 04:14

**背景**: 全国台联每年为台胞青年举办夏令营，促进两岸交流。今年的辽宁分营包括篮球交流等文化和体育活动。

**标签**: `#cultural exchange`, `#basketball`, `#Taiwan`, `#Liaoning`

---