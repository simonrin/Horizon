---
layout: default
title: "Horizon Summary: 2026-06-18 (ZH)"
date: 2026-06-18
lang: zh
---

> 从 367 条内容中筛选出 28 条重要资讯。

---

1. [Lore：面向游戏开发的可扩展开源版本控制系统](#item-1) ⭐️ 8.0/10
2. [北大科学家创立脑机接口公司，获近亿元种子轮融资](#item-2) ⭐️ 8.0/10
3. [Transformer 核心作者 Noam Shazeer 离开谷歌加入 OpenAI](#item-3) ⭐️ 8.0/10
4. [虚幻引擎 5.8 发布：Lumen Lite 性能翻倍，支持 Switch 2](#item-4) ⭐️ 8.0/10
5. [阿里开源 LOGOS，以 1/56 参数超越微软 NatureLM](#item-5) ⭐️ 8.0/10
6. [史上第二大泄露事件曝光 240 亿条记录](#item-6) ⭐️ 8.0/10
7. [美国暂缓将逾百家中国企业列入出口管制清单](#item-7) ⭐️ 8.0/10
8. [国务院将接管 CDC 全球卫生工作](#item-8) ⭐️ 8.0/10
9. [Anthropic 断供事件后，多国领导人担忧美国掌控 AI](#item-9) ⭐️ 8.0/10
10. [俄语黑客组织大规模入侵 Fortinet 防火墙](#item-10) ⭐️ 8.0/10
11. [Odyssey 获亚马逊投资，估值达 14.5 亿美元](#item-11) ⭐️ 8.0/10
12. [多年冻土融化加速岩石风化，形成碳汇](#item-12) ⭐️ 7.0/10
13. [光纤变身“微型灵巧手”实现微纳操控](#item-13) ⭐️ 7.0/10
14. [警惕软件供应链投毒](#item-14) ⭐️ 7.0/10
15. [具身智能公司穹彻智能完成数亿元融资](#item-15) ⭐️ 7.0/10
16. [中国警告假冒公安应用窃取支付数据](#item-16) ⭐️ 7.0/10
17. [英国 CMA 要求谷歌 6 个月内整改搜索透明度](#item-17) ⭐️ 7.0/10
18. [G7 达成共识：2030 年前将对华稀土依赖降至 60%以下](#item-18) ⭐️ 7.0/10
19. [AI 公司 CEO 将与 G7 领导人会面讨论政策](#item-19) ⭐️ 7.0/10
20. [泰坦号内爆归咎于设计缺陷和群体思维](#item-20) ⭐️ 6.0/10
21. [我国启动 2026 年新能源汽车下乡活动](#item-21) ⭐️ 5.0/10
22. [中国能源转型与碳市场建设成就显著](#item-22) ⭐️ 5.0/10
23. [海南自贸港封关后出入境人员增长超三成](#item-23) ⭐️ 4.0/10
24. [2026 暑期档 IMAX“高级定制”趋势](#item-24) ⭐️ 4.0/10
25. [香港 4 所大学跻身 QS 全球五十强，港中大升至第 18 位](#item-25) ⭐️ 3.0/10
26. [国家发改委将印发现代物流领域“十五五”专项规划](#item-26) ⭐️ 3.0/10
27. [民企在文昌打造商业航天配套产业链](#item-27) ⭐️ 3.0/10
28. [北京图博会展示 AI 情绪识别与智能荐书](#item-28) ⭐️ 3.0/10

---

<a id="item-1"></a>
## [Lore：面向游戏开发的可扩展开源版本控制系统](https://lore.org/) ⭐️ 8.0/10

Epic Games 开源了 Lore，这是一个专为处理大型二进制文件和独占文件锁定而设计的下一代版本控制系统，旨在与 Perforce 竞争，服务于游戏开发领域。 Lore 解决了游戏开发中的一个关键痛点：传统版本控制系统（如 Git）难以处理大型非文本文件，而 Perforce 虽占主导地位但属于专有且复杂。Lore 的开源特性可能使各种规模的游戏工作室都能平等地使用可扩展的版本控制。 Lore 已是 Unreal Editor for Fortnite (UEFN) 的内置版本控制系统，但由于使用了专有压缩格式，当前的开源工具尚无法与 UEFN 通信。该系统设计支持任意内容类型、多维度扩展、多租户安全以及公开的版本化规范。

hackernews · regnerba · 6月17日 14:30 · [社区讨论](https://news.ycombinator.com/item?id=48571081)

**背景**: 版本控制系统（VCS）用于跟踪文件随时间的变化。Git 是代码管理的标准，但处理二进制文件效果不佳，且缺乏独占文件锁定功能，而这对于 3D 模型和纹理等游戏资产至关重要。Perforce (P4) 是游戏开发领域的现有标准，支持大文件和文件锁定，但属于专有且昂贵。Lore 旨在作为开源替代方案提供类似功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://epicgames.github.io/lore/explanation/system-design/">The Lore Version Control System - Lore Developer Documentation</a></li>
<li><a href="https://github.com/EpicGames/lore">GitHub - EpicGames/ lore : Lore is a next-generation, open source...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Perforce">Perforce - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区普遍认为 Lore 满足了游戏开发的真实需求，许多人称赞其挑战 Perforce 的潜力。一些评论者指出 Git 的用户界面不友好且不适合二进制资产，而另一些人则强调 Lore 与 Unreal Engine 工作流程的特定相关性。少数人对采用持谨慎态度，因为与 UEFN 之间存在专有压缩格式的差距。

**标签**: `#version control`, `#game development`, `#open source`, `#scalability`

---

<a id="item-2"></a>
## [北大科学家创立脑机接口公司，获近亿元种子轮融资](https://36kr.com/p/3855480467543042?f=rss) ⭐️ 8.0/10

中国侵入式脑机接口公司芯生视界完成近亿元人民币种子轮融资，由经纬创投领投，星连资本、燕缘创投、水木创投跟投。该公司旨在开发用于视觉和语言功能重建的“神经显卡”脑机接口系统。 本轮融资表明投资者对中国脑机接口领域信心增强，尤其关注超越运动控制的高带宽应用。该团队专注于视觉和语言重建，针对巨大的未满足医疗需求，可能加速实用脑机接口的进程。 该公司的“神经显卡”概念旨在实现与大脑的高通量双向通信，目标达到万通道。团队已流片出 28nm 级 256 通道脑机芯片，并计划今年推出更高通量的双向交互芯片。

rss · 36Kr Feed · 6月18日 01:34

**背景**: 侵入式脑机接口（BCI）通过将电极直接植入大脑来记录或刺激神经活动。现有 BCI 已在运动功能恢复（如控制光标）方面取得成功，但视觉和语言重建需要更高的数据带宽，因为视觉和语义信息具有高维度特性。“神经显卡”的类比指的是专门设计的芯片，用于处理实时视觉编解码所需的大规模并行数据流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eu.36kr.com/en/p/3855480467543042">Peking University Scientists Dive into Brain - Computer Interface ...</a></li>
<li><a href="https://neuralink.com/">Neuralink — Pioneering Brain Computer Interfaces</a></li>
<li><a href="https://en.wikipedia.org/wiki/Brain–computer_interface">Brain–computer interface - Wikipedia</a></li>

</ul>
</details>

**标签**: `#brain-computer interface`, `#neuralink`, `#AI`, `#startup funding`, `#neuroscience`

---

<a id="item-3"></a>
## [Transformer 核心作者 Noam Shazeer 离开谷歌加入 OpenAI](https://www.ithome.com/0/965/937.htm) ⭐️ 8.0/10

Transformer 架构的核心作者 Noam Shazeer 宣布离开谷歌加入 OpenAI，尽管谷歌在 2024 年花费 27 亿美元才将他请回。 这一举动凸显了 AI 领域对顶尖人才的激烈竞争，可能大幅提升 OpenAI 的研发能力，从而加速下一代 AI 模型的开发。 Shazeer 曾在 2021 年离开谷歌共同创立 Character.AI，谷歌后来在 2024 年通过 27 亿美元的技术许可协议将其收回。他随后在谷歌共同领导 Gemini 项目，但再次离开。

rss · ITHome Feed · 6月18日 05:07

**背景**: Transformer 架构在 2017 年的论文《Attention Is All You Need》中提出，彻底改变了深度学习，并成为 GPT-4 和 Gemini 等现代大型语言模型的基础。Noam Shazeer 被广泛认为是 AI 领域最具影响力的研究者之一，对 Transformer 和混合专家模型等关键创新做出了贡献。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Noam_Shazeer">Noam Shazeer - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Character.ai">Character.ai</a></li>
<li><a href="https://en.wikipedia.org/wiki/Transformer_architecture">Transformer architecture</a></li>

</ul>
</details>

**标签**: `#AI`, `#Transformers`, `#OpenAI`, `#Google`, `#Talent`

---

<a id="item-4"></a>
## [虚幻引擎 5.8 发布：Lumen Lite 性能翻倍，支持 Switch 2](https://www.ithome.com/0/965/932.htm) ⭐️ 8.0/10

Epic Games 于 2026 年 6 月 18 日发布了虚幻引擎 5.8，引入了 Lumen Lite——一种运行速度是 Lumen 高质量模式两倍的全新全局光照模式，以及实验性的网格体地形系统。该更新还使得在 Nintendo Switch 2 上实现 60 帧全局光照成为可能。 此次发布显著提升了实时全局光照的性能，使高质量光照在 Switch 2 等低功耗硬件上成为可能。网格体地形系统用真正的 3D 网格体取代了传统基于高度图的地形，能够创建更复杂、更逼真的环境。 Lumen Lite 使用带有探针遮挡的辐照场，以较低的 GPU 成本保持视觉质量。网格体地形在 5.8 中为实验性功能，使用非破坏性修饰符实现灵活编辑。其他更新包括 Control Rig Physics（Beta）、MegaLights 可用于生产，以及支持数千个角色的 MetaHuman 群体。

rss · ITHome Feed · 6月18日 04:45

**背景**: 虚幻引擎是一款流行的实时 3D 创作工具，用于游戏开发、电影和可视化。Lumen 是 UE5 的动态全局光照系统，能够逼真地模拟光线反弹。Switch 2 是任天堂即将推出的游戏主机，在全局光照下实现 60 帧是一项显著的技术成就。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wccftech.com/unreal-engine-5-8-lumen-lite-60-fps-switch-2/">Unreal Engine 5 . 8 Lands With Lumen Lite To Deliver 60 FPS On...</a></li>
<li><a href="https://www.pcgamer.com/software/unreal-engine-5-8-launches-with-improved-terrain-and-vegetation-tools-a-lumen-lite-option-for-faster-global-illumination-and-for-the-times-we-now-live-in-an-open-standard-plugin-for-llm-systems/">Unreal Engine 5 . 8 launches with improved terrain and... | PC Gamer</a></li>
<li><a href="https://www.techtimes.com/articles/318511/20260616/unreal-engine-58-previewed-unreal-fest-chicago-mesh-terrain-faster-lumen-games-film.htm">Unreal Engine 5.8 Previewed at Unreal Fest Chicago: Mesh Terrain, Faster Lumen for Games and Film</a></li>

</ul>
</details>

**标签**: `#Unreal Engine`, `#Game Development`, `#Real-time Rendering`, `#Graphics`

---

<a id="item-5"></a>
## [阿里开源 LOGOS，以 1/56 参数超越微软 NatureLM](https://www.ithome.com/0/965/928.htm) ⭐️ 8.0/10

阿里巴巴联合中国人民大学开源了统一科学基础模型 LOGOS，该模型采用创新的“科学语法”将多种科学对象编码为离散 Token 序列。LOGOS-1B 在六项科学任务上超越微软 NatureLM（8×7B），参数量仅为后者的 1/56。 LOGOS 表明，一个高效设计的小模型可以超越大得多的对手，通过降低计算需求可能使科学 AI 更加普及。其开源发布和统一多领域能力有望加速生物学、化学和材料科学的研究。 LOGOS 在涵盖 7 种模态的 44.87B tokens 上预训练，包括蛋白质、小分子和蛋白质-配体复合物。它通过将 3D 空间接触模式转化为离散 Token，消除了对显式 3D 坐标的需求，实现了纯序列到序列建模。

rss · ITHome Feed · 6月18日 04:33

**背景**: 传统的科学 AI 模型通常需要为不同任务（如结构预测与分子生成）设计独立架构，并依赖显式 3D 坐标。LOGOS 引入了统一的“科学语法”，将所有对象编码到共享词表中，使单一模型无需针对特定任务微调即可处理多种任务。

**标签**: `#AI`, `#open-source`, `#scientific-model`, `#efficiency`, `#NLP`

---

<a id="item-6"></a>
## [史上第二大泄露事件曝光 240 亿条记录](https://www.ithome.com/0/965/823.htm) ⭐️ 8.0/10

2025 年 6 月 12 日，Cybernews 发现了一起涉及 240 亿条记录（8.3TB）的巨型数据泄露事件，其中包含来自信息窃取软件日志的登录凭据，成为史上第二大泄露事件。 此次泄露暴露了数十亿条明文密码和邮箱地址，对全球用户构成凭证填充和账户被盗的严重风险。它凸显了信息窃取软件的持续威胁以及暴露的 Elasticsearch 集群的脆弱性。 数据来自 36 个来源，包括 Telegram 频道（超过 17 亿条记录）和一个来源不明的 226 亿条记录的集合。研究人员无法确定唯一用户数量或数据的新旧程度。

rss · ITHome Feed · 6月18日 02:56

**背景**: 信息窃取软件（infostealer）会悄悄从受感染设备中窃取凭据、cookie 等敏感数据，并常在暗网市场出售。Elasticsearch 是一种分布式搜索引擎，常用于日志分析；若配置不当未启用认证，可能将数据暴露在公网。此前的记录保持者是 2024 年的“泄露之母”（MOAB），包含 260 亿条记录（12TB）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybernews.com/security/billions-passwords-credentials-leaked-mother-of-all-breaches/">Mother of All Breaches : a Historic Data Leak Reveals 26... | Cybernews</a></li>
<li><a href="https://flare.io/glossary/stealer-logs">Stealer Logs: Guide for Security Teams - Flare</a></li>

</ul>
</details>

**标签**: `#data breach`, `#cybersecurity`, `#infostealer`, `#credentials leak`, `#Elasticsearch`

---

<a id="item-7"></a>
## [美国暂缓将逾百家中国企业列入出口管制清单](https://www.rfi.fr/cn/%E7%A7%91%E6%8A%80%E4%B8%8E%E6%96%87%E5%8C%96/20260617-%E7%BE%8E%E6%9A%82%E7%BC%93%E5%B0%86deepseek-%E9%95%BF%E9%91%AB%E5%AD%98%E5%82%A8%E7%AD%89%E9%80%BE100%E5%AE%B6%E4%B8%AD%E4%BC%81%E5%88%97%E5%85%A5%E5%87%BA%E5%8F%A3%E7%AE%A1%E5%88%B6%E5%AE%9E%E4%BD%93%E6%B8%85%E5%8D%95) ⭐️ 8.0/10

据路透社消息人士称，美国商务部暂时推迟将包括 AI 初创公司 DeepSeek 和存储芯片制造商长鑫存储（CXMT）在内的逾 100 家中国企业列入出口管制实体清单。此举被视为特朗普政府为避免与北京紧张关系升级而采取的措施。 这一延迟可能标志着美中科技脱钩策略的转变，影响 AI 和半导体供应链。同时也引发了对出口管制作为地缘政治工具有效性的质疑。 这些企业此前已被认定为国家安全风险，但尚未被正式列入实体清单。这一延迟引发了关于美国是否削弱了关键国家安全管制工具的争论。

rss · RFI Chinese · 6月17日 08:45

**背景**: 实体清单是美国出口管制工具，限制向清单上的实体出售美国技术。DeepSeek 是一家以大型语言模型闻名的中国 AI 公司，而长鑫存储是主要的 DRAM 制造商。美国越来越多地使用出口管制来限制中国获取先进技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(chatbot)">DeepSeek (chatbot) - Wikipedia</a></li>
<li><a href="https://www.lawfaremedia.org/article/recent-additions-entity-list-part-broader-us-effort-targeting-spyware">Recent Additions to Entity List Part of Broader U . S . Effort Targeting...</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#export controls`, `#AI`, `#semiconductors`, `#US-China`

---

<a id="item-8"></a>
## [国务院将接管 CDC 全球卫生工作](https://www.nytimes.com/2026/06/17/health/pepfar-cdc-cuts.html) ⭐️ 8.0/10

国务院将接管此前由 CDC 管理的多项全球卫生倡议，缩减该机构在海外疾病预防方面的作用。 这一政策转变可能削弱全球疾病监测和疫情应对能力，因为国务院缺乏 CDC 在公共卫生方面的技术专长。 批评者认为国务院缺乏有效管理这些项目所需的专业知识，引发对全球卫生安全未来的担忧。

rss · The New York Times World · 6月17日 19:43

**背景**: CDC 长期以来一直是全球卫生领域的关键参与者，在全球范围内提供技术援助和疾病监测。国务院的接管标志着美国全球卫生工作的重大重组。

**标签**: `#public health`, `#policy`, `#CDC`, `#global health`, `#government`

---

<a id="item-9"></a>
## [Anthropic 断供事件后，多国领导人担忧美国掌控 AI](https://techcrunch.com/2026/06/17/world-leaders-want-american-ai-they-just-dont-want-america-to-be-able-to-turn-it-off/) ⭐️ 8.0/10

在 G7 峰会上，法国总统马克龙和印度总理莫迪表示担忧美国可能一夜之间切断对美国 AI 系统的访问，而最近的 Anthropic 断供事件让这一担忧成为现实。 这凸显了围绕 AI 主权的日益加剧的地缘政治紧张局势，各国意识到依赖美国控制的 AI 基础设施会带来国家安全风险并削弱战略自主性。 Anthropic 断供事件指的是美国政府突然采取行动限制对 Anthropic AI 模型的访问，这引发了盟友的担忧，担心类似行动可能针对他们的国家。

rss · TechCrunch · 6月17日 19:01

**背景**: AI 主权指一个国家独立开发、控制和治理自身 AI 系统的能力。美国目前拥有 Anthropic、OpenAI 和 Google 等众多领先 AI 公司，使其在全球 AI 访问方面拥有显著影响力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blockrora.com/opinions/us-anthropic-blackout-backfires-ai-geopolitics/">The Sovereign Trap: How the US Anthropic Blackout Backfires</a></li>
<li><a href="https://www.linkedin.com/pulse/why-ai-sovereignty-matters-more-than-you-think-arpit-tandon-ncfmc">Why AI Sovereignty Matters More Than You Think</a></li>

</ul>
</details>

**标签**: `#AI`, `#geopolitics`, `#AI sovereignty`, `#Anthropic`, `#G7`

---

<a id="item-10"></a>
## [俄语黑客组织大规模入侵 Fortinet 防火墙](https://techcrunch.com/2026/06/17/cybercriminals-allegedly-hacked-tens-of-thousands-of-fortinet-firewalls-used-by-major-companies-all-over-the-world/) ⭐️ 8.0/10

一个俄语网络犯罪组织据称利用已知密码入侵了全球各大公司使用的数万台 Fortinet 防火墙。 此事件暴露了严重的操作安全失误，使用已知密码表明凭证管理不善，且大规模入侵可能导致广泛的数据泄露和网络入侵。 此次被称为“FortiBleed”的攻击针对了 32 万台 Fortinet 设备，并确认了 7.5 万个针对管理员和 SSL VPN 接口的有效凭证，影响了 194 个国家的组织。

rss · TechCrunch · 6月17日 18:20

**背景**: Fortinet 防火墙被企业广泛用于保护网络边界。攻击者利用凭证重用、凭证填充和密码喷洒攻击暴露的管理和 VPN 接口，利用了弱密码或重复使用的密码，而非零日漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.darkreading.com/cyberattacks-data-breaches/sweeping-credential-harvesting-heist-compromises-30k-fortinet-devices">Sweeping Credential Heist Compromises 30K+ Fortinet Devices</a></li>
<li><a href="https://pasqualepillitteri.it/en/news/5278/fortibleed-fortinet-vpn-credentials-stolen">FortiBleed: 75,000 Fortinet VPN Credentials Stolen Across 194 Countries</a></li>
<li><a href="https://hackread.com/fortibleed-attack-fortinet-firewalls-credentials/">FortiBleed Attack Exposes Fortinet Firewall Credentials in 194 Countries</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#Fortinet`, `#firewall`, `#data breach`, `#VPN`

---

<a id="item-11"></a>
## [Odyssey 获亚马逊投资，估值达 14.5 亿美元](https://techcrunch.com/2026/06/17/world-model-maker-odyssey-nabs-1-45b-valuation-backed-by-amazon-and-other-big-names/) ⭐️ 8.0/10

世界模型初创公司 Odyssey 完成一轮融资，估值达 14.5 亿美元，亚马逊等主要投资者参与。 这标志着业界对世界模型作为大语言模型之后的下一个前沿领域充满信心，并使 Odyssey 成为 AI 驱动模拟和交互式 3D 世界领域的关键参与者。 Odyssey 由自动驾驶先驱 Oliver Cameron 和 Jeff Hawke 创立，此前已发布 Agora-1 等模型，支持多人交互式 3D 环境。

rss · TechCrunch · 6月17日 17:43

**背景**: 世界模型是学习模拟环境运作方式（而不仅仅是外观）的 AI 系统。它们超越了大语言模型，能够实现因果、多模态的长期预测和交互。Odyssey 的技术允许用户实时与流式 3D 视频进行交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2025/05/28/odysseys-new-ai-model-streams-3d-interactive-worlds/">Odyssey 's new AI model streams 3D interactive worlds | TechCrunch</a></li>
<li><a href="https://odyssey.ml/">Odyssey</a></li>

</ul>
</details>

**标签**: `#AI`, `#world models`, `#funding`, `#startups`, `#Amazon`

---

<a id="item-12"></a>
## [多年冻土融化加速岩石风化，形成碳汇](https://www.chinanews.com.cn/cj/2026/06-18/10642925.shtml) ⭐️ 7.0/10

一项由中国团队领衔的研究发现，多年冻土融化会加速岩石的自然风化过程，这一过程能吸收二氧化碳，形成一个此前被忽视的碳汇，部分抵消了冻土融化释放的碳。 这一发现挑战了多年冻土融化仅释放碳的传统观点，有助于改进气候模型，将这一自然碳汇纳入考量，可能改变全球碳预算的估算。 研究强调，多年冻土融化虽然会增加河流二氧化碳的释放，但同时加速的岩石风化过程起到了碳汇作用，部分抵消了排放。该研究由中国团队完成，并由中新网报道。

rss · China News Service Scroll · 6月18日 03:23

**背景**: 多年冻土含有大量有机碳；随着冻土融化，微生物分解这些碳，释放二氧化碳和甲烷。岩石风化在长时间尺度上自然消耗二氧化碳，但其与冻土融化的相互作用此前了解甚少。这项研究揭示了碳循环中一个新的反馈机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Permafrost_carbon_cycle">Permafrost carbon cycle - Wikipedia</a></li>

</ul>
</details>

**标签**: `#permafrost`, `#carbon cycle`, `#climate change`, `#geoscience`

---

<a id="item-13"></a>
## [光纤变身“微型灵巧手”实现微纳操控](https://www.chinanews.com.cn/gn/2026/06-18/10642774.shtml) ⭐️ 7.0/10

安徽大学与中国科学技术大学的研究人员将光纤改造成“微型灵巧手”，能够进行先进的微纳操控。这一突破于 2026 年 6 月 18 日公布。 这项创新实现了微纳米尺度的精确操控，可能彻底改变精密工程、生物医学应用和单细胞手术等领域。它提供了一种灵活、微创的工具，可完成现有方法难以实现的任务。 “微型灵巧手”基于四芯光纤设计，能够像人手一样多方向弯曲和抓取。该技术利用光镊和光纤传感实现实时控制。

rss · China News Service China · 6月18日 01:20

**背景**: 微纳操控涉及在微米或纳米尺度上操作物体，由于尺度效应而具有挑战性。传统方法包括基于激光、微针和无线微工具的方法。光纤因其尺寸小、灵活性高而被探索用于此类任务，但实现像手一样的灵巧操控是一项重大进展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/249651249_Four-Core_Optical_Fiber_Micro-Hand">(PDF) Four-Core Optical Fiber Micro - Hand</a></li>

</ul>
</details>

**标签**: `#micro-nano manipulation`, `#optical fiber`, `#precision engineering`, `#biomedical`, `#research breakthrough`

---

<a id="item-14"></a>
## [警惕软件供应链投毒](https://www.chinanews.com.cn/gn/2026/06-18/10642752.shtml) ⭐️ 7.0/10

一篇中国新闻文章警告软件供应链投毒风险日益增长，恶意代码注入上游组件后会向下游传播，影响大量用户。 这种攻击方式可能危害广泛使用的软件，导致大规模安全漏洞，且难以检测和缓解。 文章指出，像 NPM 和 PyPI 这样的开源包生态系统是常见目标，现有的静态分析方法往往误报率较高。

rss · China News Service China · 6月17日 23:19

**背景**: 软件供应链投毒是指攻击者破坏被许多项目复用的依赖或组件。上游指依赖的原始来源，下游指依赖它的项目。一个被投毒的上游包可以感染无数下游应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Supply_chain_attack">Supply chain attack - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2409.09356">[2409.09356] Towards Robust Detection of Open Source Software Supply Chain Poisoning Attacks in Industry Environments</a></li>
<li><a href="https://en.wikipedia.org/wiki/Upstream_(software_development)">Upstream ( software development) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#software supply chain`, `#security`, `#supply chain attack`, `#cybersecurity`

---

<a id="item-15"></a>
## [具身智能公司穹彻智能完成数亿元融资](https://36kr.com/p/3856708724315400?f=rss) ⭐️ 7.0/10

具身智能企业穹彻智能（Noematrix）近日完成新一轮数亿元融资，由无锡数据集团领投，上海交通大学 AI 未来基金等跟投。公司计划于近期发布新一代具身世界模型。 本轮融资标志着具身智能行业从关注单一动作能力转向真实环境中的工程稳定性。穹彻智能的虚实结合数据策略和药房落地案例展示了具身智能走向实用化和规模化的路径。 穹彻智能的“伴随式数据采集”方案通过自研外骨骼 CoMiner 和便携式 RoboPocket 低成本采集真实数据。公司已在连锁药房部署机器人，单店投资回报周期约 1.5 至 2 年。

rss · 36Kr Feed · 6月18日 01:28

**背景**: 具身智能旨在赋予机器人理解和交互物理世界的能力。与传统机器人执行预设指令不同，具身 AI 系统利用大模型在非结构化环境中进行感知、规划和行动。行业目前正从实验室演示转向工程稳定性优先。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.noematrix.ai/noematrix-brain">具 身 智 能 大 脑 | Noematrix Brain | 穹 彻 智 能</a></li>
<li><a href="https://www.iyiou.com/news/202602101121823">专攻机器人“通用大脑”，穹彻智能完成 数 亿元A轮融资</a></li>
<li><a href="https://www.noematrix.ai/news/noematrix-pre-a++">穹彻 智 能 完成数亿元Pre-A++...</a></li>

</ul>
</details>

**标签**: `#embodied intelligence`, `#funding`, `#robotics`, `#AI`, `#startup`

---

<a id="item-16"></a>
## [中国警告假冒公安应用窃取支付数据](https://www.ithome.com/0/965/936.htm) ⭐️ 7.0/10

国家网络安全通报中心于 2025 年 6 月 18 日发布警告，提醒用户防范伪装成“公安一网通办”的恶意应用程序。该应用托管在 110GongAn.com（IP 207.56.30.188），内置木马程序，可窃取支付信息并远程控制设备。 该警告至关重要，因为该应用冒充官方政府服务，利用公众信任进行金融盗窃和间谍活动。它凸显了针对中国移动用户的社会工程学攻击日益增长的威胁。 恶意应用从 110GongAn.com（IP 207.56.30.188）下载。官方“公安一网通办”应用由公安部信息通信中心开发，用户应仅从官方应用商店或公安部平台获取。

rss · ITHome Feed · 6月18日 05:00

**背景**: 社会工程学攻击利用人类心理操纵用户安装恶意软件。在此案例中，攻击者冒充可信的政府服务以降低用户警惕。国家网络安全通报中心定期发布警报以保护公民免受此类威胁。

**标签**: `#cybersecurity`, `#malware`, `#phishing`, `#China`, `#mobile security`

---

<a id="item-17"></a>
## [英国 CMA 要求谷歌 6 个月内整改搜索透明度](https://www.ithome.com/0/965/858.htm) ⭐️ 7.0/10

英国竞争与市场管理局（CMA）发布具有法律约束力的要求，责令谷歌在六个月内整改其搜索排名算法，包括 AI 概述功能和数据可移植性。 这标志着数字市场监管的重大转变，可能为搜索引擎必须透明、公平运营树立先例，影响英国数百万用户和企业。 谷歌必须确保所有自然搜索结果仅基于客观、非歧视性标准排名，且相同规则适用于 AI 概述。公司需在三个月内完成数据可移植性架构，六个月内全面实施公平排名系统。

rss · ITHome Feed · 6月18日 03:39

**背景**: CMA 根据英国新的数字竞争框架，于 2025 年认定谷歌具有“战略市场地位”，此前英国企业投诉其排名做法不公。谷歌处理英国超过 90%的搜索查询，拥有显著市场力量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.163.com/dy/article/KBJDSQLL0514R9OJ.html">谷歌被认定英国首家“ 战 略 市 场 地 位 ”企业，将面临更严格审查| cma ...</a></li>

</ul>
</details>

**标签**: `#regulation`, `#search engine`, `#Google`, `#AI`, `#digital markets`

---

<a id="item-18"></a>
## [G7 达成共识：2030 年前将对华稀土依赖降至 60%以下](https://www.rfi.fr/cn/%E5%9B%BD%E9%99%85/20260617-g7%E8%BE%BE%E6%88%90%E5%85%B1%E8%AF%86-%E4%BB%BB%E4%BD%95%E5%8D%95%E4%B8%80%E5%9B%BD%E5%AE%B6%E4%BE%9B%E5%BA%94%E7%9A%84%E7%A8%80%E5%9C%9F%E5%9D%87%E4%B8%8D%E5%BA%94%E8%B6%85%E8%BF%87%E5%85%B6%E6%80%BB%E8%BF%9B%E5%8F%A3%E9%87%8F%E7%9A%8460) ⭐️ 7.0/10

七国集团（G7）已达成一致，到 2030 年，任何单一国家供应的稀土和永磁体不应超过其总进口量的 60%，以减少对中国的依赖。 该政策可能重塑用于电动汽车、风力涡轮机和国防技术的关键材料的全球供应链，削弱中国在市场上的主导地位。 该目标适用于稀土元素和永磁体，而中国目前控制着这些材料超过 90%的加工能力。

rss · RFI Chinese · 6月17日 14:19

**背景**: 稀土元素对于智能手机、电动汽车电机和军事装备等高科技产品至关重要。中国在全球开采和加工领域占据主导地位，拥有显著的地缘政治影响力。G7 此举旨在实现供应来源多元化，增强供应链安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://businessengineer.ai/p/rare-earth-minerals-and-ai-supply">Rare Earth Minerals & AI Supply Chain Geopolitics</a></li>

</ul>
</details>

**标签**: `#geopolitics`, `#rare earths`, `#supply chain`, `#trade policy`, `#technology`

---

<a id="item-19"></a>
## [AI 公司 CEO 将与 G7 领导人会面讨论政策](https://www.nytimes.com/2026/06/17/world/europe/g7-summit-ai-tech-leaders-openai-anthropic.html) ⭐️ 7.0/10

Anthropic、OpenAI 和 Mistral 的 CEO 将参加与 G7 领导人的午餐会，讨论 AI 政策。 此次会议表明 AI 治理正成为世界领导人的首要议题，与行业高管的直接对话可能影响未来监管方向。 该会议是 G7 峰会的一部分，参会 CEO 来自美国和欧洲领先的 AI 公司，凸显了 AI 政策讨论的全球性。

rss · The New York Times World · 6月17日 12:08

**背景**: G7 是由七个主要发达经济体组成的集团，每年举行会议讨论全球议题。随着 AI 技术快速发展，AI 治理已成为关键议题，涉及安全、伦理和经济影响等担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Arthur_Mensch">Arthur Mensch - Wikipedia</a></li>
<li><a href="https://mistral.ai/about/">About Mistral | Open, frontier AI for all.</a></li>

</ul>
</details>

**标签**: `#AI`, `#policy`, `#G7`, `#governance`, `#tech industry`

---

<a id="item-20"></a>
## [泰坦号内爆归咎于设计缺陷和群体思维](https://www.theguardian.com/world/2026/jun/17/titan-sub-design-flaws-company-groupthink-report) ⭐️ 6.0/10

加拿大安全官员于 2026 年 6 月 17 日发布报告，结论认为 2023 年 6 月泰坦号潜水器的灾难性内爆是由设计缺陷、测试不足以及 OceanGate 公司内部的群体思维和确认偏误文化所致。 该报告强调了高风险环境中工程安全的关键教训，揭示了组织文化和测试不足如何导致灾难性故障。它可能影响未来载人潜水器及其他安全关键系统的监管。 泰坦号的船体采用碳纤维材料，该材料此前未获认证用于载人深海潜水器，且公司未进行全面测试。报告还指出，此前一次潜水中听到的巨响表明存在结构损伤，但被忽视。

rss · The Guardian World · 6月17日 18:24

**背景**: 泰坦号潜水器于 2023 年 6 月 18 日在前往泰坦尼克号残骸途中内爆，导致船上五人全部遇难。运营商 OceanGate 曾宣传该潜水器具有创新性，但多次遭到专家对其非常规设计的警告。群体思维是一种心理现象，即追求共识的愿望压倒了风险的关键评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Titan_submersible_implosion">Titan submersible implosion - Wikipedia</a></li>
<li><a href="https://www.wkyt.com/2024/09/25/ntsb-engineer-says-carbon-fiber-hull-titan-submersible-showed-signs-flaws/">NTSB engineer says carbon fiber hull from Titan submersible ...</a></li>
<li><a href="https://www.wired.com/story/us-coast-guard-report-titan-submersible-implosion-oceangate-ceo-stockton-rush/">US Coast Guard Report on Titan Submersible Implosion... | WIRED</a></li>

</ul>
</details>

**标签**: `#engineering`, `#safety`, `#failure analysis`, `#submersible`

---

<a id="item-21"></a>
## [我国启动 2026 年新能源汽车下乡活动](https://www.chinanews.com.cn/cj/2026/06-18/10642956.shtml) ⭐️ 5.0/10

2026 年 6 月 18 日，工业和信息化部、商务部等五部门联合发布通知，启动 2026 年新能源汽车下乡活动，活动设置以旧换新专区，且乡村地区消费者申领补贴不受资格数量限制。 该政策旨在提升新能源汽车在农村地区的普及率（目前仍较低），有望扩大中国新能源汽车市场，并助力实现碳中和目标。 活动选取新能源汽车推广比例不高、市场潜力较大的典型县域城市，通过线下活动、试乘试驾和直播引流等方式吸引消费者。同时推动充换电设施、保险、信贷等配套服务协同下乡。

rss · China News Service Scroll · 6月18日 04:54

**背景**: 中国的新能源汽车下乡活动已开展多年，是刺激绿色消费、升级农村交通的举措之一。以旧换新政策允许消费者在购买新能源汽车时用旧车换取补贴，资金由中央和地方按比例分担。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.pedaily.cn/202506/550571.shtml">新 能 源 汽 车 下 乡 又来了，但 乡 亲们真想换掉油 车 吗？_ 投资界</a></li>
<li><a href="http://paper.people.com.cn/rmrb/images/2023-08/10/02/rmrb2023081002.pdf">YW2BRMRB02B20230810C</a></li>

</ul>
</details>

**标签**: `#new energy vehicles`, `#China policy`, `#automotive industry`

---

<a id="item-22"></a>
## [中国能源转型与碳市场建设成就显著](https://www.chinanews.com.cn/gn/2026/06-18/10642736.shtml) ⭐️ 5.0/10

中国生态环境部宣布，可再生能源装机占发电总装机的比例已超过 60%，风电、太阳能发电装机总容量和蓄电量已提前实现中国 2030 年国家自主贡献目标。 这一里程碑表明中国在能源系统脱碳方面取得了重大进展，巩固了其在可再生能源部署和气候行动中的全球领先地位。这也表明中国的碳市场和能源转型政策正在有效推动减排。 该声明由副部长李高在广西南宁的一次活动中宣布。数据反映的是装机容量而非实际发电量，且提前实现 2030 年国家自主贡献目标是基于风电、太阳能和储能的合计容量。

rss · China News Service China · 6月17日 17:06

**背景**: 中国的国家自主贡献目标是其在《巴黎协定》下的气候行动目标。2030 年国家自主贡献目标包括碳达峰和提高非化石能源在一次能源消费中的比重。中国一直在快速扩大可再生能源并建设全国碳市场以促进排放交易。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.stats.gov.cn/zs/tjwh/tjkw/tjqk/zgxxb/202508/P020250827312516488419.pdf">02B20250827C</a></li>
<li><a href="https://m.ithome.com/html/943852.htm">占 比 超六成：我国 可 再 生 能 源 截至 3 月底累计 装 机 约 24 亿千瓦 - IT之家</a></li>
<li><a href="http://scces.cn/newsinfo/8766994.html">中 国 2035年 国 家 自 主 贡 献 目 标 意味着什么-企业官网</a></li>

</ul>
</details>

**标签**: `#energy transition`, `#carbon market`, `#China`, `#renewable energy`, `#climate change`

---

<a id="item-23"></a>
## [海南自贸港封关后出入境人员增长超三成](https://www.chinanews.com.cn/cj/2026/06-18/10642922.shtml) ⭐️ 4.0/10

自 2025 年 12 月 18 日海南自贸港全岛封关运作以来，边检机关累计检查出入境人员 165.4 万人次，同比增长超三成。其中，逾九成入境外籍旅客是免签入境。 这一数据表明海南自贸港封关政策在促进旅游和国际人员流动方面立竿见影。免签入境人数激增，显示出全球兴趣的增长，并可能进一步推动海南融入全球经济。 封关于 2025 年 12 月 18 日正式启动，使海南成为特殊海关监管区域，对大部分货物实施零关税政策。目前，85 个国家的人员可免签入境海南。

rss · China News Service Scroll · 6月18日 03:21

**背景**: 海南自贸港是中国的一项重大举措，旨在到 2025 年建成具有全球影响力的自由贸易港。"全岛封关"意味着海南作为单独关税区运作，促进货物、人员、资金和数据更自由流动。该政策被视为中国进一步扩大开放的标志性步骤。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.gmw.cn/2025-12/21/content_38489690.htm">这五个方面 带你读懂 海 南 自 贸 港 全 岛 封 关</a></li>
<li><a href="https://www.163.com/dy/article/KGTGRS8305149D15.html">定了！12月18日起 海 南 全 岛 封 关 ，对你我有何影响？</a></li>
<li><a href="https://m.mp.oeeee.com/a/BAAFRD0000202512191496118.html">海 南 自贸港封关利好旅游业：元旦三亚酒店搜索热度暴涨2倍</a></li>

</ul>
</details>

**标签**: `#policy`, `#travel`, `#China`

---

<a id="item-24"></a>
## [2026 暑期档 IMAX“高级定制”趋势](https://www.chinanews.com.cn/cul/2026/06-18/10642911.shtml) ⭐️ 4.0/10

一篇中国新闻文章指出，2026 年暑期档票房证实了电影行业正转向 IMAX 等高端格式的“高级定制”，超越了关于此类银幕是否值得投资的争论。 这一趋势标志着制片方和影院运营商的战略转向，因为高端巨幕（PLF）成为吸引观众和最大化收入的关键差异化因素，可能重塑制作和发行策略。 文章提及 2026 年暑期档片单，包括计划以 IMAX 和多种 PLF 格式上映的《奥德赛》等影片，表明制片方正越来越多地为这些格式定制内容。

rss · China News Service Scroll · 6月18日 03:09

**背景**: 高端巨幕（PLF）影院（如 IMAX）提供增强的银幕、音响和座椅，票价更高。行业长期以来对安装此类银幕的投资回报存在争议，但近期票房趋势表明，观众愿意为差异化体验支付更高价格，推动制片方制作针对这些格式优化的内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/The_Odyssey_(2026_film)">The Odyssey ( 2026 film) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#film industry`, `#IMAX`, `#entertainment`, `#trends`

---

<a id="item-25"></a>
## [香港 4 所大学跻身 QS 全球五十强，港中大升至第 18 位](https://www.chinanews.com.cn/edu/2026/06-18/10642936.shtml) ⭐️ 3.0/10

2027 年 QS 世界大学排名于 2026 年 6 月 18 日公布，香港有四所大学跻身全球前 50 名，其中香港中文大学从第 32 位跃升至第 18 位，首次进入前 20 名。 这一排名凸显了香港高等教育日益增强的国际竞争力，有助于吸引更多全球人才和研究合作，促进该地区的学术与经济发展。 进入前 50 名的四所香港大学分别是香港大学、香港中文大学、香港科技大学和香港理工大学。其中香港中文大学上升 14 位，进步最为显著。

rss · China News Service Scroll · 6月18日 04:11

**背景**: QS 世界大学排名由总部位于伦敦的高等教育分析机构 Quacquarelli Symonds 每年发布。排名基于学术声誉、雇主声誉、师生比例、篇均引用、国际教师比例和国际学生比例等指标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/QS_World_University_Rankings">QS World University Rankings - Wikipedia</a></li>
<li><a href="https://www.topuniversities.com/world-university-rankings/methodology">QS World University Rankings : Methodology | TopUniversities</a></li>

</ul>
</details>

**标签**: `#education`, `#university rankings`, `#Hong Kong`

---

<a id="item-26"></a>
## [国家发改委将印发现代物流领域“十五五”专项规划](https://www.chinanews.com.cn/cj/2026/06-18/10642931.shtml) ⭐️ 3.0/10

2026 年 6 月 18 日，国家发展改革委宣布将会同有关部门，印发实施现代物流领域“十五五”专项规划（2026-2030 年）。 该规划将指导未来五年中国物流基础设施和服务的发展，可能影响供应链效率与经济增长。这表明政府持续关注物流行业的现代化。 该消息由国家发改委发言人李超在新闻发布会上宣布。规划的具体内容和实施时间表尚未公布。

rss · China News Service Scroll · 6月18日 03:35

**背景**: 中国的五年计划是设定经济和社会发展目标的综合性国家战略。“十五五”规划覆盖 2026-2030 年。现代物流是提高供应链效率、降低成本的关键领域。

**标签**: `#policy`, `#logistics`, `#China`

---

<a id="item-27"></a>
## [民企在文昌打造商业航天配套产业链](https://www.chinanews.com.cn/cj/2026/06-18/10642929.shtml) ⭐️ 3.0/10

民营企业正在海南自贸港文昌投资建设商业航天配套产业链，依托新投入运营的海南国际商业航天发射中心。 这标志着中国商业航天生态的重要进展，民营资本和技术与国有发射基础设施融合，有望加速创新并降低成本。 海南国际商业航天发射中心是中国首个商业航天发射场，于 2024 年 11 月首次发射成功，此后已进行多次发射。文昌靠近赤道的地理位置为火箭发射提供了燃料效率优势。

rss · China News Service Scroll · 6月18日 03:28

**背景**: 商业航天是指由市场需求和私人投资驱动的太空活动，包括卫星发射、太空旅游和货物运输。海南自贸港于 2025 年 12 月启动全岛封关运作，提供税收优惠和简化监管以吸引高科技产业。文昌已是中国大型载荷的主要航天发射场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.haikou.bendibao.com/news/70194.shtm">海南 文 昌 商 业 航 天 发射场观赏指南（不断丰富）- 海口本地宝</a></li>
<li><a href="https://www.jfdaily.com/wx/detail.do?id=745357">文 昌 发射场凭啥总“挑重担”？ 秘密在这里</a></li>
<li><a href="https://www.cicphoto.com/cn/view14381029">海南 文 昌 ：我国首个 商 业 航 天 发射场首发圆满成功</a></li>

</ul>
</details>

**标签**: `#commercial aerospace`, `#China`, `#supply chain`, `#private enterprise`

---

<a id="item-28"></a>
## [北京图博会展示 AI 情绪识别与智能荐书](https://www.chinanews.com.cn/sh/2026/06-18/10642921.shtml) ⭐️ 3.0/10

第 32 届北京国际图书博览会于 2026 年 6 月 18 日至 21 日举办，展示了基于 AI 的情绪识别和智能荐书系统，吸引了来自 82 个国家和地区的 1700 余家展商。 AI 与书展的结合标志着个性化阅读体验的兴起，可能改变读者发现书籍的方式以及出版商与受众的互动模式。 该报道缺乏关于情绪识别和推荐算法的技术细节，且该新闻没有社区讨论。

rss · China News Service Scroll · 6月18日 03:16

**背景**: 情绪识别 AI 通过面部表情、语音或文本推断用户情绪状态，而 AI 驱动的推荐系统分析用户偏好以推荐相关内容。这些技术越来越多地应用于电商、娱乐及出版领域，以提升用户参与度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/AhmedAslam28/AI-Emotion-Recognition">GitHub - AhmedAslam28/ AI - Emotion - Recognition : Emotion ...</a></li>
<li><a href="https://medium.com/@cagatay.akcamm/building-an-ai-powered-book-recommendation-system-7454ba66c607">Building an AI - Powered Book Recommendation System | Medium</a></li>
<li><a href="https://github.com/avikal07/BookMind">avikal07/BookMind: AI - powered Book Recommendation System ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#book fair`, `#emotion recognition`, `#recommendation system`

---