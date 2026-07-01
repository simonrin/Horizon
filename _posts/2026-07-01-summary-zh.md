---
layout: default
title: "Horizon Summary: 2026-07-01 (ZH)"
date: 2026-07-01
lang: zh
---

> 从 350 条内容中筛选出 28 条重要资讯。

---

1. [Claude Code 隐写标记用户请求](#item-1) ⭐️ 9.0/10
2. [Realta Fusion 实现直接从聚变反应发电](#item-2) ⭐️ 9.0/10
3. [互联网先驱温顿·瑟夫下周从谷歌退休](#item-3) ⭐️ 8.0/10
4. [世界首套水下焊接中子衍射装置在中国投入使用](#item-4) ⭐️ 8.0/10
5. [BioShocking 攻击曝光 6 款 AI 浏览器存在数据泄露漏洞](#item-5) ⭐️ 8.0/10
6. [中国电动汽车新国标强制要求一键物理断电](#item-6) ⭐️ 8.0/10
7. [数据中心碳排放量比 IEA 预估高出 57%](#item-7) ⭐️ 8.0/10
8. [巴黎法院裁定道达尔须对客户碳排放负责](#item-8) ⭐️ 8.0/10
9. [Etched 估值达 50 亿美元，AI 芯片销售额达 10 亿](#item-9) ⭐️ 8.0/10
10. [Arcturus 利用纳米注入铜将电网损耗减半](#item-10) ⭐️ 8.0/10
11. [感知纪元获千万级融资，研发机器人触觉电子皮肤](#item-11) ⭐️ 7.0/10
12. [Anthropic 在 Claude 平台全球上线 Fable 5](#item-12) ⭐️ 7.0/10
13. [韩国拟研究缩短核电站建设周期以应对 AI 用电需求](#item-13) ⭐️ 7.0/10
14. [Tenstorrent 发布 Ascalon S RISC-V CPU，面积效率提升 1.4 倍](#item-14) ⭐️ 7.0/10
15. [台湾搜查超微电脑，涉向中国走私英伟达芯片](#item-15) ⭐️ 7.0/10
16. [中国计划保护就业免受 AI 影响](#item-16) ⭐️ 7.0/10
17. [美国议员调查默沙东和艾伯维在华临床试验](#item-17) ⭐️ 6.0/10
18. [第三届粤创赛在韶关圆满落幕](#item-18) ⭐️ 3.0/10
19. [飞机 100 毫升液体限制的由来](#item-19) ⭐️ 3.0/10
20. [中国要求散装液态食品运输需持准运证](#item-20) ⭐️ 2.0/10
21. [香港庆祝回归 29 周年 提出三大重点工作](#item-21) ⭐️ 2.0/10
22. [中国发布四川高县 5.5 级地震烈度图](#item-22) ⭐️ 2.0/10
23. [A 股午评：超 4500 只个股上涨，创业板指下跌](#item-23) ⭐️ 2.0/10
24. [乡村教师合唱研讨会在沪举行](#item-24) ⭐️ 2.0/10
25. [银行助餐服务解决老人用餐难题](#item-25) ⭐️ 2.0/10
26. [四明山乡村诊所留住好医生](#item-26) ⭐️ 2.0/10
27. [广西 5 条河流出现超警洪水](#item-27) ⭐️ 2.0/10
28. [宁夏启动“阅游宁夏”文旅融合活动](#item-28) ⭐️ 2.0/10

---

<a id="item-1"></a>
## [Claude Code 隐写标记用户请求](https://thereallo.dev/blog/claude-code-prompt-steganography) ⭐️ 9.0/10

一名开发者发现，Anthropic 的 Claude Code 工具（版本 2.1.196）根据用户的 API 基础 URL 和时区，在系统提示中静默嵌入不可见的 Unicode 隐写标记，用于标记与中国相关的流量，且未作任何披露。 这引发了严重的隐私和信任问题，因为用户未被告知其请求被标记，可能违反了对 AI 工具透明度的期望，并影响对 Anthropic 及类似提供商的信任。 这些标记通过隐写术隐藏在系统提示中，旨在识别中国公司用于模型蒸馏的使用情况；该技术是通过反编译本地 Claude Code 安装发现的，标记根据 API 基础 URL 和时区而变化。

hackernews · kirushik · 6月30日 15:44 · [社区讨论](https://news.ycombinator.com/item?id=48734373)

**背景**: 隐写术是将信息隐藏在其他数据中的做法，例如在文本中使用不可见的 Unicode 字符。Claude Code 是 Anthropic 推出的基于终端的 AI 编码代理，它向 Anthropic 的 API 发送提示。这一发现揭示了 Anthropic 在未经同意或文档说明的情况下秘密跟踪用户请求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aimadetools.com/blog/claude-code-steganography-explained/">Claude Code Is Steganographically Marking Requests: What It Means</a></li>
<li><a href="https://byteiota.com/claude-code-is-marking-requests-what-anthropic-hid/">Claude Code Is Marking Requests: What Anthropic Hid</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论反应不一：一些人淡化其严重性，认为意图（防止中国公司进行模型蒸馏）是明确的，而另一些人则批评缺乏透明度和实现粗糙，指出本可以使用更巧妙的隐蔽技术。还有人担心这会侵蚀对 AI 实验室的信任。

**标签**: `#steganography`, `#AI ethics`, `#security`, `#Anthropic`, `#transparency`

---

<a id="item-2"></a>
## [Realta Fusion 实现直接从聚变反应发电](https://techcrunch.com/2026/06/30/realta-fusion-generates-electricity-directly-from-a-fusion-reaction-an-apparent-first/) ⭐️ 9.0/10

Realta Fusion 声称首次直接从聚变反应中发电，利用原型转换器收集α粒子，产生 100 伏特、数安培的电流。 这一突破通过绕过传统蒸汽轮机，可能大幅改善聚变能的经济性，从而加速商业聚变能的实现。 直接转换方法捕获了约 20%来自α粒子的聚变能量，原型成功点亮了几个灯泡，证明了可行性。

rss · TechCrunch · 6月30日 19:12

**背景**: 传统聚变反应堆设计将中子产生的热能转化为蒸汽驱动涡轮机，效率较低。直接能量转换概念于 20 世纪 60 年代提出，通过直接捕获带电粒子发电，但此前从未在聚变反应堆中实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/30/realta-fusion-generates-electricity-directly-from-a-fusion-reaction-an-apparent-first/">Realta Fusion generates electricity directly from a fusion reaction, an apparent first | TechCrunch</a></li>
<li><a href="https://realtafusion.com/technology/">Technology - Realta Fusion</a></li>
<li><a href="https://en.wikipedia.org/wiki/Direct_energy_conversion">Direct energy conversion - Wikipedia</a></li>

</ul>
</details>

**标签**: `#fusion energy`, `#clean energy`, `#breakthrough`, `#nuclear fusion`, `#energy technology`

---

<a id="item-3"></a>
## [互联网先驱温顿·瑟夫下周从谷歌退休](https://www.ithome.com/0/970/992.htm) ⭐️ 8.0/10

TCP/IP 协议共同发明人、谷歌首席互联网布道师温顿·瑟夫在 Open Frontier 大会上被宣布将于下周退休，结束其在谷歌超过 20 年的职业生涯。 瑟夫的退休标志着互联网奠基人之一的一个时代结束，而他近期对正式 AI 智能体通信标准的倡导，凸显了自主 AI 智能体普及过程中面临的关键挑战。 瑟夫认为自然语言因歧义性不足以用于 AI 智能体通信，需要精确的正式协议来确保可靠的互操作性，并将此与 TCP/IP 的早期发展相类比。

rss · ITHome Feed · 7月1日 03:47

**背景**: 温顿·瑟夫与罗伯特·卡恩在 20 世纪 70 年代设计了 TCP/IP，这是实现互联网数据通信的基础协议套件。瑟夫于 2005 年加入谷歌，担任副总裁兼首席互联网布道师，倡导互联网标准和全球政策。会议讨论还涉及少数资金雄厚的实验室对先进 AI 模型的垄断趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vint_Cerf">Vint Cerf</a></li>
<li><a href="https://en.wikipedia.org/wiki/TCP/IP_Protocol">TCP/IP Protocol</a></li>
<li><a href="https://agentprotocol.ai/">Home - AgentProtocol. ai</a></li>

</ul>
</details>

**标签**: `#internet history`, `#TCP/IP`, `#Vint Cerf`, `#AI standards`, `#retirement`

---

<a id="item-4"></a>
## [世界首套水下焊接中子衍射装置在中国投入使用](https://www.ithome.com/0/970/977.htm) ⭐️ 8.0/10

中国在中国散裂中子源（CSNS）上部署了世界首套水下焊接原位中子衍射研究装置，并成功完成了首次水下焊接过程的实时观测实验。 这一突破实现了水下焊接过程中材料微观结构的实时监测，解决了长期依赖焊后取样的“黑箱”问题。它将显著提高核电、海上风电和海洋管道等关键基础设施中水下焊接的安全性和可靠性。 该装置使用重水（D₂O）代替普通水来模拟水下环境，使中子束能够无干扰地通过。它由华南理工大学和中国散裂中子源科学中心的团队联合研发，并由振海智能科技（珠海）有限公司制造。

rss · ITHome Feed · 7月1日 03:32

**背景**: 中子衍射是一种利用中子束探测材料原子尺度结构的技术。原位观测意味着在过程中实时监测变化，而非事后分析。水下焊接对于修复海上结构至关重要，但此前研究人员只能在焊接后分析样本，错过了影响焊接质量的动态变化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.stdaily.com/web/gdxw/2026-07/01/content_540081.html">世界首套！ 我国自研的水下焊接 原 位 中 子 衍 射 研究装置投入使用</a></li>
<li><a href="https://zh.wikipedia.org/zh-cn/中国散裂中子源">中国散裂中子源 - 维基百科，自由的百科全书</a></li>
<li><a href="https://zh.wikipedia.org/zh-hans/重水">重水 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**标签**: `#underwater welding`, `#neutron diffraction`, `#materials science`, `#China`, `#engineering`

---

<a id="item-5"></a>
## [BioShocking 攻击曝光 6 款 AI 浏览器存在数据泄露漏洞](https://www.ithome.com/0/970/876.htm) ⭐️ 8.0/10

安全公司 LayerX 披露了名为 BioShocking 的漏洞，影响包括 ChatGPT Atlas 和 Perplexity Comet 在内的 6 款 AI 浏览器产品，攻击者可通过欺骗性提示诱导泄露用户敏感数据，如已保存密码和会话 Cookie。 该漏洞凸显了 AI 浏览器中的关键安全风险，攻击者可绕过安全约束访问隐私信息，可能影响数百万用户。这强调了在 AI 代理中需要强大的提示注入防御措施。 攻击利用一个恶意网页呈现类似《生化奇兵》游戏的谜题，其中错误答案如“2+2=5”反而得分，从而削弱 AI 的安全约束。LayerX 在 2025 年 10 月至 2026 年 1 月期间向厂商报告了该问题；OpenAI 修复了 ChatGPT Atlas，Perplexity 未采取行动，Anthropic 对 Claude 扩展的补丁未通过验证。

rss · ITHome Feed · 7月1日 02:18

**背景**: AI 浏览器集成了大语言模型，用于帮助用户完成总结网页或填写表单等任务。提示注入攻击利用 AI 遵循外部内容指令的能力，可能覆盖安全规则。BioShocking 技术特别通过游戏化方式操纵 AI 行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.malwarebytes.com/blog/news/2025/08/ai-browsers-could-leave-users-penniless-a-prompt-injection-warning">AI browsers could leave users penniless: A prompt injection warning</a></li>
<li><a href="https://dibishks.medium.com/prompt-injection-vulnerabilities-in-ai-browsers-like-comet-and-fellou-c75231874add">Prompt Injection Vulnerabilities in AI Browsers Like... | Medium</a></li>
<li><a href="https://www.aol.com/articles/openai-says-ai-browsers-chatgpt-161050241.html">OpenAI says prompt injections that can trick AI browsers like... - AOL</a></li>

</ul>
</details>

**标签**: `#security`, `#AI browsers`, `#vulnerability`, `#prompt injection`, `#data leak`

---

<a id="item-6"></a>
## [中国电动汽车新国标强制要求一键物理断电](https://www.ithome.com/0/970/853.htm) ⭐️ 8.0/10

两项电动汽车强制性国家标准 GB 18384—2025 和 GB 38031—2025 于 2026 年 7 月 1 日正式实施，要求配备物理一键断电装置，并强化电池热扩散防护要求。 这些标准大幅提升了电动汽车安全性，确保在电子系统失效时仍能物理切断高压电源，并强制电池热失控时不起火、不爆炸，保护乘员并增强消费者信心。 热扩散测试从“着火前 5 分钟报警”升级为“不起火、不爆炸”，新增底部撞击测试（10kg 撞头撞击 3 次）和刮底测试（35km/h 撞击 15cm 半球），并增加 300 次快充循环后的安全测试。

rss · ITHome Feed · 7月1日 01:14

**背景**: 此前电动汽车安全标准依赖软件控制高压断电，但事故中电子电路可能受损失效。新标准要求独立于电子系统的物理机械开关。锂离子电池热失控可能引发火灾，新规旨在彻底杜绝此类风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hz.group/insight/gb38031-battery-safety-ev-regulation/">GB 38031 - 2025 and the Future of Battery Safety in EVs | H&Z Consulting</a></li>
<li><a href="https://www.sanwood.com/news/131.html">GB 38031 - 2025 new national standard implementation: Sanwood...</a></li>

</ul>
</details>

**标签**: `#electric vehicles`, `#safety standards`, `#battery safety`, `#regulation`, `#China`

---

<a id="item-7"></a>
## [数据中心碳排放量比 IEA 预估高出 57%](https://www.dw.com/zh/%E7%A0%94%E7%A9%B6%E6%8A%A5%E5%91%8A%EF%BC%9A%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%E7%9A%84%E7%A2%B3%E6%8E%92%E6%94%BE%E6%AF%94%E9%A2%84%E6%83%B3%E7%9A%84%E4%B8%A5%E9%87%8D/a-77771437?maca=chi-rss-chi-all-1127-rdf) ⭐️ 8.0/10

一项新研究报告称，2025 年全球数据中心二氧化碳排放量达到 2.86 亿吨，比国际能源署（IEA）此前的估计高出 57%。 这一显著差异表明数据中心排放比之前认为的严重得多，凸显了在科技行业进行更精确测量和制定更强可持续性政策的紧迫性。 该研究估计的 2.86 亿吨二氧化碳与 IEA 基于自下而上和总量汇总等不同建模方法得出的早期数据形成对比。这一新发现表明，当前的减排努力可能不足。

rss · DW Chinese · 6月30日 12:09

**背景**: 数据中心消耗大量电力用于计算和冷却，导致大量碳排放。IEA 追踪了数据中心的能源使用，但其模型可能因备用发电机和制冷剂数据不完整等因素低估了实际排放。准确测量具有挑战性，且方法尚未达成共识。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.iea-4e.org/wp-content/uploads/2025/05/Data-Centre-Energy-Use-Critical-Review-of-Models-and-Results.pdf">Data Centre Energy Use: Critical Review of Models and Results</a></li>
<li><a href="https://www.iea.org/energy-system/buildings/data-centres-and-data-transmission-networks">Data centres & networks - IEA</a></li>
<li><a href="https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions">Data centre electricity use surged in 2025, even with ...</a></li>

</ul>
</details>

**标签**: `#data centers`, `#carbon emissions`, `#sustainability`, `#energy`, `#environment`

---

<a id="item-8"></a>
## [巴黎法院裁定道达尔须对客户碳排放负责](https://www.rfi.fr/cn/%E4%B8%93%E6%A0%8F%E6%A3%80%E7%B4%A2/%E7%8E%AF%E4%BF%9D%E5%A4%A9%E5%9C%B0/20260630-%E5%8E%86%E5%8F%B2%E6%80%A7%E6%B0%94%E5%80%99%E5%AE%A1%E5%88%A4-%E9%81%93%E8%BE%BE%E5%B0%94%E9%A1%BB%E5%AF%B9%E5%85%B6%E9%A1%BE%E5%AE%A2%E7%9A%84%E7%A2%B3%E6%8E%92%E6%94%BE%E6%89%BF%E8%B4%A3) ⭐️ 8.0/10

2026 年 6 月 25 日，巴黎司法法院裁定，道达尔能源必须将其客户使用其产品产生的范围三温室气体排放纳入企业警惕计划，并给予该公司六个月时间执行。 这是法国首例要求公司对客户碳排放承担责任的重要气候裁决，为企业对范围三排放的责任树立了先例，并可能影响全球气候诉讼。 道达尔能源作为世界第六大石油和天然气生产商，2025 年其运营和产品使用产生的二氧化碳排放量超过 3.35 亿吨。该诉讼由巴黎市政府和三家非政府组织于八年前提起。

rss · RFI Chinese · 6月30日 12:38

**背景**: 范围三排放是指公司价值链中发生的间接温室气体排放，包括客户使用其产品产生的排放。法国的《警惕义务法》要求大型企业识别并预防其运营中的人权和环境风险。该裁决将这一义务扩展到包括产品使用带来的气候风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://brusselssignal.eu/2026/06/totalenergies-ordered-by-paris-court-to-account-for-customer-emissions/">TotalEnergies ordered by to account for customer emissions</a></li>
<li><a href="https://iclg.com/news/paris-court-rules-vigilance-plans-must-address-scope-3-emissions/">Paris court rules vigilance plans must address Scope 3 emissions</a></li>
<li><a href="https://blogs.law.columbia.edu/climatechange/2025/12/16/greenwashing-on-trial-the-paris-tribunal-finds-totalenergies-misled-consumers-with-its-carbon-neutrality-claims/">Greenwashing on Trial: The Paris Tribunal Finds TotalEnergies ...</a></li>

</ul>
</details>

**标签**: `#climate change`, `#legal ruling`, `#corporate accountability`, `#TotalEnergies`, `#France`

---

<a id="item-9"></a>
## [Etched 估值达 50 亿美元，AI 芯片销售额达 10 亿](https://techcrunch.com/2026/06/30/nvidia-competitor-etched-hits-5b-valuation-1b-in-sales-for-ai-chip/) ⭐️ 8.0/10

AI 芯片初创公司 Etched 宣布其 Sohu 推理系统已获得 10 亿美元合同，并在完成 5 亿美元融资后估值达到 50 亿美元。 这一里程碑标志着 Nvidia 在 AI 硬件领域的主导地位面临有力挑战，可能重塑推理芯片格局，为大规模 AI 部署提供替代方案。 Etched 的 Sohu 芯片是专为基于 transformer 的 AI 模型设计的定制 ASIC，该公司由哈佛辍学生 Gavin Uberti 和 Chris Zhu 于 2022 年创立。

rss · TechCrunch · 6月30日 18:13

**背景**: AI 推理是运行已训练好的 AI 模型进行预测的过程，需要专用硬件以提高效率。Nvidia 目前凭借其 GPU 主导这一市场，但像 Etched 这样的初创公司正在开发专用芯片，为大型语言模型等特定工作负载提供更好的性能和更低的成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Etched.ai">Etched (company) - Wikipedia</a></li>
<li><a href="https://www.etched.com/">Etched</a></li>
<li><a href="https://www.datacenterdynamics.com/en/news/etchedai-raises-500m-for-a-5bn-valuation-report/">Etched.ai raises $500m for a $5bn valuation – report - DCD</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#Nvidia competitor`, `#inference chips`, `#startup funding`

---

<a id="item-10"></a>
## [Arcturus 利用纳米注入铜将电网损耗减半](https://techcrunch.com/2026/06/30/arcturus-could-halve-the-grids-electrical-losses-using-its-nano-infused-copper/) ⭐️ 8.0/10

隐秘初创公司 Arcturus 开发了一种基于激光的工艺，将碳纳米材料注入铜中，显著提高了其导电性，并有可能将电网电力损耗减半。 如果成功，这项技术可以显著减少电网中的能源浪费，从而降低电力成本，并为全球公用事业和消费者提高效率。 该工艺使用激光将碳纳米材料精确嵌入铜基体中，在不影响机械性能的情况下提高导电性。该公司声称这种材料可以将电网损耗降低高达 50%。

rss · TechCrunch · 6月30日 15:01

**背景**: 由于铜线的电阻，电网在传输过程中会损失约 5-10% 的能量，以热量的形式散失。碳纳米材料（如石墨烯）具有优异的电学性能，但将其整合到金属中一直具有挑战性。Arcturus 的激光注入技术旨在克服这一障碍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/30/arcturus-could-halve-the-grids-electrical-losses-using-its-nano-infused-copper/">Arcturus could halve the grid’s electrical losses using its nano-infused copper | TechCrunch</a></li>

</ul>
</details>

**标签**: `#energy`, `#materials science`, `#nanotechnology`, `#electrical grid`

---

<a id="item-11"></a>
## [感知纪元获千万级融资，研发机器人触觉电子皮肤](https://36kr.com/p/3874358072710407?f=rss) ⭐️ 7.0/10

感知纪元科技有限公司完成由松禾资本领投的千万级天使轮融资，用于推进多模态智能触觉电子皮肤的研发与量产。 触觉感知是具身智能的关键瓶颈，本轮融资支持的新型解决方案有望让机器人完成抓取物体、辅助医疗等精细操作。 该电子皮肤在单张柔性片上集成了压力、滑动、温度、纹理和形变感知，拉伸延展性超过 400%，已完成百万次可靠性测试。它采用全弹性设计和空间分区以避免信号串扰。

rss · 36Kr Feed · 7月1日 01:20

**背景**: 目前大多数机器人触觉传感器是单点式器件，仅能测量力或位置，限制了机器人执行简单任务。多模态电子皮肤模仿人类皮肤提供丰富的触觉数据，但在可拉伸材料中集成多种感知模态在技术上具有挑战性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/1977694116948227794">电子皮肤未来趋势：多模态感知+阵列化，如何突破材料/工艺/算法三重山...</a></li>
<li><a href="https://www.jove.com/cn/t/70286/system-level-integration-multimodal-signal-acquisition-electronic">电子皮肤中的系统级集成与多模态信号采集：综述与演示</a></li>
<li><a href="https://www.tahou.com/article/202875562241666053">关于 具 身 智 能 「 触 觉 」，你想 知 道的都在这篇综述里了-塔猴速递-塔猴</a></li>

</ul>
</details>

**标签**: `#robotics`, `#tactile sensing`, `#electronic skin`, `#funding`, `#embodied AI`

---

<a id="item-12"></a>
## [Anthropic 在 Claude 平台全球上线 Fable 5](https://36kr.com/newsflashes/3876522131386372?f=rss) ⭐️ 7.0/10

Anthropic 宣布，其最强大的视觉与编程模型 Fable 5 将于明天在 Claude 平台全球上线，并通过 Glasswing 计划扩大 Mythos 5 的开放范围。 此次上线将最先进的 AI 能力带给更广泛的用户（包括政府合作伙伴），并表明 Anthropic 在发布先进模型与安全协调之间寻求平衡。 Fable 5 是 Mythos 级别的模型，能够从科学图表中提取精确数字，并根据截图重建网页应用源代码。Pro、Max、Team 和 Select Enterprise 用户可访问，每周使用上限为 50%，有效期至 7 月 7 日。

rss · 36Kr Feed · 7月1日 03:22

**背景**: Anthropic 的 Mythos 模型专为防御性网络安全设计，用于发现关键软件中的漏洞。Fable 5 是经过安全处理、可公开发布的通用版本，而 Mythos 5 仍受限制。Glasswing 计划为特定合作伙伴提供早期访问权限，以评估网络安全领域的 AI 工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/project/glasswing">Project Glasswing \ Anthropic</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#AI model`, `#Fable 5`, `#government coordination`

---

<a id="item-13"></a>
## [韩国拟研究缩短核电站建设周期以应对 AI 用电需求](https://www.ithome.com/0/970/924.htm) ⭐️ 7.0/10

韩国政府宣布将研究缩短核电站建设周期（目前为 9-10 年）的方法，以满足 AI 发展带来的激增电力需求。该方案将写入即将发布的长期电力供需基本计划。 此举凸显了 AI 能源需求与核电政策之间日益紧密的联系，可能加速核电部署以支持 AI 基础设施。它可能影响全球为大规模数据中心和半导体集群供电的方式。 韩国目前约三分之一的电力来自核能。政府正推动三星电子、SK 海力士等科技企业在半导体产业集群和数据中心领域投资至少 1350 万亿韩元（约合 5.94 万亿元人民币）。

rss · ITHome Feed · 7月1日 02:53

**背景**: 核电能够全天候稳定供电且碳排放较低，因此对 AI 数据中心供电具有吸引力。然而，核电站建设因监管审批复杂、施工难度高而进展缓慢。小型模块化反应堆（SMR）有望缩短工期，但尚未实现广泛商业应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-cn/小型模塊化反應堆">小型模块化反应堆 - 维基百科，自由的百科全书</a></li>
<li><a href="https://nnsa.mee.gov.cn/ztzl/haqshmhsh/haqrdmyyt/202405/202401/t20240123_1064446.html">小型模块化反应堆发展现状与趋势_国家核安全局</a></li>
<li><a href="https://www.news.cn/liangzi/20260630/74bd2452311e41aaad4d9d558bfca31b/c.html">韩国政府将投资千万亿韩元于AI和半导体产业-新华网</a></li>

</ul>
</details>

**标签**: `#AI`, `#energy`, `#nuclear power`, `#South Korea`, `#infrastructure`

---

<a id="item-14"></a>
## [Tenstorrent 发布 Ascalon S RISC-V CPU，面积效率提升 1.4 倍](https://www.ithome.com/0/970/866.htm) ⭐️ 7.0/10

Tenstorrent 发布了 TT-Ascalon S RISC-V CPU 内核，该内核以旗舰 Ascalon X 一半的面积实现了其 70%的性能，单位面积性能提升 1.4 倍。该内核针对代理式 AI 工作负载和边缘部署进行了优化。 这一发布标志着 RISC-V CPU 设计的重要进步，其出色的面积性能比可能挑战 Arm 等成熟架构在 AI 和边缘计算市场的地位。这也巩固了 Tenstorrent 在 RISC-V 生态系统中的关键地位，该公司由著名芯片架构师 Jim Keller 领导。 TT-Ascalon S 是一款 4 宽乱序超标量内核，符合 RVA23 配置文件，配备单个 256 位矢量单元、32KB L1 指令缓存和 64KB L1 数据缓存。它在 SPECint2006 中每 GHz 可实现 15 分的 IPC，单个集群最多可扩展到 8 个内核，并具有可配置的共享 L2 缓存。

rss · ITHome Feed · 7月1日 01:42

**背景**: RISC-V 是一种开放标准的指令集架构（ISA），允许任何人无需许可费用即可设计自定义处理器。RVA23 配置文件是 64 位应用处理器的标准，确保不同实现之间的软件兼容性。代理式 AI 指的是能够自主追求目标、使用工具并采取行动的 AI 系统，通常需要高效处理混合、分支密集的执行模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tenstorrent.com/en/ip/risc-v-cpu">Tenstorrent</a></li>
<li><a href="https://www.beijingnews.net/news/279156836/tenstorrent-sets-new-performance-records-launches-tt-ascalon-s-and-expands-across-japan">Tenstorrent Sets New Performance Records, Launches TT- Ascalon ...</a></li>
<li><a href="https://docs.riscv.org/reference/rva23/_attachments/rva23-profile.pdf">RVA23 Profiles - docs.riscv.org</a></li>

</ul>
</details>

**标签**: `#RISC-V`, `#CPU Design`, `#AI Hardware`, `#Tenstorrent`, `#Semiconductor`

---

<a id="item-15"></a>
## [台湾搜查超微电脑，涉向中国走私英伟达芯片](https://www.rfi.fr/cn/%E7%A7%91%E6%8A%80%E4%B8%8E%E6%96%87%E5%8C%96/20260630-%E6%B6%89%E4%BB%A5%E4%B8%8D%E5%AE%9E%E6%96%87%E4%BB%B6%E5%B0%86%E8%8B%B1%E4%BC%9F%E8%BE%BE%E8%8A%AF%E7%89%87%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%94%80%E4%B8%AD%E6%B8%AF%E6%BE%B3-%E5%8F%B0%E6%A3%80%E6%96%B9%E6%90%9C%E8%B6%85%E5%BE%AE%E7%94%B5%E8%84%91%E7%AD%893%E5%85%AC%E5%8F%B8%E5%A3%B0%E6%8A%BC3%E4%BA%BA) ⭐️ 7.0/10

2026 年 6 月 30 日，台湾基隆地检署搜查了超微电脑（Supermicro）台湾亚太总部及另外两家公司，并声押三人，指控其使用不实文件将搭载高端英伟达芯片的服务器销往中国、香港和澳门。 这标志着在持续打击向中国非法出口受限英伟达 AI 芯片的行动中，最重大的执法行动之一，凸显了地缘政治紧张局势以及超微电脑等大型科技公司面临的供应链风险。 搜查行动针对 12 个地点，包括超微电脑台湾办公室及关联公司青云科技和是方电讯。该调查是台湾首次对英伟达芯片走私至中国进行的刑事侦查。

rss · RFI Chinese · 6月30日 09:39

**背景**: 美国以国家安全为由，对高端英伟达 AI 芯片实施对华出口管制。尽管有这些限制，黑市依然出现，被禁芯片在中国以美国价格 2-3 倍出售。超微电脑此前在美国已被起诉，涉嫌向中国出口价值至少 25 亿美元的英伟达 AI 服务器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cryptobriefing.com/super-micro-taiwan-raid-nvidia-chip-smuggling/">Super Micro Computer's Taiwan offices raided in Nvidia chip...</a></li>
<li><a href="https://thenextweb.com/news/super-micro-taiwan-raid-nvidia-chip-smuggling-probe">Taiwan raids Super Micro office as Nvidia chip smuggling...</a></li>
<li><a href="https://www.benzinga.com/trading-ideas/movers/26/06/60171652/super-micro-taiwan-offices-raided-stock-takes-another-hit">Super Micro Taiwan Offices Raided — Stock Takes... - Benzinga</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#export controls`, `#Supermicro`, `#geopolitics`, `#hardware`

---

<a id="item-16"></a>
## [中国计划保护就业免受 AI 影响](https://www.nytimes.com/2026/06/30/world/china-ai-jobs-birthright-hormuz.html) ⭐️ 7.0/10

中国正在积极制定策略，以减轻人工智能在各行业整合过程中对就业的影响。 这很重要，因为中国的做法可能为其他面临 AI 导致就业流失的国家提供范例，影响全球劳动政策和经济稳定。 文章强调了中国在将 AI 嵌入各行各业的同时，如何保持人类就业的思考，但未提供具体政策细节。

rss · The New York Times World · 7月1日 04:42

**背景**: 人工智能和自动化预计将颠覆全球劳动力市场，可能导致数百万人失业。中国作为主要的制造业和技术中心，尤其容易受到这些变化的影响。政府历来利用产业政策管理经济转型，这似乎是该方法的延伸。

**标签**: `#AI`, `#China`, `#job displacement`, `#policy`, `#labor economics`

---

<a id="item-17"></a>
## [美国议员调查默沙东和艾伯维在华临床试验](https://www.dw.com/zh/%E7%BE%8E%E5%9B%BD%E8%AE%AE%E5%91%98%E8%B0%83%E6%9F%A5%E4%B8%A4%E5%AE%B6%E6%9C%89%E5%9C%A8%E5%8D%8E%E4%B8%9A%E5%8A%A1%E7%9A%84%E7%94%9F%E7%89%A9%E5%8C%BB%E8%8D%AF%E5%85%AC%E5%8F%B8/a-77774250?maca=chi-rss-chi-all-1127-rdf) ⭐️ 6.0/10

美国国会一个跨党派议员小组已对默沙东和艾伯维展开国家安全调查，调查这两家公司在华进行的临床试验是否可能助长中国的军事能力。 此次调查凸显了美国对生物医药领域与中国合作中国家安全风险的日益担忧，可能影响制药公司开展全球临床试验及与中国机构合作的方式。 调查聚焦于在中国军事医院和新疆进行的试验，引发伦理和安全问题。默沙东表示将患者安全和伦理诚信作为临床研究的优先事项，并遵守所有全球指南；艾伯维则拒绝置评。

rss · DW Chinese · 6月30日 14:06

**背景**: 由于成本较低且招募患者速度更快，中国已成为临床试验的主要中心，但美国议员担心这些试验的数据可能被用于提升中国的军事生物技术。此次调查是美国在地缘政治紧张加剧背景下，审查对华生物技术投资与合作更广泛努力的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mezha.net/eng/bukvy/8ac08f68_us_lawmakers_demand/">US lawmakers demand national security probes into pharma trials in...</a></li>
<li><a href="https://www.ntd.com/us-lawmakers-probe-security-ethical-risks-in-china-biotech-trials_1156024.html">US Lawmakers Probe Security , Ethical Risks in China Biotech Trials</a></li>
<li><a href="https://www.devdiscourse.com/article/law-order/3943131-us-lawmakers-probe-drugmakers-china-clinical-trials-for-national-security-risks">U.S. Lawmakers Probe Drugmakers' China Clinical Trials for ...</a></li>

</ul>
</details>

**标签**: `#biopharma`, `#national security`, `#clinical trials`, `#US-China`

---

<a id="item-18"></a>
## [第三届粤创赛在韶关圆满落幕](https://www.chinanews.com.cn/tp/2026/07-01/10650544.shtml) ⭐️ 3.0/10

6 月 25 日，第三届粤东西北知识产权创新运用大赛（粤创赛）在韶关落幕，从千余个项目中评选出 30 个优秀项目并颁奖。 该赛事凸显了知识产权在推动粤东西北地区产业升级中的作用，展示了区域创新潜力。 活动在广东北部的韶关市举行，重点关注知识产权在本地产业中的应用。

rss · China News Service Scroll · 7月1日 04:51

**背景**: 粤创赛是一年一度的赛事，旨在促进广东省欠发达地区的知识产权创造和运用，鼓励当地企业和创新者利用知识产权推动经济增长。

**标签**: `#intellectual property`, `#regional competition`, `#China`

---

<a id="item-19"></a>
## [飞机 100 毫升液体限制的由来](https://www.chinanews.com.cn/life/2026/07-01/10650509.shtml) ⭐️ 3.0/10

一篇文章解释了飞机上 100 毫升液体限制的历史起源，追溯到 2006 年一起涉及液体炸药的未遂恐怖袭击。 这一规定每天影响数百万旅客，了解其背景有助于乘客理解这一常令人不便的安检规则背后的安全逻辑。 该限制是在英国当局挫败一起使用过氧化氢混合物在多架跨大西洋航班上引爆液体炸药的阴谋后全球实施的。100 毫升的限量被选为一个阈值，低于该阈值液体炸药难以有效引爆。

rss · China News Service Scroll · 7月1日 03:27

**背景**: 2006 年之前，乘客可以随身携带较大容量的液体容器。这起被称为“2006 年跨大西洋飞机阴谋”的恐怖袭击计划中，恐怖分子试图使用日常液体在机上组装炸弹。作为回应，美国运输安全管理局（TSA）及全球其他机构采纳了“3-1-1 规则”：液体容器容量不超过 3.4 盎司（100 毫升），并放入一个一夸脱大小的袋子中。

**标签**: `#travel`, `#aviation`, `#security`

---

<a id="item-20"></a>
## [中国要求散装液态食品运输需持准运证](https://www.chinanews.com.cn/cj/2026/07-01/10650543.shtml) ⭐️ 2.0/10

从今天起，中国规定五大类重点液态食品的道路散装运输必须取得准运证方可进行。 该法规通过实施全链条、专业化和可追溯管理来加强食品安全，直接保护公众健康。 该法规涵盖五类未明确指明的重点液态食品，并要求从市场监管部门获得准运证。其目的是确保运输全过程的可追溯性和责任落实。

rss · China News Service Scroll · 7月1日 04:51

**背景**: 散装运输液态食品（如食用油）若管理不当会带来污染风险。中国在过去的食品安全丑闻后一直在加强食品安全法律。这一准运证制度增加了监管层级，以防止掺假并确保质量。

**标签**: `#regulation`, `#food safety`, `#logistics`

---

<a id="item-21"></a>
## [香港庆祝回归 29 周年 提出三大重点工作](https://www.chinanews.com.cn/dwq/2026/07-01/10650533.shtml) ⭐️ 2.0/10

香港特区行政长官李家超在庆祝香港回归祖国 29 周年酒会上提出未来发展的三大重点工作：全速编制香港首个五年规划、推进北部都会区建设、进一步改善民生。 这是香港首次编制自己的五年规划，标志着香港向更系统、更长远的战略规划转变。北部都会区项目是一项重大基础设施计划，通过融合创新科技与城市发展，可能重塑香港的经济地理格局。 五年规划（2026-2030 年）预计于 2026 年底公布完整文本，涵盖经济发展、创新科技、社会福利等领域。北部都会区占地约 300 平方公里，旨在打造一个融合高端专业服务、物流和创新科技枢纽的新都会区。

rss · China News Service Scroll · 7月1日 04:46

**背景**: 香港于 1997 年 7 月 1 日回归中国，结束了 156 年的英国殖民统治。北部都会区由前行政长官林郑月娥于 2021 年首次提出，旨在将香港北部发展为一个融合创新科技、产业发展与生态保育的综合区域。五年规划是本届政府的新举措，旨在使香港的发展与国家战略对接。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-tw/北部都會區">北部都會區 - 維基百科，自由的百科全書</a></li>
<li><a href="https://baike.baidu.com/item/香港五年规划/67394987">香港五年规划_百度百科</a></li>
<li><a href="https://sc.news.gov.hk/TuniS/www.news.gov.hk/chi/2026/03/20260317/20260317_103729_040.html">香港政府新闻网 - 香港五年规划正式文本年底公布</a></li>

</ul>
</details>

**标签**: `#politics`, `#Hong Kong`, `#news`

---

<a id="item-22"></a>
## [中国发布四川高县 5.5 级地震烈度图](https://www.chinanews.com.cn/gn/2026/07-01/10650526.shtml) ⭐️ 2.0/10

2026 年 7 月 1 日，中国地震局正式发布了针对 2026 年 6 月 29 日四川宜宾高县 5.5 级地震的烈度图，该图基于 66 个调查点的震害调查及多项科技支撑成果编制而成。 该烈度图为灾区灾害评估、救援规划及未来地震减灾提供了关键数据，展示了中国标准化的震后响应流程。 此次地震震源深度 6 公里，烈度图依据 GB/T 18208.3-2011、GB/T 17742-2020 和 DB/T 107-2025 等国家标准编制，并参考了余震分布、震源机制解和仪器烈度等数据。

rss · China News Service Scroll · 7月1日 03:58

**背景**: 地震烈度图展示地震动和破坏程度在受影响区域的分布，使用烈度表（如中国地震烈度表）对影响进行分类。震源机制解描述断层类型和滑动方向，仪器烈度则来自地震仪记录。这些工具帮助地震学家了解地震影响并指导应急响应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cea.gov.cn/cea/xwzx/fzjzyw/5845436/index.html">中国地震局发布青海海西6.3级地震烈度图</a></li>
<li><a href="https://zh.wikipedia.org/wiki/震源机制解">震源机制解 - 维基百科，自由的百科全书</a></li>
<li><a href="https://baike.baidu.com/item/震源机制/4835374">震源机制_百度百科 震源机制解、走滑类型 - Leslie° - 博客园 中国震源机制解 - Earthquake 不会沙滩排球的地震学家不是一个好的科研人 - 知乎 震源机制 (Focal Mechanism)之断层基本知识-CSDN博客</a></li>

</ul>
</details>

**标签**: `#earthquake`, `#disaster response`, `#China`

---

<a id="item-23"></a>
## [A 股午评：超 4500 只个股上涨，创业板指下跌](https://www.chinanews.com.cn/cj/2026/07-01/10650524.shtml) ⭐️ 2.0/10

上午交易时段，A 股超 4500 只个股上涨，沪指和深指收涨，创业板指收跌。券商和保险板块大幅上涨，通信设备和电工电网板块下跌。 这一市场走势反映了中国股市的广泛乐观情绪，但板块分化凸显了投资者关注点的转移。金融股的强劲表现可能预示着政策支持或市场情绪改善。 上证综合指数和深证成指均上涨，而创业板指下跌。券商和保险板块领涨，通信设备和电工电网板块跌幅居前。

rss · China News Service Scroll · 7月1日 03:50

**标签**: `#stock market`, `#China`, `#finance`

---

<a id="item-24"></a>
## [乡村教师合唱研讨会在沪举行](https://www.chinanews.com.cn/cj/2026/07-01/10650495.shtml) ⭐️ 2.0/10

第四届中小学乡村教师合唱教育及振兴研讨会于 2026 年 6 月 27 日至 29 日在上海成功举行。 该研讨会通过培训教师来支持乡村音乐教育，有助于促进农村地区的文化发展和教育公平。 本次活动由中国教育学会音乐教育分会、上海市高等教育学会和上海音乐学院附属中等音乐专科学校共同主办。

rss · China News Service Scroll · 7月1日 03:28

**背景**: 中国乡村合唱教育面临缺乏专业教师和资源等挑战。该系列研讨会旨在通过为乡村音乐教师提供专业发展来应对这些问题。

**标签**: `#education`, `#music`, `#rural`, `#China`

---

<a id="item-25"></a>
## [银行助餐服务解决老人用餐难题](https://www.chinanews.com.cn/cj/2026/07-01/10650498.shtml) ⭐️ 2.0/10

中国农业银行在厦门推出“农银养老·金岁餐厅”养老助餐服务平台，让老年人可以线上点餐、享受补贴并送餐到家。 该服务解决了许多老年人日常用餐难的问题，提升了他们的生活质量，也展示了金融机构如何将服务延伸至社会福利领域。 该平台是“农银养老”品牌的一部分，该品牌涵盖养老金金融、养老服务金融和养老产业金融，注重科技支撑和消费者权益保护。

rss · China News Service Scroll · 7月1日 03:27

**背景**: 中国人口老龄化带来了日益增长的养老服务需求。许多银行正在开发针对老年人的专属金融产品和服务，包括简化版手机应用和专用热线，以更好地服务这一群体。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://www.bt.chinanews.com.cn/jingji/2024-10-11/doc-ihehwccy6197377.shtml">金色岁月 农情相伴：农业银行发布养老金融服务品牌“农银养老”</a></li>
<li><a href="https://paper.people.com.cn/rmrb/pc/content/202508/19/content_30097064.html">农银养老 金色岁月 农情相伴 打造人民满意的养老金融特色银行</a></li>

</ul>
</details>

**标签**: `#banking`, `#elderly services`, `#meal delivery`

---

<a id="item-26"></a>
## [四明山乡村诊所留住好医生](https://www.chinanews.com.cn/sh/2026/07-01/10650505.shtml) ⭐️ 2.0/10

一篇新闻报道聚焦宁波四明山脚下的一家乡村诊所，通过改善当地条件和激励机制，成功留住了合格的医生。 这一案例展示了解决中国农村医疗人才短缺问题的有效策略，可为面临类似挑战的其他地区提供借鉴。 该文章是中新网于 2026 年 7 月 1 日发布的一篇地方新闻，聚焦四明山地区基层医疗的改善。

rss · China News Service Scroll · 7月1日 03:26

**背景**: 中国农村医疗长期以来因薪酬低、资源有限和地理位置偏远而难以吸引和留住医生。政府已实施多项政策加强基层医疗，包括对农村从业者的激励措施。

**标签**: `#healthcare`, `#China`, `#local news`

---

<a id="item-27"></a>
## [广西 5 条河流出现超警洪水](https://www.chinanews.com.cn/sh/2026/07-01/10650501.shtml) ⭐️ 2.0/10

2026 年 7 月 1 日，广西水文中心报告称，受 6 月 30 日至 7 月 1 日强降雨影响，武称河、者仙河等 5 条河流出现超警 0.07 米至 0.95 米的洪水。 此次事件凸显了广西雨季持续的洪水风险，可能威胁当地社区、农业和基础设施。及时的监测和预警对于防灾减灾至关重要。 最大日降雨量出现在河池市环江县川山镇，达 163.5 毫米。5 条河流的 5 个水文站报告水位超过警戒线。

rss · China News Service Scroll · 7月1日 03:26

**背景**: 广西是中国南方地区，夏季季风季节常出现强降雨，导致河流洪水。水文监测网络跟踪水位以发布预警并指导应急响应。

**标签**: `#flood`, `#Guangxi`, `#weather`, `#China`

---

<a id="item-28"></a>
## [宁夏启动“阅游宁夏”文旅融合活动](https://www.chinanews.com.cn/sh/2026/07-01/10650500.shtml) ⭐️ 2.0/10

2026 年“阅游宁夏”全民阅读文旅融合服务推广活动已全面启动，系列文化惠民活动在宁夏各地有序铺开。 该活动推动阅读与旅游融合，可能提升当地文化参与度和旅游业，但属于常规地方活动，影响范围有限。 该活动由宁夏图书馆于 2026 年 7 月 1 日宣布，包含多项面向公众的文化惠民活动。

rss · China News Service Scroll · 7月1日 03:25

**标签**: `#cultural event`, `#reading promotion`, `#tourism`

---