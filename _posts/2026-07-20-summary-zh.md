---
layout: default
title: "Horizon Summary: 2026-07-20 (ZH)"
date: 2026-07-20
lang: zh
---

> 从 308 条内容中筛选出 28 条重要资讯。

---

1. [SRE 用 1600 美元的 ESP32 替代了 12 万美元的保龄球系统](#item-1) ⭐️ 8.0/10
2. [我国智能算力规模达 2185 EFLOPS](#item-2) ⭐️ 8.0/10
3. [Meshy 完成近 4 亿美元 B 轮融资，创 AI 3D 领域纪录](#item-3) ⭐️ 8.0/10
4. [芯展速 AI90 将 SSD 用作 GPU 显存，首 Token 延迟降低 50 倍](#item-4) ⭐️ 8.0/10
5. [鸿海拿下 SpaceX 520 亿美元 AI 服务器订单，打破戴尔/超微垄断](#item-5) ⭐️ 8.0/10
6. [Kimi 因 K3 模型需求暂停新用户订阅](#item-6) ⭐️ 8.0/10
7. [Netflix 以 5.87 亿美元收购本·阿弗莱克的 AI 电影制作初创公司](#item-7) ⭐️ 8.0/10
8. [天基通算融合初创公司星联天枢获数千万元天使轮融资](#item-8) ⭐️ 7.0/10
9. [百度昆仑芯 M100 在 WAIC 2026 首次公开展出](#item-9) ⭐️ 7.0/10
10. [摩尔线程 MTT C256 超节点：256 张 GPU 合为一台计算机](#item-10) ⭐️ 7.0/10
11. [爱芯元智发布元曦系列，AI 推理卡算力超 1000TOPS](#item-11) ⭐️ 7.0/10
12. [月之暗面拟六个月内赴港上市](#item-12) ⭐️ 7.0/10
13. [玩沙含石棉：安全保证基于未经核实的供应商数据](#item-13) ⭐️ 7.0/10
14. [澳大利亚将限制政府使用自动化 AI 决策](#item-14) ⭐️ 7.0/10
15. [奇异电池：熔盐与人类汗水储存可再生能源](#item-15) ⭐️ 7.0/10
16. [自动驾驶出租车规则之争升温](#item-16) ⭐️ 7.0/10
17. [非营利组织 Current AI 致力于构建免费 AI 网络](#item-17) ⭐️ 7.0/10
18. [中国人形机器人整机产品超全球半数](#item-18) ⭐️ 6.0/10
19. [侏儒症研究揭示预防癌症线索](#item-19) ⭐️ 6.0/10
20. [香港作家用 AI 重现上世纪六七十年代香港风貌](#item-20) ⭐️ 5.0/10
21. [超聚变在 WAIC 2026 展示企业 AI 解决方案](#item-21) ⭐️ 5.0/10
22. [中国科协年会举办光网络、AI 与工业软件论坛](#item-22) ⭐️ 5.0/10
23. [澳门创新主体获准接入珠海专利预审服务](#item-23) ⭐️ 5.0/10
24. [中国在上海成立世界人工智能合作组织](#item-24) ⭐️ 5.0/10
25. [2026 世界人工智能大会举办多场 AI 人才生态论坛](#item-25) ⭐️ 5.0/10
26. [证监会将召开稳市场专题座谈会](#item-26) ⭐️ 4.0/10
27. [健康传播会议探讨中医药参与全球慢病防治](#item-27) ⭐️ 4.0/10
28. [湖南出台办法鼓励社会力量设立科技奖](#item-28) ⭐️ 4.0/10

---

<a id="item-1"></a>
## [SRE 用 1600 美元的 ESP32 替代了 12 万美元的保龄球系统](https://news.ycombinator.com/item?id=48968606) ⭐️ 8.0/10

一位 SRE 使用 ESP32 微控制器为每对球道花费约 200 美元构建了保龄球计分系统原型，替代了成本 8 万至 12 万美元的商业系统。这个名为 OpenLaneLink 的开源项目采用了 ESPNow 网状网络、Redis 事件流和 React 前端。 这展示了现代嵌入式系统如何大幅降低改造传统工业设备的成本，挑战了供应商锁定和专有定价。它可能使小型保龄球馆更负担得起，并激发其他行业的类似 DIY 改造。 该系统采用 ESPNow 星形拓扑网状网络，并配有 RS485 有线备用方案，将传感器和继电器连接到运行 Redis 和状态机的树莓派。作者计划在准备就绪后开源硬件、固件和软件栈。

hackernews · section33 · 7月19日 14:41

**背景**: ESP32 是一种低成本、低功耗的微控制器，集成 Wi-Fi 和蓝牙，广泛用于物联网项目。保龄球计分系统通常使用基于摄像头的球瓶检测和继电器控制排瓶机，但由于市场小众和供应商锁定，商业替换成本可超过 10 万美元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ESP32">ESP32 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automatic_scorer">Automatic scorer - Wikipedia</a></li>
<li><a href="https://www.digikey.com/en/maker/blogs/2024/a-guide-for-the-esp32-microcontroller-series">A Guide for the ESP32 Microcontroller Series</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了类似经历：有人拥有使用 1970 年代 Intel 微控制器的迷你保龄球道，有人用现代控制器改造旧机床。讨论验证了该方法的可行性，并强调了用现代嵌入式技术改造传统系统的广泛适用性。

**标签**: `#embedded systems`, `#retrofit`, `#ESP32`, `#legacy systems`, `#DIY`

---

<a id="item-2"></a>
## [我国智能算力规模达 2185 EFLOPS](https://www.chinanews.com.cn/gn/2026/07-20/10662812.shtml) ⭐️ 8.0/10

据工信部消息，截至 2026 年 6 月底，我国智能算力规模达 2185 EFLOPS（FP16），同比增长 177%。 这一里程碑凸显了中国在 AI 基础设施上的快速扩张，对于训练大规模 AI 模型和保持全球 AI 竞争力至关重要。 智能算力以 FP16 精度衡量，全国算力设施整体上架率为 71.4%。围绕国家算力枢纽节点已建设超 70 条算力大通道，网络性能提升 10%。

rss · China News Service China · 7月20日 03:17

**背景**: EFLOPS 即每秒百亿亿次浮点运算，是衡量计算性能的单位。FP16（半精度）常用于 AI 训练和推理。中国一直在积极建设全国算力网络以支持 AI 发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://de.wikipedia.org/wiki/Floating_Point_Operations_Per_Second">Floating Point Operations Per Second – Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#computing power`, `#China`, `#infrastructure`, `#EFLOPS`

---

<a id="item-3"></a>
## [Meshy 完成近 4 亿美元 B 轮融资，创 AI 3D 领域纪录](https://36kr.com/newsflashes/3903365138270088?f=rss) ⭐️ 8.0/10

Meshy 宣布完成近 4 亿美元 B 轮融资，投后估值超过 100 亿元人民币，这是 AI 3D 领域迄今规模最大的单轮融资。 这笔创纪录的融资表明投资者对 AI 3D 技术信心十足，可能加速多模态 AI 模型的研发和全球市场拓展，对游戏、影视和设计等行业产生影响。 投资方包括 IDG 资本、经纬中国、Monolith 砺思资本等，现有股东 Granite Asia、红杉中国、BAI 资本、源码资本等超额跟投。资金将用于 AI 多模态模型研发和全球市场拓展。

rss · 36Kr Feed · 7月20日 02:28

**背景**: Meshy 是一款 AI 驱动的 3D 模型生成器，可在 20-30 秒内从文本或图像创建可用于生产的 3D 模型，支持 FBX、OBJ、GLB 和 STL 等格式。AI 3D 领域发展迅速，相关工具能够加速游戏、影视和设计领域的内容创作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.meshy.ai/">AI 3 D Model Generator: Create 3 D from Text & Images | Meshy</a></li>
<li><a href="https://www.crunchbase.com/organization/meshy">Meshy AI - Crunchbase Company Profile & Funding</a></li>
<li><a href="https://virtuall.pro/blog-posts/ai-tools-for-3-d-modeling">12 Best AI Tools for 3D Modeling in 2026 (Tested & Ranked)</a></li>

</ul>
</details>

**标签**: `#AI`, `#3D modeling`, `#funding`, `#venture capital`

---

<a id="item-4"></a>
## [芯展速 AI90 将 SSD 用作 GPU 显存，首 Token 延迟降低 50 倍](https://www.ithome.com/0/978/942.htm) ⭐️ 8.0/10

芯展速（GenStorAIGE）在 WAIC 2026 上发布了 AI90 AI 推理加速方案，该方案将高性能 SSD 纳入 GPU 显存体系，用于卸载 KV Cache，形成 HBM+DRAM+SSD 三级存储体系。这使首 Token 延迟从秒级降至亚秒级（提升 50 倍），吞吐量提升 5.1 倍，显存节省 39%。 该方法解决了大语言模型推理中 GPU 显存不足的关键瓶颈，使得在 RTX 5090 等消费级 GPU 上实现经济高效的部署成为可能。它通过降低硬件成本同时保持高性能，有望推动 AI 推理的普及。 AI90 方案结合智能 P2P 多卡互联技术，可使 8 卡 RTX 5090 集群的推理加速达 5.8 倍，并支持 128K+上下文。配套的 PT200Z AI SSD 采用 pSLC 闪存、PCIe Gen5 接口，DWPD 高达 100，顺序读取 14.8GB/s，随机读取 3100K IOPS，读取时延 54μs，写入时延 10μs。

rss · ITHome Feed · 7月20日 03:57

**背景**: 大语言模型推理需要存储 KV Cache（键值缓存）以避免重复计算，这会消耗大量 GPU 显存。将 KV Cache 卸载到 SSD 面临高写入负载和延迟要求的挑战。pSLC（伪 SLC）闪存将 MLC/TLC 单元以单比特模式运行，以获得更高的耐久性和性能，而 DWPD（每日全盘写入次数）是衡量 SSD 耐久性的指标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cactus-tech.com/products/industrial-pslc/">Pseudo SLC Flash ( pSLC ) Flash Memory Products - Cactus Tech</a></li>
<li><a href="https://www.szyunze.com/support/principles-advantages-and-applications-of-pslc-flash-memory/">Principles, Advantages, & Applications of pSLC Flash Memory</a></li>
<li><a href="https://www.delkin.com/blog/pslc/">pSLC | Delkin Devices</a></li>

</ul>
</details>

**标签**: `#AI inference`, `#SSD`, `#KV Cache`, `#hardware acceleration`, `#memory hierarchy`

---

<a id="item-5"></a>
## [鸿海拿下 SpaceX 520 亿美元 AI 服务器订单，打破戴尔/超微垄断](https://www.ithome.com/0/978/843.htm) ⭐️ 8.0/10

鸿海（富士康）首次获得 SpaceX 的 AI 服务器代工订单，总价值 520 亿美元，用于为 SpaceX 的 Colossus 2 数据中心生产英伟达 GB300 服务器。这笔订单打破了戴尔和超微在 AI 服务器市场的长期垄断。 这笔订单标志着 AI 服务器供应链的重大转变，鸿海进入了此前由戴尔和超微主导的市场。同时，这也凸显了 SpaceX 在 AI 基础设施上的巨额投资，其 Colossus 2 数据中心现已拥有超过 55 万颗 GPU。 该订单涵盖超过 1.3 万个机柜的英伟达 GB300 服务器，每个机柜估价 400 万美元。鸿海预计将于 2026 年第四季度开始交付。

rss · ITHome Feed · 7月20日 01:34

**背景**: 英伟达 GB300 是基于 Grace Blackwell 架构的下一代 AI 服务器平台，专为大规模 AI 训练和推理设计。SpaceX 的 Colossus 2 数据中心是全球最大的 GPU 集群之一，用于训练太空探索等领域的 AI 模型。鸿海是一家大型电子制造商，以组装苹果等科技巨头的产品而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.trendforce.com/news/2025/03/10/news-nvidia-to-unveil-gb300-at-gtc-with-shipment-reportedly-to-begin-in-may-driving-cooling-demands/">[News] NVIDIA to Unveil GB 300 at GTC, with Shipment Reportedly to...</a></li>

</ul>
</details>

**标签**: `#AI servers`, `#SpaceX`, `#Foxconn`, `#NVIDIA GB300`, `#manufacturing`

---

<a id="item-6"></a>
## [Kimi 因 K3 模型需求暂停新用户订阅](https://www.ithome.com/0/978/808.htm) ⭐️ 8.0/10

2026 年 7 月 19 日，月之暗面宣布即日起暂停 Kimi C 端新用户订阅，以优先保障现有用户，原因是新发布的 2.8 万亿参数 Kimi K3 模型需求远超预期。 此举凸显了 AI 部署中现实存在的扩展挑战，即便是头部公司在热门模型发布后也面临算力紧缺。同时，这也标志着战略重心从快速增长转向优先保障用户体验和长期信任。 Kimi K3 模型于 2026 年 7 月 16 日发布，拥有 2.8 万亿参数和 1 亿 Token 上下文窗口。月之暗面计划为未来订阅用户拆分 Kimi 主权益和 Kimi Code 权益，以更精准匹配算力。

rss · ITHome Feed · 7月19日 15:08

**背景**: Kimi 是月之暗面开发的大语言模型，以其长上下文能力著称。K3 模型是该公司迄今最强的模型，拥有 2.8 万亿参数，是全球最大的开源模型之一。发布后用户请求量激增，超出了现有算力集群的承载极限，导致订阅暂停。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.160.com/article/13216.html">月之暗面最强模型Kimi K3发布：2.8万亿参数，现在就能用 - 驱动人生</a></li>
<li><a href="https://emwap.eastmoney.com/a/202607193811848323.html">月之暗面Kimi：算力紧缺 即日起暂停C端新用户订阅 _ 东方财富网</a></li>
<li><a href="https://platform.kimi.com/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API 开放平台</a></li>

</ul>
</details>

**标签**: `#AI`, `#Kimi`, `#scaling`, `#subscription`, `#model deployment`

---

<a id="item-7"></a>
## [Netflix 以 5.87 亿美元收购本·阿弗莱克的 AI 电影制作初创公司](https://techcrunch.com/2026/07/19/netflix-paid-587m-for-ben-afflecks-ai-filmmaking-startup/) ⭐️ 8.0/10

Netflix 在 SEC 文件中披露，它于 2026 年 3 月以 5.87 亿美元现金收购了由本·阿弗莱克联合创立的 AI 电影制作初创公司 InterPositive。 此次高额收购表明 Netflix 致力于将 AI 整合到内容制作中，可能加速电影制作流程并降低成本。这也凸显了主要制片厂投资 AI 工具用于创意产业的增长趋势。 InterPositive 开发 AI 工具，可摄入原始制作样片并构建定制 AI 模型，以加速后期制作中的视觉效果（VFX）处理。此次收购为全现金交易，于 2026 年 3 月完成。

rss · TechCrunch · 7月19日 21:45

**背景**: InterPositive 是由演员兼电影制作人本·阿弗莱克联合创立的初创公司，专注于 AI 驱动的后期制作工具。其技术旨在通过针对电影的原始素材训练定制 AI 模型来简化 VFX 工作流程，可能节省时间和成本。Netflix 作为主要流媒体服务商，制作大量原创内容，并一直在探索 AI 以提高制作效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nofilmschool.com/what-does-interpositive-do">Ben Affleck’s AI Startup Reportedly Cost Netflix $600 Million. Here’s What it Actually Promises to Do | No Film School</a></li>
<li><a href="https://variety.com/2026/film/news/netflix-acquires-ben-affleck-ai-filmmaking-startup-interpositive-1236679498/">Netflix Acquires Ben Affleck's AI Filmmaker Tools Start-Up InterPositive</a></li>
<li><a href="https://mashable.com/tech/netflix-paid-587-million-for-ben-affleck-ai-startup-interpositive">Netflix bought Ben Affleck's AI startup for $587 million | Mashable</a></li>

</ul>
</details>

**标签**: `#AI`, `#acquisition`, `#Netflix`, `#filmmaking`, `#startup`

---

<a id="item-8"></a>
## [天基通算融合初创公司星联天枢获数千万元天使轮融资](https://36kr.com/p/3903365398185857?f=rss) ⭐️ 7.0/10

专注于无人系统天基通算融合的初创公司星联天枢宣布完成数千万元天使轮融资。该公司旨在让无人机、无人车等无人系统直连卫星，并在星上进行 AI 处理与决策。 这标志着中国卫星互联网产业从基础设施建设转向应用变现，瞄准无人系统对实时数据处理日益增长的需求。该方案可降低无人机、自动驾驶车辆等平台的通信成本和延迟。 该公司首款产品是重 2 公斤的 Ka 波段卫星终端，据称是国内最轻量的，并采用异构计算架构进行星上 AI 处理。该初创公司计划在 2025 年 9 月交付首批样机，明年进行星载算力载荷的在轨验证。

rss · 36Kr Feed · 7月20日 02:30

**背景**: 中国低轨卫星星座正进入规模化部署阶段，中国星网、垣信卫星等公司已取得进展。然而，行业目前正聚焦于如何将这些卫星用于实际应用。星联天枢的方法不同于建设太空数据中心，而是瞄准无人系统等特定场景，力求更快实现商业闭环。

**标签**: `#satellite internet`, `#edge computing`, `#unmanned systems`, `#startup funding`, `#AI`

---

<a id="item-9"></a>
## [百度昆仑芯 M100 在 WAIC 2026 首次公开展出](https://www.ithome.com/0/978/920.htm) ⭐️ 7.0/10

百度昆仑芯第四代 AI 芯片 M100 在 2026 世界人工智能大会上首次公开展出，该芯片针对大模型推理进行了优化，延续了自研 XPU 架构理念。 M100 芯片代表了中国国产 AI 硬件的重要进展，为大模型推理提供了高性价比的解决方案，有望减少对外国 GPU 的依赖并降低 AI 应用的部署成本。 M100 针对大规模推理场景优化，主打通用、高效和经济。百度还展示了 32/64 卡超节点产品及 256 卡超节点集群，是国内率先实现量产交付的超节点产品之一。

rss · ITHome Feed · 7月20日 03:21

**背景**: 百度昆仑芯是百度旗下的 AI 芯片子公司，专注于开发定制 AI 加速器。XPU 架构是一种专有设计，旨在平衡 AI 工作负载的性能和效率。大模型推理是指运行已训练的 AI 模型（如 GPT-4）以生成输出，这需要大量计算资源。超节点集群是连接多个 AI 芯片的高密度计算系统，用于处理大规模模型的训练和推理任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.yicaiglobal.com/news/chinas-computing-power-shifts-from-standalone-chips-to-full-system-ecosystems">China’s Computing Power Shifts From Standalone Chips to...</a></li>

</ul>
</details>

**标签**: `#AI chip`, `#large model inference`, `#Baidu Kunlun`, `#XPU architecture`

---

<a id="item-10"></a>
## [摩尔线程 MTT C256 超节点：256 张 GPU 合为一台计算机](https://www.ithome.com/0/978/856.htm) ⭐️ 7.0/10

在 2026 年世界人工智能大会上，摩尔线程首次公开展示了 MTT C256 超节点，通过创新的一层 Scale-up 网络将 256 张 GPU 聚合为一台超级计算机，实现亚微秒级延迟和 256 卡全互联。 这一突破解决了大规模 AI 训练中传统多层网络带来的带宽损耗和高延迟问题，实现了更高的 GPU 密度和更高效的分布式训练。它增强了中国本土 AI 基础设施能力，减少了对 NVLink 等国外 GPU 互联技术的依赖。 MTT C256 超节点采用计算与交换一体化高密设计，仅通过两个标准机柜即可容纳 256 张 GPU。它突破了业界普遍的一层 Scale-up 网络 64 卡限制，并支持从万卡向十万卡级平滑扩展。

rss · ITHome Feed · 7月20日 02:02

**背景**: 在大规模 AI 训练中，GPU 之间需要频繁通信。传统架构使用多层网络（如 Scale-up 和 Scale-out），会引入延迟和带宽瓶颈。摩尔线程的一层 Scale-up 网络通过将所有 256 张 GPU 直接连接在单一高速网络中简化了这一过程，类似于 NVIDIA 的 NVLink 在节点内连接 GPU，但规模更大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://naddod.medium.com/understanding-scale-up-vs-scale-out-in-ai-infrastructure-584723afb94d">Understanding Scale - Up vs. Scale-Out in AI Infrastructure | Medium</a></li>
<li><a href="https://chinabizinsider.com/moore-threads-unveils-new-architecture-and-roadmap-to-scale-ai-clusters-to-100-000-chips/">Moore Threads Unveils New Architecture and Roadmap to Scale AI...</a></li>

</ul>
</details>

**标签**: `#GPU`, `#AI infrastructure`, `#supercomputing`, `#Moore Threads`, `#WAIC`

---

<a id="item-11"></a>
## [爱芯元智发布元曦系列，AI 推理卡算力超 1000TOPS](https://www.ithome.com/0/978/841.htm) ⭐️ 7.0/10

在 WAIC 2026 上，爱芯元智发布了元曦系列大算力产品，包括算力超过 1000TOPS 的 A 系列 AI 推理卡，以及算力达 1500TOPS 的具身智能大脑控制器。 这标志着边缘 AI 和具身智能硬件的重大进步，为数据中心、多路视频分析和机器人等领域提供高性能推理解决方案，有望降低企业 AI 部署成本并提升效率。 A 系列推理卡拥有超过 1000TOPS 算力、超大显存和高带宽；大脑控制器提供 1500TOPS 算力，支持自定义算子开发，原生兼容世界模型和 VLA。此外，AX8910 视觉感知芯片已搭载于双目相机，用于商用和服务机器人。

rss · ITHome Feed · 7月20日 01:33

**背景**: 爱芯元智的元曦系列基于自研爱芯通元混合精度 NPU 架构，专为服务器集群、私有知识库等高并发高负载场景设计。该产品线与已落地的 M.2 算力卡和核心模组形成边缘算力矩阵，旨在实现可扩展、合规的 AI 部署。

**标签**: `#AI hardware`, `#edge computing`, `#NPU`, `#embodied intelligence`, `#inference acceleration`

---

<a id="item-12"></a>
## [月之暗面拟六个月内赴港上市](https://www.rfi.fr/cn/%E4%B8%AD%E5%9B%BD/20260719-%E4%B8%AD%E5%9B%BDai%E5%88%9D%E5%88%9B%E5%85%88%E9%94%8B%E6%9C%88%E4%B9%8B%E6%9A%97%E9%9D%A2%E6%8D%AE%E6%8A%A5%E6%8B%9F%E6%9C%80%E6%97%A9%E5%85%AD%E4%B8%AA%E6%9C%88%E5%86%85%E8%B5%B4%E6%B8%AF%E4%B8%8A%E5%B8%82) ⭐️ 7.0/10

据报道，中国 AI 初创公司月之暗面已向投资者发出股东决议，寻求支持其在香港上市，最早可能在未来六个月内进行 IPO。 此次 IPO 将标志着中国 AI 公司在地缘政治紧张局势下的重要里程碑，并为月之暗面提供资金以参与全球竞争，尤其是在其最新模型引发市场震荡之后。 该公司最新模型 Kimi K2 是一个万亿参数的基础模型，具备先进的编码和智能体能力，并已向全球开源社区开放。

rss · RFI Chinese · 7月19日 12:48

**背景**: 月之暗面成立于 2023 年 3 月，由清华大学校友创立，是中国六大“AI 虎”之一，专注于开发大语言模型。其公司名灵感来自平克·弗洛伊德的专辑《月之暗面》。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI</a></li>
<li><a href="https://www.moonshot.ai/about">Moonshot AI</a></li>

</ul>
</details>

**标签**: `#AI`, `#IPO`, `#China`, `#Moonshot AI`, `#Hong Kong`

---

<a id="item-13"></a>
## [玩沙含石棉：安全保证基于未经核实的供应商数据](https://www.theguardian.com/australia-news/2026/jul/20/play-sand-asbestos-safety-assurances-australia-nz-based-on-supplier-assessment) ⭐️ 7.0/10

《卫报》独家披露，澳大利亚和新西兰监管机构仅依据供应商自身的评估就向家长保证受石棉污染的玩沙健康风险低，并未进行独立检测。后续检测发现 90%的样本释放出石棉纤维，与早先的说法相矛盾。 这一监管失误削弱了公众对消费者安全机构的信任，并使儿童暴露于已知致癌物中。它凸显了依赖未经核实的行业数据进行健康风险评估的危险性。 受污染沙产品自 2025 年 11 月起被召回，涉及 20 多个品牌。发现的石棉类型为透闪石，虽被认为比青石棉危险性低，但吸入后仍具有致癌性。

rss · The Guardian World · 7月19日 15:00

**背景**: 石棉是一组天然纤维状矿物，曾广泛用于建筑和消费品，直到其健康风险被明确认识。吸入石棉纤维可导致肺癌、间皮瘤和石棉肺。澳大利亚和新西兰均已禁止石棉，但进口原材料如沙子中仍可能出现污染。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.odt.co.nz/star-news/star-districts/star-selwyn/unfortunately-it-cancer-causing-how-dangerous-asbestos-coloured-rnz">'Unfortunately it is a cancer causing': How dangerous is the asbestos ....</a></li>
<li><a href="https://www.karmactive.com/asbestos-play-sand-recall-australia-new-zealand-2025/">Asbestos In Children’s Play Sand : ACCC Recall After... - Karmactive</a></li>
<li><a href="https://www.bbc.co.uk/news/articles/cnve03m0d94o">Nearly 70 schools to close in Australia over fears of asbestos in play ...</a></li>

</ul>
</details>

**标签**: `#public health`, `#regulation`, `#asbestos`, `#consumer safety`

---

<a id="item-14"></a>
## [澳大利亚将限制政府使用自动化 AI 决策](https://www.theguardian.com/australia-news/2026/jul/19/national-ai-plan-labor-anthony-albanese-andrew-charlton) ⭐️ 7.0/10

澳大利亚新的国家 AI 计划将对政府使用自动化决策施加严格规定，范围涵盖消费者保护、工作场所安全和隐私。 这标志着政府 AI 使用的重大监管转变，可能影响全球在自动化系统公平性、准确性和透明度方面的标准。 该计划包括工党推动的数字注意义务立法，要求将安全性嵌入政府内部的 AI 流程中。

rss · The Guardian World · 7月19日 12:00

**背景**: 自动化决策是指使用 AI 在没有人工干预的情况下做出决策的系统，例如在福利资格或签证处理中。对偏见、错误和缺乏透明度的担忧已促使全球政府考虑更严格的监管。

**标签**: `#AI regulation`, `#government policy`, `#Australia`, `#automated decision-making`, `#privacy`

---

<a id="item-15"></a>
## [奇异电池：熔盐与人类汗水储存可再生能源](https://www.theguardian.com/environment/2026/jul/19/molten-salt-human-sweat-weird-batteries-store-renewable-energy) ⭐️ 7.0/10

《卫报》报道了正在试验的新型电池技术，包括熔盐和基于人类汗水的电池，用于储存可再生能源，同时阿联酋正在建设一个 5.2 吉瓦太阳能加 19 吉瓦时储能的巨型项目。 这些创新解决了可再生能源的间歇性问题，实现全天候清洁电力，减少对化石燃料的依赖，对全球脱碳至关重要。 阿联酋项目将 5.2 吉瓦太阳能容量与 19 吉瓦时电池储能相结合，成为全球最大的电池计划，覆盖面积相当于 12,600 个足球场。

rss · The Guardian World · 7月19日 11:00

**背景**: 太阳能和风能等可再生能源具有间歇性，仅在阳光照射或风吹时发电。电池等储能系统对于储存多余能量以供低发电时段使用至关重要。熔盐电池以热能形式储存能量，而基于汗水的电池利用酶从汗液中的乳酸产生电力。

**标签**: `#renewable energy`, `#energy storage`, `#batteries`, `#solar power`, `#innovation`

---

<a id="item-16"></a>
## [自动驾驶出租车规则之争升温](https://techcrunch.com/2026/07/19/techcrunch-mobility-the-battle-over-robotaxi-rules/) ⭐️ 7.0/10

TechCrunch Mobility 报道了围绕自动驾驶出租车规则的监管冲突日益激烈，联邦、州和地方政府正在就如何管理自动驾驶汽车展开辩论。 这些监管之争将塑造交通的未来，决定自动驾驶出租车部署的速度以及事故责任的归属。 文章强调，规则正在华盛顿、州议会和市政厅实时制定，NHTSA 也在 2026 年 3 月将对特斯拉 FSD 系统的调查升级为工程分析。

rss · TechCrunch · 7月19日 16:05

**背景**: 自动驾驶出租车是无需人类驾驶员即可作为出租车运营的自动驾驶车辆。其部署需要明确的法规来确保安全并解决责任问题，但目前各司法管辖区的法律差异很大，形成了复杂的拼凑局面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.axios.com/2026/07/15/robotaxi-rulebook-laws-regulations">Robotaxi growth meets a regulatory maze</a></li>
<li><a href="https://tesorb.com/robotaxi-regulatory-map-2026/">The 2026 Robotaxi Regulatory Map | Tesorb</a></li>

</ul>
</details>

**标签**: `#autonomous vehicles`, `#robotaxi`, `#regulation`, `#transportation`, `#AI`

---

<a id="item-17"></a>
## [非营利组织 Current AI 致力于构建免费 AI 网络](https://techcrunch.com/2026/07/19/nonprofit-current-ai-is-racing-to-build-the-world-wide-web-of-ai-free-for-all/) ⭐️ 7.0/10

非营利组织 Current AI 正致力于构建开放、公共的 AI 基础设施，使其跨设备和跨文化运行，旨在创建一个类似万维网的免费 AI 生态系统。 这一举措可能使 AI 访问民主化，确保全球社区（尤其是连接或资源有限的社区）能够使用和控制 AI，而无需受制于特定供应商。 Current AI 在 2026 年 2 月的印度 AI 峰会上与 Bhashini 合作，其基础设施设计为可离线运行，从而支持偏远地区的使用。

rss · TechCrunch · 7月19日 14:00

**背景**: Current AI 是一个非营利组织，专注于构建社区可以拥有和控制的公共 AI 基础设施。与大型科技公司的专有 AI 系统不同，Current AI 旨在让所有文化和设备（包括互联网接入有限的设备）都能使用 AI。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/19/nonprofit-current-ai-is-racing-to-build-the-world-wide-web-of-ai-free-for-all/">Nonprofit Current AI is racing to build the World Wide... | TechCrunch</a></li>
<li><a href="https://newsgab.com/not-for-profit-current-ai-races-to-build-open-ai-web/">Not-for- profit Current AI Racing To Build An Open AI Web - Newsgab</a></li>

</ul>
</details>

**标签**: `#AI`, `#nonprofit`, `#democratization`, `#accessibility`

---

<a id="item-18"></a>
## [中国人形机器人整机产品超全球半数](https://www.chinanews.com.cn/cj/2026/07-20/10662824.shtml) ⭐️ 6.0/10

中国工业和信息化部宣布，全球超过半数的人形机器人整机产品由中国研发，中国四足机器人占全球销量近 70%。 这凸显了中国在机器人产业中日益增强的主导地位，可能重塑全球供应链和先进制造业的竞争格局。 该数据于 2026 年 7 月 20 日在 2026 年上半年工业和信息化发展情况新闻发布会上公布。人形机器人整机产品超过 400 款。

rss · China News Service Scroll · 7月20日 03:43

**背景**: 人形机器人旨在模仿人类外观和动作，而四足机器人是四足机器，常用于巡检、搜救等任务。中国一直将人工智能和机器人作为工业战略重点进行大力投资。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://c.m.163.com/news/a/L18HI4MM05346RC6.html">今年我国 人 形 机 器 人 整 机 产 量有望突破10万台</a></li>

</ul>
</details>

**标签**: `#robotics`, `#humanoid robots`, `#quadruped robots`, `#China`, `#industry statistics`

---

<a id="item-19"></a>
## [侏儒症研究揭示预防癌症线索](https://www.bbc.com/zhongwen/articles/cvgle9q1vdxo/trad?at_medium=RSS&at_campaign=rss) ⭐️ 6.0/10

一项对 100 名侏儒症患者进行的 22 年研究发现，他们没有出现糖尿病病例，仅有一例非致命性癌症，而他们的 1600 名亲属中这两种疾病的发病率要高得多。 这一发现表明，导致侏儒症的基因突变可能也能预防癌症和糖尿病，为药物开发和长寿研究开辟了新途径。 该研究聚焦于患有 Laron 综合征的个体，这是一种由生长激素受体缺陷引起的罕见侏儒症，导致 IGF-1 水平低下。

rss · BBC Chinese · 7月19日 09:38

**背景**: 侏儒症是一种以身材矮小为特征的疾病，通常由基因突变引起。Laron 综合征是一种特定类型，身体无法利用生长激素，导致 IGF-1 水平极低。此前的研究在动物模型中已将低 IGF-1 与降低的癌症风险联系起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Laron_syndrome">Laron syndrome</a></li>
<li><a href="https://medlineplus.gov/genetics/condition/laron-syndrome/">Laron syndrome : MedlinePlus Genetics</a></li>

</ul>
</details>

**标签**: `#health`, `#cancer research`, `#genetics`, `#longevity`

---

<a id="item-20"></a>
## [香港作家用 AI 重现上世纪六七十年代香港风貌](https://www.chinanews.com.cn/dwq/2026/07-20/10662803.shtml) ⭐️ 5.0/10

香港作家杨向杰（笔名石中英）在第 36 届香港书展上发布了一部 AI 生成的短片，将其散文集《我爱秋风劲》中描写的上世纪六七十年代香港风貌可视化。 该项目展示了 AI 在文化遗产保护中的新颖应用，可能通过视觉叙事吸引年轻观众了解本地历史，凸显了 AI 在弥合历史欣赏代际差距方面的潜力。 该短片在第 36 届香港书展期间首映，散文集《我爱秋风劲》是素材来源。AI 技术被用于将文字描述转化为视觉场景。

rss · China News Service Scroll · 7月20日 03:48

**背景**: AI 生成图像在创意领域（包括电影和艺术）中越来越多地被用于重现历史场景。该项目特别针对可能对香港过去不太熟悉的年轻读者，利用现代技术让历史更易接近。

**标签**: `#AI`, `#cultural heritage`, `#Hong Kong`, `#visualization`

---

<a id="item-21"></a>
## [超聚变在 WAIC 2026 展示企业 AI 解决方案](https://www.chinanews.com.cn/cj/2026/07-20/10662835.shtml) ⭐️ 5.0/10

在 2026 世界人工智能大会上，超聚变展示了其企业 AI 解决方案，包括智企 ERP、Token Factory 智企 AI 生产系统和 TokenBox 企业 Token 生产平台，展示了从 AI 能力建设到业务价值转化的完整路径。 这很重要，因为它为企业提供了一种系统化的 AI 采用方法，可能加速各行业的 AI 整合，并为将 AI 投资转化为实际业务成果提供了蓝图。 超聚变的智企 ERP 将 AI 集成到企业资源规划中，而 Token Factory 和 TokenBox 分别专注于 AI 生产和 Token 管理。该公司还展示了生态伙伴的行业实践，以说明实际应用。

rss · China News Service Scroll · 7月20日 03:47

**背景**: 超聚变是 AI 和数据时代的全栈解决方案提供商，专注于算力、城企数智和能源智慧解决方案。WAIC（世界人工智能大会）是一个重要的全球 AI 活动，企业在此展示前沿技术。“智能体时代”的概念指的是 AI 智能体自主执行任务并驱动业务流程的未来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.xfusion.com/cn/about">关于 超聚变 - 超聚变 数字技术股份有限公司</a></li>
<li><a href="https://news.sina.com.cn/zx/gj/2026-07-19/doc-iniiirzc3432625.shtml">超聚变亮相WAIC 2026：共建 智 能体时代，看见 智 企 进化新路径 | 新浪网</a></li>

</ul>
</details>

**标签**: `#AI`, `#企业软件`, `#WAIC`, `#超聚变`

---

<a id="item-22"></a>
## [中国科协年会举办光网络、AI 与工业软件论坛](https://www.chinanews.com.cn/gn/2026/07-20/10662805.shtml) ⭐️ 5.0/10

第二十八届中国科协年会近日在北京举办了三个专题论坛，分别聚焦光信息与光网络技术、数据驱动的地球科学（融合人工智能与大数据）以及核心工业软件。 这些论坛凸显了中国对下一代通信基础设施、人工智能驱动的科学研究以及自主工业软件开发的战略重视，这些对于技术自主和数字化转型至关重要。 这些论坛是第二十八届中国科协年会的一部分，该年会是中国的重大科技政策活动。光网络论坛可能讨论了用于 5G/6G 回传的光子技术，而地球科学论坛则强调了数据同化和机器学习在地球系统建模中的应用。

rss · China News Service Scroll · 7月20日 03:44

**背景**: 光信息网络利用光传输数据，为电信提供高带宽和低延迟。数据驱动的地球科学利用人工智能和大数据改进气候模型和自然灾害预测。核心工业软件是指先进工业所需的设计、仿真和制造工具，中国正寻求减少对外依赖。

**标签**: `#optical networks`, `#AI`, `#earth sciences`, `#industrial software`, `#conference`

---

<a id="item-23"></a>
## [澳门创新主体获准接入珠海专利预审服务](https://www.chinanews.com.cn/dwq/2026/07-20/10662829.shtml) ⭐️ 5.0/10

国家知识产权局已同意将澳门特别行政区相关创新主体纳入珠海市知识产权保护中心专利预审服务范围，自 2026 年 7 月 20 日起生效。 该政策使澳门创新主体能够加速专利布局，更快获得专利授权，促进澳门与内地知识产权体系的跨境创新与融合。 专利预审服务可将专利授权时间从数年缩短至数月，但仅限于特定技术领域，且要求主体符合珠海中心设定的资格条件。

rss · China News Service Scroll · 7月20日 03:41

**背景**: 专利预审是中国知识产权保护中心为合格申请人提供的快速审查服务，旨在加速专利审查。珠海中心由广东省市场监督管理局主管，主要服务本地创新主体。此次扩展是澳门实体首次被纳入此类服务范围。

**标签**: `#intellectual property`, `#patent`, `#Macau`, `#China`, `#innovation`

---

<a id="item-24"></a>
## [中国在上海成立世界人工智能合作组织](https://www.chinanews.com.cn/gn/2026/07-19/10662599.shtml) ⭐️ 5.0/10

中国宣布在上海成立世界人工智能合作组织（WAICO），习近平主席称其为人工智能发展史上的一个重要里程碑。 这标志着全球 AI 治理迈出重要一步，为国际合作提供了新的制度框架，尤其有利于全球南方国家。 WAICO 总部设在上海，旨在促进 AI 经验分享，推动合作而非排他性控制 AI 技术。

rss · China News Service China · 7月19日 12:53

**背景**: 世界人工智能合作组织（WAICO）是一个专注于 AI 的国际组织，成立于 2026 年。中国提出该倡议，作为在联合国框架下推动全球 AI 治理的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_Artificial_Intelligence_Cooperation_Organization">World Artificial Intelligence Cooperation Organization</a></li>
<li><a href="https://www.rt.com/news/643148-china-russia-ai-organization/">The other AI superpower: How Russia and China... — RT World News</a></li>
<li><a href="https://www.trtworld.com/article/90c7ec48b92e">China calls for global AI body, greater Global South... - TRT World</a></li>

</ul>
</details>

**标签**: `#AI`, `#policy`, `#international cooperation`

---

<a id="item-25"></a>
## [2026 世界人工智能大会举办多场 AI 人才生态论坛](https://www.chinanews.com.cn/gn/2026/07-19/10662507.shtml) ⭐️ 5.0/10

2026 年 7 月 19 日，2026 世界人工智能大会暨人工智能全球治理高级别会议进入第三天，在上海世博中心举办多场聚焦 AI 人才生态的论坛及发布活动。 这些论坛凸显了培养和管理 AI 人才日益增长的重要性，这对于维持 AI 行业的创新和应对伦理挑战至关重要。 大会包含一系列论坛和发布活动，但报道未提供关于主题、演讲者或成果的具体细节。

rss · China News Service China · 7月19日 10:52

**背景**: 世界人工智能大会是一年一度的重要活动，汇聚全球专家、政策制定者和行业领袖，讨论 AI 进展与治理。对人才生态的关注反映了行业认识到熟练专业人员对于负责任的 AI 发展至关重要。

**标签**: `#AI`, `#conference`, `#talent`

---

<a id="item-26"></a>
## [证监会将召开稳市场专题座谈会](https://www.chinanews.com.cn/cj/2026/07-20/10662851.shtml) ⭐️ 4.0/10

中国证监会宣布将于 7 月 20 日召开上市公司、证券公司及基金机构座谈会，听取各方关于促进资本市场平稳健康发展的意见建议。 这表明监管机构正积极应对市场关切，可能出台影响投资者情绪和市场稳定的政策调整。 座谈会将包括上市公司、证券公司和基金机构的代表，重点讨论稳定资本市场的措施。

rss · China News Service Scroll · 7月20日 03:59

**背景**: 中国证监会是本国证券和期货市场的主要监管机构。此类座谈会是常规政策沟通的一部分，但往往预示着重要的市场导向措施。

**标签**: `#finance`, `#regulation`, `#China`

---

<a id="item-27"></a>
## [健康传播会议探讨中医药参与全球慢病防治](https://www.chinanews.com.cn/sh/2026/07-20/10662781.shtml) ⭐️ 4.0/10

第九届健康传播国际学术研讨会在北京大学举行，专家丁于洲讨论了中医药在全球慢性病防治中的作用。 这表明中医药在全球健康战略中日益受到认可，可能影响未来的慢性病管理政策。 会议期间，中国脾胃病专家、塔吉克斯坦国家科学院外籍院士丁于洲发表演讲，倡导中医药的整合。

rss · China News Service Scroll · 7月20日 03:48

**背景**: 中医药是一个拥有数千年历史的整体医学体系，常用于慢性病管理。全球卫生系统正越来越多地探索补充方法来应对日益增长的慢性病负担。

**标签**: `#health communication`, `#traditional Chinese medicine`, `#chronic disease`

---

<a id="item-28"></a>
## [湖南出台办法鼓励社会力量设立科技奖](https://www.chinanews.com.cn/sh/2026/07-20/10662743.shtml) ⭐️ 4.0/10

湖南省科学技术厅于 2026 年 7 月 19 日印发了《湖南省社会力量设立科学技术奖管理办法》，鼓励组织或个人依法设立科学技术奖，支持在重点学科和关键领域创设高水平奖项，并鼓励面向青年科技工作者、女性科技工作者以及基础和前沿领域研究人员设立奖项。 该政策使湖南的科技奖励体系更加多元化，可能增加对新兴领域和弱势研究人员的认可与资助，从而加速地方创新和人才培养。 该办法与国家科技部 2023 年发布的《社会力量设立科学技术奖管理办法》一脉相承。湖南版特别强调面向青年科技工作者、女性科技工作者以及基础和前沿领域研究人员设立奖项。

rss · China News Service Scroll · 7月20日 03:45

**背景**: 社会力量设立科学技术奖是指由企业、高校或个人等非政府实体设立的奖项，与政府奖项相对。中国一直鼓励此类奖项以补充官方认可并激发基层创新。国家层面的管理办法于 2023 年更新，以规范并促进其健康发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://most.cn/xxgk/xinxifenlei/fdzdgknr/fgzc/gfxwj/gfxwj2023/202303/t20230320_185166.html">most.cn/xxgk/xinxifenlei/fdzdgknr/fgzc/gfxwj/gfxwj2023/202303...</a></li>

</ul>
</details>

**标签**: `#science policy`, `#awards`, `#China`, `#technology management`

---