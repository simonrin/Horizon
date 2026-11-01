---
layout: default
title: "Horizon Summary: 2026-11-01 (ZH)"
date: 2026-11-01
lang: zh
---

> 从 285 条内容中筛选出 28 条重要资讯。

---

1. [Linux TCP 释放后使用漏洞 CVE-2026-98432（CVSS 9.8）](#item-1) ⭐️ 9.0/10
2. [联想 ThinkPlus 指纹 U 盘虚假宣传 AES-256 加密，数据明文存储](#item-2) ⭐️ 8.0/10
3. [OpenAI、谷歌、微软、Anthropic 承诺推出统一 AI 抓取退出机制](#item-3) ⭐️ 8.0/10
4. [FBI 称朝鲜黑客制造币安 63 亿美元史上最大盗窃案](#item-4) ⭐️ 8.0/10
5. [法国拟批准向互联网巨头收“流量税”，每 GB 内容 0.055 欧元](#item-5) ⭐️ 7.0/10
6. [Grok 文本输出将添加隐形水印以符合欧盟 AI 法案](#item-6) ⭐️ 7.0/10
7. [中国载人登月方案：两次发射，一次登月](#item-7) ⭐️ 7.0/10
8. [商汤开源 SenseNova Loop-9B-Preview，宣称媲美 27B 参数模型](#item-8) ⭐️ 7.0/10
9. [Roblox 平台 AI 游戏突破 7 万款，前 100 名超 80% 使用 AI 辅助开发](#item-9) ⭐️ 7.0/10
10. [北大团队为华为鲲鹏 920 优化 ABACUS DFT 软件，最高提速 10.7 倍](#item-10) ⭐️ 7.0/10
11. [美国司法部揭露 2 亿美元 AI 学生贷款欺诈案](#item-11) ⭐️ 7.0/10
12. [中国发布“妈祖”海洋预报数值模式 2.0，重点海域分辨率达 1 公里](#item-12) ⭐️ 6.0/10
13. [中国发布合成生物领域科学智能体，整合 300 多万篇文献与 200 多种工具](#item-13) ⭐️ 6.0/10
14. [美国计划禁止中国电信企业直接接入美国电话号码](#item-14) ⭐️ 6.0/10
15. [名不见经传的公司背负数据中心债务，加剧 AI 泡沫担忧](#item-15) ⭐️ 6.0/10
16. [Grayndler 选区艺术家联合反对 AI 抓取版权内容提案](#item-16) ⭐️ 6.0/10
17. [法官允许 NAACP 针对 xAI 数据中心污染的诉讼继续推进](#item-17) ⭐️ 6.0/10
18. [据报道 OpenAI 下调最新一轮融资目标](#item-18) ⭐️ 6.0/10
19. [浙东首台光子计数 CT 在宁大一院投用](#item-19) ⭐️ 4.0/10
20. [数据中心成为布鲁克林中期选举议题](#item-20) ⭐️ 4.0/10
21. [芹菜降压、苦瓜降糖、大蒜抗癌？识破食物功效神化的套路！](#item-21) ⭐️ 3.0/10
22. [神舟二十三号航天员在太空进行摸鼻子实验](#item-22) ⭐️ 3.0/10
23. [中德科学院举办第三届“科学与未来”研讨会，聚焦气候变化与健康](#item-23) ⭐️ 3.0/10
24. [中瑞创新战略伙伴关系建立 10 周年 将推动科技创新务实合作](#item-24) ⭐️ 3.0/10
25. [江西史上最宽大件运输将大飞机设备运抵南昌](#item-25) ⭐️ 3.0/10
26. [《鲁班文化研究论丛（第四辑）》在山东滕州发行](#item-26) ⭐️ 2.0/10
27. [前三季度物流数据发布：稳中有进、质效双升](#item-27) ⭐️ 2.0/10
28. [中新网发布秋冬流感防治八问八答](#item-28) ⭐️ 2.0/10

---

<a id="item-1"></a>
## [Linux TCP 释放后使用漏洞 CVE-2026-98432（CVSS 9.8）](https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf) ⭐️ 9.0/10

Linux 内核 IPv4 TCP 握手路径中的一个严重释放后使用漏洞被披露，编号为 CVE-2026-98432，CVSS 评分为 9.8。该漏洞影响 4.4 及之后的内核版本，远程未认证攻击者可通过精心构造的 TCP 数据包可能实现代码执行。 这对大量 Linux 服务器（包括广泛用于企业和云环境的 Ubuntu 和 RHEL）构成严重的远程代码执行风险。高 CVSS 评分和活跃的社区讨论凸显了修补和缓解措施的紧迫性。 利用该漏洞需要多个 CPU 核心，并且通过互联网利用的可能性较低，因为大多数 ISP 路由器会丢弃带有 IP 选项字段的数据包；根据 Red Hat 的说法，自行丢弃此类数据包有帮助但并非完全缓解。截至讨论时，Ubuntu 和 RHEL 尚未提供补丁。

hackernews · oger · 10月31日 19:16 · [社区讨论](https://news.ycombinator.com/item?id=50319143)

**背景**: 释放后使用漏洞发生在程序释放内存后继续使用指向该内存的指针，可能允许攻击者执行任意代码。CVSS 9.8 是严重级别的评分，表明该漏洞易于远程利用，并对机密性、完整性和可用性造成高影响。Linux 内核的 TCP 协议栈是处理网络连接的核心组件，因此其中的漏洞尤其危险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/security/security-bulletins/2026-160-aws/">CVE-2026-98432 - Linux kernel IPv4 TCP use-after-free ...</a></li>
<li><a href="https://access.redhat.com/security/cve/cve-2026-98432">CVE-2026-98432 - Red Hat Customer Portal</a></li>
<li><a href="https://thehackernews.com/2026/10/linux-kernel-tcp-flaw-with-98-cvss.html">Linux Kernel TCP Flaw With 9.8 CVSS Score Affects Ubuntu, Red ...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出标题应明确是 Linux 漏洞，因为其他操作系统不受影响，并澄清不需要 MPTCP，且利用受 IP 选项过滤和单核系统限制。一些人对 Ubuntu 和 RHEL 等主要发行版尚未发布补丁表示不满，另一些人则对 C 与 Rust 发表了讽刺性评论。

**标签**: `#security`, `#linux-kernel`, `#vulnerability`, `#tcp`, `#cve`

---

<a id="item-2"></a>
## [联想 ThinkPlus 指纹 U 盘虚假宣传 AES-256 加密，数据明文存储](https://www.ithome.com/1/020/696.htm) ⭐️ 8.0/10

研究人员发现，联想 ThinkPlus FU100 指纹 U 盘宣称使用 AES-256 硬件加密，但实际上数据以明文形式存储于内部 SD 卡中；同时，联想对 TSD303 指纹 SSD 的修复方案使用了一个由类似时间戳的值生成的可预测 SM4 密钥。 此次披露涉及五家厂商，凸显了消费级存储设备中的严重安全缺陷，可能导致敏感用户数据泄露，并削弱人们对硬件加密宣传的信任。 FU100 上的指纹识别器仅控制 U 盘是否与电脑连接，并不保护 SD 卡中的文件；联想发布了安全公告 LEN-210545，列出三个高危 CVE 编号，并为受影响用户提供免费升级。

rss · ITHome Feed · 11月1日 03:53

**背景**: AES-256 是一种广泛使用的对称加密标准，用于保护静态数据，硬件加密通常被宣传为比软件方案更安全。SM4 是一种类似 AES 的中国分组密码标准。M.2 是内部 SSD 的常见外形规格。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/M.2">M . 2 - Wikipedia</a></li>
<li><a href="https://www.oryx-embedded.com/doc/sm4_8c_source.html">sm 4 .c Source Code - SM 4 encryption algorithm</a></li>

</ul>
</details>

**标签**: `#security`, `#hardware`, `#encryption`, `#vulnerability-disclosure`, `#storage`

---

<a id="item-3"></a>
## [OpenAI、谷歌、微软、Anthropic 承诺推出统一 AI 抓取退出机制](https://www.rfi.fr/cn/%E7%A7%91%E6%8A%80%E4%B8%8E%E6%96%87%E5%8C%96/20261031-%E5%A4%9A%E5%AE%B6%E7%A7%91%E6%8A%80%E5%B7%A8%E5%A4%B4%E5%90%91%E5%AA%92%E4%BD%93%E6%89%BF%E8%AF%BA-%E5%B0%86%E5%87%BA%E5%8F%B0%E6%96%B0%E6%96%B9%E6%A1%88%EF%BC%8C%E7%A6%81%E6%AD%A2%E6%8A%93%E5%8F%96%E6%96%B0%E9%97%BB%E5%86%85%E5%AE%B9%E7%94%A8%E4%BB%A5%E8%AE%AD%E7%BB%83ai%E6%A8%A1%E5%9E%8B) ⭐️ 8.0/10

据法新社报道，2026 年 10 月 30 日（周五），OpenAI、谷歌、微软和 Anthropic 承诺为媒体机构及网站提供一种统一的方式，阻止其内容被抓取用于训练 AI 模型。这些公司表示该机制将作为一项即将推出的方案落地，具体技术细节仍有待公布。 这是大型 AI 开发商首次联合支持统一的退出标准，可能重塑出版商与 AI 公司之间关于训练数据的谈判方式，并减少网站目前必须逐家向各公司分别声明偏好的碎片化局面。此举直接涉及版权争议和新兴的 AI 透明度规则，影响新闻机构、创作者以及任何内容被用于模型训练的网站。 该退出机制预计将写入网站现有的 robots.txt 文件中——这是长期以来告知爬虫可访问范围的惯例——而不再需要向每家 AI 公司单独发送信号。不过，这目前仅是一项承诺：具体语法、执行方式，以及未签署协议的 AI 开发商是否会遵守，均尚未明确。

rss · RFI Chinese · 10月31日 09:00

**背景**: AI 模型依赖海量网络数据训练，其中大量内容受版权保护；截至 2023 年，美国已有多起诉讼质疑这种数据抓取是否属于合理使用。网站历来通过 robots.txt 表明搜索索引和归档的抓取许可，但 AI 训练偏好此前需要分别向各家公司传达。统一标准将把这一信号集中化，为出版商提供更清晰、机器可读的退出方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/tech/1023763/openai-google-microsoft-ai-scraping-standard-opt-out">The biggest names in AI are backing a new way to opt out of scraping</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_intelligence_and_copyright">Artificial intelligence and copyright - Wikipedia</a></li>
<li><a href="https://riseuplabs.com/compliant-web-scraping-for-ai-training-datasets/">Compliant Web Scraping for AI Training Datasets - Riseup Labs</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#content scraping`, `#copyright`, `#media`, `#OpenAI`

---

<a id="item-4"></a>
## [FBI 称朝鲜黑客制造币安 63 亿美元史上最大盗窃案](https://www.nytimes.com/2026/10/31/world/asia/north-korea-hacking.html) ⭐️ 8.0/10

美国联邦调查局（FBI）将加密货币交易所币安遭到的 63 亿美元黑客攻击归咎于朝鲜国家支持的 TraderTraitor 组织，这是有记录以来最大的加密货币盗窃案。币安表示已替换了 90%的被盗资产，并将承担剩余 10%的损失，确保用户不承担财务损失。 此次盗窃规模超过 2025 年的 Bybit 黑客事件，凸显朝鲜网络部队已成为加密货币交易所和全球金融安全的重大威胁。这也引发了对交易所安全实践以及执法部门追回被盗数字资产能力的质疑。 攻击者利用 EIP-7702 功能，在大约 20 分钟内从 10 条区块链上的钱包中盗走资产，约 30 亿美元的稳定币已被冻结。币安最初暂停了所有交易，提款预计于周日恢复。

rss · The New York Times World · 10月31日 23:05

**背景**: TraderTraitor 又称 Lazarus Group，是朝鲜的一个黑客组织，与一系列加密货币盗窃案有关，包括 2025 年 Bybit 的 15 亿美元黑客事件。朝鲜被指控利用窃取的加密货币资助其武器项目，FBI 已多次就此类国家支持的活动发布警报。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/cwg7xp8kx4v5o">Crypto giant Binance hit by hack suspected to be largest in ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/2026_Binance_hack">2026 Binance hack - Wikipedia</a></li>
<li><a href="https://www.fbi.gov/investigate/cyber/alerts/2026/north-korea-responsible-for-6-billion-binance-attack">North Korea Responsible for $6 Billion+ Binance Attack — FBI</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#cryptocurrency`, `#North Korea`, `#hacking`, `#Binance`

---

<a id="item-5"></a>
## [法国拟批准向互联网巨头收“流量税”，每 GB 内容 0.055 欧元](https://www.ithome.com/1/020/724.htm) ⭐️ 7.0/10

2026 年 10 月 30 日，法国国民议会以 11 票对 10 票的微弱优势通过了第 I-1358 号修正案，规定对谷歌、Netflix、TikTok 和 Meta 等内容提供商向法国用户传输的每 GB 数据征收 0.055 欧元的税。该修正案由社会党议员洛朗·拉尔迪提出，现已纳入 2027 年预算案，尚需进一步议会审查。 若最终生效，这将成为首个针对互联网流量的按 GB 征税的主要税种，可能重塑互联网经济模式，并为其他国家开创先例。大型科技公司每年可能面临数十亿欧元的成本，该税还可能影响法国境内内容的传输和定价方式。 该税将根据法国互联网服务提供商测量的流量计算，ISP 需在电信监管机构 Arcep 的监督下按季度向税务机关提交汇总数据。提案预计每年可带来约 100 亿欧元的收入，五家主要公司占法国每年 2000 亿 GB 传输量的一半，且征税对象是内容提供商而非广告收入或订阅量。

rss · ITHome Feed · 11月1日 06:24

**背景**: 像 Akamai 这样的内容分发网络（CDN）是由边缘服务器组成的全球分布式网络，通过将网页内容缓存并分发到离用户更近的位置来降低延迟、提升性能。该税针对产生大量流量的公司，包括 CDN 提供商，并引发了关于网络中立性的讨论——即所有互联网流量都应被平等对待，不应受到歧视或差别定价。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ababnews.com/en/news/cb8a0fbd-5ccc-4587-a800-6dbd11a9dd19">The French National Assembly passes a data tax by 11 votes to ...</a></li>
<li><a href="https://circleid.com/posts/french-lawmakers-back-per-gigabyte-internet-traffic-tax-despite-government-opposition">French Lawmakers Back Per-Gigabyte Internet Traffic Tax ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Net_neutrality">Net neutrality - Wikipedia</a></li>

</ul>
</details>

**标签**: `#internet-policy`, `#taxation`, `#big-tech`, `#france`, `#net-neutrality`

---

<a id="item-6"></a>
## [Grok 文本输出将添加隐形水印以符合欧盟 AI 法案](https://www.ithome.com/1/020/721.htm) ⭐️ 7.0/10

SpaceXAI 宣布，自 11 月 7 日起，将在全球范围内为 Grok 模型生成的所有文本添加隐形水印，涵盖 grok-4.7、grok-4.6、grok-4.5、grok-4.3 以及 grok-4.20 系列模型，团队管理员可以针对单个模型关闭水印。 这使 SpaceXAI 成为首批在全球范围内部署 token 级隐形水印的主要 AI 提供商之一，为其他公司如何遵守欧盟《人工智能法案》对 AI 生成内容的透明度要求树立了先例。 该水印并非通过隐藏字符或元数据实现，而是融入模型生成文本时对 token 的选择过程，检测器可通过识别该信号来判断一段文本是否带有隐形水印。

rss · ITHome Feed · 11月1日 06:11

**背景**: 欧盟《人工智能法案》于 2024 年 3 月正式通过并分阶段生效，要求 AI 系统提供商对 AI 生成内容进行标记，以便识别其为机器生成。像 KGW 这样的水印技术会在 LLM 推理过程中将统计模式嵌入 token 的选择中，使文本对人类不可感知但可被算法检测。这种方法旨在平衡可检测性与生成文本的语义质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2402.18059v3">Token-Specific Watermarking with Enhanced Detectability and ...</a></li>
<li><a href="https://datainnovation.org/2024/07/the-ai-acts-ai-watermarking-requirement-is-a-misstep-in-the-quest-for-transparency/">The AI Act ’s AI Watermarking Requirement Is a Misstep in the Quest...</a></li>

</ul>
</details>

**标签**: `#AI governance`, `#EU AI Act`, `#watermarking`, `#LLM`, `#Grok`

---

<a id="item-7"></a>
## [中国载人登月方案：两次发射，一次登月](https://www.ithome.com/1/020/683.htm) ⭐️ 7.0/10

10 月 31 日在北京举行的第七届载人航天学术大会上，中国正式公开了载人登月方案，计划在 2030 年前采用“两次发射、一次登月”的方式实现中国人登陆月球。两枚长征十号火箭将先后发射揽月着陆器和梦舟飞船，在环月轨道交会对接；3 名航天员飞往环月轨道，其中 2 人乘坐着陆器降落到月面。 这一公布是中国航天计划的重大里程碑，详细说明了首次载人登月任务的具体架构，标志着国际探月竞赛进入新阶段。该方案强调月球极区水冰科学，并计划在首次任务中就携带月球车，可能影响未来月球资源利用和长期探索战略。 任务将使用两枚长征十号火箭：第一枚将揽月着陆器送入环月轨道，第二枚发射搭载 3 名航天员的梦舟飞船；交会对接后，2 名航天员乘坐揽月着陆器降落到月面，完成任务后再次在环月轨道交会，由飞船将航天员送回地球。值得注意的是，首次载人登月就将携带月球车，以提升月面机动性和作业能力。

rss · ITHome Feed · 11月1日 03:07

**背景**: 中国载人登月计划建立在嫦娥无人探月任务成功的基础上，包括月球采样返回和月背探测。长征十号是专门为载人登月研制的新一代重型运载火箭，梦舟飞船和揽月着陆器则分别是载人飞船和月面着陆器。“两次发射、一次登月”方案将载人运输和着陆功能分离，使每种飞行器都能针对安全性和效率进行优化，这与其它航天机构研究过的架构类似。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/wiki/长征十号运载火箭">长征十号运载火箭 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.baike.com/wikiid/7338878677747089443">揽 月 月 面 着 陆 器 -快懂百科</a></li>
<li><a href="https://paper.people.com.cn/rmrb/pc/attachement/202508/18/52f6f5cd-4f71-47ba-90bd-f48a8abe4b97.pdf">paper.people.com.cn/rmrb/pc/attachement/202508/18/52f6f5cd-4f71-47...</a></li>

</ul>
</details>

**标签**: `#space exploration`, `#crewed lunar mission`, `#aerospace engineering`, `#China space program`, `#orbital rendezvous`

---

<a id="item-8"></a>
## [商汤开源 SenseNova Loop-9B-Preview，宣称媲美 27B 参数模型](https://www.ithome.com/1/020/654.htm) ⭐️ 7.0/10

商汤科技于 10 月 30 日宣布开源 SenseNova Loop-9B-Preview，这是一个基于 Looped Transformer 架构的 90 亿参数模型，通过多轮迭代复用共享层来扩展有效计算深度。官方宣称其性能可媲美 270 亿参数模型，并在 WorkBuddy Bench、RaccoonPPT Bench 和 AutomationBench 等评测中超过 Qwen3.5-27B。 这一发布表明，像 Looped Transformer 这样的参数高效架构有可能以远少于大模型的参数量，实现接近大模型的推理和任务表现，从而降低推理成本，并推动更强大的小模型在代码、办公和智能体任务中的应用。这也反映出中国主要 AI 实验室正日益关注超越简单规模扩展的新型架构设计。 该模型保留首尾各 4 层原始解码器模块，将中间层改造为参数共享的循环计算模块，并引入 mHC（流形约束超连接）与多路残差连接来稳定信号传播。消融实验显示，mHC 使 GPQA Diamond 提升 4.42 分、TeamBench 提升 13.34 分，不过该版本仍为预览版，尚未经过同行评审验证。

rss · ITHome Feed · 11月1日 01:02

**背景**: Looped Transformer 是一种参数高效的设计，它通过多次重复应用相同的 Transformer 模块来模拟更深网络的深度，而不增加参数量。mHC 是一种较新的技术，它将残差连接空间投影到数学流形上，以在极深或循环模型中保持稳定的恒等映射。商汤的日日新（SenseNova）是其大模型系列，此次开源也是高效架构开源趋势的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/sensenova/SenseNova-Loop-9B-Preview">sensenova / SenseNova - Loop - 9 B - Preview · Hugging Face</a></li>
<li><a href="https://github.com/OpenSenseNova/SenseNova-Loop">GitHub - OpenSenseNova/ SenseNova - Loop · GitHub</a></li>
<li><a href="https://arxiv.org/abs/2512.24880">[2512.24880] mHC: Manifold-Constrained Hyper-Connections mHC: Manifold-Constrained Hyper-Connections - arXiv.org mHC: Manifold-Constrained Hyper-Connections mHC: Manifold-Constrained Hyper-Connections - GitHub Manifold-Constrained Hyper-Connections (mHC) - GitHub mHC: Manifold-Constrained Hyper-Connections - OpenReview [paper] mHC: Manifold-Constrained Hyper-Connections</a></li>

</ul>
</details>

**标签**: `#LLM`, `#open-source`, `#Looped Transformer`, `#model-architecture`, `#efficient-models`

---

<a id="item-9"></a>
## [Roblox 平台 AI 游戏突破 7 万款，前 100 名超 80% 使用 AI 辅助开发](https://www.ithome.com/1/020/651.htm) ⭐️ 7.0/10

Roblox 在 2026 财年第三季度报告中透露，使用 Build 工具创建的 AI 游戏已超过 7 万款，9 月游玩时长排名前 100 的游戏中超过 80% 使用了 AI 辅助开发。两款几乎完全由 AI 创作的游戏进入同时在线玩家排行榜前 20 名，自 2026 年 7 月推出以来已有超过 50 万用户使用 Build。 这强烈表明生成式 AI 正从实验性工具走向全球最大用户生成游戏平台的主流生产流程，降低了创作者的门槛，并可能重塑游戏的大规模制作与消费方式。同时也引发了关于内容质量、年龄适宜性以及平台驱动 AI 创作经济性的问题。 Build 是一款移动端优先的 AI 工具，用户用自然语言描述游戏想法即可获得可玩、可发布的游戏；该工具面向年满 9 岁且完成年龄验证的用户开放，但已发布的 AI 生成游戏仅限 16 岁以上用户游玩。Roblox 还计划推出 Universal Player 计划，允许开发者导入现有的主机、PC 或移动游戏，并指出第三季度日活跃用户中 26% 为 18 至 34 岁，18% 未满 18 岁。

rss · ITHome Feed · 11月1日 00:40

**背景**: Roblox 是一个大型在线平台，用户使用其自研引擎和基于 Lua 的脚本创建并游玩游戏。2026 年 7 月，它推出了 Build——一款移动端优先的 AI 创作工具，无需编程或游戏开发经验，仅凭文本提示即可生成可玩的游戏。此类生成式 AI 工具正越来越多地被集成到游戏引擎和平台中，以加速原型制作并降低业余创作者的技术门槛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://create.roblox.com/docs/ai/build">Create games with Build | Documentation - Roblox Creator Hub</a></li>
<li><a href="https://create.roblox.com/docs/generative-AI">Games with Generative AI | Documentation - Roblox Creator Hub</a></li>
<li><a href="https://www.five.reviews/how-to/roblox-ai-game-builder/">Roblox AI Game Builder: Create Games With AI</a></li>

</ul>
</details>

**标签**: `#AI game development`, `#Roblox`, `#generative AI`, `#platform economy`, `#industry trends`

---

<a id="item-10"></a>
## [北大团队为华为鲲鹏 920 优化 ABACUS DFT 软件，最高提速 10.7 倍](https://www.ithome.com/1/020/650.htm) ⭐️ 7.0/10

北京大学陈默涵研究员团队完成了开源密度泛函理论软件 ABACUS 在华为鲲鹏 920 全系列平台上的适配，并对 19 类材料领域核心算子进行了逐项优化。在 28 核标准测试中，采用 SVE 指令集的版本比业界主流 x86 CPU 快 1.3 至 3.9 倍，在启用矩阵运算单元的单节点满核配置下最高快 10.7 倍；相关代码已在 GitHub 开源。 这表明国产 Arm 架构硬件在真实的科学计算负载中能够超越主流 x86 CPU，可能增强鲲鹏在高性能计算和材料科学领域的竞争力。相关优化经验和工具还可能惠及更多向国产平台迁移的大型科学软件项目。 团队分别为 NEON、SVE 和 SVE512 及矩阵运算单元版本建立了独立的编译路径，新增 USE_KML 选项以接入鲲鹏数学库，并重写了 19 类算子以降低平方级复杂度和冗余计算。所有数值结果均与主流实现进行了核对，但这些基准测试由厂商发布，尚未经过同行评审。

rss · ITHome Feed · 11月1日 00:35

**背景**: 密度泛函理论（DFT）是一种广泛用于研究半导体、金属等材料性质的第一性原理方法。ABACUS（原子算筹）是国内自主研发的开源 DFT 软件，全球用户超过一千人。华为鲲鹏 920 是一款基于 Arm 架构的服务器 CPU，支持 NEON、SVE 和 SVE512 向量指令集，其中 SVE 是 Arm 为高性能计算和机器学习负载设计的可伸缩向量扩展指令集。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.csdn.net/AngelLover2017/article/details/124808387">SVE (Scalable Vector Extension)简介【翻译自 armDeveloper ...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/189589184">SVE(可伸缩矢量扩展)介绍 - 知乎</a></li>
<li><a href="https://pip.nju.edu.cn/CN/volumn/volumn_78.shtml">物 理 学进展</a></li>

</ul>
</details>

**标签**: `#HPC`, `#DFT`, `#Kunpeng`, `#performance-optimization`, `#open-source`

---

<a id="item-11"></a>
## [美国司法部揭露 2 亿美元 AI 学生贷款欺诈案](https://www.ithome.com/1/020/649.htm) ⭐️ 7.0/10

美国司法部于 10 月 30 日公布了“捉鬼敢死队行动”的结果，这是一项针对学生贷款欺诈的全国性调查，犯罪分子利用被盗身份和人工智能冒充在线学生，造成超过 2 亿美元的损失。目前已有五人被起诉，涉及 26 个联邦调查局现场办事处和 20 个美国检察官办公室的 40 多起未结欺诈案件。 此案凸显了 AI 如何被武器化以扩大金融欺诈规模，利用联邦援助项目的漏洞，并使无辜受害者背负欺诈性贷款。它强调了在政府金融系统中加强身份验证和 AI 检测的迫切需求。 欺诈者利用被盗身份申请联邦学生资助，并使用 AI 使假学生看起来像是在参加在线课程，部分资金被转移到海外。该计划针对 FAFSA 项目，自 2021 年起被社区学院和大学首次怀疑。

rss · ITHome Feed · 11月1日 00:31

**背景**: FAFSA 是联邦学生援助免费申请表，美国大学用它来确定学生获得联邦和州财政援助的资格。该项目依赖自我报告和核实的信息，使其成为欺诈的目标。深度伪造和自动填表等 AI 技术现在可以模仿合法学生的行为，使检测更加复杂。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ivytrack.org/forum.php?mod=viewthread&tid=937">CSS Profile和 FAFSA 简介 - 奖 学 金 申 请 常春藤之路 ivytrack.org</a></li>
<li><a href="https://juejin.cn/post/7350209063522107430">【AIGC】生成式 AI ...</a></li>

</ul>
</details>

**标签**: `#AI fraud`, `#student loans`, `#cybersecurity`, `#financial crime`, `#policy`

---

<a id="item-12"></a>
## [中国发布“妈祖”海洋预报数值模式 2.0，重点海域分辨率达 1 公里](https://www.chinanews.com.cn/gn/2026/11-01/10724247.shtml) ⭐️ 6.0/10

2026 年 11 月 1 日，自然资源部国家海洋环境预报中心在第十一届世界妈祖文化论坛主论坛上正式发布我国自主研发的“妈祖”海洋预报数值模式 2.0 版本。新版本实现了全球可变分辨率数值模拟、物理动力框架更新、海冰和海洋生态应用场景拓展以及大规模并行计算等升级，全球预报分辨率较上一代提升一倍至 5 公里，我国近海、西太平洋等重点海域分辨率提升至 1 公里。 海洋数值模式是海洋预报的核心技术，“妈祖”2.0 的升级使我国业务化海洋预报能力整体跻身国际先进水平，可服务于深海极地探索、海上通道安全和各类海上生产活动。该模式保留 GPU 高性能加速和轻量化低能耗优势，并与太平洋小岛屿国家开展国际合作与技术输出，显示中国在海洋预报技术领域的影响力不断提升。 2.0 版本保留了 GPU 高性能加速和轻量化低能耗优势，并已在“雪龙 2”号科考船上成功完成船载运行测试。自 2018 年以来，我国先后推出“妈祖·海流”和“妈祖·海浪”1.0 版本，这是首个支持 GPU 加速的全球业务化海洋预报模式，2024 年实现全球代码开源，并已在我国沿海省市部署应用。

rss · China News Service Scroll · 11月1日 05:16

**背景**: 海洋环流数值模式利用数值方法模拟海流、温度、盐度和海冰等要素，其分辨率决定了模式能否精细刻画涡旋、近岸地形等小尺度特征。分辨率越高，预报通常越准确，但计算量也急剧增加，因此 GPU 加速和可变分辨率网格（在重点海域加密、其他区域粗化）成为重要技术方向。“妈祖”系列是我国自主研发的海洋数值模式，旨在提升业务化预报能力和高能效高性能计算水平。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/General_circulation_model">General circulation model - Wikipedia</a></li>
<li><a href="https://beyondeastmedia.com/articles/chinas-mazu-2-0-ocean-model-gpu-acceleration">China’s 'Mazu 2.0' Ocean Model Achieves 1km Resolution via GPU ...</a></li>
<li><a href="https://www.ircmnr.com/html/island/mazu/index.html">Model Home | Mazu Ocean Models - ircmnr.com</a></li>

</ul>
</details>

**标签**: `#ocean-modeling`, `#numerical-forecasting`, `#HPC`, `#climate-science`, `#scientific-computing`

---

<a id="item-13"></a>
## [中国发布合成生物领域科学智能体，整合 300 多万篇文献与 200 多种工具](https://www.chinanews.com.cn/gn/2026/10-31/10724063.shtml) ⭐️ 6.0/10

中国发布了一款合成生物领域科学智能体，整合了 300 多万条高质量科技文献数据、200 多种科研工具和 50 多个生物数据库，并初步验证了 AI 驱动生物制造研发的潜力。该智能体可支持序列比对与注释、蛋白结构预测与功能分析、代谢通路重建与通量分析等任务。 这一领域专用 AI 智能体有望通过自动化复杂工作流程、减少手动整合不同数据源和工具的需求，从而加速合成生物学研究。它反映了构建专用科学 AI 智能体的更广泛趋势，旨在降低高级生物信息学分析的门槛并加快生物制造创新。 该智能体旨在处理序列比对与注释、蛋白结构预测与功能分析以及代谢通路重建与通量分析，但报道未提供技术基准、性能指标或模型架构细节。文中提到初步验证了 AI 驱动生物制造研发的潜力，但未给出具体结果或对比。

rss · China News Service China · 10月31日 13:20

**背景**: 合成生物学是一门跨学科领域，运用工程原理设计和构建新的生物部件、装置和系统，常用于生物制造、医药和农业等应用。AI 智能体是一种软件系统，能够通过对数据的推理和调用工具来自主执行任务，领域专用智能体正越来越多地被用于辅助科学发现。代谢通量分析是一种用于量化代谢物在细胞通路中流动的技术，帮助研究人员优化微生物菌株以生产有价值的化合物。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.synthbiosci.com/posts/the-invisible-arms-race-when-ai-meets-synthetic-biology">The Invisible Arms Race: When AI Meets Synthetic Biology</a></li>
<li><a href="https://en.wikipedia.org/wiki/Metabolic_flux_analysis">Metabolic flux analysis - Wikipedia</a></li>

</ul>
</details>

**标签**: `#synthetic-biology`, `#AI-agents`, `#biomanufacturing`, `#scientific-research`, `#bioinformatics`

---

<a id="item-14"></a>
## [美国计划禁止中国电信企业直接接入美国电话号码](https://www.rfi.fr/cn/%E5%9B%BD%E9%99%85/20261031-%E7%BE%8E%E5%9B%BD%E4%BB%A5%E5%9B%BD%E5%AE%89%E4%B8%BA%E7%94%B1-%E8%AE%A1%E5%88%92%E7%A6%81%E6%AD%A2%E4%B8%AD%E5%9B%BD%E7%94%B5%E4%BF%A1%E4%BC%81%E4%B8%9A%E7%9B%B4%E6%8E%A5%E6%8E%A5%E5%85%A5%E7%BE%8E%E5%9B%BD%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81) ⭐️ 6.0/10

据路透社报道，美国以国家安全为由，计划近期禁止中国电信企业直接接入美国电话号码，以防范诈骗电话和非法自动拨号活动。 这一监管举措可能严重扰乱中美运营商之间的语音互联，影响国际通话路由，并加剧中美科技关系的紧张。它还可能为美国市场对外国电信运营商实施更严格的安全审查开创先例。 该禁令针对的是直接接入美国电话号码，这通常通过运营商之间的电信互联协议实现。报道未说明具体时间表或受影响的中国企业，也不清楚通话是否需经由第三方中介路由。

rss · RFI Chinese · 10月31日 08:49

**背景**: 电信互联使一个运营商网络中的通话能够到达另一个网络的用户；没有互联，不同运营商之间的通话就无法接通。自动拨号电话是利用自动拨号器发出的自动化呼叫，常与电话营销或诈骗相关，而美国监管机构出于国家安全考虑一直在收紧对外国运营商的规则。美国联邦通信委员会（FCC）一直在审查外国电信运营商的牌照，并与国家安全机构协调。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Robocall">Robocall - Wikipedia</a></li>
<li><a href="https://globlar.com/what-is-interconnection-in-telecommunications/">What Is Interconnection in Telecommunications</a></li>
<li><a href="https://convergedigest.com/fcc-looks-to-reevaluate-licenses-of-foreign-telecom-operators/">FCC looks to reevaluate licenses of foreign telecom operators</a></li>

</ul>
</details>

**标签**: `#telecom regulation`, `#national security`, `#US-China relations`, `#robocalls`, `#policy`

---

<a id="item-15"></a>
## [名不见经传的公司背负数据中心债务，加剧 AI 泡沫担忧](https://www.bbc.co.uk/news/articles/cje36degrgv5o?at_medium=RSS&at_campaign=rss) ⭐️ 6.0/10

BBC 的一篇报道指出，一些名不见经传的公司持有数百亿英镑的数据中心债务，这加剧了人们对 AI 投资热潮可能形成泡沫的担忧。文章认为，与 AI 基础设施相关的借贷规模构成了金融风险来源。 如果 AI 收入达不到预期，靠债务融资的数据中心建设可能放大金融不稳定，影响投资者、贷款机构以及更广泛的科技经济。这一点很重要，因为 AI 热潮正越来越多地依赖杠杆而非经营现金流来融资。 BBC 报道提到，不知名公司持有数百亿英镑的数据中心债务，但所提供的摘录没有具体说明涉及哪些公司或贷款机构。更广泛的担忧在于，这些债务大多与未来 AI 收入仍不确定的项目相关。

rss · BBC World · 11月1日 01:37

**背景**: AI 泡沫是指投资者热情推动 AI 相关资产价格和投资远超其 underlying 收入所能支撑的水平，类似于互联网泡沫。数据中心是 AI 的物理基础，容纳训练和运行模型所需的大规模计算集群，而它们正越来越多地通过债务而非股权融资。随着 AI 基础设施支出激增，贷款机构和投资者正在审视回报是否足以偿还不断增长的债务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ft.com/content/5970614a-b1f7-4b4e-b1e5-6038e1dde654?syn-25a6b1a6=1">Investors turn on data centres</a></li>
<li><a href="https://www.cnbc.com/2026/08/14/ai-infrastructure-debt-leverage-risks.html">AI infrastructure debt and leverage draw market scrutiny - CNBC</a></li>
<li><a href="https://armason.co.uk/data-centre-funding/">Data Centre Funding — Debt & equity Finance for... | Armason Advisory</a></li>

</ul>
</details>

**标签**: `#AI bubble`, `#data centres`, `#debt`, `#financial risk`, `#AI infrastructure`

---

<a id="item-16"></a>
## [Grayndler 选区艺术家联合反对 AI 抓取版权内容提案](https://www.theguardian.com/australia-news/2026/nov/01/artists-against-ai-proposal-anthony-albanese-grayndler-sydney-inner-west) ⭐️ 6.0/10

澳大利亚总理安东尼·阿尔巴尼斯所在的悉尼 Grayndler 选区的艺术家和创意工作者正在组织起来，反对一项允许 AI 公司抓取澳大利亚在线创意内容的联邦提案。这场反弹凸显了总理自家选区因版权法修改而日益加剧的政治紧张。 这场辩论可能重塑澳大利亚的版权框架，并为 AI 训练数据的获取方式树立先例，直接影响创作者、AI 开发者和出版商。由于 Grayndler 是总理本人选区且创意经济密集，当地反弹具有超乎寻常的政治分量。 Grayndler 拥有超过 3000 家文化和创意企业，其 10%的劳动者从事文化和创意领域工作，而全国平均水平为 4.2%。该提案将允许 AI 公司抓取澳大利亚人在线创作的一切内容，一些 AI 公司则推动采用“选择退出”模式而非协商许可。

rss · The Guardian World · 10月31日 19:00

**背景**: 澳大利亚一直在辩论是否在版权法中引入文本和数据挖掘例外，允许 AI 开发者在未经许可的情况下使用受保护作品训练模型。政府最近表示不会推进广泛的 TDM 例外，但 AI 公司继续游说争取更便捷的训练数据获取途径，往往倾向于“选择退出”机制而非许可协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/australia-news/2026/nov/01/artists-against-ai-proposal-anthony-albanese-grayndler-sydney-inner-west">Disquiet grows in Albanese’s back yard as Grayndler artists ...</a></li>
<li><a href="https://www.ibanet.org/AI-and-copyright-in-Australia">Artificial intelligence and copyright in Australia: from ...</a></li>
<li><a href="https://australiatimes.com/australia-will-not-permit-free-use-of-copyright-protected-works-for-ai-training">Australia Will Not Permit Free Use of Copyright-Protected ...</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#copyright`, `#content scraping`, `#Australian politics`, `#creative industry`

---

<a id="item-17"></a>
## [法官允许 NAACP 针对 xAI 数据中心污染的诉讼继续推进](https://techcrunch.com/2026/10/31/judge-allows-naacp-lawsuit-over-xai-data-center-pollution-to-move-forward/) ⭐️ 6.0/10

一名联邦法官驳回了 xAI 要求驳回 NAACP 诉讼的动议，允许该案继续审理。NAACP 指控 xAI 在孟菲斯地区的数据中心违反《清洁空气法》，未经许可运行 27 台燃气轮机，在居民区附近排放有害污染物。 这是对 AI 数据中心是否必须遵守联邦环境法律的一次重要法律检验，而且正值公众对数据中心的反对情绪日益高涨之际，纽约最近通过了暂停新建数据中心的禁令。若 xAI 败诉，可能为 AI 公司如何选址和供电其高能耗基础设施树立先例。 诉讼的核心是 NAACP 所称在 xAI 位于孟菲斯西南部的 Colossus 数据中心未经许可安装的 27 台燃气轮机；燃气轮机会排放细颗粒物和有害化学物质等污染物。美国司法部在此案中支持 xAI，为诉讼增添了政治色彩。

rss · TechCrunch · 10月31日 21:17

**背景**: 《清洁空气法》是美国监管空气污染的主要联邦法律，于 1963 年颁布，并在 1970 年和 1990 年大幅扩展。它要求主要排放源获得许可，并制定国家空气质量标准。xAI 由埃隆·马斯克于 2023 年创立，在孟菲斯运营 Colossus 超级计算机集群以训练其 Grok 模型，该集群的电力需求引发了环境担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/10/31/judge-allows-naacp-lawsuit-over-xai-data-center-pollution-to-move-forward/">Judge allows NAACP lawsuit over xAI data center pollution to move...</a></li>
<li><a href="https://www.engadget.com/2195032/doj-backs-xai-naacp-data-center-pollution-lawsuit/">Justice Department Backs xAI In NAACP Lawsuit Over Data Center ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Clean_Air_Act_(United_States)">Clean Air Act (United States) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#data centers`, `#environmental law`, `#xAI`, `#legal`

---

<a id="item-18"></a>
## [据报道 OpenAI 下调最新一轮融资目标](https://techcrunch.com/2026/10/31/openai-reportedly-lowers-funding-target-for-new-round/) ⭐️ 6.0/10

据 TechCrunch 于 2026 年 10 月 31 日发布的报道，OpenAI 已下调其最新一轮融资的目标金额。报道称该轮融资的表现低于预期，但未披露原定目标与调整后目标的具体数字。 OpenAI 是备受关注的 AI 公司之一，下调融资目标可能表明投资者对前沿 AI 开发的经济性日益谨慎。由于 OpenAI 的融资动向常被视为该领域资本充裕度的风向标，此事可能影响更广泛的 AI 创业生态。 该报道篇幅简短，未说明原定或调整后的融资金额、目标估值以及参与投资的机构。目前也不清楚下调目标是源于需求疲软、战略优先级变化，还是有意避免过度融资。

rss · TechCrunch · 10月31日 16:12

**背景**: OpenAI 在此前多轮融资中已筹集数十亿美元，投资方包括微软及多家风险投资机构。这些资金用于支撑训练和运行 GPT-4 等大语言模型所需的巨额算力成本。融资目标是指公司计划筹集的金额，下调目标可能意味着投资者的认购承诺未达到预期。

**标签**: `#OpenAI`, `#funding`, `#AI industry`, `#business news`

---

<a id="item-19"></a>
## [浙东首台光子计数 CT 在宁大一院投用](https://www.chinanews.com.cn/jk/2026/11-01/10724244.shtml) ⭐️ 4.0/10

2026 年 11 月 1 日，宁波大学附属第一医院举行光子计数探测器 CT 启用仪式暨学术活动，该设备为浙东地区首台。该院影像科主任阮新忠将此次设备更新比作从“黑白电视”直接飞跃到“8K 超高清彩色电视”。 这标志着光子计数 CT 技术在浙东地区进入临床使用，当地患者将能获得更高分辨率、更低剂量的影像检查。这也反映出先进 CT 探测器正从科研和大型学术中心走向区域医院常规临床应用的趋势。 光子计数探测器可逐个计数 X 射线光子，以极高空间分辨率提供能量分辨数据且无电子噪声，而传统能量积分探测器需将 X 射线转换为可见光并积分总能量。该报道未披露设备厂商、型号或具体临床性能数据。

rss · China News Service Scroll · 11月1日 05:29

**背景**: 传统 CT 使用能量积分探测器（EID），先将 X 射线光子转换为可见光再对沉积能量求和，这限制了空间分辨率并引入电子噪声。光子计数探测器 CT（PCD-CT）则逐个计数光子并记录其能量，可实现更高分辨率、能谱（多能量）成像，并有望降低辐射剂量。PCD-CT 已于 2021 年 9 月获美国 FDA 批准用于临床，目前正逐步应用于心脏、血管、胸部、肌骨和神经影像等领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Photon-counting_detector">Photon-counting detector</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/37787672/?trk=article-ssr-frontend-pulse_little-text-block">Clinical Applications of Photon - counting CT : A Review of Pioneer...</a></li>
<li><a href="https://scispace.com/papers/seeing-more-with-less-clinical-benefits-of-photon-counting-1lk9iwz3">Seeing More with Less: Clinical Benefits of Photon - counting Detector...</a></li>

</ul>
</details>

**标签**: `#medical imaging`, `#photon-counting CT`, `#healthcare technology`, `#clinical adoption`

---

<a id="item-20"></a>
## [数据中心成为布鲁克林中期选举议题](https://techcrunch.com/2026/10/31/data-centers-are-now-a-midterm-issue-even-in-brooklyn/) ⭐️ 4.0/10

TechCrunch 报道称，在选举日五天前于布鲁克林举行的一场中期选举聚会上，从市议员的炉边谈话到关于民主党的辩论，每一场对话都不断回到人工智能和数据中心这两个话题上。 这表明数据中心和人工智能基础设施已从技术或行业议题转变为主流地方政治议题，意味着候选人可能面临就选址、公用事业费用和社区影响表明立场的压力。这一转变可能影响美国各市镇人工智能基础设施项目的审批和监管方式。 该报道仅是对一场地方活动的轶事性观察，没有提供技术数据、民调或实质性政策分析；但它仍说明数据中心相关担忧已迅速蔓延到传统科技中心之外。

rss · TechCrunch · 11月1日 02:22

**背景**: 数据中心是容纳服务器、支撑云服务和人工智能工作负载的大型设施，自 2023 年以来的快速扩张引发了当地对电力与水资源消耗、公用事业费率以及经济收益公平分配的担忧。随着人工智能需求增长， hosting 或考虑建设这些设施的社区正越来越多地辩论其成本与收益，使这一曾经小众的基础设施议题成为主流政治话题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ncrc.org/the-local-costs-of-the-ai-boom-ensuring-data-centers-deliver-community-benefits-in-the-midst-of-hypergrowth/">The Local Costs of the AI Boom: Ensuring Data Centers Deliver ...</a></li>
<li><a href="https://www.bakertilly.com/insights/data-center-impact-on-local-communities">Data center impact on local communities: Balancing growth ...</a></li>
<li><a href="https://shattered.io/why-data-centers-use-so-much-water-17-4-billion-gallons-2026/">Why Data Centers Use 17.4B Gallons of Water [2026]</a></li>

</ul>
</details>

**标签**: `#data centers`, `#AI policy`, `#politics`, `#infrastructure`, `#tech industry`

---

<a id="item-21"></a>
## [芹菜降压、苦瓜降糖、大蒜抗癌？识破食物功效神化的套路！](https://www.chinanews.com.cn/life/2026/11-01/10724269.shtml) ⭐️ 3.0/10

2026 年 11 月 1 日，中国新闻网发布文章，驳斥社交平台上常见的养生谣言，如芹菜汁降压、苦瓜是天然胰岛素、大蒜抗癌、黑木耳清血管等，指出这些普通蔬果被夸大为“天然药物”的现象。 这很重要，因为此类错误信息可能让人们依赖食物而非经过验证的医学治疗，从而延误高血压、糖尿病等慢性病的有效治疗。它凸显了加强科学传播、帮助公众批判性评估健康声明的必要性。 文章指出，这些说法往往夸大特定成分（如大蒜中的大蒜素、苦瓜中的苦瓜苷）的作用，却忽略了剂量、生物利用度以及缺乏临床证据等因素。它强调，没有任何单一食物可以替代药物或均衡饮食。

rss · China News Service Scroll · 11月1日 05:47

**背景**: 社交平台上充斥着养生建议，将普通蔬果吹捧为灵丹妙药，常冠以“天然药物”之名。这一现象反映了健康传播中的更广泛挑战：区分对食物成分的初步研究与经过验证的临床治疗。了解剂量、研究设计、监管审批等基本概念有助于消费者避免被误导。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://health.baidu.com/m/detail/ar_6459194446347642662">大蒜抗癌的科学依据 | 百度健康·医学科普</a></li>
<li><a href="https://www.familydoctor.cn/hlthsci/dasuansu-kangai-pu-kexue-jiedu-zheba-shuangrenjian-635610.html">大蒜抗癌潜力解析：正确吃法激活三重机制！ - 辟谣与新知 - 家医大健...</a></li>
<li><a href="https://www.sohu.com/a/861053132_121948382">日本研究：大蒜可抑制99%癌细胞？吃大蒜能抗癌吗？真相来了</a></li>

</ul>
</details>

**标签**: `#health misinformation`, `#science communication`, `#nutrition`, `#myth debunking`

---

<a id="item-22"></a>
## [神舟二十三号航天员在太空进行摸鼻子实验](https://www.chinanews.com.cn/gn/2026/11-01/10724234.shtml) ⭐️ 3.0/10

中国新闻网的一则报道聚焦神舟二十三号航天员在太空进行摸鼻子实验，这很可能是一项本体感觉测试，旨在研究微重力如何影响身体感知。该简讯未提供详细结果或方法。 此类实验有助于科学家理解太空中的感觉运动适应，这对航天员在长期任务中的表现和安全至关重要。研究结果可为未来的月球或火星探险提供对策。 摸鼻子任务通过要求航天员在没有视觉反馈的情况下定位自己的鼻子来评估本体感觉——即身体位置感。在微重力环境下，本体感觉线索会发生变化，使其成为一项简单但信息丰富的感觉运动整合测试。

rss · China News Service China · 11月1日 04:25

**背景**: 本体感觉是身体在不依赖视觉的情况下感知自身位置和运动的能力。在太空中，微重力会扰乱这种感觉，影响协调和平衡。航天员经常参与生理实验以研究这些影响，并为长期太空飞行制定对策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Shenzhou_23">Shenzhou 23 - Wikipedia</a></li>
<li><a href="https://my.clevelandclinic.org/health/articles/proprioception">Proprioception : What It Is, How To Improve It & Disorder</a></li>
<li><a href="https://en.wikipedia.org/wiki/Physiological_effects_in_space">Physiological effects in space - Wikipedia</a></li>

</ul>
</details>

**标签**: `#spaceflight`, `#human-factors`, `#physiology`, `#China-space-program`, `#news`

---

<a id="item-23"></a>
## [中德科学院举办第三届“科学与未来”研讨会，聚焦气候变化与健康](https://www.chinanews.com.cn/gn/2026/11-01/10724197.shtml) ⭐️ 3.0/10

中国科学院与德国国家科学院（利奥波第那科学院）于 2026 年 10 月 29 日至 30 日在北京举行第三届“科学与未来”双边研讨会，主题为“气候变化与健康的相互关联性：中国与德国的应对之道”。来自两国高校和科研机构的专家学者及青年学生代表围绕人类与公共健康、人工智能赋能健康与环境领域研究等议题展开跨学科交流。 此次研讨会延续了中德在气候与健康关联领域的科学对话，两国在这一领域面临共同风险，跨境数据与建模合作可为公共卫生政策提供参考。同时，这也表明人工智能赋能健康与环境研究正成为高层双边学术交流的正式议题。 这是“科学与未来”系列研讨会的第三届，活动以跨学科交流为主，并未公布具体研究成果；公告中未披露技术细节、资助承诺或联合行动计划。德方合作机构利奥波第那科学院是德国国家科学院，为政策制定者和社会提供独立咨询。

rss · China News Service China · 11月1日 03:11

**背景**: 德国国家科学院利奥波第那科学院成立于 1652 年，位于哈雷（萨勒），于 2008 年被指定为德国国家科学院，就面向未来的议题为政策制定者提供咨询。中国科学院是中国领先的自然科学研究机构。“人工智能赋能健康与环境研究”指利用机器学习开展临床决策支持、卫生系统管理以及气候和天气建模等任务，这些领域的人工智能应用日益增多，但其可持续性和环境成本仍存在争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/German_National_Academy_of_Sciences_Leopoldina">German National Academy of Sciences Leopoldina</a></li>
<li><a href="https://www.leopoldina.org/en">Leopoldina: Home</a></li>
<li><a href="https://www.qmul.ac.uk/news/latest-news/2025/science-and-engineering/se/can-ai-and-sustainability-co-exist.html">Can AI and sustainability co-exist? - Queen Mary University of London</a></li>

</ul>
</details>

**标签**: `#climate change`, `#public health`, `#AI in health`, `#academic collaboration`, `#China-Germany`

---

<a id="item-24"></a>
## [中瑞创新战略伙伴关系建立 10 周年 将推动科技创新务实合作](https://www.chinanews.com.cn/gn/2026/10-31/10724100.shtml) ⭐️ 3.0/10

2026 年 10 月 31 日，中国科技部部长阴和俊在北京会见瑞士联邦主席兼经济事务、教育和研究部长居伊·帕姆兰，双方就深化中瑞创新战略伙伴关系、推动科技创新务实合作交换意见。 此次会晤正值 2016 年建立的创新战略伙伴关系成立 10 周年，该框架常被视为中国与西方国家关系的典范，表明双方在更广泛的贸易与科学协议背景下继续致力于双边研发合作。 科技部发布的通稿未提及具体协议、资金数额或新项目，而此次会晤恰逢帕姆兰访华期间签署升级版中瑞自由贸易协定和双边研发合作协议。

rss · China News Service China · 10月31日 14:14

**背景**: 中瑞两国于 2016 年建立创新战略伙伴关系，瑞士是首个与中国签署自由贸易协定的欧洲大陆国家。双边科技合作包括由瑞士国家科学基金会与中方伙伴共同资助的联合研究项目（瑞方每个四年期项目资助上限为 35 万瑞士法郎），以及 2019 年启动的中瑞（常州）国际产业创新园。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://www.chinatoday.com.cn/ctenglish/2018/et/202506/t20250603_800403476.html">Creating a New Future for Sino-Swiss Innovative Strategic ...</a></li>
<li><a href="https://www.schweiz-china.eda.admin.ch/en/switzerland-china-strengthen-cooperation-in-trade-and-science">Switzerland and China strengthen cooperation in trade and science</a></li>
<li><a href="https://www.snf.ch/en/uFVQpBCWSS0IITqo/funding/programmes/bilateral-programmes-sino">Sino-Swiss Science and Technology Cooperation</a></li>

</ul>
</details>

**标签**: `#international-cooperation`, `#science-policy`, `#diplomacy`, `#innovation`, `#China-Switzerland`

---

<a id="item-25"></a>
## [江西史上最宽大件运输将大飞机设备运抵南昌](https://www.chinanews.com.cn/gn/2026/10-31/10724095.shtml) ⭐️ 3.0/10

据江西省交通运输执法局 10 月 31 日消息，一件用于国产大飞机零部件生产的关键工艺设备当天在江西境内完成转运，平安运抵南昌，此次运输任务刷新了江西大件运输的宽度纪录。 这次运输凸显了国产大飞机项目背后的物流与公路基础设施挑战，因为运输此类超大、不可解体设备需要办理特殊许可、勘察路线并协调省级交通主管部门。这也表明江西处理极端超限货物的能力在提升，对吸引航空与重型制造业向内陆布局具有意义。 按照中国相关规定，车货总高度超过 4 米、总宽度超过 2.55 米、总长度超过 18.1 米或总质量超过 49 吨即属于大件（超限）运输，需依法办理超限运输许可。报道未披露此次运输的具体宽度、重量或路线，仅说明其打破了江西此前的宽度纪录。

rss · China News Service China · 10月31日 14:08

**背景**: 以 2023 年投入商业运营的 C919 窄体客机为核心的中国国产大飞机项目，依赖遍布全国的专用制造设备供应链。大件运输指运送超过公路标准限值的不可解体货物，通常涉及许可申请、路线规划、桥梁隧道净空核查以及护送安排。各省此类运输纪录常被视为当地重工业物流能力的体现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mot.gov.cn/zhuanti/kuashengdjysxkbszn/">跨省大件运输许可办事指南</a></li>
<li><a href="https://ailegal.baidu.com/legalarticle/qadetail?id=963d4067becf53250403">最新大件运输管理办法 - ailegal.baidu.com</a></li>

</ul>
</details>

**标签**: `#logistics`, `#infrastructure`, `#aviation-manufacturing`, `#china`, `#transport`

---

<a id="item-26"></a>
## [《鲁班文化研究论丛（第四辑）》在山东滕州发行](https://www.chinanews.com.cn/cul/2026/11-01/10724276.shtml) ⭐️ 2.0/10

11 月 1 日，《鲁班文化研究论丛（第四辑）》在鲁班故里山东滕州正式揭彩发行。该论丛由山东建筑大学与滕州市联合组织编撰，是校地协同开展鲁班文化学术研究的系列成果之一。 此次发行体现了通过校地合作传承与研究中国传统工匠文化的持续努力，有助于推动滕州的文化遗产教育与旅游发展，但其影响主要局限于区域和学术层面。 该论丛是由山东建筑大学与滕州市共同编撰的系列第四辑，聚焦鲁班文化的学术研究。简短报道中未提供更多关于具体内容或发行范围的细节。

rss · China News Service Scroll · 11月1日 06:20

**背景**: 鲁班是中国春秋时期的传奇木匠和发明家，被尊为建筑工匠的祖师爷。山东滕州被视为鲁班故里，长期通过学术研究和纪念活动推广鲁班文化。山东建筑大学是一所以建筑和工程为特色的高校，与地方政府合作开展文化遗产项目。

**标签**: `#cultural heritage`, `#academic publication`, `#China`, `#local news`, `#non-technical`

---

<a id="item-27"></a>
## [前三季度物流数据发布：稳中有进、质效双升](https://www.chinanews.com.cn/cj/2026/11-01/10724277.shtml) ⭐️ 2.0/10

11 月 1 日，中国物流与采购联合会发布前三季度物流运行数据：全国社会物流总额 280.0 万亿元，按可比价格计算同比增长 4.9%；物流业总收入 11.1 万亿元，同比增长 4.3%。社会物流总费用与 GDP 比率回落至 13.8%，较上年同期下降 0.2 个百分点，相当于节约全社会物流成本 2100 亿元。 社会物流总费用与 GDP 比率持续回落，表明中国供应链效率在提升，这关系到制造业和贸易的整体竞争力。数据还显示，需求结构和运输结构的优化正在对冲燃料成本上涨压力，有助于实现降低全社会物流成本、畅通经济循环的目标。 13.8%的物流费用与 GDP 比率是衡量物流效率的核心指标，0.2 个百分点的下降按同期 GDP 计算约合 2100 亿元的成本节约。尽管上游燃料成本上涨，报告将改善归因于经济结构、运输结构和需求结构的三重优化。

rss · China News Service Scroll · 11月1日 06:18

**背景**: 社会物流总费用与 GDP 比率是衡量单位经济产出所需物流支出的常用指标，比率越低说明物流效率越高。中国的这一比率多年来持续下降，从 2012 年的 18%降至 2025 年的 13.9%，但仍高于欧美国家水平。中国物流与采购联合会是经政府授权承担物流统计工作的全国性行业组织，也负责编制发布制造业 PMI 等指数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/社会物流总费用与GDP比率/67273256">社会物流总费用与GDP比率 - 百度百科</a></li>
<li><a href="https://baike.baidu.com/item/中国物流与采购联合会/7171905">中国物流与采购联合会 - 百度百科 视频丨稳中有进、质效双升 前三季度物流运行数据发布|中国物流与采购... 工作职能_联合会专区_中国物流与采购网 中国物流与采购网 - 中国物流与采购行业门户网站 工作职责_科技信息部_中国物流与采购联合会</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2072620082145015227">2025年社会物流总费用与GDP比率降至13.9% - 知乎</a></li>

</ul>
</details>

**标签**: `#logistics`, `#macroeconomic-data`, `#china`, `#industry-report`

---

<a id="item-28"></a>
## [中新网发布秋冬流感防治八问八答](https://www.chinanews.com.cn/jk/2026/11-01/10724272.shtml) ⭐️ 2.0/10

2026 年 11 月 1 日，第九个世界流感日，中国新闻网发布文章，以八问八答的形式解答秋冬流感季关于流感预防和疫苗接种的常见问题。 该文章有助于提高公众对流感及疫苗接种的认识，在秋冬呼吸道疾病高发、流感病毒活跃的时期具有重要意义。 文章强调接种疫苗是重要预防手段，并针对重点人群提供防护建议，但未涉及技术细节或具体疫苗推荐。

rss · China News Service Scroll · 11月1日 06:06

**背景**: 世界流感日定于每年 11 月 1 日，由中国疾控中心联合国际专家于 2018 年发起，旨在纪念 1918 年大流感并推动流感防控。季节性流感每年在全球导致 300-500 万重症病例，在中国，多种流感亚型同时流行，包括 H3N2 和 Victoria 系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/世界流感日/69551009">世界流感日（流感防控宣传日）_百度百科</a></li>
<li><a href="https://news.qq.com/rain/a/20261030A0AW0200">科学识流感，健康过秋冬—— 2026 年世界流感日：致全体市民的健康倡议_...</a></li>
<li><a href="https://m.ithc.cn/article/475764">秋冬季呼吸道传染病防控提示：优先落实 流 感 疫 苗 接 种</a></li>

</ul>
</details>

**标签**: `#public health`, `#influenza`, `#vaccination`, `#health awareness`

---