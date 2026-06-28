---
layout: default
title: "Horizon Summary: 2026-06-28 (ZH)"
date: 2026-06-28
lang: zh
---

> 从 313 条内容中筛选出 28 条重要资讯。

---

1. [DeepSeek DSpark：推测解码加速大模型推理](#item-1) ⭐️ 9.0/10
2. [央视曝光手机测评系统性作弊](#item-2) ⭐️ 8.0/10
3. [首个开源鸿蒙机器人操作系统捐赠至开放原子基金会](#item-3) ⭐️ 8.0/10
4. [近 20 年最严侧碰新国标 7 月 1 日实施](#item-4) ⭐️ 8.0/10
5. [国内首个第四代半导体全产业链项目落户郑州](#item-5) ⭐️ 8.0/10
6. [美国法案拟堵 AI 芯片出口云端漏洞](#item-6) ⭐️ 8.0/10
7. [美国允许 Anthropic 向受信机构发布 Mythos 5](#item-7) ⭐️ 8.0/10
8. [亚洲 AI 初创公司推出类 Mythos 模型应对出口禁令](#item-8) ⭐️ 7.0/10
9. [AI 需求推动功率半导体涨价潮](#item-9) ⭐️ 7.0/10
10. [比亚迪与地平线 CEO 会面，暗示智驾大单](#item-10) ⭐️ 7.0/10
11. [AI 在《文明 VI》中对决：Claude 核平法国仍落败](#item-11) ⭐️ 7.0/10
12. [苹果游说特朗普政府，寻求从被拉黑的长鑫存储采购芯片](#item-12) ⭐️ 7.0/10
13. [老人遭私域营销轰炸，77 万条未读消息](#item-13) ⭐️ 6.0/10
14. [中国成立超低轨技术创新和产业发展联盟](#item-14) ⭐️ 6.0/10
15. [大秦数字能源冲港股 IPO，锂价豪赌巨亏后扭亏](#item-15) ⭐️ 6.0/10
16. [法国将于 2026 年 9 月起征收 PFAS 排放费](#item-16) ⭐️ 6.0/10
17. [澳大利亚对规避 16 岁以下禁令的社交媒体加倍罚款](#item-17) ⭐️ 6.0/10
18. [苹果 Vision Pro 副总裁 Paul Meade 据悉将加入 OpenAI](#item-18) ⭐️ 6.0/10
19. [智能家居行业仍押注 Matter 标准](#item-19) ⭐️ 6.0/10
20. [西电发起成立网安育人共同体](#item-20) ⭐️ 5.0/10
21. [C909 支线客机商业运营十周年](#item-21) ⭐️ 5.0/10
22. [湖南湘江新区 AI 从演示走向真实应用](#item-22) ⭐️ 4.0/10
23. [中国修订黄金进出口管理办法](#item-23) ⭐️ 3.0/10
24. [中国地震局评估委内瑞拉、日本地震](#item-24) ⭐️ 3.0/10
25. [2026 年世界杯 32 强全部产生](#item-25) ⭐️ 2.0/10
26. [东南大学连续六年举办 AI 星空投影毕业典礼](#item-26) ⭐️ 2.0/10
27. [江苏招募 320 名毕业生服务基层](#item-27) ⭐️ 2.0/10
28. [第二十二届粮洽会在厦门举办](#item-28) ⭐️ 2.0/10

---

<a id="item-1"></a>
## [DeepSeek DSpark：推测解码加速大模型推理](https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf) ⭐️ 9.0/10

DeepSeek 发表了一篇关于 DSpark 的论文，该技术通过推测解码显著加速大模型推理，并已在 Hugging Face 上发布了相应模型。 这项创新解决了大模型部署中的关键瓶颈——推理延迟，使大型模型更适用于实时应用，而 DeepSeek 的开放发布与一些西方实验室日益保密的做法形成对比。 DSpark 模型（DeepSeek-V4-Flash-DSpark 和 DeepSeek-V4-Pro-DSpark）已在 Hugging Face 上发布，将推测解码模块直接集成到原始模型中。

hackernews · aurenvale · 6月27日 09:18 · [社区讨论](https://news.ycombinator.com/item?id=48696585)

**背景**: 推测解码是一种推理优化技术，由较小的草稿模型提出多个 token，较大的目标模型并行验证，在保持输出质量的同时将延迟降低 2-3 倍。该技术类似于 CPU 中的推测执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding</a></li>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/">An Introduction to Speculative Decoding for Reducing Latency in AI ...</a></li>

</ul>
</details>

**社区讨论**: 社区称赞 DeepSeek 的开放性和创新性，与美国实验室不再发布此类细节的做法形成对比。用户注意到模型已上线 Hugging Face，并对未来可能集成到本地推理表示兴奋。

**标签**: `#speculative decoding`, `#LLM inference`, `#DeepSeek`, `#AI acceleration`, `#open research`

---

<a id="item-2"></a>
## [央视曝光手机测评系统性作弊](https://36kr.com/newsflashes/3872143344817158?f=rss) ⭐️ 8.0/10

央视调查揭露，手机厂商为测评博主提供经过硬件筛选的特供媒体机、固件内置识别程序自动开启高性能模式，以及云端远程控制下发作弊配置，层层美化测评数据。 这种系统性作弊行为损害了消费者对科技测评的信任，普通用户几乎无法分辨真实性能与造假结果，严重破坏了科技媒体的公信力。 作弊体系分为三层：特供媒体机的硬件筛选、固件识别博主身份并提升性能、云端实时下发作弊配置。切换应用时仅加载界面而非完整应用，以营造流畅假象。

rss · 36Kr Feed · 6月28日 02:00

**背景**: 手机测评对消费者购买决策影响巨大。厂商长期被怀疑提供“特供媒体机”，但此次调查提供了多层作弊系统的确凿证据，这种作弊难以检测和验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sohu.com/a/1042687395_121019331">央视曝手机测评作弊乱象：厂商为测评博主专供特供媒体机、固件内置识...</a></li>
<li><a href="https://zx.sina.cn/push/2026-06-28/zx-iniexipy4073123.d.html?vt=4">央视曝手机测评作弊乱象|网络安全|远程控制|固件|央视新闻|监管_手机...</a></li>
<li><a href="https://news.qq.com/rain/a/20260628A02VGM00">央视曝手机测评作弊乱象：厂商为测评博主专供特供媒体机、固件内置识...</a></li>

</ul>
</details>

**标签**: `#tech reviews`, `#cheating`, `#smartphones`, `#consumer protection`, `#ethics`

---

<a id="item-3"></a>
## [首个开源鸿蒙机器人操作系统捐赠至开放原子基金会](https://www.ithome.com/0/969/580.htm) ⭐️ 8.0/10

深圳开鸿数字产业发展有限公司宣布，将全国首个基于开源鸿蒙的机器人操作系统 M-Robots OS 完整捐赠给开放原子开源基金会，并同步启动专属一级根社区运营。 此次捐赠标志着中国开源机器人领域的重要里程碑，提供了一个统一、低延迟的操作系统基础，可加速机器人开发并实现跨硬件互操作，有望减少行业碎片化。 M-Robots OS 2.0 具备积木式框架，支持 20 KB 到 X GB 的灵活部署，中断响应时延≤1μs，自研 M-DDS 分布式通信技术实现音视频时延低至 4 毫秒（比 Fast-DDS 降低 42%），并兼容 ROS1/ROS2 和 Dora-rs 等中间件，迁移成本降低 80%。

rss · ITHome Feed · 6月28日 03:23

**背景**: 开放原子开源基金会是中国首个开源基金会，于 2020 年成立，得到工信部及多家科技企业支持。鸿蒙是华为开发的面向多设备场景的分布式操作系统。M-Robots OS 利用鸿蒙的分布式能力，为各类机器人提供实时协同的操作系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/0/969/580.htm">两年深耕：全国首个开源鸿蒙机器人操作系统 M-Robots OS 完整捐献至开...</a></li>
<li><a href="https://www.kaihong.com/cpxg/1037.html">开源鸿蒙机器人操作系统M-Robots OS 2.0重磅发布</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAtom_Foundation">OpenAtom Foundation</a></li>

</ul>
</details>

**标签**: `#HarmonyOS`, `#robotics`, `#open-source`, `#operating system`, `#M-Robots OS`

---

<a id="item-4"></a>
## [近 20 年最严侧碰新国标 7 月 1 日实施](https://www.ithome.com/0/969/555.htm) ⭐️ 8.0/10

2026 年 7 月 1 日起，中国将实施新的汽车侧面碰撞和后方碰撞强制性国家标准，包括 GB 20071-2025《汽车侧面碰撞的乘员保护》和《乘用车后碰撞安全要求》。侧面碰撞台车质量从 950 公斤提升至 1400 公斤，并新增要求：侧碰后乘员舱内电池不得发生位移，碰撞结束后 30 分钟内不起火不爆炸。 这是近 20 年来中国侧面碰撞安全标准最重大的一次升级，大幅提高了乘员保护基线，并与国际最佳实践接轨。新标准还针对日益增长的电动汽车市场引入了具体的电池安全要求，将推动车企优化车身结构和电池防护设计，最终提升消费者安全。 侧面碰撞台车质量从 950 公斤提升至 1400 公斤，增幅近 50%，使测试更贴近与 SUV 等较重车辆碰撞的真实场景。后碰撞新标准将燃油泄漏监测收紧为前 5 分钟严控，并更新了蓄电池和车辆起火要求。

rss · ITHome Feed · 6月28日 01:30

**背景**: 中国的汽车安全标准由国家标准化管理委员会和工业和信息化部管理。此前的侧面碰撞标准（GB 20071）已实施近 20 年未作重大修订。新标准参考了 Euro NCAP 的 AE-MDB（1400 公斤）壁障等国际规程，同时纳入了针对电动汽车的独特要求，反映了中国电动汽车市场的快速增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.catarc.ac.cn/detail/f81f5330b34a427c9762be7a92e63b1b">标准解读 | 强制性国家标准《汽车侧面碰撞的乘员保护》</a></li>
<li><a href="https://news.cctv.cn/2026/06/28/ARTISxFJsTW16R54ZPdNImoT260628.shtml">侧碰后碰考核更严苛 一批汽车安全碰撞新国标将实施_新闻频道_央视网 (...</a></li>
<li><a href="https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=8F5988AF9D56501579AE48E86CF7A2AB">国家标准|GB 20071-2025</a></li>

</ul>
</details>

**标签**: `#automotive safety`, `#regulation`, `#EV safety`, `#crash testing`, `#China`

---

<a id="item-5"></a>
## [国内首个第四代半导体全产业链项目落户郑州](https://www.ithome.com/0/969/548.htm) ⭐️ 8.0/10

郑州高新区与中科粉研签署协议，建设国内首个第四代半导体材料全产业链项目，聚焦金刚石和氧化镓，总投资 15 亿元。 该项目标志着中国在先进半导体材料自给自足方面迈出关键一步，这些材料对 AI 芯片、5G/6G 通信和电动汽车至关重要，有望减少对外国供应商的依赖。 该基地将配备 500 台 MPCVD 设备用于 2-4 英寸单晶晶圆生产，以及 50 条 LPPHT 生产线用于微米/纳米球形金刚石生产，预计今年年底 200 台 MPCVD 投产，三年内年产值达 30 亿元。

rss · ITHome Feed · 6月28日 01:06

**背景**: 第四代半导体如金刚石和氧化镓是超宽禁带材料，在高温、高频、高功率应用中具有卓越性能，被誉为“终极半导体材料”，对下一代电子设备至关重要。该项目依托中科粉研于 2026 年 3 月启动的世界首条 LPPHT 微纳米金刚石产线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/1909182942628026285">解析：第四代半导体是什么？（半导体材料演变史） - 知乎</a></li>
<li><a href="https://baike.baidu.com/item/第四代半导体/67351571">第四代半导体_百度百科</a></li>
<li><a href="https://www.toutiao.com/article/7623596509266788902/">推动我国第四代半导体发展 郑州上线世界首条LPPHT微纳米金刚石产线 - ...</a></li>

</ul>
</details>

**标签**: `#semiconductor`, `#fourth-generation`, `#diamond`, `#China`, `#materials science`

---

<a id="item-6"></a>
## [美国法案拟堵 AI 芯片出口云端漏洞](https://www.rfi.fr/cn/%E4%B8%AD%E5%9B%BD/20260627-%E7%BE%8E%E8%B7%A8%E5%85%9A%E6%B4%BE%E6%8F%90%E6%B3%95%E6%A1%88%E6%8B%9F%E5%A0%B5ai%E8%8A%AF%E7%89%87%E5%87%BA%E5%8F%A3%E7%AE%A1%E5%88%B6%E6%BC%8F%E6%B4%9E-%E9%98%B2%E4%B8%AD%E5%9B%BD%E7%A7%9F%E7%94%A8%E4%BA%91%E7%AB%AF) ⭐️ 8.0/10

美国跨党派议员提出《云端安全法》，旨在填补现行 AI 芯片出口管制漏洞，防止中国通过租用美国云端服务获取先进 AI 算力，从而绕过芯片出口限制。 该法案可能大幅收紧美国对 AI 技术的出口管制，影响中国 AI 企业获取高性能算力，并重塑全球 AI 云服务市场格局。 《云端安全法》专门针对通过云服务获取先进 AI 芯片（如 NVIDIA Blackwell）的途径，这些芯片已受出口管制。该法案紧随美国商务部工业安全局近期关闭涉及海外子公司类似漏洞的行动。

rss · RFI Chinese · 6月27日 18:23

**背景**: 美国对先进 AI 芯片实施出口管制，以防止中国获取可能增强其军事能力的技术。然而，中国企业通过海外子公司购买芯片或租用美国云服务商算力等方式利用漏洞。云端安全法旨在堵住云租赁这一执行中的重大缺口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opendatascience.com/u-s-moves-to-close-nvidia-ai-chip-export-loophole-for-chinese-firms-abroad/">U.S. Moves to Close NVIDIA AI Chip Export Loophole For ...</a></li>
<li><a href="https://www.techtimes.com/articles/317905/20260606/bis-closed-china-ai-chip-loophole-trump-officials-dispute-whether-gap-ever-existed.htm">BIS Closed China AI Chip Loophole: Trump Officials Dispute ...</a></li>
<li><a href="https://informedclearly.com/en/ai/55933/chinese-ai-chip-loophole-us-export-controls-2026">The $100 Billion Loophole: How Chinese AI Firms Evaded US ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#export control`, `#cloud computing`, `#US-China tech`, `#policy`

---

<a id="item-7"></a>
## [美国允许 Anthropic 向受信机构发布 Mythos 5](https://www.rfi.fr/cn/%E7%A7%91%E6%8A%80%E4%B8%8E%E6%96%87%E5%8C%96/20260627-%E5%8D%8E%E7%9B%9B%E9%A1%BF%E5%85%81%E8%AE%B8anthropic%E5%90%91%E5%8F%97%E4%BF%A1%E4%BB%BB%E7%BE%8E%E6%9C%BA%E6%9E%84%E5%8F%91%E5%B8%83mythos-5%E6%A8%A1%E5%9E%8B-fable-5%E6%9C%80%E6%97%A9%E4%B8%8B%E5%91%A8%E8%A7%A3%E7%A6%81) ⭐️ 8.0/10

美国政府部分解除了对 Anthropic 的 Claude Mythos 5 模型的限制，允许超过 100 家受信任的美国机构（包括财富 500 强公司）访问该模型。Fable 5 预计最早下周解禁。 这标志着政府对 AI 模型部署的影响力达到了新高度，在国家安全关切与企业访问之间取得平衡。它为未来强大 AI 模型的控制和分发开创了先例。 Mythos 5 和 Fable 5 共享相同的基础架构，但 Mythos 5 的安全护栏较少，仅通过 Project Glasswing 向受信任机构开放。Fable 5 则面向公众，具有强大的安全防护措施。

rss · RFI Chinese · 6月27日 14:28

**背景**: 2026 年 6 月中旬，美国政府以国家安全风险为由，命令 Anthropic 阻止非美国公民访问 Mythos 5 和 Fable 5。这些模型是最强大的 AI 系统之一，能够自主执行软件工程和生命科学领域的长期任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://techjournal.org/us-ai-export-controls-anthropic-ban-2026">US AI Export Controls 2026: The Anthropic Ban Explained</a></li>
<li><a href="https://www.anthropic.com/claude/mythos">Claude Mythos \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#government regulation`, `#national security`, `#Claude`

---

<a id="item-8"></a>
## [亚洲 AI 初创公司推出类 Mythos 模型应对出口禁令](https://techcrunch.com/2026/06/27/asian-ai-startups-launch-mythos-like-models-as-anthropics-export-ban-drags-on/) ⭐️ 7.0/10

包括 Sakana AI 在内的亚洲 AI 初创公司推出了如 Fugu Ultra 等声称具有类 Mythos 能力的模型，而 Anthropic 的 Mythos 和 Fable 模型已被美国政府禁止出口。 这一转变可能重塑全球 AI 市场，亚洲初创公司填补了美国出口管制留下的空白，可能削弱美国 AI 实验室的市场份额和影响力。 Fugu Ultra 并非单一模型，而是一个多智能体编排系统，可在多个底层模型间路由任务，类似于 OpenRouter 的 Fusion。社区评论质疑其基准测试的可靠性和实际性能。

hackernews · TechCrunch · 6月27日 13:10 · [社区讨论](https://news.ycombinator.com/item?id=48697958)

**背景**: Anthropic 的 Mythos 是一个强大但未公开发布的 AI 模型，被认为过于危险而不适合公开发布。2026 年 6 月，美国政府以国家安全为由对 Anthropic 的 Fable 5 和 Mythos 5 实施出口管制，实质上禁止了它们在美国以外的使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mythos_(model)">Mythos (model)</a></li>
<li><a href="https://www.anthropic.com/claude/mythos">Claude Mythos \ Anthropic</a></li>
<li><a href="https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/">Anthropic disables Fable and Mythos AI models following U.S ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论对新模型的性能和基准测试可靠性表示怀疑。一位用户报告称 Fugu Ultra 比 Opus 更慢且结果更差，另一位用户指出，没有可靠的基准测试，称它们为“类 Mythos”毫无意义。

**标签**: `#AI`, `#startups`, `#export ban`, `#benchmarks`, `#models`

---

<a id="item-9"></a>
## [AI 需求推动功率半导体涨价潮](https://36kr.com/newsflashes/3871215128237313?f=rss) ⭐️ 7.0/10

功率半导体厂商因 AI 数据中心需求激增再次提价，一家国内厂商表示其 AI 相关电源订单爆满，生产根本忙不过来。 此次涨价表明，在 AI 基础设施建设推动下，功率半导体正成为继存储之后的新增长引擎。具备量产能力的国内厂商将受益，行业加速向拥有 IDM 全链条能力或与上游深度绑定的头部企业集中。 该厂商提到其产品涵盖面向数据中心 800V HVDC 等一次电源和服务器二次电源，已进入多家头部客户供应链并实现规模量产。业内人士预计本轮成本驱动的涨价周期仍将持续，加速低端功率器件产能出清。

rss · 36Kr Feed · 6月27日 09:23

**背景**: 功率半导体是数据中心服务器和 AI 加速器等设备中用于转换和管理电能的关键元件。800V HVDC 架构是 AI 数据中心的新型配电标准，相比传统的 54V 系统能提高效率并减少能量损耗。IDM（集成器件制造商）指公司内部完成芯片设计、制造、封装和销售全流程，从而对质量和供应链有更强控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/">NVIDIA 800 VDC Architecture Will Power the Next Generation of ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Integrated_device_manufacturer">Integrated device manufacturer - Wikipedia</a></li>

</ul>
</details>

**标签**: `#power semiconductors`, `#AI infrastructure`, `#hardware supply chain`, `#data centers`

---

<a id="item-10"></a>
## [比亚迪与地平线 CEO 会面，暗示智驾大单](https://www.ithome.com/0/969/591.htm) ⭐️ 7.0/10

比亚迪董事长王传福与地平线 CEO 余凯被拍到共同体验智驾，车型为比亚迪海豹，暗示双方将在智能驾驶领域深度合作。余凯随后在社交媒体上透露，正在谈一笔“特别大”的合作。 此次会面可能促成全球最大新能源汽车制造商与中国领先自动驾驶芯片公司之间的重大合作，有望加速比亚迪大众车型智能驾驶功能的普及。 地平线 HSD 2.0 全场景城区智驾方案有望在比亚迪车型上首发落地，双方可能深度协同“迪迪虾”与“咖咖虾”两大整车智能体系统。地平线“星空”舱驾融合芯片可帮助每辆车节省 1500-4000 元硬件成本。

rss · ITHome Feed · 6月28日 04:51

**背景**: 比亚迪近期发布了自研 4nm 智驾芯片“璇玑 A3”，单颗算力超 700TOPS，导致地平线股价暴跌超 7%，市场担忧大客户流失。但地平线仍是比亚迪天神之眼 C 方案主力供应商，2025 年出货约 250 万套征程 6 芯片。比亚迪需要高性价比第三方方案覆盖走量车型，以实现“智驾平权”战略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.horizon.auto/en/news/horizon-news/473">Horizon Robotics Rolls Out HSD Urban Driving Assistance ...</a></li>
<li><a href="https://www.prnewswire.com/news-releases/horizon-robotics-rolls-out-hsd-urban-driving-assistance-system-for-mass-production-global-debut-with-chery-automobile-scheduled-for-september-302432880.html">Horizon Robotics Rolls Out HSD Urban Driving Assistance ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Horizon_Robotics">Horizon Robotics - Wikipedia</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#BYD`, `#Horizon Robotics`, `#partnership`, `#smart driving`

---

<a id="item-11"></a>
## [AI 在《文明 VI》中对决：Claude 核平法国仍落败](https://www.ithome.com/0/969/570.htm) ⭐️ 7.0/10

数据科学家 Liam Wilkinson 用 76 个 MCP 工具搭建系统，让 Claude、GPT、Gemini 等四个前沿 AI 模型在《文明 VI》中对战，共进行 23 局游戏以测试其战略推理能力。其中一局，Claude 扮演的葡萄牙造出核弹摧毁了法国的文化重镇图卢兹，但最终法国以外交胜利获胜。 该实验揭示了当前 AI 模型的关键弱点，如对单一威胁的视野狭窄和长期规划能力差，这对治理和自主决策等现实应用有直接影响。它表明即使顶尖模型也难以处理多线程战略任务，挑战了仅靠扩展规模就能实现通用智能的假设。 AI 模型通过纯文本界面（无图形）接入游戏，并配有日记系统作为外部记忆。关键指标显示，AI 检查全局状态的行为仅占 1-2%（感知盲区效应），且在 10 回合内实际执行计划的比例仅为 48-66%（知行差距）。实验使用了三个逐步升级的场景：Ground Control、Snowflake 和 Cry Havoc。

rss · ITHome Feed · 6月28日 02:45

**背景**: 模型上下文协议（MCP）是一种开放协议，允许 AI 模型通过工具与外部系统交互，例如查询数据库或执行操作。《文明 VI》是一款复杂的策略游戏，玩家需要在数百回合内管理城市、单位、外交和科技，其决策空间堪比围棋。该实验受 GovBench（一个 AI 治理知识基准）启发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://modelcontextprotocol.io/specification/2025-06-18/server/tools">Tools - Model Context Protocol</a></li>
<li><a href="https://letsdatascience.com/news/ai-agent-triggers-nuclear-strike-in-civilization-vi-f7f1a843">AI Agent Triggers Nuclear Strike in Civilization VI</a></li>
<li><a href="https://arxiv.org/abs/2512.04416v1">[2512.04416v1] GovBench: Benchmarking LLM Agents for Real ... GitHub - obielin/govbench: Open benchmark dataset for agentic ... GitHub - Tanav1/GovBench www.govbench.com GovBench: FROM NATURAL LANGUAGE TO EXE CUTABLE ... - OpenReview</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#strategy game`, `#benchmarking`, `#decision-making`

---

<a id="item-12"></a>
## [苹果游说特朗普政府，寻求从被拉黑的长鑫存储采购芯片](https://www.rfi.fr/cn/%E7%A7%91%E6%8A%80%E4%B8%8E%E6%96%87%E5%8C%96/20260627-%E9%9D%A2%E5%AF%B9%E6%B6%A8%E4%BB%B7-%E8%8B%B9%E6%9E%9C%E6%AD%A3%E6%B8%B8%E8%AF%B4%E7%89%B9%E6%9C%97%E6%99%AE%E6%94%BF%E5%BA%9C-%E5%AF%BB%E6%B1%82%E8%8E%B7%E5%87%86%E4%BB%8E%E9%95%BF%E9%91%AB%E5%AD%98%E5%82%A8%E9%87%87%E8%B4%AD%E8%8A%AF%E7%89%87) ⭐️ 7.0/10

苹果正在游说特朗普政府，寻求获准从中国供应商长鑫存储（CXMT）采购 DRAM 芯片，该公司因被指与解放军有关联而被五角大楼列入黑名单。 此举凸显了苹果为分散存储芯片供应链、缓解 RAM 价格上涨压力所做的努力，同时也试探了美中科技脱钩政策的边界。 长鑫存储是中国主要的 DRAM 制造商，生产 LPDDR4、DDR4 和 DDR5 内存，并于 2026 年 6 月被列入五角大楼黑名单。苹果正寻求豁免，以便在限制下从长鑫采购芯片。

rss · RFI Chinese · 6月27日 11:59

**背景**: 五角大楼维护着一份中国军事企业黑名单，限制美国实体与其开展业务。长鑫存储于 2026 年 6 月与阿里巴巴、比亚迪等其他中国大型企业一同被列入该名单。由于供应紧张，DRAM 价格持续上涨，给苹果的利润率带来压力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CXMT">CXMT</a></li>
<li><a href="https://www.nationpress.com/sciencetech/pentagon-blacklists-alibaba-baidu-byd">Pentagon blacklist adds Alibaba, Baidu, BYD in Chinese ...</a></li>
<li><a href="https://www.fastcompany.com/91556345/pentagon-just-blacklisted-tech-giant-alibaba-electric-car-maker-byd-heres-why">Why the Pentagon blacklisted Alibaba and Chinese car maker ...</a></li>

</ul>
</details>

**标签**: `#Apple`, `#supply chain`, `#geopolitics`, `#semiconductors`, `#CXMT`

---

<a id="item-13"></a>
## [老人遭私域营销轰炸，77 万条未读消息](https://www.chinanews.com.cn/sh/2026/06-28/10648731.shtml) ⭐️ 6.0/10

一位 90 多岁的老奶奶微信收到 77 万条未读消息，并被拉入 90 多个情感陪伴账号，揭示了针对老年人的私域营销乱象。 此案例暴露了弱势老年群体如何被不受监管的私域营销所利用，引发了对数字安全、隐私保护的严重担忧，并凸显了加强老年人消费者权益保护的紧迫性。 这位奶奶的微信积累了 77 万条来自营销群的未读消息，删除后很快又新增数万条。此外，她还被订阅了 90 多个情感陪伴账号，这些账号通常以模拟陪伴为由收取费用。

rss · China News Service Scroll · 6月28日 02:52

**背景**: 私域营销是指企业通过微信等平台直接与消费者建立联系，常利用群聊和个人账号进行低成本精准推广。情感陪伴账号则提供模拟对话和情感支持服务，有时会瞄准孤独的老年人。老年人，尤其是对技术不太熟悉的群体，因其信任和参与意愿，正日益成为此类手法的目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/私域营销/67490248">私域营销_百度百科</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/502064445">一文看懂“私域”，目前最全的私域介绍 - 知乎</a></li>

</ul>
</details>

**标签**: `#social media`, `#privacy`, `#elderly`, `#marketing`

---

<a id="item-14"></a>
## [中国成立超低轨技术创新和产业发展联盟](https://www.chinanews.com.cn/gn/2026/06-27/10648613.shtml) ⭐️ 6.0/10

2026 年 6 月 27 日，由中国科学院力学研究所和中国力学学会联合主办的第二届超低轨科技学术会议在深圳召开，会上正式揭牌成立了超低轨技术创新和产业发展联盟。 该联盟整合了中国在超低轨道（VLEO）技术领域的努力，这是下一代卫星星座、遥感和 6G 通信的战略领域。它旨在加速技术突破和产业生态建设，使中国在全球空间治理中发挥更大作用。 该联盟由超低轨领域 34 家优势单位共同发起组建，涵盖科研院所、高校和企业。其使命包括推动协同创新、成果转化以及制定行业标准，以服务国家航天战略和全球空间治理需求。

rss · China News Service China · 6月27日 12:32

**背景**: 超低轨道（VLEO）通常指轨道高度低于 300 公里的区域，具有低延迟、高分辨率对地观测等优势。但由于大气阻力增大和辐射增强，VLEO 面临重大技术挑战。中国一直在积极发展 VLEO 技术，例如 2025 年 5 月“楚天”星座卫星成功完成关键试验，以及 2023 年“乾坤一号”卫星的发射。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.chinanews.com/gn/2026/06-27/10648613.shtml">中国成立超低轨技术创新和产业发展联盟 服务全球空间治理需求</a></li>
<li><a href="https://cj.sina.com.cn/articles/view/5953190046/162d6789e06703e9do">超低轨技术创新和产业发展联盟揭牌成立__财经头条__新浪财经</a></li>
<li><a href="https://www.cas.cn/cm/202505/t20250522_5069545.shtml">【科技日报】超低轨空间探索：往“更低处”抢占“制高点”</a></li>

</ul>
</details>

**标签**: `#space technology`, `#ultra-low orbit`, `#China`, `#industry alliance`, `#space governance`

---

<a id="item-15"></a>
## [大秦数字能源冲港股 IPO，锂价豪赌巨亏后扭亏](https://36kr.com/p/3871109381035011?f=rss) ⭐️ 6.0/10

大秦数字能源技术股份有限公司于 2025 年 6 月 26 日向港交所提交上市申请，此前公司从 2024 年净亏损 3.78 亿元扭转为 2025 年净利润 1.25 亿元，收入同比增长 244.3%至 25.25 亿元。 此案例凸显了锂价投机对储能公司的严重影响，而大秦的复苏和 IPO 尝试标志着随着锂价企稳和欧洲需求回暖，该行业可能出现转机。 大秦在 2023 年初碳酸锂价格高达每吨 50 万元时大量采购电芯，生产了 28.4 万台户用 ESS 电池，后来不得不低价甩卖，导致 2024 年毛利率为-19.9%，累计存货撇减超过 1.28 亿元。

rss · 36Kr Feed · 6月27日 07:37

**背景**: 碳酸锂价格在 2022-2023 年飙升至历史高位，随后在 2023 年暴跌超过 80%，重创了囤积高价库存的公司。大秦是一家专注于海外市场的中国储能制造商，严重依赖分销商（2025 年销售额的 98.2%），2025 年 61%的收入来自欧洲。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.qq.com/rain/a/20260626A0BB3I00">大秦数字能源技术股份有限公司向港交所提交上市申请书</a></li>
<li><a href="https://aiqicha.baidu.com/company_detail_30891819301130">大秦数字能源技术股份有限公司 - 大秦数字 - 爱企查</a></li>
<li><a href="https://www.dyness.cn/">大秦数能 - 全场景一站式智慧储能解决方案服务商</a></li>

</ul>
</details>

**标签**: `#储能`, `#IPO`, `#锂价`, `#财务分析`, `#能源`

---

<a id="item-16"></a>
## [法国将于 2026 年 9 月起征收 PFAS 排放费](https://www.rfi.fr/cn/%E6%B3%95%E5%9B%BD/20260627-%E6%B3%95%E5%9B%BD9%E6%9C%88%E4%BB%BD%E5%BC%80%E5%A7%8B%E5%AE%9E%E6%96%BDpfas%E7%A6%81%E4%BB%A4) ⭐️ 6.0/10

2026 年 6 月 27 日发布的法国政府法令规定，向水道排放 PFAS 的工业企业需缴纳费用，该费用自 2026 年 9 月 1 日起生效。 这项法规标志着在控制持久性化学污染方面迈出了重要一步，可能为其他国家树立先例，并迫使工业界减少 PFAS 的使用。 该费用适用于向水体排放全氟烷基和多氟烷基物质（PFAS）的工业行为，相关法令已于周六在法国官方公报上发布。

rss · RFI Chinese · 6月27日 20:32

**背景**: PFAS 被称为“永久化学品”，是合成化合物，在环境中不会分解，并在生物体内积累。它们与癌症、甲状腺疾病和免疫系统抑制等健康问题有关。法国的行动与全球监管这些物质的努力一致，此前《斯德哥尔摩公约》已将某些 PFAS 列入限制清单。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/全氟和多氟烷基物質">全氟和多氟烷基物质 - 维基百科，自由的百科全书</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1938568213265883164">PFAS全面解析与全球合规指南 - 知乎</a></li>

</ul>
</details>

**标签**: `#environmental regulation`, `#PFAS`, `#France`, `#industrial policy`

---

<a id="item-17"></a>
## [澳大利亚对规避 16 岁以下禁令的社交媒体加倍罚款](https://www.rfi.fr/cn/%E5%9B%BD%E9%99%85/20260627-%E7%BB%95%E8%BF%87%E7%A4%BE%E7%BE%A4%E5%AA%92%E4%BD%93%E7%A6%81%E4%BB%A4-%E6%BE%B3%E6%B4%B2%E5%AF%B9%E5%A4%A7%E5%9E%8B%E7%A7%91%E6%8A%80%E5%85%AC%E5%8F%B8%E7%BD%9A%E6%AC%BE%E5%8A%A0%E5%80%8D) ⭐️ 6.0/10

澳大利亚宣布将对允许 16 岁以下用户绕过禁令的社交媒体平台加倍罚款，罚款金额提高至近 6000 万欧元（9900 万澳元）。eSafety 专员正在调查 Facebook、Instagram、Snapchat、TikTok 和 YouTube 可能存在的违规行为。 此举标志着政府在社交媒体年龄限制执法上的重大升级，可能为其他国家树立先例。它迫使科技巨头实施更有效的年龄验证和内容审核系统。 罚款增加适用于未能阻止 16 岁以下用户访问其服务的平台，旨在打击普遍存在的欺诈和伤害。根据拟议的改革，eSafety 专员的信息收集权力也将得到加强。

rss · RFI Chinese · 6月27日 20:20

**背景**: 澳大利亚于 2025 年通过了全球领先的法律，禁止 16 岁以下儿童使用社交媒体，但执法面临挑战。政府认为科技公司在阻止儿童访问有害网站方面做得不够，因此提高了罚款。

**标签**: `#social media`, `#regulation`, `#Australia`, `#tech policy`

---

<a id="item-18"></a>
## [苹果 Vision Pro 副总裁 Paul Meade 据悉将加入 OpenAI](https://techcrunch.com/2026/06/27/apple-vision-pro-exec-is-reportedly-leaving-for-openai/) ⭐️ 6.0/10

据报道，负责苹果 Vision Pro 头显的副总裁 Paul Meade 将离开苹果，加入 OpenAI 的硬件团队。 此举表明 OpenAI 在硬件领域的雄心日益增强，可能开发智能眼镜或其他 AI 驱动设备，同时使苹果失去其 AR/VR 业务的关键领导者。 Meade 在苹果工作了七年，负责打造 Vision Pro，并领导苹果的智能眼镜项目。他的离职正值 OpenAI 面临交付智能眼镜的截止日期。

rss · TechCrunch · 6月27日 16:45

**背景**: Apple Vision Pro 是一款混合现实头显，于 2023 年 6 月发布，2024 年上市。它运行 visionOS，支持眼动追踪、手势和语音输入。OpenAI 一直在扩展硬件业务，据报道正在开发 AI 驱动的智能眼镜。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/27/apple-vision-pro-exec-is-reportedly-leaving-for-openai/">Apple Vision Pro exec is reportedly leaving for OpenAI</a></li>
<li><a href="https://www.techtimes.com/articles/319175/20260627/apple-vision-pro-hardware-chief-joins-openai-smart-glasses-deadline-looms.htm">Apple Vision Pro Hardware Chief Joins OpenAI As Smart Glasses ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_Vision_Pro">Apple Vision Pro</a></li>

</ul>
</details>

**标签**: `#Apple`, `#OpenAI`, `#Vision Pro`, `#hardware`, `#personnel`

---

<a id="item-19"></a>
## [智能家居行业仍押注 Matter 标准](https://www.theverge.com/tech/958008/matter-unify-conference-csa-apple-google-amazon-samsung-smart-home-interoperability) ⭐️ 6.0/10

在推出四年后，智能家居行业仍在投资 Matter 互操作性标准，据阿姆斯特丹的一场会议报道。 Matter 旨在通过使不同制造商的设备无缝协作来统一碎片化的智能家居生态系统，这可能简化消费者选择并加速智能家居的普及。 Matter 是一个基于 IPv6 的开源应用层协议，可在 Wi-Fi、Thread 和以太网上运行，并得到苹果、谷歌、亚马逊和三星等主要公司的支持。

rss · The Verge · 6月27日 13:00

**背景**: Matter，前身为 Project CHIP（Connected Home over IP），于 2022 年推出，旨在解决智能家居设备之间缺乏互操作性的问题。它在 OSI 模型的应用层运行，因此可以在各种网络技术上工作。该标准由连接标准联盟（CSA）开发和维护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Matter_(standard)">Matter (standard) - Wikipedia matter-handbook | This is the repository for the Matter ... Top Stories Welcome to Matter’s documentation — Matter documentation What Is Matter? We Explain the Smart Home Standard (2025 ... Matter Protocol in 2026: The Smart Home Interoperability ... Introduction to Matter — Matter 2.3.1-1.3 documentation</a></li>
<li><a href="https://www.wired.com/story/what-is-matter/">What Is Matter? We Explain the Smart Home Standard (2025 ...</a></li>
<li><a href="https://csa-iot.org/all-solutions/matter/">Build With Matter | Smart Home Device Solution - CSA-IOT</a></li>

</ul>
</details>

**标签**: `#smart home`, `#Matter`, `#interoperability`, `#IoT`

---

<a id="item-20"></a>
## [西电发起成立网安育人共同体](https://www.chinanews.com.cn/edu/2026/06-28/10648735.shtml) ⭐️ 5.0/10

2026 年 6 月 26 日，西安电子科技大学联合全国多所高校、科研院所及行业龙头企业，共同发起成立“网安阵线”育人共同体，探索全域协同网安育人新范式。 该举措通过整合高校、科研院所和行业龙头企业的资源，强化了中国的网络安全人才储备，直接支撑教育强国和网络强国战略。它为网络安全教育的跨机构合作树立了典范。 该共同体被描述为陕西省首个此类联盟，聚焦“全域协同网安育人”，旨在培养具备坚定政治信仰和硬核实力的网络安全人才。公告未披露具体成员单位。

rss · China News Service Scroll · 6月28日 03:08

**背景**: 在网络安全威胁日益严峻和科技自立自强战略推动下，中国的网络安全教育已成为国家优先事项。西安电子科技大学是网络安全研究和教育的领先机构。“网安阵线”育人共同体旨在打破学术界与产业界之间的壁垒，更好地培养学生应对实际挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.chinanews.com/edu/2026/06-28/10648735.shtml">“网安阵线”育人共同体在西电成立-中新网</a></li>
<li><a href="https://news.xidian.edu.cn/info/2106/304686.htm">“网安阵线”育人共同体在西电成立-西安电子科技大学新闻网</a></li>
<li><a href="https://www.163.com/dy/article/L0GRAO3V05259U67.html">陕西首个！“网安阵线”育人共同体在西电成立|教育|安全观_网易订阅</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#education`, `#collaboration`, `#China`

---

<a id="item-21"></a>
## [C909 支线客机商业运营十周年](https://www.chinanews.com.cn/gn/2026/06-28/10648722.shtml) ⭐️ 5.0/10

中国 C909 支线飞机完成商业运营十周年，累计交付 186 架，占国内支线机队 70%，载客超 3700 万人次，开通 860 余条航线。 这一里程碑表明中国商飞具备设计、认证和规模化运营支线客机的能力，为其更大的 C919 窄体机项目奠定基础，并在支线市场挑战波音-空客双头垄断格局。 C909（原 ARJ21）是一款 78-90 座级支线客机，航程 2225-3700 公里，采用 GE CF34 发动机。2024 年底从 ARJ21 更名为 C909，以统一商飞产品命名体系。

rss · China News Service China · 6月28日 02:19

**背景**: C909 是中国首款自主研制的支线客机，2014 年获得中国民航局型号合格证。它与更大的 C919 窄体机和未来的 C929 宽体机共同构成商飞的商用飞机家族。该机专为短窄跑道设计，在高温、高原和侧风条件下表现良好。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Comac_C909">Comac C909 - Wikipedia China’s COMAC takes on Boeing, Airbus — here's all you need ... Comac C919 - Wikipedia Comac C909 - Technical parameters COMAC - Company Analysis and Outlook Report 2026 (Updated) COMAC C919: China’s Narrowbody Takes On the Duopoly</a></li>
<li><a href="http://english.comac.cc/products/c909/">C909_Commercial Aircraft Corporation of China, Ltd.</a></li>
<li><a href="https://technicalparameters.eu/comac-c909/">Comac C909 - Technical parameters</a></li>

</ul>
</details>

**标签**: `#aviation`, `#China`, `#regional aircraft`, `#milestone`

---

<a id="item-22"></a>
## [湖南湘江新区 AI 从演示走向真实应用](https://www.chinanews.com.cn/cj/2026/06-28/10648738.shtml) ⭐️ 4.0/10

一篇新闻报道指出，湖南湘江新区的 AI 应用已从演示走向实际的生产和服务环境，机器人在车间分拣钢板，系统辅助临床诊疗。 这一转变表明 AI 正在关键行业中产生实际价值，可能提高制造业和医疗领域的效率与准确性，并为中国其他地区提供示范。 报道提到机器人在车间分拣钢板、AI 系统辅助医院诊疗以及 GPU 在机房支撑模型推理，但缺乏具体技术细节或性能指标。

rss · China News Service Scroll · 6月28日 03:26

**背景**: AI 长期以来在受控环境中演示，但实际部署面临硬件退化、数据质量以及与现有工作流集成等挑战。GPU 对 AI 推理至关重要，近期指南推荐 RTX 5090 等型号以实现经济高效的部署。AI 辅助诊断是一个活跃的研究领域，研究表明其有潜力改善临床决策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://slyd.com/guides/inference-gpu-guide">Best GPUs for AI Inference 2026: Complete Buying Guide</a></li>
<li><a href="https://www.sciencenewstoday.org/artificial-intelligence-in-healthcare-diagnosis-by-algorithm">Artificial Intelligence in Healthcare: Diagnosis by Algorithm</a></li>

</ul>
</details>

**标签**: `#AI`, `#industry`, `#China`, `#news`

---

<a id="item-23"></a>
## [中国修订黄金进出口管理办法](https://www.chinanews.com.cn/cj/2026/06-28/10648734.shtml) ⭐️ 3.0/10

2026 年 6 月 26 日，中国人民银行与海关总署联合发布了修订后的《黄金及黄金制品进出口管理办法（征求意见稿）》，现面向社会公开征求意见。 此次修订旨在规范黄金进出口行为，促进贸易便利化，优化营商环境，可能影响黄金市场流动性和交易者的合规要求。 该草案公开征求意见，公告中未详细说明与旧版的具体变化。此次修订属于常规监管更新。

rss · China News Service Scroll · 6月28日 03:04

**背景**: 中国是全球最大的黄金消费国和进口国之一。央行与海关总署联合监管黄金及黄金制品进出口，以防止非法流动并确保市场稳定。此前管理办法已实施多年。

**标签**: `#regulation`, `#finance`, `#gold`, `#China`

---

<a id="item-24"></a>
## [中国地震局评估委内瑞拉、日本地震](https://www.chinanews.com.cn/gn/2026/06-27/10648571.shtml) ⭐️ 3.0/10

中国地震局针对两天前委内瑞拉 7.1 级地震和日本 6.9 级地震，开展了快速灾害损失评估和专家会商研判。 这展示了中国快速评估海外地震影响的能力，有助于国际灾害响应，并加强全球地震减灾合作。 评估由中国地震局工程力学研究所牵头，多个专家团队参与。该所岩土工程中心为委内瑞拉地震产出了液化风险分布图，强震动观测中心为日本地震产出了峰值加速度和仪器烈度分布图。

rss · China News Service China · 6月27日 11:24

**背景**: 中国地震局工程力学研究所成立于 1954 年，是中国地震工程和防灾减灾领域的顶级研究机构，专注于强震动观测、工程地震、结构工程和城市防灾等。地震灾害快速评估利用地震数据和建筑易损性模型，在震后短时间内估算人员伤亡和经济损失。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.chinanews.com.cn/gn/2026/06-27/10648571.shtml">中国地震局组织开展委内瑞拉、日本地震灾害快速评估会商研判</a></li>
<li><a href="https://www.iem.ac.cn/zxgl/info?id=4346">我所迅即组织开展委内瑞拉、日本地震灾害快速评估会商研判 中国地震局...</a></li>
<li><a href="https://baike.baidu.com/item/中国地震局工程力学研究所/1159271">中国地震局工程力学研究所_百度百科 单位简介 中国地震局工程力学研究所 - IEM 中国地震局工程力学研究所 - iem.cn 中国地震局工程力学研究所 - 维基百科，自由的百科全书 中国地震局工程力学研究所_院校信息_中国研究生招生信息网 研究员 中国地震局工程力学研究所 - iem.net.cn</a></li>

</ul>
</details>

**标签**: `#earthquake`, `#disaster assessment`, `#China`

---

<a id="item-25"></a>
## [2026 年世界杯 32 强全部产生](https://www.chinanews.com.cn/ty/2026/06-28/10648761.shtml) ⭐️ 2.0/10

2026 年国际足联世界杯小组赛已经结束，所有 32 支参赛队伍均已确定。 这标志着赛事阵容的最终确定，为淘汰赛阶段和最终冠军的诞生奠定了基础。 2026 年世界杯由美国、加拿大和墨西哥联合主办，原本采用 48 支球队的扩军赛制，但文章称 32 强已经产生。

rss · China News Service Scroll · 6月28日 04:21

**标签**: `#sports`, `#world cup`, `#football`

---

<a id="item-26"></a>
## [东南大学连续六年举办 AI 星空投影毕业典礼](https://www.chinanews.com.cn/edu/2026/06-28/10648757.shtml) ⭐️ 2.0/10

2026 年 6 月 27 日，东南大学连续第六年举办“夜空中最亮的星”毕业星空投影活动，利用 AI 光影将 12908 名毕业生的姓名投射在至善亭上。 该活动展示了大学如何将科技与人文融合以创造有意义的仪式，但其技术新颖性和对 AI 研究的广泛影响有限。 投影采用 AI 光影技术，以亭台为幕布，该仪式已连续举办六年，2026 年涉及超过 12000 名毕业生。

rss · China News Service Scroll · 6月28日 03:51

**背景**: 东南大学是位于南京的中国重点大学。“星空投影”仪式是一项本地传统，利用技术个性化毕业典礼，但并不代表 AI 或光影技术的突破。

**标签**: `#education`, `#event`, `#AI lighting`

---

<a id="item-27"></a>
## [江苏招募 320 名毕业生服务基层](https://www.chinanews.com.cn/sh/2026/06-28/10648751.shtml) ⭐️ 2.0/10

江苏省于 6 月 27 日举行了 2026 年“三支一扶”计划招募笔试，计划招募 320 名高校毕业生到基层从事支教、支农、支医和帮扶乡村振兴等服务。 该计划有助于缓解高校毕业生就业压力，同时引导人才流向农村，支持中国的乡村振兴战略，体现了政府平衡城乡发展的持续努力。 考试在南京、徐州、南通等 9 个设区市同步进行。“三支一扶”计划通常服务期为 2 年，参与者在公务员考试等方面可享受政策优惠。

rss · China News Service Scroll · 6月28日 03:46

**背景**: “三支一扶”计划是中国政府发起的一项招募高校毕业生到基层从事支教、支农、支医和帮扶乡村振兴等服务的项目，是促进农村发展和解决青年就业问题的重要举措。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/三支一扶/4564826">三支一扶_百度百科</a></li>
<li><a href="https://www.gov.cn/zhengce/202505/content_7025870.htm">如何招募，有何变化?——解读2025年“三支一扶”计划</a></li>

</ul>
</details>

**标签**: `#recruitment`, `#rural revitalization`, `#China`

---

<a id="item-28"></a>
## [第二十二届粮洽会在厦门举办](https://www.chinanews.com.cn/cj/2026/06-28/10648753.shtml) ⭐️ 2.0/10

该活动促进了跨区域的粮食贸易与合作，对保障中国粮食安全、稳定粮食供应具有重要意义。 本次洽谈会聚焦粮食产销协作，汇聚了生产者、贸易商和政策制定者，共同探讨市场整合与效率提升。

rss · China News Service Scroll · 6月28日 03:45

**背景**: 粮洽会是福建省一年一度的活动，旨在加强粮食主产区和主销区之间的联系。它作为签署采购协议和分享市场信息的平台。

**标签**: `#grain trade`, `#agriculture`, `#China`

---