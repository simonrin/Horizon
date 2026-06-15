---
layout: default
title: "Horizon Summary: 2026-06-15 (ZH)"
date: 2026-06-15
lang: zh
---

> 从 295 条内容中筛选出 28 条重要资讯。

---

1. [里约热内卢自称自研的大语言模型被揭露为现有模型的加权合并](#item-1) ⭐️ 8.0/10
2. [SK 海力士本月向主要客户交付 HBM4E 样品](#item-2) ⭐️ 8.0/10
3. [央视曝光非法将电动汽车电池改装用于电动自行车](#item-3) ⭐️ 8.0/10
4. [Anthropic 因美国安全担忧全球暂停 AI 模型](#item-4) ⭐️ 8.0/10
5. [世航智能完成超 10 亿元 A 轮融资](#item-5) ⭐️ 7.0/10
6. [谷歌与 UCSD 将旧 Pixel 手机改造成低成本数据中心](#item-6) ⭐️ 7.0/10
7. [韩国启动 5000 亿韩元研发计划，攻关下一代功率半导体](#item-7) ⭐️ 7.0/10
8. [英国首相斯塔默宣布对 16 岁以下青少年实施‘澳大利亚加强版’社交媒体禁令](#item-8) ⭐️ 7.0/10
9. [AI 加速可控核聚变研究](#item-9) ⭐️ 6.0/10
10. [网件起诉 TP-Link 虚假宣传为美国公司](#item-10) ⭐️ 6.0/10
11. [计算机历史博物馆从德国仓库回收 2000 余件文物](#item-11) ⭐️ 6.0/10
12. [通用汽车计划让电动汽车为电网供电，但硬件成本高达 2 万美元](#item-12) ⭐️ 6.0/10
13. [新厄尔尼诺事件已宣布，可能成为‘超级’厄尔尼诺](#item-13) ⭐️ 6.0/10
14. [黑灯工厂：威胁中国年轻人就业？](#item-14) ⭐️ 6.0/10
15. [FBI 建造模拟小镇用于网络攻击演练](#item-15) ⭐️ 6.0/10
16. [中国构建全国一体化算力网赋能数字经济](#item-16) ⭐️ 5.0/10
17. [远程医疗公司面临控制肥胖药物成本的压力](#item-17) ⭐️ 5.0/10
18. [半固态电池填补全固态电池延迟的空白](#item-18) ⭐️ 5.0/10
19. [黑土地保护国际会议在长春举行](#item-19) ⭐️ 4.0/10
20. [初创公司借 AI 上市潮，追随 SpaceX](#item-20) ⭐️ 4.0/10
21. [公安部公布 10 起网络谣言典型案例](#item-21) ⭐️ 3.0/10
22. [福建海事部门发布 5 项举措促两岸航运发展](#item-22) ⭐️ 3.0/10
23. [A 股开盘普涨，三大指数集体高开](#item-23) ⭐️ 2.0/10
24. [央行开展 4250 亿元 7 天期逆回购操作](#item-24) ⭐️ 2.0/10
25. [人民币中间价报 6.8088，上调 21 个基点](#item-25) ⭐️ 2.0/10
26. [中国驻菲律宾使馆提醒入境旅客备齐文件](#item-26) ⭐️ 2.0/10
27. [专家解读中国房地产市场分化](#item-27) ⭐️ 2.0/10
28. [英法德意准备解除对伊朗制裁](#item-28) ⭐️ 2.0/10

---

<a id="item-1"></a>
## [里约热内卢自称自研的大语言模型被揭露为现有模型的加权合并](https://github.com/nex-agi/Nex-N2/issues/4) ⭐️ 8.0/10

一个 GitHub 问题指出，里约热内卢市政府声称自研的 Qwen3.5 微调模型 Rio-3.5-Open-397B，实际上是约 60%的 Nex-N2 Pro 和 40%的 Qwen3.5-397B-A17B 的加权合并，且没有进行额外训练。 这一争议引发了对开源 AI 透明度和归属问题的严重担忧，因为一个政府实体可能将合并模型谎称为原创工作，可能削弱对自称自研 AI 开发的信任。 分析显示，Rio 模型中的每个权重张量在数千个标准差范围内，都是 Nex 和 Qwen 的 0.6/0.4 混合，覆盖所有 60 层和网络的每个组件，这无法用典型的微调来解释。

hackernews · unrvl22 · 6月14日 15:37 · [社区讨论](https://news.ycombinator.com/item?id=48528371)

**背景**: 模型合并是一种将两个或多个预训练模型的权重组合成一个模型的技术，无需额外训练，常用方法包括线性插值或 SLERP。这可以产生一个继承双方能力的模型，但不同于微调或从头训练。这一争议凸显了开源 AI 中正确归属的重要性，未披露的合并可能会误导他人对作品原创性的认知。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2212.09849">[2212.09849] Dataless Knowledge Fusion by Merging Weights of Language Models</a></li>
<li><a href="https://openrouter.ai/nex-agi/nex-n2-pro:free">Nex-N2-Pro (free) - API Pricing & Providers | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了怀疑和担忧，一位用户指出权重在所有层上都与 0.6/0.4 的混合相同，另一位则讽刺地评论说这是在未注明出处的情况下获利。也有人为该方法辩护，认为合并可能结合了在线策略蒸馏，但蒸馏后的模型并未上传。

**标签**: `#LLM`, `#open-source`, `#AI ethics`, `#model merging`, `#controversy`

---

<a id="item-2"></a>
## [SK 海力士本月向主要客户交付 HBM4E 样品](https://36kr.com/newsflashes/3853695838016515?f=rss) ⭐️ 8.0/10

SK 海力士正筹备向主要客户送样 HBM4E，首批样品最快本月出货，为明年量产做准备。 这一里程碑加速了 AI 硬件内存路线图，HBM4E 带宽是 HBM4 的两倍，对下一代 AI 加速器和数据中心至关重要。 HBM4E 是 HBM4 的增强版，每堆栈带宽达 2 TB/s，而 HBM4 为 1.625 TB/s，同时保持相近的能效。量产计划于明年进行。

rss · 36Kr Feed · 6月15日 00:22

**背景**: 高带宽存储器（HBM）是一种 3D 堆叠 DRAM 技术，相比传统内存提供更高带宽、更低功耗和更小体积。HBM4 于 2025 年 4 月标准化，HBM4E 是其增强版本，带宽翻倍。SK 海力士和三星是该领域的领先制造商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://semiengineering.com/hbm4e-raises-the-bar-for-ai-memory-bandwidth/">HBM4E Raises The Bar For AI Memory Bandwidth</a></li>
<li><a href="https://nerds.xyz/2026/06/samsung-hbm4e-memory/">Samsung ships industry-first HBM 4 E memory as AI infrastructure race...</a></li>

</ul>
</details>

**标签**: `#HBM`, `#SK Hynix`, `#memory`, `#semiconductor`, `#AI hardware`

---

<a id="item-3"></a>
## [央视曝光非法将电动汽车电池改装用于电动自行车](https://www.ithome.com/0/964/174.htm) ⭐️ 8.0/10

央视财经调查节目曝光，深圳众投新能源有限公司非法拆解新能源汽车废旧动力电池，并将电芯销售给电动自行车使用，通过将工厂藏匿于偏远山谷来逃避监管。 这种做法带来严重的火灾风险，约 33%的电动自行车火灾由非法改装电池引发，其中约 80%的电芯来自新能源汽车废旧电池。此次曝光凸显了电池回收监管的关键漏洞和公共安全威胁。 该公司的拆解厂用帐篷遮挡，仓库与拆解厂相距 20 多公里，不同电芯产品从不同仓库发货以逃避检查。我国《新能源汽车废旧动力电池回收和综合利用管理暂行办法》明确禁止将废旧动力电池用于电动自行车。

rss · ITHome Feed · 6月14日 13:14

**背景**: 新能源汽车退役电池仍有余量，有时被用于电动自行车或储能等要求较低的领域，这一过程称为“梯次利用”。但若缺乏适当检测和安全措施，此类电池可能变得不稳定并引发火灾。中国已出台法规确保安全回收，并禁止非法改装。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gxt.fujian.gov.cn/jdhy/zxzcfg/gjzcfg/202601/t20260119_7082067.htm">新能源汽车废旧动力电池回收和综合利用管理暂行办法 _ 国家政策法规 _ 省工信厅</a></li>
<li><a href="https://www.catarc-adc.com/xwzxDetail/qyyw/85f6f207cf5741e9933e0b20b9ef9ab5">政策解读《新能源汽车废旧动力电池回收和综合利用管理暂行 ...</a></li>

</ul>
</details>

**标签**: `#battery safety`, `#EV batteries`, `#illegal recycling`, `#e-bike fires`, `#regulation`

---

<a id="item-4"></a>
## [Anthropic 因美国安全担忧全球暂停 AI 模型](https://www.dw.com/zh/%E5%92%8C%E4%B8%AD%E5%9B%BD%E6%9C%89%E5%85%B3-anthropic%E6%9C%80%E6%96%B0ai%E6%A8%A1%E5%9E%8B%E5%85%A8%E7%90%83%E6%96%AD%E4%BE%9B/a-77543796?maca=chi-rss-chi-all-1127-rdf) ⭐️ 8.0/10

2026 年 6 月 12 日，在美国商务部发布国家安全指令禁止向外国公民分发后，Anthropic 暂停了全球所有用户对其最新 AI 模型 Claude Fable 5 和 Claude Mythos 5 的访问权限。 这标志着美国首次对通用 AI 模型实施出口管制，开创了可能重塑全球对尖端 AI 访问的先例，并加剧了欧洲及其他地区对技术主权的呼声。 白宫担心与中国有关联的组织已访问了这些模型，从而引发了紧急行动。欧盟委员会正在评估影响，并强调此类措施不应歧视合作伙伴。

rss · DW Chinese · 6月14日 10:25

**背景**: Anthropic 是一家领先的 AI 公司，以其 Claude 系列大型语言模型而闻名。对 AI 模型的出口管制很少见；历史上，美国曾限制过超级计算机等硬件。这一事件让人联想到 1999 年因性能达到超级计算机水平而对苹果 Power Mac G4 实施的出口禁令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/">Anthropic disables Fable and Mythos AI models following... | Fortune</a></li>
<li><a href="https://www.politico.com/news/2026/06/13/inside-the-whirlwind-24-hours-that-led-the-white-house-to-slap-export-controls-on-anthropic-00961519">Inside the whirlwind 24 hours that led the White House to slap export ...</a></li>
<li><a href="https://www.euronews.com/my-europe/2026/06/14/us-export-controls-on-anthropic-should-not-be-discriminatory-eu-commission-warns">US export controls on Anthropic 'should not be... | Euronews</a></li>

</ul>
</details>

**社区讨论**: 一些 Reddit 用户猜测此次暂停可能是 Anthropic 在 IPO 前的营销噱头，而其他人则讨论了国家安全影响以及印度提升自身 AI 能力的必要性。

**标签**: `#AI`, `#geopolitics`, `#Anthropic`, `#national security`, `#tech regulation`

---

<a id="item-5"></a>
## [世航智能完成超 10 亿元 A 轮融资](https://36kr.com/newsflashes/3853744868348932?f=rss) ⭐️ 7.0/10

海洋具身智能公司世航智能完成 A 轮融资，金额超过 10 亿元，这是目前全球海洋机器人领域规模最大的单轮融资。投资方包括摩尔线程和昆仑芯的产业投资方上河动量基金、新加坡 Vertex Growth、上市公司大洋电机以及金沙江创投等。 这笔创纪录的融资表明投资者对海洋机器人和具身 AI 的信心强劲，可能加速自主水下机器人在工业应用中的部署。芯片公司的参与暗示了在海洋环境中推动软硬件一体化解决方案的趋势。 金沙江创投创始人朱啸虎已是第五轮投资世航智能，祥峰中国、华映资本、长石资本等老股东全部超额跟投。资金将用于核心技术研发、全球化市场拓展及产业链生态建设。

rss · 36Kr Feed · 6月15日 01:12

**背景**: 海洋具身智能是指集成到水下物理机器人中的 AI 系统，结合感知、决策和执行能力。世航智能开发自主水下航行器（AUV）和机器人解决方案，用于检测、维护和勘探等复杂水下任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.com/ogawa_tter/status/1939989396679487915">=> Moore Threads (摩尔线程) IPO accepted: Plans to raise CNY8B ...</a></li>
<li><a href="https://www.163.com/dy/article/KT0A1L3D0552HBC9.html">163.com/dy/article/KT0A1L3D0552HBC9.html</a></li>

</ul>
</details>

**标签**: `#marine robotics`, `#funding`, `#AI`, `#robotics`, `#venture capital`

---

<a id="item-6"></a>
## [谷歌与 UCSD 将旧 Pixel 手机改造成低成本数据中心](https://www.ithome.com/0/964/204.htm) ⭐️ 7.0/10

UCSD 与谷歌的研究人员通过移除非必要组件并安装 Linux 系统，将旧 Pixel 智能手机改造成数据中心节点，以极低的成本实现了与高端服务器相当的单核性能。 这种方法为大学和小型机构提供了一种可持续且经济高效的计算方案，减少了电子垃圾，并为昂贵的云服务或新硬件提供了替代方案。 25-50 台旧手机集群的总算力可媲美一台双路服务器 CPU，20 台手机集群可支持 75 人以上班级的应用需求。团队计划部署 2000 台手机集群以支持 100 个班级。

rss · ITHome Feed · 6月14日 23:56

**背景**: 隐含碳排放指设备制造和运输过程中产生的排放，废弃手机是电子垃圾的主要来源之一。SPEC 基准测试衡量单核性能，由于架构差异，旧手机的单核跑分可能高于某些服务器。Kubernetes 是一个用于自动化容器部署和扩展的开源平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.oryoy.com/news/kubernetes-rong-qi-bian-pai-cong-ru-men-dao-shi-zhan-jie-suo-wei-fu-wu-jia-gou-gao-xiao-yun-wei-zhi.html">Kubernetes ...</a></li>
<li><a href="https://www.jnr.ac.cn/EN/abstract/article/1000-3037/42041">Input-output Analysis of Embodied Carbon Emissions and SO<sub...</a></li>

</ul>
</details>

**标签**: `#sustainability`, `#edge computing`, `#data center`, `#e-waste`, `#Google`

---

<a id="item-7"></a>
## [韩国启动 5000 亿韩元研发计划，攻关下一代功率半导体](https://www.ithome.com/0/964/175.htm) ⭐️ 7.0/10

韩国启动了“超级创新经济项目”，投资 5000 亿韩元（约合 22.3 亿元人民币），用于开发下一代功率半导体，重点聚焦 SiC（碳化硅）和 GaN（氮化镓）材料。 该计划旨在增强韩国在功率半导体领域的竞争力，这类芯片对 AI 数据中心、电动汽车和可再生能源系统至关重要，有望降低能耗并提升多个高增长行业的效率。 该项目要求所有使用功率半导体的企业参与，旨在构建完整生态体系。SiC 和 GaN 相比传统硅具有耐高温、低能耗和高转换效率等优势。

rss · ITHome Feed · 6月14日 13:31

**背景**: 功率半导体用于管理和转换电力，常见于逆变器和充电器等设备。传统硅基器件正接近物理极限，而 SiC 和 GaN 等宽禁带材料可实现更高电压、频率和效率，对 AI 数据中心、电动汽车和工业应用至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rohm.com.cn/products/sic-power-devices/sic-power-module">SiC （ 碳 化 硅 ） 功 率 模块_产品搜索结果_罗姆 半 导 体 集团(ROHM...)</a></li>
<li><a href="https://www.rohm.com.cn/products/sic-power-devices">SiC （ 碳 化 硅 ） 功 率 器件_分立式元器件_罗姆 半 导 体 集团(ROHM...)</a></li>
<li><a href="https://www.elecfans.com/d/7552451.html">“三个必然”战略论断对国产 SiC ...</a></li>

</ul>
</details>

**标签**: `#power semiconductors`, `#SiC`, `#GaN`, `#AI data centers`, `#South Korea`

---

<a id="item-8"></a>
## [英国首相斯塔默宣布对 16 岁以下青少年实施‘澳大利亚加强版’社交媒体禁令](https://www.theguardian.com/uk-news/2026/jun/14/starmer-to-announce-australia-plus-ban-on-social-media-for-under-16s) ⭐️ 7.0/10

英国首相基尔·斯塔默将宣布禁止 16 岁以下青少年使用 TikTok、Instagram 和 X 等主要社交媒体应用，并对游戏应用施加额外限制，以防止与陌生人聊天。 这项‘澳大利亚加强版’政策标志着社交媒体监管的重大升级，可能为全球儿童在线安全树立先例，并影响数百万年轻用户和科技公司。 该禁令涵盖所有主要社交平台，而未涵盖的游戏应用必须移除 16 岁以下用户与陌生人聊天的功能。目前的 13 岁年龄限制并非政府强制，而这项新禁令将具有法律效力。

rss · The Guardian World · 6月14日 21:42

**背景**: 澳大利亚于 2024 年通过了类似法律，禁止 16 岁以下青少年使用社交媒体，英国现在试图效仿并扩大该政策。英国政府一直面临加强在线安全措施的压力，尤其是在最近的社会动荡和对虚假信息的担忧之后。该禁令预计将于 2026 年 6 月 15 日星期一宣布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/uk-news/2026/jun/14/what-is-uk-introducing-australia-plus-social-media-ban-how-will-it-work">Why is the UK launching an ‘ Australia plus ’ social media ban and...</a></li>
<li><a href="https://www.bbc.com/news/articles/cr472xry99lo">Newspaper headlines: UK's ' Australia plus ' social media ban and.....</a></li>

</ul>
</details>

**标签**: `#social media`, `#regulation`, `#child safety`, `#UK policy`

---

<a id="item-9"></a>
## [AI 加速可控核聚变研究](https://www.chinanews.com.cn/gn/2026/06-14/10640315.shtml) ⭐️ 6.0/10

中关村学院与中关村人工智能研究院的研究人员正在利用强化学习、生成式模型和自进化智能体等 AI 技术，通过快速诊断、等离子体预测和不稳定性控制来加速可控核聚变研究。 这项工作可能显著缩短实现实用聚变能源的时间线，而聚变能源有望提供近乎无限的清洁电力。它展示了 AI 如何应对最艰巨的科学与工程挑战之一。 该团队采用“物理+数据”双轮驱动的方法，将物理模型与 AI 结合以应对聚变关键挑战。该研究是中国“活力中国”调研活动的一部分，凸显了国家对 AI 驱动能源解决方案的关注。

rss · China News Service China · 6月14日 11:25

**背景**: 可控核聚变旨在通过极高温度下轻原子核的聚变，在地球上复制太阳的能量产生方式。由于约束和控制超高温等离子体的困难，实现稳定持续的聚变一直是长达数十年的挑战。AI 提供了预测等离子体行为和防止可能中断反应的不稳定性的新方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aroundphysics.com/avoiding-fusion-plasma-tearing-instability-with-deep-reinforcement-learning/">AI深度 学 习 :可控 核 聚 变 的 新出路 – Around Physics 物理边界</a></li>

</ul>
</details>

**标签**: `#AI`, `#nuclear fusion`, `#energy`, `#research`

---

<a id="item-10"></a>
## [网件起诉 TP-Link 虚假宣传为美国公司](https://www.ithome.com/0/964/232.htm) ⭐️ 6.0/10

网件于 2026 年 6 月 11 日提交了一份 49 页的反诉，指控 TP-Link 虚假声称自己是美国公司，并称这一欺骗行为导致网件损失了数千万美元的销售额。 这场法律战凸显了美国网络市场日益增长的国家安全担忧——FCC 近期已禁止外国制造的路由器——并可能重塑消费者对主要路由器品牌的信任和市场竞争格局。 网件的反诉引用了 TP-Link 2024 年可持续发展报告，显示大部分生产仍在中国进行，尽管 TP-Link 声称已完全剥离中国业务。TP-Link 回应称网件的指控“不准确且歪曲事实”。

rss · ITHome Feed · 6月15日 01:30

**背景**: TP-Link 是一家中国网络设备制造商，1996 年成立于深圳。2024 年，它在加州尔湾设立了美国总部，并声称已与中国关联公司分离。FCC 于 2026 年 3 月以安全为由禁止了新的外国制造路由器，并给予网件等少数公司临时豁免。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TP-Link">TP - Link - Wikipedia</a></li>
<li><a href="https://me.pcmag.com/en/wi-fi-mesh-networking-systems/31411/why-were-continuing-to-recommend-tp-link-routers-despite-security-concerns">The FCC 's Foreign - Made Router Ban : Is Your TP-Link or Asus...</a></li>

</ul>
</details>

**标签**: `#networking`, `#legal`, `#false advertising`, `#TP-Link`, `#Netgear`

---

<a id="item-11"></a>
## [计算机历史博物馆从德国仓库回收 2000 余件文物](https://www.ithome.com/0/964/208.htm) ⭐️ 6.0/10

计算机历史博物馆（CHM）从德国卡斯特罗普-劳克塞尔镇一座三层仓库中回收了 2000 余件复古计算文物，装满 7 辆重型半挂卡车。这批藏品横跨 20 世纪 30 年代至 80 年代，包括大型机、小型机、磁盘驱动器及穿孔卡设备。 这是 CHM 历史上最大规模的一次藏品收购，保护了可能被遗失的稀有计算历史。文物包括冷战时期东欧集团的机器和早期欧洲硬件，填补了计算历史记录的空白。 这批藏品最初由亚琛工业大学的一位教授收集；仓库中还发现了一枚未爆炸的二战炸弹，清理工作一度中断。CHM 专门建造了新的恒温仓库来存放这些文物，现归入 SAP 藏品专区。

rss · ITHome Feed · 6月15日 00:19

**背景**: 位于加州山景城的计算机历史博物馆致力于保存计算历史。这批文物于 2006 年由一位税务顾问向博物馆爆料后被发现，但回收工作历时多年才完成。藏品包括 Diablo 磁盘驱动器、DECtape 和早期 OCR 设备等稀有物品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Computer_History_Museum">Computer History Museum</a></li>
<li><a href="https://www.youtube.com/channel/UCHDr4RtxwA1KqKGwxgdK4Vg">Computer History Museum - YouTube</a></li>
<li><a href="https://www.wikiwand.com/en/articles/Computer_History_Museum">Computer History Museum - Wikiwand</a></li>

</ul>
</details>

**标签**: `#computer history`, `#museum`, `#vintage computing`, `#artifact recovery`

---

<a id="item-12"></a>
## [通用汽车计划让电动汽车为电网供电，但硬件成本高达 2 万美元](https://www.ithome.com/0/964/197.htm) ⭐️ 6.0/10

通用汽车宣布了一项车网互动（V2G）计划，允许其闲置的电动汽车通过双向充电向电网反向供电，但所需硬件设备不含安装费约需 2 万美元。 如果广泛采用，V2G 可将数百万辆电动汽车转变为分布式储能资产，有助于在用电高峰稳定电网，并为车主开辟新的收入来源，但高昂的前期成本和监管碎片化构成了重大障碍。 通用汽车表示，美国已有超过 25 万辆具备双向充电能力的电动汽车上路，储存的电量足以满足约 12 万户家庭一周的用电需求。但车主需配备约 2 万美元的专用双向充电器，大约需要五年才能收回成本。

rss · ITHome Feed · 6月14日 23:20

**背景**: 车网互动（V2G）技术使电动汽车不仅能从电网取电，还能在需要时将储存的电能送回电网。双向充电需要兼容的车辆和专用充电器。通用汽车已与太平洋燃气电力公司和 DTE 能源公司合作开展试点项目，但全国推广面临监管和基础设施挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.autoconnectedcar.com/2026/06/how-to-get-gm-vehicle-to-grid-bi-directional-charging-is-the-cost-worth-it/">How to Get GM Vehicle to Grid Bi - Directional Charging & is the Cost ...</a></li>
<li><a href="https://emobilityplus.com/2026/06/11/gm-urges-utilities-to-embrace-evs-as-grid-assets-through-vehicle-to-grid-technology/">GM Urges Utilities to Embrace EVs as Grid Assets Through...</a></li>
<li><a href="https://arstechnica.com/cars/2026/06/gm-energy-introduces-v2g-support-and-new-energy-storage-battery-chemistry/">GM Energy introduces V2G support and new energy ... - Ars Technica</a></li>

</ul>
</details>

**标签**: `#electric vehicles`, `#vehicle-to-grid`, `#energy`, `#GM`, `#infrastructure`

---

<a id="item-13"></a>
## [新厄尔尼诺事件已宣布，可能成为‘超级’厄尔尼诺](https://www.bbc.com/zhongwen/articles/cly0ne5y8x5o/trad?at_medium=RSS&at_campaign=rss) ⭐️ 6.0/10

美国机构宣布热带太平洋出现新一轮厄尔尼诺现象，近几个月海面温度急剧上升。许多预测显示，这次事件可能形成‘超级’厄尔尼诺，甚至可能成为有记录以来最强之一。 厄尔尼诺事件会显著扰乱全球天气模式，在世界各地引发干旱、洪水等极端天气。‘超级’厄尔尼诺可能对许多地区的农业、水资源和经济造成严重影响。 该事件的特点是热带太平洋中部和东部海面温度异常升高。预测模型显示，未来几个月这次厄尔尼诺现象很可能进一步增强。

rss · BBC Chinese · 6月14日 03:12

**背景**: 厄尔尼诺是一种气候模式，每 2-7 年发生一次，当热带太平洋的暖水向东移动，改变大气环流时出现。它是厄尔尼诺-南方涛动（ENSO）循环的暖相位，相反相位是拉尼娜。强厄尔尼诺事件可能产生全球性后果，包括某些地区降雨增加，其他地区干旱。

**标签**: `#climate`, `#El Niño`, `#environment`, `#science`

---

<a id="item-14"></a>
## [黑灯工厂：威胁中国年轻人就业？](https://www.dw.com/zh/%E9%BB%91%E7%81%AF%E5%B7%A5%E5%8E%82-%E7%85%A7%E4%B8%8D%E4%BA%AE%E4%B8%AD%E5%9B%BD%E5%B9%B4%E8%BD%BB%E4%BA%BA%E7%9A%84%E5%B0%B1%E4%B8%9A%E4%B9%8B%E8%B7%AF/a-77527764?maca=chi-rss-chi-all-1127-rdf) ⭐️ 6.0/10

德国之声的一篇文章分析指出，中国快速推广的“黑灯工厂”——完全自动化的无人工厂——可能会减少年轻人的就业机会，尽管政府将机器人和人工智能视为工业增长的引擎。 这很重要，因为中国是全球最大的工业机器人市场，自动化可能取代传统上雇佣年轻低技能工人的数百万制造业岗位，可能加剧青年失业问题。 2025 年中国机器人产量占全球 40%以上，制造业机器人密度位居世界第三。文章质疑一些机器人演示是否只是作秀而非实际部署。

rss · DW Chinese · 6月14日 07:08

**背景**: “黑灯工厂”是指完全依靠机器人和自动化设备自主运行、无需人工现场操作的制造设施。中国大力投资机器人和人工智能以升级制造业，但这引发了关于大量年轻劳动力失业的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lights_out_(manufacturing)">Lights out (manufacturing) - Wikipedia</a></li>
<li><a href="https://www.eyeshenzhen.com/content/2021-11/11/content_24728159.htm">Catch Phrase | 黑灯工厂（hēidēng gōngchǎng）</a></li>
<li><a href="https://news.cctv.cn/2025/08/12/ARTI49y0ACUzXrygaAx0joyx250812.shtml">news.cctv.cn/2025/08/12/ARTI49y0ACUzXrygaAx0joyx250812.shtml</a></li>

</ul>
</details>

**标签**: `#automation`, `#employment`, `#China`, `#robotics`, `#AI`

---

<a id="item-15"></a>
## [FBI 建造模拟小镇用于网络攻击演练](https://www.theverge.com/tech/949648/fbi-fake-town-cyberattacks-kinetic-cyber-range) ⭐️ 6.0/10

FBI 在阿拉巴马州亨茨维尔开设了一个占地 22000 平方英尺的模拟小镇，名为“动能网络靶场”，用于模拟网络攻击以进行训练。 该设施为网络特工提供了逼真的实战训练环境，弥合了课堂学习与现实事件响应之间的差距，在网络威胁日益复杂的背景下至关重要。 该小镇包括便利店、加油站、医院和带家具的房屋，使受训者能够在模拟真实基础设施的物理环境中练习应对网络事件。

rss · The Verge · 6月14日 20:35

**背景**: FBI 的动能网络靶场仿照自 1987 年起用于战术训练的模拟小镇“霍根小巷”。传统的网络培训通常在教室或虚拟环境中进行，而该设施增加了物理维度，以模拟网络攻击与物理攻击的融合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fbi.gov/news/stories/inside-the-fbis-kinetic-cyber-range">Inside the FBI ’s Kinetic Cyber Range — FBI</a></li>
<li><a href="https://cybernews.com/cybercrime/fbi-kinetic-cyber-range-training/">First look at the FBI 's "Kinetic Cyber Range " | Cybernews</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hogan's_Alley_(FBI)">Hogan ' s Alley ( FBI ) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#FBI`, `#training`, `#simulation`

---

<a id="item-16"></a>
## [中国构建全国一体化算力网赋能数字经济](https://www.chinanews.com.cn/gn/2026/06-14/10640309.shtml) ⭐️ 5.0/10

中国正在建设全国一体化算力网，旨在让算力像水电一样普惠便捷，以满足人工智能爆发式增长带来的算力需求。 该举措有望将算力转变为无处不在的公共资源，加速各行业的 AI 创新和数字化转型，并增强中国数字基础设施的竞争力。 该网络旨在全国范围内统筹通用算力、智能算力和超级算力资源，实现算力与数据、算法及绿色电力的协同融合。

rss · China News Service China · 6月14日 11:13

**背景**: 算力是 AI 训练和推理的关键，但目前资源分散且成本高昂。统一网络可实现高效调度与共享，类似于电网分配电力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xueqiu.com/4443570191/377808043">xueqiu.com/4443570191/377808043</a></li>
<li><a href="https://www.taogongwei.com/news/detail/23948">算 力 网 来了！ 国 家要砸7万亿建“六张 网 ”</a></li>
<li><a href="http://paper.people.com.cn/rmrb/images/2024-04/12/09/rmrb2024041209.pdf">GCRMRB09B20240412C</a></li>

</ul>
</details>

**标签**: `#computing network`, `#digital economy`, `#China`, `#AI infrastructure`

---

<a id="item-17"></a>
## [远程医疗公司面临控制肥胖药物成本的压力](https://www.npr.org/2026/06/14/nx-s1-5805984/glp1-telehealth-weight-loss-drugs) ⭐️ 5.0/10

雇主要求 Vida Health 等远程医疗公司不仅为肥胖药物使用者提供生活方式支持，还要限制昂贵的 GLP-1 药物（如 Wegovy）的支出。 这一趋势凸显了患者获得有效肥胖治疗与雇主成本控制措施之间日益紧张的关系，可能重塑远程医疗公司在减肥药物市场的运营方式。 Wegovy 的标价约为每月 1350 美元，对雇主来说是一笔巨大开支。最初专注于生活方式指导的远程医疗公司现在面临管理药物使用和成本的压力。

rss · NPR News · 6月14日 09:00

**背景**: GLP-1 受体激动剂（如 Wegovy、Ozempic）等肥胖药物因其有效性而成为重磅药物。远程医疗公司进入这一领域提供远程护理和支持，但为这些药物买单的雇主希望控制不断上涨的药房成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.npr.org/2026/06/14/nx-s1-5805984/glp1-telehealth-weight-loss-drugs">Telehealth companies limit who gets weight loss drugs : NPR</a></li>
<li><a href="https://www.theatlantic.com/health/archive/2023/11/ozempic-wegovy-obesity-drugs-benefits/676011/">The Obesity - Drug Era Starts Now - The Atlantic</a></li>
<li><a href="https://www.fiercehealthcare.com/health-tech/telehealth-companies-target-100b-weight-loss-drug-market-patients-grapple-access-costs">Startups, big players ramp up focus on weight loss drug market</a></li>

</ul>
</details>

**标签**: `#telehealth`, `#healthcare`, `#obesity drugs`, `#policy`

---

<a id="item-18"></a>
## [半固态电池填补全固态电池延迟的空白](https://www.theverge.com/column/948594/solid-state-batteries-semi-solid-state) ⭐️ 5.0/10

文章指出，全固态电池因界面退化和制造难题尚未准备好大规模应用，而半固态（凝胶）电池正作为一种实用的中间解决方案出现。 这很重要，因为半固态电池相比传统锂离子电池提供了更高的安全性和能量密度，可能在不等待全固态技术的情况下加速电动汽车和便携电子设备的普及。 半固态电池使用凝胶状电解质，降低了热失控和泄漏的风险，同时比真正的全固态电池更容易制造。然而，它们尚未达到全固态电池的理论能量密度。

rss · The Verge · 6月14日 12:00

**背景**: 传统锂离子电池使用液态电解质，可能泄漏并引发火灾。全固态电池用固态电解质替代液体，承诺更高的能量密度和安全性，但面临界面电阻和高生产成本等挑战。半固态电池使用凝胶电解质作为折中方案，在现有制造工艺下提供部分固态电池的优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://spectrum.ieee.org/semi-solid-state-battery">Semi - Solid -State Batteries : Coming Soon to Electric... - IEEE Spectrum</a></li>
<li><a href="https://www.theverge.com/column/948594/solid-state-batteries-semi-solid-state">Solid -state batteries still aren’t ready, but gels are | The Verge</a></li>
<li><a href="https://www.digit.in/features/mobile-phones/what-is-semi-solid-battery-in-vivo-x200-pro-and-why-does-it-matter.html">What is Semi - Solid Battery in Vivo X200 Pro, and why does it matter?</a></li>

</ul>
</details>

**标签**: `#batteries`, `#solid-state`, `#energy storage`, `#technology`

---

<a id="item-19"></a>
## [黑土地保护国际会议在长春举行](https://www.chinanews.com.cn/gn/2026/06-14/10640336.shtml) ⭐️ 4.0/10

第六届黑土地保护利用国际会议暨 FAO 国际黑土联盟年会在吉林长春举行，300 余位中外专家学者围绕黑土地健康培育、产能提升、智慧农业发展和生态屏障建设四大主题展开研讨。 黑土地对全球粮食安全至关重要，本次会议促进了国际合作以应对土壤退化、推动可持续农业，这对长期农业生产力至关重要。 会议设有四个主题分会：黑土地健康培育、产能提升、智慧农业发展和生态屏障建设。会议由 FAO 国际黑土联盟与中国机构共同组织。

rss · China News Service China · 6月14日 12:50

**背景**: 黑土富含有机质，主要分布在中国东北、乌克兰和美国中西部。它非常肥沃，但易受侵蚀和退化。中国已启动“黑土粮仓”科技会战以保护这一资源。

**标签**: `#agriculture`, `#soil conservation`, `#conference`

---

<a id="item-20"></a>
## [初创公司借 AI 上市潮，追随 SpaceX](https://techcrunch.com/2026/06/14/as-ai-companies-race-to-go-public-who-else-is-along-for-the-ride/) ⭐️ 4.0/10

TechCrunch 的一篇文章报道称，初创公司正试图利用 AI 公司上市的趋势，以 SpaceX 的 IPO 为标杆。例如，Quantum Space 正在通过 SPAC 合并来搭乘 SpaceX 的 IPO 浪潮。 这一趋势预示着 AI 和太空领域可能出现泡沫，投资者争相追捧高调 IPO。它可能重塑 IPO 格局，如果估值变得不可持续，将影响市场稳定。 文章指出，SpaceX 的 IPO 创纪录，以 1.8 万亿美元估值筹集了 750 亿美元。一些交易员警告称，涉及 SpaceX、OpenAI 和 Anthropic 的 IPO 浪潮类似于互联网泡沫顶峰。

rss · TechCrunch · 6月14日 16:38

**背景**: IPO（首次公开募股）是指私人公司首次向公众出售股票。SPAC（特殊目的收购公司）是与私人公司合并以使其更快上市的空壳公司。AI 行业估值激增，据报道 OpenAI 和 Anthropic 等公司也在考虑 IPO。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bloomberg.com/opinion/articles/2026-06-12/spacex-anthropic-openai-ipos-are-a-red-flag-for-stock-market-s-future">SpaceX -Anthropic-OpenAI IPOs Are a Red Flag for Stock... - Bloomberg</a></li>
<li><a href="https://techcrunch.com/2026/06/14/as-ai-companies-race-to-go-public-who-else-is-along-for-the-ride/">Startups are trying to "ride that SpaceX IPO wave ." | TechCrunch</a></li>
<li><a href="https://www.tradingview.com/news/stocktwits:fea462165094b:0-tsla-stock-slips-overnight-spacex-ipo-hype-is-starting-to-look-like-amazon-s-dot-com-bubble-peak-in-2000-warns-ex-lehman-trader/">TSLA Stock Slips Overnight: SpaceX IPO Hype... — TradingView News</a></li>

</ul>
</details>

**标签**: `#AI`, `#startups`, `#IPO`, `#finance`

---

<a id="item-21"></a>
## [公安部公布 10 起网络谣言典型案例](https://www.chinanews.com.cn/gn/2026/06-15/10640436.shtml) ⭐️ 3.0/10

2026 年 6 月 15 日，公安部网安局公布了 10 起打击整治网络谣言违法犯罪典型案例，展示了政府持续打击网络虚假信息的努力。 这一公告凸显了中国政府对网络安全和网络内容监管的加强，可能影响互联网平台和用户在中国的运营方式。 这些案例涵盖涉及公共安全、社会秩序和个人名誉等各类网络谣言，展示了传播虚假信息的法律后果。

rss · China News Service Scroll · 6月15日 00:10

**背景**: 网络谣言在中国已成为一个重大问题，导致社会不稳定和个人权益受损。公安部一直积极开展打击此类违法活动的专项行动，此次发布旨在警示潜在违法者。

**标签**: `#cybersecurity`, `#law enforcement`, `#online rumors`

---

<a id="item-22"></a>
## [福建海事部门发布 5 项举措促两岸航运发展](https://www.chinanews.com.cn/gn/2026/06-14/10640270.shtml) ⭐️ 3.0/10

在 2026 年海峡两岸航海文化交流活动上，福建海事部门发布了五项促进两岸航运高质量发展的新举措。 这些举措旨在加强福建与台湾之间的海上互联互通和经济合作，有望简化航运流程并提升贸易效率。 公告中未详细说明五项措施的具体内容，但它们是在海峡论坛框架下深化两岸交流的持续努力的一部分。

rss · China News Service China · 6月14日 11:36

**背景**: 海峡论坛是促进两岸民间交流的年度活动。福建因地理上靠近台湾，在两岸交通和贸易中扮演关键角色。

**标签**: `#maritime`, `#policy`, `#cross-strait`, `#shipping`

---

<a id="item-23"></a>
## [A 股开盘普涨，三大指数集体高开](https://www.chinanews.com.cn/cj/2026/06-15/10640477.shtml) ⭐️ 2.0/10

周一，A 股三大指数集体高开，超 3600 只个股上涨，贵金属、海运板块领涨，煤炭、油气、航天军工板块下跌。 这一日常市场波动反映了短期投资者情绪和板块轮动，但对更广泛的技术或 AI 行业没有显著的技术或政策影响。 涨势广泛但缺乏明确催化剂；贵金属因全球不确定性上涨，煤炭和石油因需求担忧下跌。数据为初步数据，盘中可能变化。

rss · China News Service Scroll · 6月15日 01:40

**标签**: `#finance`, `#stock market`, `#China`

---

<a id="item-24"></a>
## [央行开展 4250 亿元 7 天期逆回购操作](https://www.chinanews.com.cn/cj/2026/06-15/10640467.shtml) ⭐️ 2.0/10

2026 年 6 月 15 日，中国人民银行以固定利率 1.40%开展了 4250 亿元 7 天期逆回购操作，全额满足了一级交易商需求。 该操作是管理银行体系短期流动性的常规工具，反映了央行维持稳定货币环境的政策立场。 操作采用固定利率数量招标方式，利率维持在 1.40%，与前期操作一致。

rss · China News Service Scroll · 6月15日 01:35

**背景**: 逆回购是央行向商业银行购买证券并约定未来卖回的短期操作，旨在向银行体系注入流动性。一级交易商是直接参与央行公开市场操作的指定金融机构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.jwview.com/jingwei/kb/m/04-16/231663.shtml">央行开展5亿元 7 天 期 逆 回 购 操 作</a></li>

</ul>
</details>

**标签**: `#finance`, `#central bank`, `#monetary policy`

---

<a id="item-25"></a>
## [人民币中间价报 6.8088，上调 21 个基点](https://www.chinanews.com.cn/cj/2026/06-15/10640465.shtml) ⭐️ 2.0/10

2026 年 6 月 15 日，中国人民银行将人民币对美元中间价定为 6.8088，较前一交易日的 6.8109 上调 21 个基点。 这一调整反映了央行对人民币汇率的日常管理，影响贸易和投资流动。虽然变化幅度小，但传递了中国有管理的浮动汇率制度下的政策信号。 中间价是交易区间的中点，允许人民币在上下 2%的幅度内浮动。上调 21 个基点意味着人民币对美元小幅升值。

rss · China News Service Scroll · 6月15日 01:34

**背景**: 中国人民银行每日设定人民币对美元中间价，作为交易参考。该汇率基于市场状况和政策考量确定。一个基点是百分之一的百分之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://forex.cfi.cn/">CFI.CN外汇_ 中 财网</a></li>

</ul>
</details>

**标签**: `#finance`, `#currency`, `#China`

---

<a id="item-26"></a>
## [中国驻菲律宾使馆提醒入境旅客备齐文件](https://www.chinanews.com.cn/hr/2026/06-15/10640461.shtml) ⭐️ 2.0/10

2026 年 6 月 15 日，中国驻菲律宾大使馆发布提醒，要求中国公民提前备齐入境材料并明确行程信息，以免在菲律宾机场被拒绝入境或遣返。 该提醒有助于中国旅客避免法律和经济麻烦，也反映了菲律宾持续加强的入境执法，可能影响旅游和商务出行。 近期案例显示，因入境材料不足或行程信息不清，有中国公民在菲律宾机场被拦截盘查甚至遣返。

rss · China News Service Scroll · 6月15日 01:32

**背景**: 中国驻外使领馆定期发布旅行提醒以保护海外公民。菲律宾是中国游客和商务旅客的热门目的地，入境规定要求提供清晰的文件和返程机票。

**标签**: `#travel advisory`, `#embassy notice`, `#Philippines`

---

<a id="item-27"></a>
## [专家解读中国房地产市场分化](https://www.chinanews.com.cn/cj/2026/06-15/10640462.shtml) ⭐️ 2.0/10

广东省住房政策研究中心首席研究员李宇嘉发表评论文章，分析中国房地产市场的分化现象。 该评论提供了专家对市场趋势的看法，可能影响中国房地产行业的投资者情绪和政策讨论。 该文章是一篇通用评论，没有具体数据或技术分析，缺乏与技术领域相关的新颖性或深度。

rss · China News Service Scroll · 6月15日 01:20

**背景**: 近年来，中国房地产市场经历了显著的区域和行业分化，部分城市房价下跌，而其他城市保持稳定。专家常分析这些趋势以指导政策和投资决策。

**标签**: `#real estate`, `#China`, `#market analysis`

---

<a id="item-28"></a>
## [英法德意准备解除对伊朗制裁](https://www.chinanews.com.cn/gj/2026/06-15/10640453.shtml) ⭐️ 2.0/10

2026 年 6 月 14 日，英国、法国、德国和意大利发表联合声明，表示在美国与伊朗达成结束战争的协议后，准备解除对伊朗的制裁，以换取伊朗在核计划方面采取举措。 这标志着欧洲对伊朗外交姿态的重大转变，可能缓解经济限制并重塑地区地缘政治格局。 该联合声明由路透社于 2026 年 6 月 14 日报道。解除制裁的前提是伊朗在其核计划方面采取具体行动。

rss · China News Service Scroll · 6月15日 01:19

**背景**: 伊朗多年来因其核活动面临国际制裁。美国与伊朗近期达成结束冲突的协议，为欧洲国家重新考虑制裁铺平了道路。

**标签**: `#geopolitics`, `#international relations`, `#sanctions`

---