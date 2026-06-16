---
layout: default
title: "Horizon Summary: 2026-06-16 (ZH)"
date: 2026-06-16
lang: zh
---

> 从 372 条内容中筛选出 28 条重要资讯。

---

1. [LinkedIn 求职邀请中的 npm 后门](#item-1) ⭐️ 9.0/10
2. [美伊达成初步协议结束战争，重开霍尔木兹海峡](#item-2) ⭐️ 9.0/10
3. [ALS 患者成为首个长期使用语音脑机接口的超级用户](#item-3) ⭐️ 9.0/10
4. [DeepSeek 完成逾 70 亿美元融资](#item-4) ⭐️ 8.0/10
5. [阿里发布首个具身智能大模型系列 Qwen-Robot](#item-5) ⭐️ 8.0/10
6. [Linux 7.1 内核发布，重写 NTFS 驱动](#item-6) ⭐️ 8.0/10
7. [Tensordyne Napier 宣称 AI 推理吞吐量达 Blackwell 的 13 倍](#item-7) ⭐️ 8.0/10
8. [乌克兰利用 AI 拦截俄罗斯无人机](#item-8) ⭐️ 8.0/10
9. [双语大脑共享单一语法引擎](#item-9) ⭐️ 8.0/10
10. [SpaceX 上市：IPO 详情与分析](#item-10) ⭐️ 8.0/10
11. [网络安全专家抗议美国禁止 Anthropic 最强模型](#item-11) ⭐️ 8.0/10
12. [山姆被约谈，智谱因美国出口禁令暴涨](#item-12) ⭐️ 7.0/10
13. [OpenAI 去年总支出 340 亿美元，研发投入 190 亿](#item-13) ⭐️ 7.0/10
14. [硅基流动完成超 20 亿元 B 轮融资](#item-14) ⭐️ 7.0/10
15. [蓝色起源火箭爆炸：贝索斯激进追赶付出代价](#item-15) ⭐️ 7.0/10
16. [公安部警告新型“银狐”木马病毒瞄准企业员工](#item-16) ⭐️ 6.0/10
17. [中国发射首颗文化遗产定制遥感卫星](#item-17) ⭐️ 6.0/10
18. [谷歌：与中国关联黑客渗透美加科研机构](#item-18) ⭐️ 6.0/10
19. [Grill'd 因“植树星期二”活动涉嫌漂绿被起诉](#item-19) ⭐️ 6.0/10
20. [2026 年 1-5 月中国发明专利授权量同比增长 12.1%](#item-20) ⭐️ 3.0/10
21. [2026 京津冀算力算法大赛颁奖](#item-21) ⭐️ 3.0/10
22. [“苏超”足球联赛促进江苏民族融合](#item-22) ⭐️ 2.0/10
23. [民企在海南自贸港深耕绿色包装](#item-23) ⭐️ 2.0/10
24. [广西 16 条河流超警洪水](#item-24) ⭐️ 2.0/10
25. [纪录片《零碳之路》第二季开播](#item-25) ⭐️ 2.0/10
26. [湖南韶山警方拘留两名散布绑架谣言者](#item-26) ⭐️ 2.0/10
27. [中欧班列东通道累计通行量突破 4 万列](#item-27) ⭐️ 2.0/10
28. [海地帮派暴力今年已致至少 2300 人死亡](#item-28) ⭐️ 2.0/10

---

<a id="item-1"></a>
## [LinkedIn 求职邀请中的 npm 后门](https://roman.pt/posts/linkedin-backdoor/) ⭐️ 9.0/10

一名安全研究人员发现，在 LinkedIn 求职面试中发送的 GitHub 仓库中隐藏着一个后门，该后门利用 npm 的 prepare 脚本在安装依赖时执行任意代码。 这种攻击向量将社会工程与供应链攻击相结合，针对正在求职的开发者，因此非常有效且难以检测。它凸显了招聘流程中的重大安全漏洞，以及建立更好报告机制的必要性。 后门被嵌入在仓库中一个已弃用的 Node 模块问题中，npm 的 prepare 脚本在 npm install 后自动运行，执行恶意负载。研究人员向 GitHub 报告了该仓库，并向 LinkedIn 报告了招聘人员，但代码仍然有效。

hackernews · lwhsiao · 6月15日 20:00 · [社区讨论](https://news.ycombinator.com/item?id=48546294)

**背景**: npm 是 Node.js 的包管理器，其 prepare 脚本是一个生命周期钩子，在 npm install 后自动运行，常用于构建步骤。针对 npm 的供应链攻击日益常见，攻击者通过篡改包或向依赖中注入恶意代码进行攻击。通过虚假求职面试进行社会工程是网络犯罪的一个增长趋势，目标是能够访问敏感系统的开发者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.npmjs.com/cli/v11/using-npm/scripts/">Scripts | npm Docs</a></li>
<li><a href="https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/">The npm Threat Landscape: Attack Surface and Mitigations (Updated June 2)</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对缺乏集中式网络犯罪报告系统的担忧，有人指出类似的遭遇正变得越来越频繁。另一个人指出，这种攻击与正常的面试任务非常相似，使得疲惫或急于求职的人很容易上当。尽管已报告，但恶意代码仍留在 GitHub 上，这引发了对微软回应的批评。

**标签**: `#security`, `#supply chain attack`, `#npm`, `#social engineering`, `#cybercrime`

---

<a id="item-2"></a>
## [美伊达成初步协议结束战争，重开霍尔木兹海峡](https://www.npr.org/2026/06/15/nx-s1-5858590/us-iran-deal-updates) ⭐️ 9.0/10

2026 年 6 月 15 日，美国与伊朗宣布达成框架协议以结束持续战争并重新开放霍尔木兹海峡，预计于 6 月 19 日在日内瓦举行签署仪式。 该协议标志着重大地缘政治突破，可能稳定全球能源市场——霍尔木兹海峡是全球约 20%石油供应的关键通道。然而，伊朗核计划及海峡通行费等未决问题使协议仍显脆弱。 谅解备忘录被描述为“大约一页半”且“非常笼统”，许多细节有待后续谈判。关键未决问题包括伊朗核计划、海峡收费权以及以色列在黎巴嫩的停火违规行为。

rss · NPR News · 6月15日 09:55

**背景**: 霍尔木兹海峡是伊朗与阿拉伯半岛之间的狭窄水道，每日约 2000 万桶石油通过。自 2026 年 2 月 28 日美以攻击伊朗后，伊朗实际封锁了该海峡，导致全球经济动荡。该协议旨在解除美国海军封锁，并为伊朗达到特定基准提供经济激励。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/c78n6p09pzno">Iran war: What is the Strait of Hormuz and why does it matter?</a></li>
<li><a href="https://www.iea.org/about/oil-security-and-emergency-response/strait-of-hormuz">Strait of Hormuz - About - IEA</a></li>
<li><a href="https://missilestrikes.com/nuclear-status/">Iran Nuclear Status — Enrichment & Breakout Timeline</a></li>

</ul>
</details>

**社区讨论**: 参议院共和党人表示怀疑，指出许多未解答的问题以及对向伊朗提供资金的担忧。欧洲领导人敦促迅速落实，分析人士则指出协议因未决问题而脆弱。

**标签**: `#geopolitics`, `#international relations`, `#Middle East`, `#global economy`

---

<a id="item-3"></a>
## [ALS 患者成为首个长期使用语音脑机接口的超级用户](https://www.technologyreview.com/2026/06/15/1138953/man-als-first-power-user-brain-implant-speak-bci/) ⭐️ 9.0/10

患有 ALS 的 Casey Harrell 使用脑机接口（BCI）近三年，累计数千小时，通过神经信号生成语音。这标志着首个在瘫痪患者中长期、高频率使用的语音恢复 BCI。 这一里程碑表明，BCI 可以成为现实世界中实用的、耐用的辅助沟通设备，而不仅仅是短期实验室演示。它为神经假体在严重运动障碍患者中的更广泛应用铺平了道路。 Harrell 的 BCI 使用植入大脑表面的皮层脑电图（ECoG）电极阵列记录神经活动，并以高达 97%的准确率解码为语音。该系统由 UC Davis Health 开发，性能稳定，无需频繁重新校准。

rss · MIT Technology Review · 6月15日 15:12

**背景**: 脑机接口（BCI）是大脑与外部设备之间的直接通信通路，绕过肌肉和神经。对于语音恢复，BCI 将来自大脑中参与语音产生的区域的神经信号解码为文本或可听语音。ALS（肌萎缩侧索硬化症）会逐渐麻痹肌肉，包括说话所需的肌肉，因此 BCI 成为一种有前景的沟通解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://health.ucdavis.edu/news/headlines/new-brain-computer-interface-allows-man-with-als-to-speak-again/2024/08">New brain-computer interface allows man with ALS to ‘speak’ again</a></li>
<li><a href="https://www.nejm.org/doi/full/10.1056/NEJMoa2314132">An Accurate and Rapidly Calibrating Speech Neuroprosthesis | New England Journal of Medicine</a></li>
<li><a href="https://www.sherringford.org/post/brain-neural-prosthesis-revolutionizes-speech-restoration-for-als-patients-a-key-breakthrough-in-bci">Brain Neural Prosthesis Revolutionizes Speech Restoration for ALS Patients: A Key Breakthrough in BCI</a></li>

</ul>
</details>

**标签**: `#brain-computer interface`, `#ALS`, `#neurotechnology`, `#speech restoration`, `#assistive technology`

---

<a id="item-4"></a>
## [DeepSeek 完成逾 70 亿美元融资](https://36kr.com/newsflashes/3855395032142849?f=rss) ⭐️ 8.0/10

DeepSeek 已完成超过 70 亿美元的融资，本轮融资对该公司的估值超过 500 亿美元。 这笔巨额融资表明投资者对 DeepSeek 的 AI 模型充满信心，这些模型已凭借低成本、高性能的能力颠覆了行业格局。 据市场消息，这是 DeepSeek 首次外部融资，估值在 500 亿至 590 亿美元之间。

rss · 36Kr Feed · 6月16日 05:10

**背景**: DeepSeek 是一家中国 AI 公司，由对冲基金幻方量化联合创始人梁文锋于 2023 年 7 月创立。2025 年 1 月，该公司发布 R1 模型，以极低的成本（使用受出口限制的较弱芯片）达到了与 OpenAI 的 GPT-4 相当的性能，从而引起全球关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>
<li><a href="https://finance.yahoo.com/sectors/technology/articles/deepseek-eyes-7-4-billion-123039218.html">DeepSeek Eyes $7.4 Billion Funding Round At Up To $59 Billion Valuation ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#funding`, `#DeepSeek`, `#startup`, `#valuation`

---

<a id="item-5"></a>
## [阿里发布首个具身智能大模型系列 Qwen-Robot](https://36kr.com/newsflashes/3855340769563907?f=rss) ⭐️ 8.0/10

6 月 16 日，阿里巴巴发布了千问具身智能大模型 Qwen-Robot 系列，包含 VLA 操作模型 Qwen-RobotManip、VLN 移动模型 Qwen-RobotNav 和世界模型 Qwen-RobotWorld 三大模型。 这标志着阿里巴巴在具身智能领域迈出了重要一步，为机器人操作、导航和物理世界预测提供了统一的基础，有望加速各类机器人的真实落地。 三个模型既可单独部署，也能协同运转：Qwen-RobotNav 统一了四类导航任务，Qwen-RobotManip 基于超过 38,100 小时的开源数据实现多机型训练，Qwen-RobotWorld 则能跨操作、驾驶和导航场景预测符合物理规律的未来。

rss · 36Kr Feed · 6月16日 04:26

**背景**: 具身智能指能够感知、推理并在物理世界中行动的 AI 系统，通常通过机器人实现。视觉-语言-动作（VLA）模型直接将视觉输入和语言指令映射为机器人动作，视觉-语言-导航（VLN）模型引导机器人导航环境，世界模型则模拟世界如何演变，支持规划和预测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vision–language–action_model">Vision–language–action model - Wikipedia</a></li>
<li><a href="https://vla-survey.github.io/">Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications</a></li>
<li><a href="https://www.researchgate.net/publication/395713824_A_Survey_of_Embodied_World_Models">(PDF) A Survey of Embodied World Models</a></li>

</ul>
</details>

**标签**: `#embodied AI`, `#robotics`, `#Alibaba`, `#Qwen`, `#large language model`

---

<a id="item-6"></a>
## [Linux 7.1 内核发布，重写 NTFS 驱动](https://www.ithome.com/0/964/732.htm) ⭐️ 8.0/10

Linus Torvalds 于 2026 年 6 月 15 日发布了 Linux 7.1 内核稳定版，其中包含完全重写的 NTFS 驱动，支持完整写入，性能提升 35% 至 110%，并引入了对 Intel Panther Lake 处理器的 FRED 支持。 此版本显著提升了 Linux 处理 NTFS 文件系统的能力，惠及双系统用户或使用外置硬盘的用户。FRED 支持为下一代 Intel 处理器做好了准备，提升了性能和安全性。 新 NTFS 驱动采用了 iomap 和 folio 等现代内核基础设施，取代了过时的 ntfs3 和 FUSE 实现。Phoronix 基准测试显示多线程写入性能提升 35% 至 110%，挂载大容量硬盘（如 4TB）的速度提升至原来的 4 倍。

rss · ITHome Feed · 6月16日 03:21

**背景**: NTFS 是 Windows 的默认文件系统，Linux 对其支持历来有限。之前的内核驱动（ntfs3）已停止维护，用户依赖基于 FUSE 的解决方案（如 NTFS-3G），存在性能开销。FRED（灵活返回与事件分发）是 Intel 和 AMD 共同开发的新型中断模型，旨在降低延迟并提高可靠性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kernel.org/doc/html/next/filesystems/ntfs.html">The Linux NTFS filesystem driver — The Linux Kernel documentation</a></li>
<li><a href="https://linuxiac.com/linux-kernel-7-1-merges-new-ntfs-driver-with-full-write-support/">Linux Kernel 7.1 Merges New NTFS Driver With Full Write Support</a></li>
<li><a href="https://www.phoronix.com/news/Linux-7.1-Best-Features">The Best Features Of Linux 7.1: FRED , New NTFS Driver... - Phoronix</a></li>

</ul>
</details>

**标签**: `#Linux`, `#kernel`, `#NTFS`, `#performance`, `#Intel`

---

<a id="item-7"></a>
## [Tensordyne Napier 宣称 AI 推理吞吐量达 Blackwell 的 13 倍](https://www.ithome.com/0/964/688.htm) ⭐️ 8.0/10

AI 芯片初创公司 Tensordyne 宣布推出 Napier 处理器，声称在 AI 推理方面，其吞吐量是 NVIDIA Blackwell 系统的 13 倍，能效是 17 倍，采用对数数学设计和台积电 3nm 工艺。 如果得到验证，这可能会颠覆 NVIDIA 主导的 AI 硬件市场，为大规模 LLM 推理提供更高效的替代方案，从而降低数据中心的成本和能耗。 Napier 芯片采用对数数制，用加法替代乘法，集成大量 SRAM 和 HBM 内存，芯片间延迟低于 1μs。TDN72 机架系统可为每个用户提供每秒 1000 token 的万亿参数 LLM 推理能力。

rss · ITHome Feed · 6月16日 02:33

**背景**: AI 推理传统上依赖浮点矩阵乘法，计算密集。对数数学通过将乘法转换为加法来简化计算，降低功耗和延迟。NVIDIA Blackwell 是目前 AI 工作负载最先进的 GPU 平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/0/964/688.htm">Tensordyne Napier 流片：宣称平台 AI 推 理 吞吐 13 倍于 Blackwell...</a></li>
<li><a href="https://www.aol.com/articles/tensordyne-claims-massive-speed-power-173109000.html">Tensordyne Claims Massive Speed and Power Improvement... - AOL</a></li>
<li><a href="https://de.linkedin.com/in/gillesbackhus">Gilles Backhus – Tensordyne | LinkedIn</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#inference`, `#startup`, `#NVIDIA`, `#chip design`

---

<a id="item-8"></a>
## [乌克兰利用 AI 拦截俄罗斯无人机](https://www.nytimes.com/2026/06/15/world/europe/ukraine-russia-war-ai.html) ⭐️ 8.0/10

乌克兰正在部署由 AI 驱动的拦截无人机，这些无人机利用在大量战时数据上训练的机器学习来自主追踪并摧毁俄罗斯无人机，拦截率超过 60%。 这标志着 AI 在军事防御中的重要实际应用，展示了自主系统如何利用战场数据快速训练以应对不断变化的威胁，可能重塑现代战争和防御策略。 这些拦截器速度可达 300 公里/小时，利用 AI 追踪锁定俄罗斯 Geran 等无人机目标，并通过动能方式摧毁。乌克兰防空系统对远程无人机和导弹也报告了高成功率。

rss · The New York Times World · 6月15日 18:34

**背景**: 自俄罗斯入侵以来，乌克兰一直面临持续的无人机攻击，包括伊朗设计的 Shahed 和俄罗斯 Geran 无人机。传统防空系统昂贵且有限，促使乌克兰开发更便宜、由 AI 驱动的拦截器，这些拦截器可以自主运行并快速适应新型无人机。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/c1k2lmmjvzxo">From AI to shotguns and cheap interceptors , Ukraine is trying to...</a></li>
<li><a href="https://www.forbes.com/sites/vikrammittal/2026/03/07/new-russian-geran-drones-are-fast-can-ukrainian-interceptors-keep-up/">New Russian Geran Drones Are Fast. Can Ukrainian Interceptors ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#military`, `#autonomous systems`, `#Ukraine`, `#drone defense`

---

<a id="item-9"></a>
## [双语大脑共享单一语法引擎](https://www.nytimes.com/2026/06/15/science/brain-language-grammar.html) ⭐️ 8.0/10

纽约大学科学家的研究发现，双语者使用单一的神经“语法引擎”来处理多种语言，而不是每种语言使用独立的系统。 这一发现挑战了关于大脑中语言处理分离的长期假设，可能重塑我们对双语现象、语言学习和神经康复的理解。 该研究使用脑磁图（MEG）显示，大脑将语法处理为一种跨语言的通用、可重复使用的计算，超越了语言特定的界限。

rss · The New York Times World · 6月15日 17:45

**背景**: 长期以来，双语被认为涉及每种语言的独立神经系统。这项研究为共享的语法引擎提供了直接的神经证据，表明大脑的语言处理比之前认为的更加统一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medicalxpress.com/news/2026-06-bilingualism-driven-neurological-grammar.html">Bilingualism may be driven by a single neurological ' grammar engine '</a></li>
<li><a href="https://neurosciencenews.com/bilingual-brain-shared-grammar-engine-30886/">Bilingual Brains Use a Single Shared Engine for... - Neuroscience News</a></li>

</ul>
</details>

**标签**: `#neuroscience`, `#bilingualism`, `#language processing`, `#cognitive science`

---

<a id="item-10"></a>
## [SpaceX 上市：IPO 详情与分析](https://techcrunch.com/2026/06/15/spacex-is-public-everything-you-need-to-know-post-ipo/) ⭐️ 8.0/10

SpaceX 已提交 S-1 注册文件进行 IPO，成为一家上市公司。TechCrunch 的专题报道涵盖了赢家、IPO 前交易以及文件中的关键细节。 SpaceX 的 IPO 是航天业的里程碑事件，为公众提供了投资机会，并可能加速航天技术的发展。同时，它也揭示了 SpaceX 的财务状况和商业战略。 S-1 文件包含完整的财务报表、风险因素和资金用途。IPO 前交易可能涉及一级私募配售或二级销售，通常仅限于合格投资者。

rss · TechCrunch · 6月15日 18:30

**背景**: S-1 是公司在 IPO 前向 SEC 提交的强制性注册文件，包含详细的财务和业务信息。IPO 前交易允许早期投资者在公开发行前购买股票，通常有折扣但风险较高。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://krokfin.com.ua/en/news/spacex-ipo-record-2026/">SpaceX Files S - 1 : The Largest IPO in History at $1.75 Trillion... | KrokFin</a></li>
<li><a href="https://www.jarsy.com/learn/pre-ipo-settlement">How Investment Settlements Work in Pre - IPO Deals : Understanding...</a></li>
<li><a href="https://www.bitget.com/wiki/what-is-pre-ipo-stock">what is pre ipo stock: Pre - IPO stock guide</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#IPO`, `#space technology`, `#business`

---

<a id="item-11"></a>
## [网络安全专家抗议美国禁止 Anthropic 最强模型](https://techcrunch.com/2026/06/15/cybersecurity-vets-protest-dangerous-us-government-ban-on-anthropics-most-powerful-models/) ⭐️ 8.0/10

数十名网络安全专家敦促白宫取消对 Anthropic 的 Fable 和 Mythos 模型的出口管制限制，认为该禁令阻碍了防御能力。 此次抗议凸显了 AI 安全法规与网络安全防御者实际需求之间日益紧张的关系，可能影响未来的出口管制政策。 Anthropic 的 Fable 5 是公开可用的 Mythos 级模型，带有阻止高风险领域的防护措施，而 Mythos 是该公司最先进的模型。出口禁令限制了国际用户对这些模型的访问。

rss · TechCrunch · 6月15日 15:29

**背景**: 美国政府已对先进 AI 模型实施出口管制，以防止对手获得可能威胁国家安全的能力。Anthropic 的 Mythos 级模型代表了尖端 AI 技术，该公司本身也警告过强大 AI 的危险性。网络安全专家认为，限制这些模型的访问会削弱全球应对网络威胁的防御能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://techcrunch.com/2026/06/09/anthropic-released-claude-fable-5-its-most-powerful-model-publicly-days-after-warning-ai-is-getting-too-dangerous/">Anthropic releases Claude Fable, a version of Mythos, days after warning AI is becoming too dangerous</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#cybersecurity`, `#Anthropic`, `#export controls`, `#policy`

---

<a id="item-12"></a>
## [山姆被约谈，智谱因美国出口禁令暴涨](https://36kr.com/p/3855082873476102?f=rss) ⭐️ 7.0/10

中国市场监管总局因山姆门店多次出现食品安全问题约谈其总部；同时，美国对 Anthropic 最新模型实施出口管制后，AI 公司智谱股价一度暴涨 47.6%。 对山姆的监管行动表明中国对外资零售商的食品安全执法趋严；而智谱股价暴涨则凸显美国 AI 模型出口管制可能意外地提振本土竞争对手。 智谱的 GLM-5.2 模型采用 MIT 协议开源，提供 1M 上下文长度，面向 Coding Plan 用户开放；美国对 Anthropic 的 Claude Fable 5 和 Mythos 5 实施出口管制，原因是存在越狱漏洞。

rss · 36Kr Feed · 6月15日 23:56

**背景**: 山姆会员店是沃尔玛在中国运营的会员制仓储式连锁超市，近期多次出现食品安全问题。智谱是中国领先的 AI 公司，致力于开发大语言模型。美国对 Anthropic 模型的出口禁令限制了包括中国在内的外国国民访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.sina.com.cn/tech/digi/2026-06-13/doc-inicfvnr2880919.shtml">智 谱 ： GLM - 5 . 2 将面向 GLM Coding Plan...</a></li>
<li><a href="https://n.yam.com/Article/20260616456524">川普政府禁 Anthropic 頂級AI模型 引爆監 管 與創新爭議 | 蕃新聞</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#food safety`, `#stock market`, `#China tech`, `#export controls`

---

<a id="item-13"></a>
## [OpenAI 去年总支出 340 亿美元，研发投入 190 亿](https://36kr.com/newsflashes/3855398597596423?f=rss) ⭐️ 7.0/10

据报道，OpenAI 去年总支出达 340 亿美元，其中约 190 亿美元用于研发，该公司正筹备首次公开募股（IPO）。 这一巨额支出凸显了 OpenAI 在 IPO 前抢占蓬勃发展的 AI 市场主导地位的激进策略，对投资者和整个 AI 行业影响深远。 除研发外，OpenAI 在销售和营销上花费近 60 亿美元，其余为其他各类开支。

rss · 36Kr Feed · 6月16日 05:34

**背景**: OpenAI 是 ChatGPT 的开发商，ChatGPT 是领先的 AI 聊天机器人。经审计的财务数据显示，该公司在从非营利组织转型为营利实体并计划 IPO 的过程中，大力投资研发以保持竞争优势。

**标签**: `#OpenAI`, `#AI industry`, `#finance`, `#R&D spending`, `#IPO`

---

<a id="item-14"></a>
## [硅基流动完成超 20 亿元 B 轮融资](https://36kr.com/newsflashes/3855302945592321?f=rss) ⭐️ 7.0/10

AI 基础设施初创公司硅基流动已完成超 20 亿元人民币的 B 轮融资。本轮融资由携程、晶科能源、金蝶、壁仞、蔚来资本、商汤、巨人网络、国泰君安创新投等产业资本和财务机构联合投资。 这笔大额融资凸显了中国对 AI 基础设施和 MaaS（模型即服务）日益增长的需求。硅基流动营收同比增长超 10 倍，服务超 1000 万用户和 1 万家企业客户，其 Token 工厂模式的可扩展性得到验证。 硅基流动的 MaaS 平台通过 Token 工厂模式日均处理数万亿 Token。公司海外市场单月营收达数百万美元，显示出强劲的全球发展势头。

rss · 36Kr Feed · 6月16日 03:36

**背景**: MaaS（模型即服务）是一种基于云的服务，通过 API 提供 AI 模型访问，降低开发者和企业集成 AI 能力的门槛。硅基流动的 Token 工厂模式指的是一种优化的基础设施，能够高效生成和服务大语言模型的 Token（文本生成的基本单位），实现大规模高吞吐推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.huaweicloud.com/productdesc-maas/productdesc_maas_0002.html">什么是 MaaS _产品介绍_ MaaS 模 型 即 服 务 -华为云</a></li>
<li><a href="https://segmentfault.com/a/1190000047723018">人工智能 - OpenRouter vs 硅 基 流 动 vs 七牛云 AI... - SegmentFault 思否</a></li>

</ul>
</details>

**标签**: `#AI`, `#funding`, `#MaaS`, `#China`, `#startup`

---

<a id="item-15"></a>
## [蓝色起源火箭爆炸：贝索斯激进追赶付出代价](https://www.ithome.com/0/964/754.htm) ⭐️ 7.0/10

2026 年 5 月 28 日，蓝色起源一枚新格伦火箭在卡纳维拉尔角进行静态点火测试时发生爆炸，火箭被毁，地面设施严重受损。事故发生时，蓝色起源正加速研发，以缩小与 SpaceX 的差距。 此次爆炸凸显了商业太空竞赛中激进开发的风险，蓝色起源挑战 SpaceX 主导地位的努力受挫。事故可能推迟蓝色起源的高频发射计划和卫星互联网项目，进一步拉大与 SpaceX 的差距。 爆炸发生在例行静态点火测试期间，初步怀疑是燃料泄漏所致。98 米高的火箭被毁，运输起竖架被掀翻，避雷塔被夷为平地；未造成人员伤亡。

rss · ITHome Feed · 6月16日 04:55

**背景**: 蓝色起源由杰夫·贝索斯创立，长期采取稳健策略，但贝索斯对落后于 SpaceX 感到不满。2023 年，前亚马逊高管戴夫·林普出任 CEO，引入激进目标和亚马逊式工作文化以加速开发。新格伦火箭于 2025 年 1 月首次成功入轨，但公司计划在 2026 年完成 12 次发射。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://bhsb.tjbhnews.com/tupian/2026/0419/140777.html">美发射翻 新 “ 新 格 伦 ”运载 火 箭 并成功回收一级 箭 体 - 天津滨海生活网</a></li>
<li><a href="https://ishare.ifeng.com/c/s/v006NUqYJMlBHeJd1lUA-_x9M1N6KDfyo3dXZ0zKqX6sz9tiDqF8uYswO--cp66bBCmSmu?spss=np&channelId=">蓝色 起 源大爆炸背后：贝佐斯不满落后SpaceX 激进追赶付出代价</a></li>

</ul>
</details>

**标签**: `#Blue Origin`, `#SpaceX`, `#rocket explosion`, `#space industry`, `#competition`

---

<a id="item-16"></a>
## [公安部警告新型“银狐”木马病毒瞄准企业员工](https://www.chinanews.com.cn/gn/2026/06-16/10641095.shtml) ⭐️ 6.0/10

公安部网安局公布了 5 起打击“银狐”木马病毒的典型案例，该病毒新变种专门针对企事业单位工作人员，特别是财务人员，实施数据窃取和远程控制。 这一警报突显了针对关键业务角色的定向恶意软件威胁不断演变，可能导致重大财务损失和数据泄露。它强调了企业和个人加强网络安全意识的必要性。 “银狐”木马病毒伪装性强，可实现远程控制、窃取密码、拦截短信验证码和盗取私密数据。该公告属于常规警告，未提供新的技术分析或防护细节。

rss · China News Service China · 6月16日 00:02

**背景**: 木马病毒是伪装成合法软件以诱骗用户安装的恶意程序。像“银狐”这样的远程访问木马（RAT）允许攻击者远程控制受感染系统。财务人员因能访问敏感财务数据和交易系统而常成为攻击目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nic.hrbeu.edu.cn/info/1004/2443.htm">关于防范“ 银 狐 ” 木 马 病 毒 的安全提示-哈尔滨工程大学信息化处</a></li>
<li><a href="https://ga.tj.gov.cn/gaxc/aqffts/202412/t20241223_6812748.html">安全防范提示_天津市公安局</a></li>
<li><a href="http://m.hkwb.net/content/2026-05/24/content_4362266.htm">m.hkwb.net/content/2026-05/24/content_4362266.htm</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#malware`, `#trojan`, `#China`

---

<a id="item-17"></a>
## [中国发射首颗文化遗产定制遥感卫星](https://www.chinanews.com.cn/gn/2026/06-15/10641050.shtml) ⭐️ 6.0/10

2026 年 6 月 15 日，中国在酒泉卫星发射中心成功发射了首颗聚焦文物保护的定制遥感监测卫星——'文物 01 星'，卫星已顺利进入预定轨道。 该卫星标志着遥感技术首次专门应用于文化遗产监测与保护，有望实现对自然灾害、人为活动或环境变化导致文物损毁的早期预警。 该卫星为文化遗产监测定制设计，但具体技术参数（如分辨率、光谱波段）尚未公布。它将定期提供中国重点文物遗址的影像数据。

rss · China News Service China · 6月15日 15:24

**背景**: 遥感卫星通常用于农业、城市规划或灾害监测等广泛领域。为文化遗产定制卫星较为罕见，此前文物监测多依赖地面调查或通用卫星影像。此次发射反映了中国在太空技术应用于文化保护方面的投入增加。

**标签**: `#satellite`, `#remote sensing`, `#cultural heritage`, `#China`

---

<a id="item-18"></a>
## [谷歌：与中国关联黑客渗透美加科研机构](https://www.rfi.fr/cn/%E4%B8%AD%E5%9B%BD/20260615-%E8%B0%B7%E6%AD%8C%E7%A7%B0%E4%B8%8E%E4%B8%AD%E5%9B%BD%E6%9C%89%E5%85%B3%E8%81%94%E9%BB%91%E5%AE%A2%E7%BB%84%E7%BB%87%E9%95%BF%E6%9C%9F%E6%B8%97%E9%80%8F%E7%BE%8E%E5%8A%A0%E7%A7%91%E7%A0%94%E6%9C%BA%E6%9E%84) ⭐️ 6.0/10

谷歌于 6 月 15 日报告称，一个被认为与中国有关联的黑客组织在一年多时间里秘密窃取美国和加拿大多家学术、医疗及军事研究机构的数据，直至其活动被发现。 此事件凸显了研究机构面临的持续网络安全威胁，这些机构拥有宝贵的知识产权，并加剧了网络领域的地缘政治紧张局势。可能促使加强安全措施和国际审查。 该黑客组织针对美国和加拿大多家机构，重点窃取学术、医疗和军事研究数据。渗透活动持续一年多才被发现，表明威胁行为者具有复杂且持久的能力。

rss · RFI Chinese · 6月15日 21:30

**背景**: 国家支持的黑客组织常以研究机构为目标，窃取知识产权以获取战略优势。谷歌威胁分析小组（TAG）经常追踪并报告此类活动。该报告进一步揭示了所谓中国针对西方实体的网络间谍活动模式。

**标签**: `#cybersecurity`, `#hacking`, `#geopolitics`, `#research institutions`

---

<a id="item-19"></a>
## [Grill'd 因“植树星期二”活动涉嫌漂绿被起诉](https://www.theguardian.com/australia-news/2026/jun/16/grilld-burger-chain-sued-over-alleged-greenwashing-by-consumer-watchdog) ⭐️ 6.0/10

澳大利亚竞争与消费者委员会（ACCC）已对汉堡连锁店 Grill'd 提起联邦法院诉讼，指控其“植树星期二”环保活动在三年多时间里虚报捐款金额。 此案凸显了 ACCC 对漂绿行为的执法力度加大，表明企业必须为其环保声明提供证据。它可能为澳大利亚企业可持续发展活动的审查树立先例。 ACCC 指控 Grill'd 在其“植树星期二”活动中夸大了捐赠给环保事业的金额，该活动承诺将部分销售额用于植树。此次法律行动涉及三年多的时间。

rss · The Guardian World · 6月16日 04:19

**背景**: 漂绿（Greenwashing）指通过欺骗性营销使公司看起来比实际更环保的行为。ACCC 已将漂绿列为 2025-26 年的执法重点，针对各行业误导性的环保声明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Greenwashing">Greenwashing - Wikipedia</a></li>
<li><a href="https://dmawlawyers.com.au/insights/regulator-focus-locks-onto-greenwashing">DMAW Lawyers • Regulator focus locks onto greenwashing</a></li>
<li><a href="https://carbonly.ai/blog/accc-greenwashing-penalties-australia">ACCC Greenwashing Fines: How Carbon Data Protects... | Carbonly.ai</a></li>

</ul>
</details>

**标签**: `#greenwashing`, `#consumer protection`, `#legal`, `#sustainability`

---

<a id="item-20"></a>
## [2026 年 1-5 月中国发明专利授权量同比增长 12.1%](https://www.chinanews.com.cn/cj/2026/06-16/10641287.shtml) ⭐️ 3.0/10

国家统计局报告，2026 年 1 月至 5 月，我国共授权发明专利 37.2 万件，同比增长 12.1%。 专利授权量的稳步增长反映了中国对创新和知识产权保护的持续重视，这可能影响全球技术竞争和投资决策。 该数据仅涵盖发明专利，不包括实用新型或外观设计专利，且基于国家统计局的官方统计。

rss · China News Service Scroll · 6月16日 03:46

**背景**: 发明专利是技术创新的关键指标。中国一直积极推动专利申请和授权，作为其成为全球创新领导者的国家战略的一部分。

**标签**: `#patents`, `#statistics`, `#China`

---

<a id="item-21"></a>
## [2026 京津冀算力算法大赛颁奖](https://www.chinanews.com.cn/sh/2026/06-16/10641290.shtml) ⭐️ 3.0/10

2026 年 6 月 15 日，2026 京津冀（廊坊）算力算法大赛颁奖仪式在廊坊市京津冀大数据创新应用中心举行。 此次区域赛事凸显了京津冀地区对算力与算法创新的日益重视，有助于推动当地人工智能产业的发展。 大赛由廊坊市人民政府主办，中国信息通信研究院承办，主题为“智汇廊坊·算赢未来——赋能区域人工智能产业创新发展”。

rss · China News Service Scroll · 6月16日 03:37

**背景**: 京津冀大数据创新应用中心是廊坊市的大型数据产业综合体，占地 10.6 万平方米。中国信息通信研究院是工业和信息化部直属的重要研究机构，专注于信息通信技术与数字经济。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.chinanews.com/tp/hd2011/2020/05-14/940049.shtml">探访 京 津 冀 大 数 据 创 新 应 用 中 心 - 中 新 网</a></li>
<li><a href="https://www.caict.ac.cn/kxyj/qwfb/bps/202401/P020240326601000238100.pdf">caict.ac.cn/kxyj/qwfb/bps/202401/P020240326601000238100.pdf</a></li>

</ul>
</details>

**标签**: `#computing power`, `#algorithm competition`, `#regional event`

---

<a id="item-22"></a>
## [“苏超”足球联赛促进江苏民族融合](https://www.chinanews.com.cn/txy/2026/06-16/10641342.shtml) ⭐️ 2.0/10

2026 年江苏省城市足球联赛（“苏超”）正在进行，以足球为平台促进各民族交往交流交融。 这一举措凸显了体育如何成为社会凝聚力和民族和谐的桥梁，为技术领域之外的社区建设提供了范例。 该联赛是中国江苏省的一项地方体育赛事，侧重于社会融合而非竞技或技术层面。

rss · China News Service Scroll · 6月16日 05:35

**背景**: “苏超”是江苏的一项草根足球联赛，旨在汇聚不同背景的人们。它强调社区凝聚力和民族团结，反映了中国更广泛的社会政策。

**标签**: `#sports`, `#community`, `#China`

---

<a id="item-23"></a>
## [民企在海南自贸港深耕绿色包装](https://www.chinanews.com.cn/cj/2026/06-16/10641327.shtml) ⭐️ 2.0/10

据中新网 2026 年 6 月 16 日报道，海南自贸港一家民营企业正专注于绿色包装，以开拓国际市场。 这凸显了民营企业如何利用海南自贸港的零关税等政策，在可持续包装领域创新并参与国际竞争。 该报道是一篇通用新闻，未提供关于该公司或其绿色包装材料的具体技术细节。

rss · China News Service Scroll · 6月16日 05:29

**背景**: 海南自贸港于 2025 年 12 月启动，提供零关税和放宽市场准入等政策以吸引投资。绿色包装使用可回收或可生物降解的材料，如纸张、纸板和玻璃，以减少环境影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://english.news.cn/20250530/7629d51fedc04f088fde017615ca6e15/c.html">A glimpse of Hainan Free Trade Port -Xinhua</a></li>
<li><a href="https://www.linkedin.com/advice/0/how-can-you-use-green-packaging-make-your-product-yveyf">How to Use Green Packaging to Stand Out</a></li>

</ul>
</details>

**标签**: `#green packaging`, `#Hainan Free Trade Port`, `#business news`

---

<a id="item-24"></a>
## [广西 16 条河流超警洪水](https://www.chinanews.com.cn/sh/2026/06-16/10641325.shtml) ⭐️ 2.0/10

6 月 15 日至 16 日的强降雨导致广西 16 条河流、18 个水文站出现超警洪水，超警幅度 0.04 米至 1.69 米。 此次洪水威胁广西当地社区和基础设施，需要应急响应，并凸显了极端天气事件的影响。 最大降雨出现在博白县（283.0 毫米）和浦北县（236.5 毫米）。受影响河流包括南流江、北流河、清水河及郁江支流。

rss · China News Service Scroll · 6月16日 05:28

**背景**: 广西是中国南方地区，夏季季风季节易发洪水。水文站监测河流水位，当水位超过危险阈值时发布预警。

**标签**: `#flood`, `#Guangxi`, `#weather`, `#China`

---

<a id="item-25"></a>
## [纪录片《零碳之路》第二季开播](https://www.chinanews.com.cn/cul/2026/06-16/10641321.shtml) ⭐️ 2.0/10

纪录片《零碳之路》第二季于 6 月 15 日在央视纪录频道首播，通过海上风电机、虚拟电厂和碳捕集等技术展示中国的绿色低碳发展。 这部纪录片有助于提高公众对中国在绿色能源和碳减排方面进展的认识，突出展示对实现碳中和目标至关重要的关键技术的实际应用。 该纪录片由五洲传播中心和国家地理出品，中国石化集团有限公司联合出品。片中展示了虚拟电厂（聚合分布式能源）以及碳捕集、利用与封存（CCUS）系统等技术。

rss · China News Service Scroll · 6月16日 05:26

**背景**: 虚拟电厂利用先进的通信和控制技术聚合各类分布式能源和负荷，实现灵活的电网互动。碳捕集技术从工业源捕获二氧化碳进行封存或利用，是减排的关键方法。海上风电机是安装在海洋中的大型风力发电设施，有助于可再生能源发电。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sprixin.com/Smart/Virtual/">虚 拟 电 厂 _ 北京国能日新</a></li>
<li><a href="https://www.nea.gov.cn/2023-06/11/c_1310726491.htm">“ 碳 捕 手”让 二 氧 化 碳 变好用---国家能源局</a></li>
<li><a href="http://www.eastwp.net/news/show.php?itemid=50457">【干货】 9大 风 电 整 机 商 海 上 机 型技术参数一览！_ 东方 风 力发 电 网</a></li>

</ul>
</details>

**标签**: `#documentary`, `#green energy`, `#China`

---

<a id="item-26"></a>
## [湖南韶山警方拘留两名散布绑架谣言者](https://www.chinanews.com.cn/sh/2026/06-16/10641323.shtml) ⭐️ 2.0/10

2026 年 6 月 16 日，湖南韶山警方宣布拘留两名在微信群散布虚假谣言的人，该谣言称公交车站有人试图绑架女学生。 此案凸显了中国当局持续打击网络虚假信息的努力，此类信息可能引发公众恐慌并扰乱社会秩序。 警方于 2026 年 6 月 15 日首次注意到该谣言，两名散布虚假信息者被拘留。警方呼吁公众不要传播未经核实的信息。

rss · China News Service Scroll · 6月16日 05:26

**背景**: 在中国，散布扰乱公共秩序的谣言可能根据《治安管理处罚法》被行政拘留。此前也有类似案例，有人因编造绑架或安全威胁信息而受到处罚。

**标签**: `#rumor`, `#police`, `#local news`

---

<a id="item-27"></a>
## [中欧班列东通道累计通行量突破 4 万列](https://www.chinanews.com.cn/cj/2026/06-16/10641320.shtml) ⭐️ 2.0/10

截至 2026 年 6 月 16 日，中欧班列“东通道”累计通行量突破 4 万列。 这一里程碑凸显了铁路货运在中欧贸易中日益重要的作用，展示了东通道的运力和效率。 东通道由满洲里、绥芬河、同江铁路口岸组成。2026 年前五个月累计开行超 2000 列。

rss · China News Service Scroll · 6月16日 05:25

**背景**: 中欧班列是连接中国与欧洲的货运列车网络，通过多条通道运行。东通道是最北端的路线，经内蒙古和黑龙江出境。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.toutiao.com/topic/7520409593797773322/">中 欧 铁路有哪些线路-今日头条</a></li>
<li><a href="https://www.linkedin.com/pulse/understanding-key-corridors-china-europe-7wrlf">Understanding the Key Corridors of the China-Europe Railway Express</a></li>

</ul>
</details>

**标签**: `#logistics`, `#infrastructure`, `#transportation`

---

<a id="item-28"></a>
## [海地帮派暴力今年已致至少 2300 人死亡](https://www.chinanews.com.cn/gj/2026/06-16/10641316.shtml) ⭐️ 2.0/10

联合国人权事务高级专员报告称，今年海地帮派暴力已造成至少 2300 人死亡、至少 1100 人受伤，以及近百起绑架事件。 这凸显了海地严重的人道主义危机，不断升级的帮派暴力威胁平民安全与稳定，引发国际关注。 该数据由联合国人权事务高级专员沃尔克·图尔克于 2026 年 6 月 15 日根据当地最新统计公布。

rss · China News Service Scroll · 6月16日 05:24

**背景**: 海地长期面临政治不稳定和帮派暴力问题。帮派控制着首都太子港的大部分地区，导致大量民众流离失所，法律秩序崩溃。

**标签**: `#news`, `#violence`, `#Haiti`

---