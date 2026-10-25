---
layout: default
title: "Horizon Summary: 2026-10-25 (ZH)"
date: 2026-10-25
lang: zh
---

> 从 314 条内容中筛选出 28 条重要资讯。

---

1. [Goose：一种具有多数据栈和可调整字段的新语言](#item-1) ⭐️ 8.0/10
2. [Block 推出全双工 AI 语音模型 Dessa，可在 MacBook 本地运行](#item-2) ⭐️ 8.0/10
3. [标普调整成长股与价值股划分规则，影响 3750 亿美元被动基金](#item-3) ⭐️ 7.0/10
4. [被解雇的 OpenAI 安全研究员否认泄密，怀疑因推动透明度被针对](#item-4) ⭐️ 7.0/10
5. [谷歌付费让家庭和企业减少用电，为 AI 数据中心腾出 1070MW 电网容量](#item-5) ⭐️ 7.0/10
6. [亚马逊 CEO 贾西：AWS 算力到 2027 年基本售罄，部分订单锁定至 2028 年](#item-6) ⭐️ 7.0/10
7. [Playden 工具让破解版 PS5 通过 Wine 和 DXVK 运行 Steam Windows 游戏](#item-7) ⭐️ 7.0/10
8. [PHP 基金会仅有一名全职员工，却支撑着七成网站](#item-8) ⭐️ 7.0/10
9. [开源项目 GPU Unlock 可提升英伟达 RTX 30 系列 AI 算力高达 60%](#item-9) ⭐️ 7.0/10
10. [PHP2Shell：两个严重 PHP 漏洞险些击垮互联网](#item-10) ⭐️ 7.0/10
11. [Grok 与 GPT-4o 在政治推荐上严重分歧](#item-11) ⭐️ 7.0/10
12. [为何必须迅速制定 SF6 排放国际标准？](#item-12) ⭐️ 6.0/10
13. [乌克兰称星链连接在限速一周后恢复稳定](#item-13) ⭐️ 6.0/10
14. [BBC Verify 追踪美国中期选举中 8000 万美元 AI 生成广告](#item-14) ⭐️ 6.0/10
15. [TechCrunch 的 AI 墓地：追踪失败与延期的 AI 项目](#item-15) ⭐️ 6.0/10
16. [相干科技成立三周年，聚焦实用型量子系统](#item-16) ⭐️ 5.0/10
17. [中国居民用电近十年首现负增长，AI 与电动车用电激增](#item-17) ⭐️ 5.0/10
18. [数据中心成为威斯康星州两党共同关注的政治议题](#item-18) ⭐️ 5.0/10
19. [专家呼吁“十五五”窗口期推进“深绿”转型](#item-19) ⭐️ 3.0/10
20. [中新网评：洁厕剂包装越像饮料，安全警示越不能像摆设](#item-20) ⭐️ 3.0/10
21. [中国三季度出口首破 8 万亿元，同比增长 22%](#item-21) ⭐️ 3.0/10
22. [正常咨询变投诉：快递业“以罚代管”怪圈](#item-22) ⭐️ 3.0/10
23. [2026 伦敦世界旅游交易会：中国展区规模创历届新高](#item-23) ⭐️ 2.0/10
24. [中国秋粮收获过八成，新技术助力提质增效](#item-24) ⭐️ 2.0/10
25. [河南粮食总产有望连续 10 年保持在 1300 亿斤以上](#item-25) ⭐️ 2.0/10
26. [亚行批准 1742 万美元融资助不丹应对物价上涨](#item-26) ⭐️ 2.0/10
27. [2026 中韩经济发展论坛在首尔开幕](#item-27) ⭐️ 2.0/10
28. [第四届中外戏剧交流与合作论坛在北京开幕](#item-28) ⭐️ 2.0/10

---

<a id="item-1"></a>
## [Goose：一种具有多数据栈和可调整字段的新语言](https://aardappel.github.io/goose/) ⭐️ 8.0/10

Goose 是由 Aardappel（Wouter van Oortmerssen）开发的一种新编程语言，它使用多个数据栈和可调整字段进行自动内存分析，从而实现直接内存映射和高效解析。该语言在 Hacker News 上通过 AMA 发布，并得到了 John Carmack 的推荐。 Goose 通过完全消除堆来挑战传统的基于堆的内存管理，这可能为受限用途的程序带来更快的解析和更安全的内存使用。John Carmack 的推荐以及 Hacker News 上的高参与度表明人们对替代内存模型有浓厚兴趣。 Goose 没有堆；每个动态值都内联在由编译器管理的数据栈上，增长时推进指针，作用域结束时释放内存。它支持固定数量的可增长内存区域，这限制了对像哈希表这样具有任意插入和删除的动态数据结构的支持。

hackernews · bobbydigitales · 10月24日 19:06 · [社区讨论](https://news.ycombinator.com/item?id=50224100)

**背景**: Goose 由 Wouter van Oortmerssen（Aardappel）设计，他以 FlatBuffers 序列化库和 Lobster 编程语言而闻名。该语言面向可以静态分析内存布局的场景，避免垃圾回收和堆分配。它借鉴了基于区域的内存管理等想法，这些想法曾在 ML 类语言中探索过。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/aardappel/goose/blob/master/README.md">goose /README.md at master · aardappel/ goose · GitHub</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 Goose 的新颖方法，一些人指出它在高效解析和直接内存映射方面的潜力。有人对表示动态大小的值以及在没有垃圾回收的情况下内存增长提出了担忧，并将其与 ML 研究中的基于区域的内存管理进行了比较。

**标签**: `#programming languages`, `#memory management`, `#static analysis`, `#language design`, `#Hacker News`

---

<a id="item-2"></a>
## [Block 推出全双工 AI 语音模型 Dessa，可在 MacBook 本地运行](https://www.ithome.com/1/017/557.htm) ⭐️ 8.0/10

杰克·多尔西旗下的金融服务公司 Block 发布了 Dessa，这是一款完全基于人类语音数据训练的全双工语音模型，训练仅使用一组英伟达 GPU 机架，可在搭载 M4 Max 及以上芯片的 MacBook 上本地运行。Dessa 能原生表达笑声、停顿、哽咽等情绪，并可一边说话一边收听，不同于主流先转文本的语音处理链路。 这挑战了 ElevenLabs v4、Fish Audio Drama 3 等依赖音频标签控制情绪的主流“先转文本”链路，并表明富有情感的全双工语音 AI 可在消费级硬件上运行。它有望降低 Block 面向商户的语音产品（如 Square 的点单业务）的成本，并推动行业转向原生语音到语音模型。 Dessa 暂不对外开放试用，Block 正邀请安全研究者测试其欺骗人类的风险，且尚不清楚该模型底层是否仍依靠某种标签来调控情绪。本地运行门槛为 M4 Max 及更高配置的 MacBook，Block 称模型的知识来源于其训练所用的对话数据，而非外部大语言模型。

rss · ITHome Feed · 10月25日 02:29

**背景**: 全双工语音模型可以同时收听和说话，支持自然打断和来回对话，类似 OpenAI 的 GPT-Live。目前大多数语音 AI 系统采用“语音转文字→大语言模型→语音合成”的流水线，会丢失语调、情绪等副语言信息。在苹果芯片上本地运行此类模型依赖统一内存和 MLX 等框架，M4 Max 提供足够的内存带宽用于端侧推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fullduplex.ai/">Fullduplex — an observatory for speech-to-speech, full-duplex ...</a></li>
<li><a href="https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4">Eleven v4 | ElevenLabs Documentation</a></li>
<li><a href="https://willitrunai.com/blog/m4-max-for-ai-local-models">M4 Max for AI — Running Local Models on Apple Silicon</a></li>

</ul>
</details>

**标签**: `#voice-ai`, `#full-duplex`, `#speech-model`, `#local-inference`, `#emotion-modeling`

---

<a id="item-3"></a>
## [标普调整成长股与价值股划分规则，影响 3750 亿美元被动基金](https://36kr.com/newsflashes/4040646265181058?f=rss) ⭐️ 7.0/10

标普道琼斯指数公司修订了成长股与价值股的划分规则，将无形资产、预期盈利和自由现金流纳入价值股评估因素，同时不再将过去 12 个月的股价上涨势头作为成长股评估标准。新规将于当地时间 12 月 21 日美股开盘前生效，跟踪指数的基金需相应调仓，约 3750 亿美元被动基金将受到影响。 这一变化重新定义了数万亿美元被动基金在成长与价值风格之间的配置方式，可能重塑许多公司的资金流向和估值，尤其是拥有大量无形资产的技术公司。它还回应了长期以来的批评，即存在缺陷的价值衡量标准导致了价值股的长期低迷表现。 新方法将无形资产、预期盈利和自由现金流纳入价值评分，而成长股分类不再依赖 12 个月动量。跟踪受影响指数的基金必须在 12 月 21 日开盘前调整持仓，研究人员和基金经理认为现有衡量标准是价值股长期回报疲软的部分原因。

rss · 36Kr Feed · 10月25日 02:15

**背景**: 标普道琼斯指数公司将股票划分为成长型和价值型风格，以创建被动基金跟踪的风格特定指数。传统上，成长股通过高盈利增长或价格动量来识别，而价值股则通过低估值指标如市净率或市盈率来识别。指数再平衡迫使跟踪基金买卖股票以匹配新的指数构成，这可能在生效日期前后产生巨大的交易量和价格影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.indexologyblog.com/2026/10/02/greek-myths-and-icelandic-sagas-reclassifications-in-the-global-market-library/">Greek Myths and Icelandic Sagas: Reclassifications in the Global...</a></li>
<li><a href="https://www.investopedia.com/index-rebalancing-7972596">The Importance of Index Rebalancing: What You Need to Know</a></li>

</ul>
</details>

**标签**: `#finance`, `#index-funds`, `#investing`, `#market-rules`, `#passive-investing`

---

<a id="item-4"></a>
## [被解雇的 OpenAI 安全研究员否认泄密，怀疑因推动透明度被针对](https://www.ithome.com/1/017/563.htm) ⭐️ 7.0/10

三名 OpenAI 安全研究员——托梅克·科尔巴克、米基塔·巴莱斯尼和王茉莉——在内部调查认定其不当处理敏感信息后被解雇，他们公开否认泄密，并暗示自己推动外部核查模型推理步骤的主张导致了被辞退。OpenAI 向《华尔街日报》表示解雇与他们的安全顾虑无关，但研究员称公司从未以书面形式说明究竟哪些信息被不当处理。 这场争议触及 AI 治理的核心问题：是否应允许外部人员查看模型的思维链推理，而这一能力正是研究者用来发现模型欺骗或阴谋行为的关键手段。如果安全人员因与外部审计人员接触而担心受罚，那么在前沿 AI 实验室面临监管和公众更高透明度要求之际，独立监督反而可能被削弱。 据报道，OpenAI 的调查主要围绕研究员与外部安全研究员瑞安·格林布拉特之间开启阅后即焚功能的 Signal 聊天记录，格林布拉特否认向记者传递机密信息；科尔巴克则辩称阅后即焚消息在硅谷本就是常规安全做法。针对王茉莉的指控则单独成立——OpenAI 称她多次访问一名高管的邮箱，而她表示自己早在近一年前就申请取消该权限，只是误点开一封敏感邮件并第一时间上报。

rss · ITHome Feed · 10月25日 03:28

**背景**: 推理型模型会在内部的“思维链”中记录解题的中间步骤，企业和安全研究员依靠这些记录理解模型如何做出判断；OpenAI 自己的研究发现，监控这种内部推理远比只监控输出更有效。2025 年，巴莱斯尼、科尔巴克和王茉莉联合多家 AI 实验室的研究者发表论文，呼吁持续保留这种可核查能力。今年 9 月 The Information 报道 OpenAI 新模型 Astra 能力更强但暴露的推理过程更少，随后 METR 与红杉研究院的审计又发现 OpenAI 基础设施存在漏洞且最终报告近一半被涂黑，使矛盾进一步激化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/evaluating-chain-of-thought-monitorability/">Evaluating chain-of-thought monitorability - OpenAI</a></li>
<li><a href="https://www.reuters.com/business/ai-safety-group-metr-finds-flaws-openais-internal-monitoring-system-2026-10-22/">External evaluators find flaws in OpenAI's AI monitoring ...</a></li>
<li><a href="https://support.signal.org/hc/en-us/articles/360007320771-Set-and-manage-disappearing-messages">Set and manage disappearing messages – Signal Support</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#OpenAI`, `#AI transparency`, `#chain-of-thought`, `#AI governance`

---

<a id="item-5"></a>
## [谷歌付费让家庭和企业减少用电，为 AI 数据中心腾出 1070MW 电网容量](https://www.ithome.com/1/017/561.htm) ⭐️ 7.0/10

谷歌与能源服务公司 Voltus 达成协议，将在 PJM 电网建立一座虚拟电厂，通过付费鼓励家庭和企业在用电高峰时段减少用电，从而为其 AI 数据中心释放最多 1070MW 的电力容量。该协议于 10 月 22 日宣布，是科技巨头为获取电网容量而开展的最大规模此类项目之一。 这凸显了一种在不新建发电厂的情况下满足 AI 基础设施巨大能源需求的新颖方法，并可能为其他面临电网限制和社区反对的科技公司树立先例。它还回应了人们日益担忧的耗电数据中心给当地电网带来压力并推高居民电价的问题。 该虚拟电厂并不依赖新建发电设施；Voltus 将招募数千家庭和企业，通过经济奖励鼓励他们在用电高峰时减少消耗，部分调整可通过智能温控器或储能电池自动完成。谷歌未披露财务条款，但表示这是科技巨头为获取电网容量而支付的最大规模交易之一，同时谷歌也在投资核能并研究减少自身数据中心高峰用电。

rss · ITHome Feed · 10月25日 03:03

**背景**: 虚拟电厂（VPP）是一种聚合分布式能源资源（如智能温控器、家用电池和电动汽车）的系统，使其作为单一电厂运行，平衡供需并提供电网服务。PJM 互联电网是美国最大的电网运营商，为从芝加哥到新泽西的 6700 万用户提供服务。Voltus 擅长的需求响应通过付费让消费者在高峰时段减少用电，有助于避免昂贵的调峰电厂并稳定电网。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Virtual_power_plant">Virtual power plant</a></li>
<li><a href="https://en.wikipedia.org/wiki/PJM_Interconnection">PJM Interconnection - Wikipedia</a></li>
<li><a href="https://www.voltus.co/">Voltus | Unlock Demand Response Revenue</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#energy`, `#virtual power plant`, `#data centers`, `#grid capacity`

---

<a id="item-6"></a>
## [亚马逊 CEO 贾西：AWS 算力到 2027 年基本售罄，部分订单锁定至 2028 年](https://www.ithome.com/1/017/549.htm) ⭐️ 7.0/10

亚马逊首席执行官安迪·贾西周五表示，受 AI 基础设施需求持续推动，AWS 云计算容量到 2027 年基本售罄，2028 年也有相当一部分容量被提前锁定。他指出，虽然会预留部分资源用于按需调用、Bedrock 和 EC2，但适合批量采购的大块算力资源大多已被订走。 这表明 AI 基础设施需求正超过超大规模云厂商的大规模产能建设，亚马逊计划 2026 年资本开支约 2200 亿美元。这凸显了云算力多年期的卖方市场，影响 AI 实验室、企业及整个云生态。 贾西提到，既然 2026 年容量已全部订满，公司可以加大投入而不会造成资金低效使用，并且 2027 年部分容量保留给按需调用、Bedrock 和 EC2 服务。亚马逊定于 10 月 29 日发布第三季度财报。

rss · ITHome Feed · 10月25日 01:37

**背景**: AWS 是亚马逊的云计算部门，提供 EC2（虚拟服务器）和 Bedrock（用于访问基础模型的托管生成式 AI 平台）等服务。亚马逊、微软和谷歌等超大规模云厂商每年投入数百亿美元建设数据中心，以满足 AI 训练和推理需求。资本开支（capex）指这些长期基础设施投资。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/bedrock/">Amazon Bedrock – Build genAI applications and agents at production...</a></li>
<li><a href="https://aws.amazon.com/cn/ec2/">Amazon EC2 弹性云服务器 - AWS云服务</a></li>
<li><a href="https://mirrorfrog.com/blog/hyperscaler-capex-q4-2026-guide/">四大云厂 2026 年资本开支与算力采购指引汇总：Q4 该盯什么 | AI 算力...</a></li>

</ul>
</details>

**标签**: `#AWS`, `#AI infrastructure`, `#cloud computing`, `#capex`, `#industry news`

---

<a id="item-7"></a>
## [Playden 工具让破解版 PS5 通过 Wine 和 DXVK 运行 Steam Windows 游戏](https://www.ithome.com/1/017/540.htm) ⭐️ 7.0/10

开发者 leolobato 发布了 Playden for PS5 的早期测试版，这是一个从 macOS 版本移植的启动器，让破解后的 PS5 能够登录 Steam、下载 Windows 游戏，并借助名为 prospero-win 的 Wine 移植版和 DXVK 图形渲染层在本地运行。该工具本周更新到 0.6.0 版本，新增 USB/FTP 导入游戏、120Hz 输出和 4K 分辨率选项；此前的 0.5.0 版本已通过 VKD3D-Proton 加入 Direct3D 12 支持。 这是主机破解领域的重要进展，使 PS5 无需单独安装 Linux 系统或借助 PC 串流即可运行 Windows/Steam 游戏，可能扩展该主机的功能并影响未来的破解方向。不过该项目仍处于实验阶段且兼容性有限，因此对主流游戏的即时影响可能不大。 目前兼容性仅限于较老的作品和独立游戏，例如《半衰期 2》《辐射：新维加斯》和《吸血鬼幸存者》，大量游戏仍会闪退或无法启动；带有内核级反作弊或需要 EA App 等第三方启动器的游戏暂不支持。开发者还提醒 Steam 登录令牌会以未加密形式保存在主机中，用户应备份云存档，因为程序漏洞可能覆盖存档文件。

rss · ITHome Feed · 10月25日 00:33

**背景**: Wine 是一个开源兼容层，通过翻译 Windows API 调用而非模拟 Windows，让 Windows 应用能在 Linux 等系统上运行。DXVK 是一个将 Direct3D 8/9/10/11 调用转换为 Vulkan 的翻译层，VKD3D-Proton 则对 Direct3D 12 做同样的事，二者共同使许多 Windows 游戏能在非 Windows 平台上运行。Playden 将这些技术移植到 PS5 上，以 prospero-win 的形式让主机无需启动 Linux 就能作为普通 PS5 应用运行 Steam 游戏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DXVK">DXVK - Wikipedia</a></li>
<li><a href="https://dxvk.org/">DXVK – Vulkan Based Direct 3 D for Linux & Wine</a></li>
<li><a href="https://heldgames.com/guides/translation-layers-explained">FEX, Box64, Proton , DXVK: What Translation Layers... | Held Games</a></li>

</ul>
</details>

**标签**: `#PS5`, `#jailbreak`, `#Wine`, `#DXVK`, `#gaming`

---

<a id="item-8"></a>
## [PHP 基金会仅有一名全职员工，却支撑着七成网站](https://www.ithome.com/1/017/528.htm) ⭐️ 7.0/10

PHP 基金会执行董事伊丽莎白·巴伦在邮件采访中透露，基金会只有一名全职员工（即她本人）和 14 名大多为兼职的外包人员，董事会成员均为无薪志愿者。这一消息公布的同周，PHP 修复了两个高危远程代码执行漏洞（CVE-2026-109618 和 CVE-2026-109619），引发全球紧急修复行动。 PHP 支撑着约 70%的网站，其资金不足对软件供应链构成系统性风险；基金会审核 AI 驱动的漏洞报告和代码贡献的能力有限，可能延误对数百万网站的关键补丁。这凸显了开源依赖与可持续资金之间的日益紧张关系。 基金会与 OpenAI、Wiz 和 Calif 合作协调补丁，Cloudflare 监测到数百万次攻击尝试，但没有证据表明漏洞在公开前被利用。AI 帮助发现了潜伏十年的漏洞并提升了程序员效率，但代码修改提案数量同比接近翻倍，贡献者人数并未同步增加，导致人工审核压力巨大。

rss · ITHome Feed · 10月24日 23:27

**背景**: PHP 基金会是一家成立于 2021 年的非营利组织，旨在支持 PHP 语言的核心开发，依靠捐赠和资助运作。PHP 是一种广泛使用的开源脚本语言，支撑着 WordPress 等主要平台，并嵌入许多 Web 框架。近期 AI 工具加速了开源项目中的漏洞发现，使往往兼职或志愿工作的维护者不堪重负。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/10/php-issues-emergency-patches-for-two.html">PHP Issues Emergency Patches for Two Critical PHP 2Shell RCE...</a></li>
<li><a href="https://cert.europa.eu/publications/security-advisories/2026-018/pdf">Critical Vulnerabilities in PHP - cert.europa.eu</a></li>
<li><a href="https://security.paloaltonetworks.com/CVE-2026-109618">CVE-2026-109618 Impact of Critical Vulnerabilities in PHP ...</a></li>

</ul>
</details>

**标签**: `#open-source sustainability`, `#PHP`, `#security vulnerabilities`, `#AI impact`, `#software infrastructure`

---

<a id="item-9"></a>
## [开源项目 GPU Unlock 可提升英伟达 RTX 30 系列 AI 算力高达 60%](https://www.ithome.com/1/017/525.htm) ⭐️ 7.0/10

GitHub 用户 Zagitta 发布了开源项目 GPU Unlock，这是一个 Linux 内核模块，可解除英伟达安培架构消费级显卡（GA102/GA103/GA104/GA106）上的指令发射速率限制，使 FP16/BF16 张量核心运算（FP32 累加）的吞吐量几乎翻倍。基准测试显示，在 ComfyUI 和 vLLM 等真实 AI 负载中性能提升可达 60%，且无需修改驱动或永久刷写 VBIOS。 这释放了广泛持有的 RTX 30 系列显卡中隐藏的计算潜力，使本地 AI 推理和图像生成无需硬件升级即可受益。它揭示了消费级显卡相比专业卡被人为限制的现象，并可能为 AI 爱好者延长现有硬件的使用寿命。 该模块在官方驱动加载前修改硬件速度选择寄存器并执行功能级重置（FLR），因此无需给驱动打补丁。性能提升取决于负载：INT8 精度下提升极小（0.3%），大语言模型的词元生成因显存带宽瓶颈而基本不变，且并非所有显卡都兼容或保证获得提升。

rss · ITHome Feed · 10月24日 23:09

**背景**: 英伟达的安培架构（RTX 30 系列）使用张量核心加速 AI 负载中常见的矩阵运算，采用 FP16/BF16 输入和 FP32 累加实现混合精度。已知消费级显卡在这些运算上的指令发射速率低于专业显卡，而该项目绕过了这一限制。该项目建立在先前针对 CMP 加密货币挖矿显卡解锁的研究之上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ampere_(microarchitecture)">Ampere (microarchitecture) - Wikipedia NVIDIA GA103 GPU Specs | TechPowerUp GPU Database NVIDIA Ampere GA102 GPU Architecture Whitepaper V1 PDF - Scribd 1. NVIDIA Ampere GPU Architecture Tuning Guide — Ampere ...</a></li>
<li><a href="https://www.nvidia.com/content/PDF/nvidia-ampere-ga-102-gpu-architecture-whitepaper-v2.pdf">NVIDIA AMPERE GA102 GPU ARCHITECTURE</a></li>
<li><a href="https://www.systemoverflow.com/learn/ml-model-optimization/model-quantization/mixed-precision-training-fp16-bf16-and-fp32-accumulation">Mixed Precision Training: FP16, BF16, and FP32 Accumulation</a></li>

</ul>
</details>

**社区讨论**: Reddit 和 X 上的社区反馈显示了乐观的实际效果：RTX 3090 Ti 用户在 ComfyUI 图像生成中报告约 58% 的加速且输出质量一致，RTX 3080 Ti/3080 用户则看到 BF16 吞吐量从约 65 TFLOPS 提升到约 110 TFLOPS。不过，也有用户指出兼容性问题以及 INT8 或大语言模型词元生成方面提升甚微。

**标签**: `#GPU`, `#NVIDIA`, `#AI hardware`, `#open-source`, `#performance optimization`

---

<a id="item-10"></a>
## [PHP2Shell：两个严重 PHP 漏洞险些击垮互联网](https://techcrunch.com/2026/10/24/php-ocalypse-how-two-critical-web-bugs-almost-broke-the-internet/) ⭐️ 7.0/10

Calif 的安全研究人员在 PHP 中发现两个严重的内存安全漏洞，编号为 CVE-2026-109618 和 CVE-2026-109619，影响 PHP 5.4 至 8.5 版本，可导致远程代码执行。这两个漏洞被命名为 PHP2Shell，由于 PHP 驱动着全球高达 70%的网站和 Web 应用，它们一度威胁造成大范围服务中断。 由于 PHP 支撑着互联网的大部分，包括政府机构和社交媒体平台运行的网站，这些漏洞使数百万网站及其数据面临风险。该事件凸显了广泛使用的开源基础设施的脆弱性，专家警告这不太可能是最后一次此类重大软件恐慌。 这两个 CVE 均为内存安全缺陷，可导致远程代码执行，使攻击者能够远程控制网站主机。它们影响从 5.4 到 8.5 的广泛 PHP 版本，这意味着许多未打补丁的遗留部署仍处于暴露状态。

rss · TechCrunch · 10月24日 15:30

**背景**: PHP 全称“Personal Home Page”，是一种广泛用于构建网站和 Web 应用的服务器端编程语言，既用于公共互联网，也用于企业内部托管系统。它驱动着全球高达 70%的网站，因此任何严重缺陷都可能演变为全互联网范围的事件。远程代码执行（RCE）是最严重的漏洞类型之一，因为它允许攻击者在受感染的服务器上运行任意命令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PHP2Shell">PHP2Shell - Wikipedia</a></li>
<li><a href="https://techcrunch.com/2026/10/24/php-ocalypse-how-two-critical-web-bugs-almost-broke-the-internet/">PHP-ocalypse: How two critical web bugs almost broke the ...</a></li>
<li><a href="https://www.cbsnews.com/news/php2shell-vulnerability-ai-security-flaw/">What to know about the PHP bug affecting 70% of the world's ...</a></li>

</ul>
</details>

**标签**: `#PHP`, `#security`, `#vulnerabilities`, `#web infrastructure`, `#open source`

---

<a id="item-11"></a>
## [Grok 与 GPT-4o 在政治推荐上严重分歧](https://techcrunch.com/2026/10/24/forced-to-pick-groks-ai-model-chooses-republicans-openais-picks-democrats/) ⭐️ 7.0/10

一项新研究发现，xAI 的 Grok 模型绝大多数情况下推荐共和党候选人，而 OpenAI 的 GPT-4o 则倾向于民主党，两者在近 500 场选举中有超过 90%的情况意见相左。 这一发现凸显了主流大语言模型中存在的显著政治偏见，随着越来越多的人通过聊天机器人获取信息，引发了人们对 AI 可能影响选民认知和选举公正性的担忧。 该研究考察了近 500 场选举，发现两个模型在超过 90%的情况下对候选人推荐存在分歧，但简要摘要中并未详细说明具体的研究方法和使用的提示词。

rss · TechCrunch · 10月24日 15:00

**背景**: 像 Grok 和 GPT-4o 这样的大语言模型基于海量互联网文本训练，可能因其训练数据和微调而表现出政治倾向。Grok 由 xAI 开发，而 GPT-4o 是 OpenAI 于 2024 年 5 月发布的多模态模型。此前的研究已记录了 LLM 中的政治偏见，通常使用投票建议应用来评估其倾向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Grok_(chatbot)">Grok (chatbot) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-4o">GPT-4o</a></li>
<li><a href="https://link.springer.com/article/10.1007/s42001-025-00376-w">Assessing political bias in large language models | Journal ...</a></li>

</ul>
</details>

**标签**: `#AI bias`, `#LLM`, `#politics`, `#elections`, `#AI ethics`

---

<a id="item-12"></a>
## [为何必须迅速制定 SF6 排放国际标准？](https://www.rfi.fr/cn/%E4%B8%93%E6%A0%8F%E6%A3%80%E7%B4%A2/%E7%8E%AF%E5%A2%83%E4%B8%8E%E5%8F%91%E5%B1%95/20261024-%E6%B0%94%E5%80%99%E5%8F%98%E5%8C%96-%E4%B8%BA%E4%BD%95%E5%BF%85%E9%A1%BB%E8%BF%85%E9%80%9F%E5%88%B6%E5%AE%9Asf6%E6%8E%92%E6%94%BE%E6%A0%87%E5%87%86) ⭐️ 6.0/10

法国国际广播电台（RFI）援引美国气候新闻网站 InsideClimateNews 的文章报道，尽管中国在可再生能源开发方面领先全球，但其电网却是最强效温室气体六氟化硫（SF6）的最大排放国。文章呼吁迅速制定国际标准来规范 SF6 排放。 SF6 在 100 年尺度上的全球变暖潜能值是二氧化碳的 23500 倍，大气寿命约 3200 年，因此即使微量泄漏也会对气候产生持久影响。若缺乏国际标准，不断扩张的电力基础设施可能锁定大量排放，削弱可再生能源和气候目标的进展。 SF6 广泛用作高压电气设备中的绝缘和灭弧气体，其排放难以监测，因为泄漏分散且各国报告要求不一。文章指出中国是最大排放国，但未提供具体排放数据或标准制定的时间表。

rss · RFI Chinese · 10月24日 15:34

**背景**: SF6 是一种无色、无味、无毒的气体，具有优异的绝缘和灭弧性能，因此是高压断路器和气体绝缘开关设备中的关键介质。它被《京都议定书》列为受控温室气体，政府间气候变化专门委员会（IPCC）第六次评估报告给出的 100 年全球变暖潜能值为 23500。尽管存在替代技术和回收技术，但采用程度不一，美国等一些地区通过合作伙伴计划已使输配电领域的排放有所下降。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-cn/六氟化硫">六氟化硫 - 维基百科，自由的百科全书</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sulfur_hexafluoride">Sulfur hexafluoride - Wikipedia</a></li>
<li><a href="https://www.epa.gov/sites/default/files/2018-01/documents/2018_complete_report.pdf">Inventory of U.S. Greenhouse Gas Emissions and Sinks: 1990-2016...</a></li>

</ul>
</details>

**标签**: `#climate change`, `#SF6 emissions`, `#greenhouse gases`, `#energy policy`, `#international standards`

---

<a id="item-13"></a>
## [乌克兰称星链连接在限速一周后恢复稳定](https://www.bbc.co.uk/news/articles/cwkg5md14j8go?at_medium=RSS&at_campaign=rss) ⭐️ 6.0/10

乌克兰于 10 月 24 日宣布，其军队的星链连接已恢复稳定，此时距离访问被限制、网速被拖慢已过去 10 天，期间军事和无人机行动受到干扰。泽连斯基总统表示正常速度已恢复，而埃隆·马斯克则指责乌克兰军方将星链用于进攻性无人机打击，违反了服务条款。 星链是乌克兰军队的关键通信骨干，任何限速都会直接影响战场协调和无人机行动。这一事件凸显了一家私营公司对战时分关键基础设施所掌握的地缘政治杠杆，并引发了对冲突地区商业卫星服务可靠性的质疑。 此次中断同时影响了商业版星链和五角大楼资助的军用版本“星盾”，不过乌克兰表示使用星盾的无人机更早恢复了正常速度。马斯克声称问题在于违反服务条款，并已于上周修复，而 SpaceX 和美国政府均未对实施限制承担责任。

rss · BBC World · 10月24日 12:12

**背景**: 星链是 SpaceX 的低地球轨道卫星互联网星座，自俄罗斯入侵初期以来一直被乌克兰军方广泛用于通信和无人机控制。星盾是一项独立的、由五角大楼资助的服务，基于星链技术构建并具备额外的军事能力，由美国政府而非 SpaceX 的商业条款管控。限速是卫星互联网中管理网络负载的常见做法，但在这里却成为了地缘政治施压的工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Starshield">SpaceX Starshield - Wikipedia</a></li>
<li><a href="https://www.defensenews.com/industry/techwatch/2026/10/16/what-is-starshield-spacexs-military-version-of-starlink/">What is Starshield , SpaceX’s military version of Starlink?</a></li>
<li><a href="https://en.wikipedia.org/wiki/Starlink_in_the_Russo-Ukrainian_War">Starlink in the Russo-Ukrainian war - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Starlink`, `#Ukraine`, `#satellite internet`, `#military technology`, `#network reliability`

---

<a id="item-14"></a>
## [BBC Verify 追踪美国中期选举中 8000 万美元 AI 生成广告](https://www.bbc.co.uk/news/videos/cm62y59zw8zko?at_medium=RSS&at_campaign=rss) ⭐️ 6.0/10

BBC Verify 追踪了美国中期选举中的数十条 AI 生成选举广告，根据其统计方法，共识别出近 170 条此类广告，相关支出约为 8000 万美元。调查发现，共和党候选人或亲共和党团体投放了其中 80%的广告，占总支出的 83%。 该报道量化了 AI 生成政治广告如何从新奇事物转变为美国选举中一股可衡量的力量，引发了对虚假信息和透明度的担忧。它凸显了各州与联邦披露规则碎片化与竞选团队快速采用廉价 AI 工具之间日益扩大的差距。 BBC Verify 利用媒体报道、学生编码员以及追踪政治广告支出的公司 AdImpact 的数据来汇总统计。报告指出，政策应对仍然碎片化，州级披露法律、联邦提案和平台审核规则各自为政。

rss · BBC World · 10月24日 05:03

**背景**: AI 生成政治广告利用语音合成和 AI 辅助视频编辑等工具制作逼真但合成的内容，通常没有明确披露。BBC Verify 是 BBC 旗下专注于虚假信息、事实核查和开源调查的部门，此前曾发布识别 AI 伪造内容的指南。在美国，此类广告的披露要求因州而异，联邦提案尚未颁布，导致平台自行制定审核政策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.co.uk/news/videos/cm62y59zw8zko">The rise of AI election ads in US midterms campaign - BBC BBC Verify | Experts in disinformation, fact-checking and ... BBC Verify: How to spot AI fakes in the US election How we detect AI images and videos - in 90 seconds | BBC Verify Experts tracked $80M spent on almost 170 AI‑generated midterm ads How BBC Verify detects AI fakes: A masterclass in digital ... We’ve tracked $80M of spending on almost 170 AI-generated ...</a></li>
<li><a href="https://www.bbc.co.uk/news/bbcverify">BBC Verify | Experts in disinformation, fact-checking and ...</a></li>
<li><a href="https://www.bbc.com/news/world-us-canada-68472248">BBC Verify: How to spot AI fakes in the US election</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#political advertising`, `#misinformation`, `#US midterms`, `#media analysis`

---

<a id="item-15"></a>
## [TechCrunch 的 AI 墓地：追踪失败与延期的 AI 项目](https://techcrunch.com/2026/10/24/the-ai-graveyard-a-running-list-of-projects-and-startups-that-didnt-make-it/) ⭐️ 6.0/10

TechCrunch 发布了一份持续更新的清单，收录了已关闭或未达预期的 AI 项目和初创公司，列举了苹果多次延期的 Siri AI 功能以及 OpenAI 混乱的“超级应用”发布等案例。 这份回顾为从业者和投资者提供了一种结构化方式来识别 AI 行业的失败模式，从过度承诺时间表到产品整合失误，有助于未来 AI 创业项目更好地进行风险评估。 该清单是精选而非穷尽的，案例涵盖大型成熟企业（苹果）和领先 AI 实验室（OpenAI），表明失败和延期并不局限于小型初创公司；不过，文章并未提供技术深度剖析或对失败案例的定量分析。

rss · TechCrunch · 10月24日 19:00

**背景**: 苹果于 2024 年宣布了 Apple Intelligence，但其更先进的 Siri 功能被推迟到 2026 年，一位高管称这些延期“令人尴尬且难堪”。OpenAI 一直在将 ChatGPT、其 Codex 编程工具和浏览器整合为一个桌面“超级应用”，为潜在的 IPO 做准备，这一复杂的发布引发了审视。TechCrunch 的墓地清单汇总了此类挫折，以帮助行业从中吸取教训。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2025/03/07/apple-delays-siri-ai-improvements-to-2026.html">Apple delays Siri AI improvements to 2026</a></li>
<li><a href="https://www.cnbc.com/2026/03/19/openai-desktop-super-app-chatgpt-browser-codex.html">OpenAI to create desktop super app, combining ChatGPT app ... Exclusive | OpenAI Plans Launch of Desktop ‘Superapp’ to ... OpenAI to launch desktop super app combining ChatGPT, browser ... OpenAI unveils long-awaited "super app" as rivalry with ... OpenAI Overhauls ChatGPT for Super App Launch OpenAI’s new ‘super app’ boss hopes to persuade users and ... OpenAI Merges ChatGPT and Codex Into 'Super… (2026) | Robot ...</a></li>
<li><a href="https://www.wsj.com/tech/openai-plans-launch-of-desktop-superapp-to-refocus-simplify-user-experience-9e19931d">Exclusive | OpenAI Plans Launch of Desktop ‘Superapp’ to ...</a></li>

</ul>
</details>

**标签**: `#AI industry`, `#startups`, `#project failures`, `#tech news`, `#lessons learned`

---

<a id="item-16"></a>
## [相干科技成立三周年，聚焦实用型量子系统](https://www.chinanews.com.cn/cj/2026/10-25/10720608.shtml) ⭐️ 5.0/10

2026 年 10 月 25 日，由北京量子信息科学研究院孵化的超导量子计算初创公司相干（北京）科技有限公司迎来成立三周年。公司聚焦实用型超导量子整机与量子云平台服务，面向科研机构、开发者和企业客户提供成套解决方案。 这一里程碑表明中国超导量子计算领域的商业化努力在持续推进，该领域目前主要由研究机构和大型科技公司主导。像相干科技这样的初创企业有助于弥合实验室研究与面向行业用户的实用量子云服务之间的差距。 该公告未提供具体技术细节，如量子比特数量、相干时间或门保真度，也未披露客户数量或收入。公司聚焦整机与云服务，表明其目标是提供交钥匙解决方案，而不仅仅是硬件组件。

rss · China News Service Scroll · 10月25日 03:54

**背景**: 超导量子比特是由包含约瑟夫森结的微波频率电路构成的人造原子，需冷却至毫开尔文温度，是谷歌、IBM 等公司开发量子处理器的主流架构。北京量子信息科学研究院是位于北京的研究机构，旨在推动量子科学与技术的发展。量子云平台允许用户通过互联网远程访问量子处理器，类似于经典云计算的工作方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Superconducting_quantum_computing">Superconducting quantum computing - Wikipedia</a></li>
<li><a href="https://english.beijing.gov.cn/investinginbeijing/InvestmentSpecial/New_Quality_Productive_Forces/202501/t20250114_3988467.html">Hi! A Quantum Wants to 'Entangle' with You!</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cloud-based_quantum_computing">Cloud -based quantum computing - Wikipedia</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#superconducting qubits`, `#China tech`, `#startups`, `#quantum cloud`

---

<a id="item-17"></a>
## [中国居民用电近十年首现负增长，AI 与电动车用电激增](https://www.dw.com/zh/%E4%B8%AD%E5%9B%BD%E5%B1%85%E6%B0%91%E7%94%A8%E7%94%B5%E8%BF%91%E5%8D%81%E5%B9%B4%E9%A6%96%E7%8E%B0%E8%B4%9F%E5%A2%9E%E9%95%BF-ai%E5%92%8C%E7%94%B5%E5%8A%A8%E8%BD%A6%E7%94%A8%E7%94%B5%E7%8C%9B%E5%A2%9E/a-79749795?maca=chi-rss-chi-all-1127-rdf) ⭐️ 5.0/10

中国国家能源局数据显示，2026 年前三季度全社会用电量同比增长 3.9%，但城乡居民生活用电量同比下降 0.3%，为近十年来同期首次负增长。与此同时，充换电服务业用电量同比大增 55.4%，互联网数据服务业用电量增长 41.6%。 这一分化凸显了中国电力需求的结构性转变：居民用电减少，而高技术制造业、电动汽车充电基础设施和 AI 驱动的数据中心成为增长的主要引擎。这对电网规划、可再生能源消纳以及电力行业的碳减排路径都有重要影响。 分析认为，居民用电下降主要归因于 8 月和 9 月的极端天气。前三季度，充换电服务业用电量达 1315 亿千瓦时，互联网数据服务业用电量为 793 亿千瓦时；后者增长源于 AI 从训练为主转向训练与推理并重，Token 调用量呈指数级攀升。

rss · DW Chinese · 10月24日 10:33

**背景**: 中国国家能源局按月度和季度发布分行业及城乡居民的用电量数据。近年来，电动汽车充电和数据中心的用电需求快速增长，2025 年充换电服务业用电量已超过 1020 亿千瓦时。随着 AI 应用的扩展，数据中心的电力需求正成为国家能源规划的关键因素。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nea.gov.cn/20261021/bab7b2135e424adeaacf169cb40115ae/c.html">2026年1-9月全社会用电量同比增长3.9%，高技术及装备制造业、充换电服...</a></li>
<li><a href="https://chd.in-en.com/html/chd-2462878.shtml">国家能源局：2026年1-9月充换电服务业用电量同比增长55.4%-统计动态-...</a></li>
<li><a href="https://www.guancha.cn/GongYe·KeJi/2026_09_16_900897.shtml">增长超四成！今年互联网数据服务业用电量已超600亿千瓦时</a></li>

</ul>
</details>

**标签**: `#energy`, `#china`, `#AI infrastructure`, `#electric vehicles`, `#data centers`

---

<a id="item-18"></a>
## [数据中心成为威斯康星州两党共同关注的政治议题](https://www.npr.org/2026/10/24/nx-s1-6011182/how-data-centers-became-a-bipartisan-political-issue-in-wisconsin) ⭐️ 5.0/10

NPR 报道称，随着中期选举临近，数据中心在关键摇摆州威斯康星州已成为一个两党共同关注的政治议题。文章探讨了当地围绕数据中心的辩论如何展开，以及这对全国性政治讨论有何借鉴意义。 这很重要，因为数据中心正日益成为能源基础设施、税收优惠和地方经济发展等辩论的核心，而该议题在威斯康星州这样的摇摆州如何演变，可能预示其在全国中期选举政治中的作用。其结果可能影响涉及科技行业和全国各地社区的政策决策。 NPR 的这篇文章是政治分析而非技术深度报道，重点在于数据中心如何成为威斯康星州两党共同关注的问题。文章未提供能源消耗或税收优惠金额的具体数据，而是将该议题作为全国中期选举辩论的案例研究。

rss · NPR News · 10月24日 21:20

**背景**: 数据中心是容纳服务器和网络设备的大型设施，为云计算、流媒体和人工智能工作负载提供动力。它们消耗大量电力，并常获得州和地方税收优惠以吸引投资，这可能在电网容量、水资源使用和公共成本方面引发紧张关系。近年来，至少五个州将税收减免与工资标准挂钩，随着审查加强，一些州正在暂停或限制激励措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ncsl.org/fiscal/policy-snapshot-data-center-incentives">Policy Snapshot: Data Center Incentives</a></li>
<li><a href="https://businessmodelanalyst.com/data-center-tax-incentives-by-state/">Data Center Tax Incentives by State (2026): Which States Are ...</a></li>
<li><a href="https://storage.is/the-growing-strain-of-data-centers-on-local-power-grids-what">Data Centers ' Impact on Local Grids : Small Business Guide</a></li>

</ul>
</details>

**标签**: `#data centers`, `#policy`, `#politics`, `#infrastructure`, `#energy`

---

<a id="item-19"></a>
## [专家呼吁“十五五”窗口期推进“深绿”转型](https://www.chinanews.com.cn/cj/2026/10-25/10720611.shtml) ⭐️ 3.0/10

中国环境与发展国际合作委员会委员、生态环境部原总工程师任勇 10 月 25 日在北京表示，未来十年是绿色转型从“浅绿”迈向“深绿”的关键窗口期。他呼吁在更多领域、更大程度、更深层次推进绿色转型，争取在更高水平上实现 2035 年美丽中国建设目标。 此番表态正值中国实施《美丽中国建设“十五五”规划》之际，该规划由国务院于 2026 年 7 月印发，将“十五五”时期定位为实现生态环境根本好转的关键阶段。“深绿”议程如何落地，可能影响 2035 年前的环境投资重点、产业升级和政策协同。 该报道为简短新闻，未界定“浅绿”与“深绿”的具体含义，也未说明政策工具，除 2035 年时间节点外没有量化目标或实施时间表。任勇是以国合会委员身份发表上述看法，国合会是高层咨询机构，其政策建议以书面形式报送国务院和有关部门供决策参考。

rss · China News Service Scroll · 10月25日 04:24

**背景**: 五年规划是中国最高层级的国家发展蓝图，“十五五”规划覆盖 2026 至 2030 年，而美丽中国建设目标提出到 2035 年基本实现美丽中国。国合会于 1992 年经中国政府批准成立，是由中外环境与发展领域高层人士和专家组成的国际性高级咨询机构，向中国政府提供前瞻性政策建议。在此语境下，“浅绿”通常指末端治理、增量式的环保措施，而“深绿”则意味着能源、产业和土地利用等结构性深层变革。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gov.cn/zhengce/content/202607/content_7074199.htm">国务院关于印发《美丽中国建设“十五五”规划》的通知_其他_中国政府网</a></li>
<li><a href="https://baike.baidu.com/item/中国环境与发展国际合作委员会/11033387">中国环境与发展国际合作委员会_百度百科 章程 - CCICED 中国环境与发展国际合作委员会2026年年会在京开幕_中华人民共和国生态... 中国环境与发展国际合作委员会2025年年会在京开幕_中华人民共和国生态... 中国环境与发展国际合作委员会2026年年会在京开幕 中国环境与发展国际合作委员会2026年年会举办_中国经济网——国家经济门...</a></li>
<li><a href="https://www.ndrc.gov.cn/fggz/fzzlgh/gjjzxgh/202609/t20260928_1407867.html">【美丽中国建设“十五五”规划】-国家发展和改革委员会</a></li>

</ul>
</details>

**标签**: `#environmental-policy`, `#green-transition`, `#china`, `#sustainability`, `#policy`

---

<a id="item-20"></a>
## [中新网评：洁厕剂包装越像饮料，安全警示越不能像摆设](https://www.chinanews.com.cn/cj/2026/10-25/10720610.shtml) ⭐️ 3.0/10

2026 年 10 月 25 日，中新网发表评论文章指出，随着清洁用品包装越来越像饮料瓶，产品上的安全警示必须更加醒目、不能流于形式。文章援引媒体报道称，一名老人因担心饮料过期替孙子“尝”了一款标称“白桃香氛洁厕慕斯”的清洁用品，导致口腔和食道化学性灼伤，相关话题“洁厕剂长得像饮料害人不浅”登上热搜。 这一事件凸显了产品设计潮流与消费者安全之间的落差：带香味的饮料式包装容易误导儿童和阅读、辨识能力较弱的老年人。它也将推动监管部门和厂商加强对危险家用化学品标签与包装的规范，对消费者权益保护和产品设计实践产生影响。 洁厕剂属于最危险的家用化学品之一，通常含有高浓度酸或漂白剂，如氢氧化钠和硫酸，误服后会灼伤舌头、口腔、食道和胃。医疗指引强调应立即联系中毒控制中心或急救服务，除非专业人员指示否则不要催吐，并尽量携带产品容器就医。

rss · China News Service Scroll · 10月25日 04:22

**背景**: 许多家用清洁产品采用水果或甜点香味以及色彩鲜艳的瓶身以增强吸引力，这可能模糊食品与毒害品之间的界限。中国的消费者权益保护框架和产品质量法规要求标签真实准确，但针对危险家用化学品的包装专项标准和执法仍较有限。其他司法辖区则依靠儿童安全包装规则，如美国《毒物预防包装法》，来减少误服事件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medlineplus.gov/ency/article/002743.htm">Toilet bowl cleaners and deodorizers poisoning - MedlinePlus Toilet Bowl Cleaners and Deodorizers Poisoning - UF Health What is the treatment for toilet cleaner liquid ingestion? Caustic Chemicals Poisoning - Injuries and Poisoning - Merck ... Chemical burns: First aid - Mayo Clinic</a></li>
<li><a href="https://iclg.com/practice-areas/consumer-protection-laws-and-regulations/china/">Consumer Protection Laws and Regulations Report 2026 China</a></li>
<li><a href="https://www.cpsc.gov/Business--Manufacturing/Business-Education/Business-Guidance/PPPA/Guide-to-Special-Packaging">Guide to Special Packaging | CPSC.gov</a></li>

</ul>
</details>

**标签**: `#consumer safety`, `#product packaging`, `#public health`, `#regulation`, `#news commentary`

---

<a id="item-21"></a>
## [中国三季度出口首破 8 万亿元，同比增长 22%](https://www.chinanews.com.cn/cj/2026/10-25/10720601.shtml) ⭐️ 3.0/10

2026 年前三季度，中国出口同比增长 16.4%，其中三季度出口规模首次突破 8 万亿元，单季增速达到 22%。机电产品、新能源产品以及算力相关产品成为这一轮出口增长的主要拉动力。 这一里程碑表明中国出口结构正转向更高附加值的制成品和技术密集型产品，可能重塑全球供应链和贸易格局。对于政策制定者、出口企业以及关注中国经济转型和全球绿色能源与算力基础设施需求的投资者而言，这一数据具有重要意义。 报道指出，机电、新能源和算力相关产品是主要贡献者，但并未给出各自的具体占比，也未说明是哪些算力产品（如服务器、芯片或数据中心设备）拉动了增长。三季度 22%的增速明显高于前三季度累计 16.4%的增速，表明增长动能在三季度有所加快。

rss · China News Service Scroll · 10月25日 03:09

**背景**: 中国海关统计将出口划分为机电产品等大类，机电产品包括消费电子、电气设备和机械设备等。新能源产品通常指电动汽车、锂离子电池和太阳能电池，近年来已成为中国出口的重要品类。算力是指计算机或数据中心处理信息的能力，随着全球对人工智能和云服务的需求增长，相关硬件出口成为中国贸易的新增长点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-cn/算力">算力 - 维基百科，自由的百科全书</a></li>
<li><a href="https://baike.baidu.com/item/算力/62066966">算力（计算机设备或计算/数据中心处理信息的能力）_百度百科 算力（Computing Power）-CSDN博客 大模型常说的“算力”，究竟指什么？一文讲清核心概念 - 知乎 算力 (suànlì) Meaning: computing power — HSK 7 Chinese Word 算力详解算力（Computing Power）是指计算机系统在单位时间内处理数据...</a></li>

</ul>
</details>

**标签**: `#macroeconomics`, `#china-trade`, `#exports`, `#new-energy`, `#computing-power`

---

<a id="item-22"></a>
## [正常咨询变投诉：快递业“以罚代管”怪圈](https://www.chinanews.com.cn/sh/2026/10-25/10720597.shtml) ⭐️ 3.0/10

中新网 2026 年 10 月 25 日的一篇报道揭示了快递行业如何将正常的客户咨询转化为正式投诉，从而依据“以罚代管”机制对快递员进行罚款。报道呼吁禁止二次转标签、要求后台标签变更留痕，国家邮政局 2026 年工作部署也明确提出平衡总部、加盟商和快递员的利益分配。 这种做法影响数百万末端快递员，他们可能因客户仅提出咨询而被投诉并面临高额罚款，扭曲了服务激励并损害劳动者权益。这也凸显了中国电商物流链条中的系统性治理问题：总部将压力转嫁给加盟商和快递员，而非改进管理。 文章指出，后台人员可手动将咨询工单改为投诉工单以凑考核指标，且罚款随投诉次数递增——二次投诉可能罚款 500 元。建议的整改措施包括禁止二次转标签、后台标签变更留日志供邮政监管部门抽查，以及将罚款上限设为月收入的一定比例。

rss · China News Service Scroll · 10月25日 02:39

**背景**: 最后一公里配送指物流过程中货物从分拣中心或配送站送达最终收货人的最后一段运输环节，通常是供应链中成本最高、劳动最密集的部分。在中国快递模式下，总部将配送网络加盟外包，加盟商常将罚款转嫁给快递员；早在 2021 年，七部门就联合印发意见，要求企业遏制“以罚代管”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.chinanews.com.cn/sh/2026/10-25/10720597.shtml">正常咨询为何变成“投诉”？揭秘快递末端“以罚代管”怪圈-中新网</a></li>
<li><a href="https://www.sohu.com/a/1092209445_220034">以罚代管的通病该治治了_问题_网点_管理 - 搜狐</a></li>
<li><a href="https://wapbaike.baidu.com/item/最后一公里配送/50951853">最后一公里配送_百度百科</a></li>

</ul>
</details>

**标签**: `#courier industry`, `#last-mile delivery`, `#labor management`, `#social news`, `#China`

---

<a id="item-23"></a>
## [2026 伦敦世界旅游交易会：中国展区规模创历届新高](https://www.chinanews.com.cn/gj/2026/10-25/10720600.shtml) ⭐️ 2.0/10

2026 年伦敦世界旅游交易会（WTM）将于 11 月 3 日至 5 日在英国伦敦皇家维多利亚码头埃克赛尔国际会展中心举办，本届展会以“韧性·复苏·重塑：全球旅游新时代”为主题。据中新网 10 月 25 日报道，中国展区规模创下历届新高。 中国展区规模创纪录，表明中国出境旅游市场在经历多年疫情冲击后正重新融入全球旅游贸易体系，也为中国目的地和旅游企业争取国际买家提供了更大平台。展会聚焦 AI 与数字创新，也反映出技术正在重塑旅游分销与营销方式。 该简讯除日期、地点和主题外细节有限，并未给出中国展区的具体面积数据或参展商名单。官方公布的主题涵盖全球旅游市场复苏、AI 与数字技术创新以及可持续旅游发展。

rss · China News Service Scroll · 10月25日 04:16

**背景**: 伦敦世界旅游交易会是全球规模最大的旅游行业年度盛会之一，汇聚目的地、旅行社、航空公司和科技供应商，用于采购、业务拓展和行业学习。展会举办地埃克赛尔国际会展中心位于伦敦东部码头区，是英国重要的展览与会议场馆。WTM 主要面向 B2B 领域，因此其发布内容多聚焦行业合作而非面向消费者的旅游产品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wtm.com/london/en-gb.html">Where Travel & Tourism Meet | World Travel Market London</a></li>
<li><a href="https://en.wikipedia.org/wiki/ExCeL_London_Exhibition_Centre">ExCeL London Exhibition Centre</a></li>

</ul>
</details>

**标签**: `#tourism`, `#trade-fair`, `#news-brief`, `#china`, `#off-topic`

---

<a id="item-24"></a>
## [中国秋粮收获过八成，新技术助力提质增效](https://www.chinanews.com.cn/cj/2026/10-25/10720613.shtml) ⭐️ 2.0/10

据中国新闻网简短报道，中国秋粮收获已超过八成，并指出新技术正在帮助提高收获的质量和效率。 秋粮占中国全年粮食产量的很大比重，因此收获进度被视为国家粮食安全和农村生计的重要指标。新技术的采用有望提高产量、减少损失，影响农民、农业供应链和粮食价格。 该报道没有具体说明使用了哪些技术、确切的收获比例或地区分布，除了标题中的说法外，没有提供技术细节或数据。

rss · China News Service Scroll · 10月25日 04:03

**背景**: 中国的秋粮通常包括水稻、玉米和大豆，秋收是全年粮食生产周期的关键部分。中国媒体定期报道收获进度以跟踪粮食安全，近期报道常强调机械化、智慧农业和改良品种对效率的提升作用。

**标签**: `#agriculture`, `#news`, `#China`, `#harvest`, `#non-technical`

---

<a id="item-25"></a>
## [河南粮食总产有望连续 10 年保持在 1300 亿斤以上](https://www.chinanews.com.cn/cj/2026/10-25/10720605.shtml) ⭐️ 2.0/10

河南省于 10 月 24 日宣布，今年全省夏粮逆势增产、秋粮丰收到手，粮食总产量有望连续 10 年保持在 1300 亿斤（6500 万吨）以上。该省还提出“十五五”期间粮食综合生产能力力争迈上 1400 亿斤（7000 万吨）新台阶。 河南是中国最大的粮食产区之一，产量占全国十分之一以上，其稳产对保障国家粮食安全至关重要。1400 亿斤目标表明，在中国进入“十五五”之际，该省将继续加大农业产能建设力度。 这里的“斤”为 500 克，因此 1300 亿斤即 6500 万吨，1400 亿斤即 7000 万吨。该表述由河南省委农办主任、省农业农村厅厅长孙巍峰在中共河南省委新闻发布会上作出。

rss · China News Service Scroll · 10月25日 03:22

**背景**: 中国的五年规划是国民经济和社会发展的蓝图，“十五五”规划覆盖 2026 年至 2030 年。河南位于中部地区，是农业大省，素有“中原粮仓”之称，粮食产量位居全国前列。粮食安全长期是中国政策重点，国家致力于保障粮食自给。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zickty.com/jintokg">Convert Chinese Jin ( 斤 ) to Kilograms (kg) Online Tool</a></li>
<li><a href="https://www.globaltimes.cn/page/202107/1229259.shtml">How will heavy rain in Central China ’s Henan affect food prices?</a></li>
<li><a href="https://www.ecns.cn/m/news/society/2026-03-09/detail-ihfaizcc2508662.shtml">China pushes to build 'birth-friendly society' in 15 th Five - Year Plan ....</a></li>

</ul>
</details>

**标签**: `#agriculture`, `#regional news`, `#China`, `#food security`, `#off-topic`

---

<a id="item-26"></a>
## [亚行批准 1742 万美元融资助不丹应对物价上涨](https://www.chinanews.com.cn/gj/2026/10-25/10720586.shtml) ⭐️ 2.0/10

据不丹《昆瑟尔报》10 月 24 日报道，亚洲开发银行已批准向不丹提供 1742 万美元融资，帮助该国弱势家庭应对食品和能源价格上涨。 这笔融资支持不丹总额 2.6788 亿美元的政府危机应对计划，该国 GDP 增速预计将从 2025 年的 8.5%放缓至 2026 年的 6.5%，有助于保护家庭收入和基本服务免受外部经济冲击。 亚行融资是政府更大规模计划的一部分，重点针对家庭收入、基本服务和就业；不丹的物价压力主要来自食品通胀以及中东冲突对贸易的干扰。

rss · China News Service Scroll · 10月25日 03:03

**背景**: 亚洲开发银行是一家区域性开发银行，致力于促进亚太地区的社会和经济发展。不丹是一个严重依赖从印度进口的内陆小经济体，食品和燃料价格上涨挤压了家庭预算，尽管整体通胀水平温和。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Asian_Development_Bank">Asian Development Bank - Wikipedia</a></li>
<li><a href="https://businessbhutan.bt/rising-prices-shrinking-wallets-inflation-hits-essentials/">Rising Prices, Shrinking Wallets: Inflation Hits Essentials</a></li>
<li><a href="https://www.devdiscourse.com/article/business/3996754-bhutans-economy-under-pressure-adb-backs-26788-million-plan-to-shield-families-and-jobs">Bhutan’s Economy Under Pressure: ADB Backs $267.88 Million ...</a></li>

</ul>
</details>

**标签**: `#development finance`, `#Bhutan`, `#Asian Development Bank`, `#news brief`, `#off-topic`

---

<a id="item-27"></a>
## [2026 中韩经济发展论坛在首尔开幕](https://www.chinanews.com.cn/gj/2026/10-25/10720585.shtml) ⭐️ 2.0/10

2026 中韩经济发展论坛于 10 月 23 日在首尔大学开幕，中国驻韩国大使戴兵出席开幕式并致辞。来自中韩各界的专家学者及企业代表共计 160 余人出席了此次活动。 该论坛是中韩双边关系背景下的一条二轨外交与经济交流渠道，但对软件工程、人工智能或系统研究领域的读者而言关联性有限。其成果可能为两国商业与政策讨论提供参考，但不太可能直接影响技术社区。 活动在首尔大学举行，中新网于 10 月 25 日——即开幕两天后——以简短通稿形式进行了报道。报道未提及论坛议程、分论坛议题或具体成果。

rss · China News Service Scroll · 10月25日 03:02

**背景**: 中韩经济发展论坛是定期举办的双边交流活动，汇聚政府官员、学者和企业领袖，讨论贸易、投资及区域经济合作等议题。此类活动通常由学术机构或商会组织，是正式外交渠道之外的非正式观点交流平台。

**标签**: `#news`, `#economics`, `#China-South Korea relations`, `#forum`, `#off-topic`

---

<a id="item-28"></a>
## [第四届中外戏剧交流与合作论坛在北京开幕](https://www.chinanews.com.cn/cul/2026/10-25/10720588.shtml) ⭐️ 2.0/10

第四届中外戏剧交流与合作论坛于 2026 年 10 月 23 日在北京启幕，其前沿论坛于 10 月 24 日上午举行。来自多个国家和地区的戏剧教育、艺术研究与文化传播领域专家学者齐聚一堂，围绕戏剧艺术传承创新及国际交流合作等议题展开对话。 该论坛为表演艺术领域的跨文化对话提供了平台，有望促进戏剧专业人士之间的国际合作与相互理解。它体现了通过艺术推动中国与其他国家文化交流的持续努力。 该报道为简短新闻，细节有限，未披露具体举办场地、完整参与国家名单，也未提及协议或合作项目等具体成果。论坛包括 10 月 23 日的主论坛和 10 月 24 日的前沿论坛。

rss · China News Service Scroll · 10月25日 03:00

**背景**: 中外戏剧交流与合作论坛是一个定期举办的文化活动，汇聚戏剧教育者、研究者和从业者，共同探讨艺术传统与跨境合作。此类论坛是更广泛文化外交努力的一部分，借助表演艺术在不同文化之间搭建桥梁。

**标签**: `#theater`, `#cultural-exchange`, `#event-news`, `#off-topic`, `#china`

---