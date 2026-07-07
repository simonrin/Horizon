---
layout: default
title: "Horizon Summary: 2026-07-07 (ZH)"
date: 2026-07-07
lang: zh
---

> 从 366 条内容中筛选出 28 条重要资讯。

---

1. [Januscape：严重的 KVM/x86 虚拟机逃逸漏洞（CVE-2026-53359）](#item-1) ⭐️ 9.0/10
2. [我国首款 5 米级可回收火箭转运至发射台](#item-2) ⭐️ 8.0/10
3. [Anthropic 与 TeraWulf 签署 190 亿美元、20 年数据中心租约](#item-3) ⭐️ 8.0/10
4. [我国建成首套高精度圆度基准装置](#item-4) ⭐️ 8.0/10
5. [中国天问二号抵达目标小行星](#item-5) ⭐️ 8.0/10
6. [快速子宫内膜异位症检测将在 NHS 推出](#item-6) ⭐️ 8.0/10
7. [苏格兰提议暂停新建数据中心，挑战英国 AI 战略](#item-7) ⭐️ 8.0/10
8. [首次 AI 勒索攻击仍需人类参与](#item-8) ⭐️ 8.0/10
9. [2026 年科技公司因 AI 裁员](#item-9) ⭐️ 8.0/10
10. [前大疆工程师获数亿融资，打造消费级纺织机](#item-10) ⭐️ 7.0/10
11. [前西门子、罗罗团队创业，获数千万元融资打造航空电驱系统](#item-11) ⭐️ 7.0/10
12. [蚂蚁灵波发布空间感知模型 LingBot-Depth 2.0](#item-12) ⭐️ 7.0/10
13. [支付宝 AI 开放平台开启邀测](#item-13) ⭐️ 7.0/10
14. [AI 演员 Tilly Norwood 将主演首部电影《Misaligned》](#item-14) ⭐️ 7.0/10
15. [新加坡在英伟达芯片案中追加洗钱指控](#item-15) ⭐️ 7.0/10
16. [熊蜂面部表情显示“喜欢”和“不喜欢”](#item-16) ⭐️ 7.0/10
17. [Vercel CEO 谈将 AI 模型与智能体分离](#item-17) ⭐️ 7.0/10
18. [虚假实习内推黑产链条曝光：5000 余份 offer 全是假的](#item-18) ⭐️ 6.0/10
19. [研究生培养不能一刀切](#item-19) ⭐️ 4.0/10
20. [中国高校为 AI 时代改革创业课程](#item-20) ⭐️ 3.0/10
21. [中国红十字会向广西台风灾区运送救灾物资](#item-21) ⭐️ 2.0/10
22. [甘肃山体滑坡后，自然资源部启动地质灾害防御Ⅲ级响应](#item-22) ⭐️ 2.0/10
23. [中国暑期旅游市场列车航班加密供需两旺](#item-23) ⭐️ 2.0/10
24. [盲盒消费投诉：销售、质量、退货问题](#item-24) ⭐️ 2.0/10
25. [汛期出行提示：全国公路、铁路、水路最新动态](#item-25) ⭐️ 2.0/10
26. [A 股午评：普跌行情，板块分化](#item-26) ⭐️ 2.0/10
27. [近视手术并非人人适合](#item-27) ⭐️ 2.0/10
28. [体检前的常见错误](#item-28) ⭐️ 2.0/10

---

<a id="item-1"></a>
## [Januscape：严重的 KVM/x86 虚拟机逃逸漏洞（CVE-2026-53359）](https://github.com/V4bel/Januscape) ⭐️ 9.0/10

KVM/x86 的 shadow MMU 模拟中存在一个严重的释放后使用漏洞（CVE-2026-53359），允许客户机逃逸到宿主机。概念验证代码可导致宿主机内核崩溃，完整利用计划在未来发布。 该漏洞对使用 KVM/x86 并启用嵌套虚拟化的云服务提供商和沙箱环境构成严重风险，攻击者可能从客户机 VM 攻破宿主机。在/dev/kvm 全局可写的发行版上，它还可作为可靠的本地提权漏洞。 该漏洞影响 Intel 和 AMD 宿主机，因为它位于通用的 x86 shadow MMU 代码中。客户机到宿主机逃逸需要启用嵌套虚拟化，禁用该功能可缓解风险。

hackernews · Imustaskforhelp · 7月6日 17:35 · [社区讨论](https://news.ycombinator.com/item?id=48807908)

**背景**: KVM（基于内核的虚拟机）是一个 Linux 内核模块，将内核转变为虚拟机监控器，允许在 x86 硬件上运行多个虚拟机。虚拟机逃逸是指客户机 VM 内运行的代码突破隔离并在宿主机上执行。嵌套虚拟化允许在 VM 内运行虚拟机监控器，增加了复杂性和潜在攻击面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine">Kernel-based Virtual Machine - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Virtual_machine_escape">Virtual machine escape - Wikipedia</a></li>
<li><a href="https://lowendtalk.com/discussion/218905/januscape-guest-to-host-escape-in-kvm-x86-cve-2026-53359">Januscape: Guest-to-Host Escape in KVM/x86 (CVE-2026-53359) — LowEndTalk</a></li>

</ul>
</details>

**社区讨论**: 评论者强调嵌套虚拟化固有的复杂性和风险，有人建议不要为公共 VM 主机启用该功能。其他人指出该漏洞在/dev/kvm 全局可写的系统上也可用于本地提权，质疑为何此类设备文件对不受信任的应用程序可访问。

**标签**: `#KVM`, `#virtualization`, `#security`, `#CVE`, `#x86`

---

<a id="item-2"></a>
## [我国首款 5 米级可回收火箭转运至发射台](https://www.ithome.com/0/973/363.htm) ⭐️ 8.0/10

我国长征十号乙（CZ-10B）火箭——国内首款 5 米芯级直径的可重复使用运载火箭——已转运至海南商业航天发射场并在 2 号发射工位起竖，首飞窗口锁定在 2026 年 7 月 10 日至 13 日。 此次任务旨在验证全球首创的“海上网系回收”技术，这是一种全新的火箭级回收方案，有望大幅降低成本并提高效率，使中国成为继美国之后第二个掌握大运力可回收火箭技术的国家。 火箭采用两级半构型，一子级配备 7 台 YF-100K 发动机，起飞质量约 540 吨，一子级回收状态下近地轨道运力不小于 16 吨。它取消了着陆腿，改用专用挂钩由回收船“领航者”号的巨型网系捕获。

rss · ITHome Feed · 7月7日 01:54

**背景**: 可重复使用火箭由 SpaceX 的猎鹰 9 号率先实现，采用着陆腿垂直着陆。长征十号乙则采用不同方案：一子级释放挂钩，由海上平台的网系捕获，从而减轻结构重量并简化再入控制。回收船“领航者”号长 144 米、宽 50 米、满载排水量 2.5 万吨，具备 DP2 动力定位能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.toutiao.com/article/7626987811048129034/">长征十号乙即将首飞，海上网系回收技术及产业链梳理</a></li>
<li><a href="https://www.cislunarspace.cn/space-news/2026/04/2026-04-28-changzheng-10yi-maiden-flight/">长征十号乙运载火箭成功首飞，全球首创海上网系回收技术验证</a></li>
<li><a href="https://zh.wikipedia.org/zh-hans/长征十号乙运载火箭">长征十号乙运载火箭 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**标签**: `#rocket`, `#reusable`, `#China`, `#space`, `#Long March`

---

<a id="item-3"></a>
## [Anthropic 与 TeraWulf 签署 190 亿美元、20 年数据中心租约](https://www.ithome.com/0/973/347.htm) ⭐️ 8.0/10

Anthropic 与 TeraWulf 签署了一份为期 20 年的租赁协议，在肯塔基州霍斯维尔建设一座 401 兆瓦的 AI 数据中心园区，总营收价值 190 亿美元。预计 2027 年下半年初步投用，2028 年初达到最大装机容量。 这笔巨额长期租约凸显了 AI 专用计算基础设施需求的激增，并标志着向超大规模、定制化数据中心的转变。它也反映了 AI 公司提前数年锁定电力容量以支持大规模模型训练和推理的趋势。 该园区将建在 TeraWulf 的 Justified Data 站点，原为世纪铝业冶炼厂，可提供约 480 兆瓦的即时可用电力。此外，TeraWulf 将其在得克萨斯合资项目中 50.1%的股份出售给了 Fluidstack，后者正主导 Anthropic 的 500 亿美元计算基础设施建设。

rss · ITHome Feed · 7月7日 01:15

**背景**: Anthropic 是一家领先的 AI 初创公司，以其 Claude 模型系列闻名，与 OpenAI 和 Google 竞争。TeraWulf 是一家数字基础设施公司，为 AI 和高性能计算开发大型数据中心。Justified Data 站点由 TeraWulf 于 2026 年 2 月以 2 亿美元现金加少数股权收购。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.terawulf.com/">TeraWulf : Leading the Digital Energy Revolution</a></li>
<li><a href="https://www.techtimes.com/articles/319776/20260706/anthropic-signs-19b-data-center-lease-wulf-surges-ai-power-crunch-deepens.htm">Anthropic Signs $19B Data Center Lease: WULF Surges as AI Power...</a></li>
<li><a href="https://blockspace.media/insight/terawulf-signs-anthropic-lease-sells-abernathy/">TeraWulf signs 20-year Anthropic lease for 401 MW at Kentucky data ...</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Data Center`, `#Anthropic`, `#Cloud Computing`, `#Investment`

---

<a id="item-4"></a>
## [我国建成首套高精度圆度基准装置](https://www.ithome.com/0/973/328.htm) ⭐️ 8.0/10

我国首套高精度圆度基准装置由中国计量科学研究院研制完成，将圆度测量不确定度从 20 纳米降至 6 纳米。 这一突破填补了我国圆度计量领域的空白，为航空航天、高端机床、先进光学和半导体制造等战略产业提供量值溯源支撑，增强了我国在精密测量领域的自主可控能力。 该装置集成了多项自主创新技术，包括新型误差分离技术以抑制主轴回转误差，以及基于高准确度滤波与全效数据利用的圆度计算模型，解决了国际性技术瓶颈。

rss · ITHome Feed · 7月6日 23:59

**背景**: 圆度是几何量形位公差体系中的核心基础参数，直接影响精密主轴、光学元件和半导体芯片的性能。此前，我国缺乏国家级圆度量值溯源源头，制约了高端制造业发展。该装置现为圆度测量校准提供了可靠基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/0/973/328.htm">ithome.com/0/973/328.htm</a></li>
<li><a href="https://tech.ifeng.com/c/8uXDDOGfHky">中国建成首套高精 度 圆 度 基准装置， 圆 度 测 量 不 确 定 度 从20nm降至6nm</a></li>

</ul>
</details>

**标签**: `#precision measurement`, `#metrology`, `#manufacturing`, `#China`, `#technology breakthrough`

---

<a id="item-5"></a>
## [中国天问二号抵达目标小行星](https://www.dw.com/zh/%E4%B8%AD%E5%9B%BD-%E5%A4%A9%E9%97%AE%E4%BA%8C%E5%8F%B7-%E6%8E%A2%E6%B5%8B%E5%99%A8%E6%8A%B5%E8%BE%BE%E7%9B%AE%E6%A0%87%E5%B0%8F%E8%A1%8C%E6%98%9F/a-77852932?maca=chi-rss-chi-all-1127-rdf) ⭐️ 8.0/10

中国天问二号探测器在历经 400 天、飞行 10 亿公里后，已抵达其目标——近地小行星 Kamo'oalewa（2016 HO3）。 这一里程碑标志着中国从月球和火星探测扩展到小行星采样返回，提升了其行星科学能力和全球太空雄心。 探测器现将在 20 公里距离上进行科学探测，计划采集样本并随后返回地球，之后还将与一颗彗星交会。

rss · DW Chinese · 7月6日 13:21

**背景**: 天问二号是中国继天问一号（火星轨道器和巡视器）之后的第二次行星探测任务。它于 2025 年 5 月 28 日发射，目标是地球的准卫星——小行星 Kamo'oalewa，进行采样返回。该任务还包括飞越彗星 311P/PANSTARRS。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dw.com/en/chinese-tianwen-2-space-probe-reaches-asteroid-for-sampling/a-77843539">Chinese Tianwen - 2 space probe reaches asteroid for sampling</a></li>
<li><a href="https://www.globaltimes.cn/page/202607/1365218.shtml">China 's Tianwen-2 probe reaches target asteroid ... - Global Times</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tianwen-2">Tianwen-2 - Wikipedia</a></li>

</ul>
</details>

**标签**: `#space exploration`, `#asteroid`, `#China`, `#Tianwen-2`

---

<a id="item-6"></a>
## [快速子宫内膜异位症检测将在 NHS 推出](https://www.theguardian.com/society/2026/jul/07/rapid-endometriosis-tests-to-be-made-available-on-nhs-in-england-and-wales) ⭐️ 8.0/10

两种快速诊断子宫内膜异位症的检测方法——唾液检测和基于肠道传感器的检测——将在英格兰和威尔士的 NHS 上提供，可能将诊断时间从数年缩短至数天。 子宫内膜异位症影响十分之一的育龄女性，但目前诊断平均需要 7-10 年；这些检测可以通过实现更早的治疗，显著改善数百万女性的生活质量。 唾液检测名为 Endotest，由法国生物技术公司 Ziwig 开发，分析 microRNA 生物标志物；肠道传感器检测使用 AI 解读消化道的肌电信号。

rss · The Guardian World · 7月7日 04:01

**背景**: 子宫内膜异位症是一种类似子宫内膜的组织在子宫外生长的疾病，导致慢性疼痛和不孕。目前的诊断通常需要腹腔镜手术，这是一种侵入性且昂贵的方法。这些非侵入性检测可以替代或分流手术需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/society/2026/jul/07/rapid-endometriosis-tests-to-be-made-available-on-nhs-in-england-and-wales">Rapid endometriosis tests to be made available on... | The Guardian</a></li>
<li><a href="https://ziwig.com/en/ziwig-endotest/">Ziwig Endotest, a saliva test for endometriosis</a></li>
<li><a href="https://endometriosis-centre.co.uk/the-science/">The Science behind the test</a></li>

</ul>
</details>

**标签**: `#healthcare`, `#medical technology`, `#endometriosis`, `#NHS`, `#diagnostics`

---

<a id="item-7"></a>
## [苏格兰提议暂停新建数据中心，挑战英国 AI 战略](https://www.theguardian.com/uk-news/2026/jul/07/scotland-could-freeze-datacentre-projects-in-challenge-to-uks-ai-strategy) ⭐️ 8.0/10

苏格兰民族党全国委员会通过了一项动议，要求冻结苏格兰所有新建数据中心项目，苏格兰政府目前正在考虑该提案。 这一暂停令可能削弱英国 AI 战略的关键支柱——该战略依赖于扩展数据中心基础设施，并可能阻碍苏格兰的科技投资。 该动议于 2026 年 7 月 5 日通过，并已提交苏格兰政府审议；苏格兰绿党对此表示欢迎，而批评者警告苏格兰可能损失数十亿英镑的投资。

rss · The Guardian World · 7月6日 23:01

**背景**: 数据中心对于 AI 开发至关重要，提供训练和运行 AI 模型所需的计算能力。英国政府将数据中心扩张作为其 AI 战略的重点，但对能源消耗和电网压力的担忧导致苏格兰出现反对声音。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/uk-news/2026/jul/07/scotland-could-freeze-datacentre-projects-in-challenge-to-uks-ai-strategy">Scotland could freeze datacentre projects in challenge... | The Guardian</a></li>
<li><a href="https://www.heraldscotland.com/news/26257521.scotland-risks-losing-billions-ai-centre-ban-put-place/">' Scotland risks losing billions' if AI data centre ban put in place</a></li>
<li><a href="https://wealthhealthself.com/scotlands-bold-move-on-data-centers-is-this-the-next-energy-war-investors-cant-ignore/">Scotland ’s Bold Move on Data Centers : Is This the Next Energy War...</a></li>

</ul>
</details>

**标签**: `#datacenters`, `#AI strategy`, `#policy`, `#Scotland`, `#UK`

---

<a id="item-8"></a>
## [首次 AI 勒索攻击仍需人类参与](https://techcrunch.com/2026/07/06/the-first-ai-run-ransomware-attack-still-needed-a-human/) ⭐️ 8.0/10

AI 代理首次完整执行了勒索软件攻击链，但人类仍负责选择受害者、搭建基础设施并提供窃取的凭证。 这标志着 AI 驱动网络犯罪的一个重要里程碑，但人类的参与表明完全自主的攻击尚未成为现实，从而缓和了此前的炒作。 该活动被命名为 JadePuffer，由 Sysdig 的研究人员发现，使用了 AI 代理来自动化整个攻击过程，从侦察到加密。

rss · TechCrunch · 7月6日 23:56

**背景**: 传统的勒索软件攻击在每个阶段都需要人工操作。AI 代理是能够自主执行任务的软件程序，它们在网络犯罪中的使用引发了新的安全担忧。JadePuffer 攻击表明，虽然 AI 可以处理技术执行，但在受害者选择等关键决策上仍需人工输入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.trolleyesecurity.com/articles-news-jadepuffer-ransomware-ai-agent-attack/">JadePuffer Ransomware Let an AI Agent Run the Entire Attack , Start...</a></li>

</ul>
</details>

**标签**: `#AI`, `#cybersecurity`, `#ransomware`, `#autonomous attacks`

---

<a id="item-9"></a>
## [2026 年科技公司因 AI 裁员](https://techcrunch.com/2026/07/06/the-running-list-major-tech-layoffs-in-2026-where-employers-cited-ai/) ⭐️ 8.0/10

TechCrunch 发布了一份 2026 年主要科技公司裁员的持续更新清单，这些公司在裁员时明确将 AI 列为原因之一，记录了这一重要的行业趋势。 这份清单凸显了 AI 的采用如何直接影响科技行业的就业，标志着劳动力需求的转变，可能影响成千上万的员工。 该清单按时间倒序排列，仅包含 2026 年宣布大规模裁员且明确将 AI 列为原因的较大型科技公司。

rss · TechCrunch · 7月6日 18:35

**背景**: 近年来，科技公司不断增加对 AI 的投资，导致以前由人类完成的任务实现自动化。这引发了关于岗位被取代的担忧，而 2026 年似乎是许多公司围绕 AI 能力重组员工队伍的一年。

**标签**: `#AI`, `#layoffs`, `#tech industry`, `#labor market`

---

<a id="item-10"></a>
## [前大疆工程师获数亿融资，打造消费级纺织机](https://36kr.com/p/3876837605585160?f=rss) ⭐️ 7.0/10

浪爪智能（CLAWLAB）由前大疆工程师胡文鑫创立，推出了一款消费级智能纺织工作站，可自动完成从设计到成品的编织过程。该公司已从红杉资本、顺为资本和米哈游等机构获得数轮超亿元融资。 这标志着在长期被忽视的家用纺织机市场中罕见的硬件创新，有望释放庞大的 DIY 社区潜力。其 AI 驱动的设计到制造流程可能降低个性化纺织品创作的门槛，类似于 3D 打印对制造业的民主化影响。 该纺织工作站使用自研 AI Agent，将用户草图或照片转换为编织版型，无需专业制版。公司首款产品自动簇绒枪作为市场验证工具，两年内创造了近亿元营收。

rss · 36Kr Feed · 7月7日 02:29

**背景**: 家用编织机在 1990 年代曾流行，但依赖纯机械操作且需要熟练的手工制版。浪爪智能的方法结合了机器人控制、运动规划和计算机图形学，将整个编织过程数字化，解决了该领域缺乏开源算法和数据集的难题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://36kr.com/p/3876837605585160">36kr.com/p/3876837605585160</a></li>
<li><a href="https://www.geekpark.net/news/218760">妈妈不在谁来给你 织 毛衣？ 这个 智 能 纺 织 机 来帮你 | 极客公园</a></li>

</ul>
</details>

**标签**: `#hardware`, `#textile`, `#startup`, `#funding`, `#consumer-electronics`

---

<a id="item-11"></a>
## [前西门子、罗罗团队创业，获数千万元融资打造航空电驱系统](https://36kr.com/p/3883721315971078?f=rss) ⭐️ 7.0/10

开普动能，一家由前西门子和罗尔斯-罗伊斯电动航空工程师创立的中国初创公司，已完成数千万元人民币的种子轮和天使轮融资，用于开发航空电驱系统。公司计划今年推出第一代技术验证样机，并于 2025 年第一季度发布具备试飞能力的样机。 电驱系统是 eVTOL 飞行器中技术壁垒最高的核心部件，占整机成本的 30-40%。开普动能的深厚航空经验有望加速高端电驱系统的国产替代，目前该领域严重依赖进口。 该团队参与了超过 20 个电动飞行平台，样机功率覆盖 30kW 至 2MW，累计超过 1500 架次电动飞行经验。公司同时瞄准 UAM（eVTOL）和 RAM（区域空中交通）市场，初期重点布局 eVTOL。

rss · 36Kr Feed · 7月6日 05:26

**背景**: eVTOL（电动垂直起降飞行器）需要高功率密度、高可靠性的电驱系统，并须通过 DO-178C 和 DO-254 等严苛的航空认证。轻量化、高性能和高可靠性的“不可能三角”是核心挑战。目前，中国中高端航空电驱部件国产化率较低，许多关键部件仍依赖进口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dewesoft.com/blog/evtol-guide">A Complete Guide to eVTOL | Dewesoft</a></li>
<li><a href="https://uk.mathworks.com/solutions/aerospace-defense/certification-standards.html">Certification Standards - MATLAB & Simulink</a></li>
<li><a href="https://www.honeywellaerospace.com/us/en/about-us/blogs/electric-aircraft-propulsion-how-it-works">Electric Aircraft Propulsion and How it Works</a></li>

</ul>
</details>

**标签**: `#eVTOL`, `#electric aviation`, `#funding`, `#electric propulsion`, `#startup`

---

<a id="item-12"></a>
## [蚂蚁灵波发布空间感知模型 LingBot-Depth 2.0](https://36kr.com/newsflashes/3885019659202566?f=rss) ⭐️ 7.0/10

7 月 7 日，蚂蚁集团旗下具身智能公司灵波科技发布了空间感知模型 LingBot-Depth 2.0，该模型基于 1.5 亿数据样本训练，并同步推出了视觉基座模型 LingBot-Vision。 此次发布提升了机器人在边缘清晰度、细小物体识别、远距离深度估计以及复杂场景鲁棒性等方面的视觉能力，解决了具身智能和空间感知领域的核心挑战。 LingBot-Depth 2.0 是一种面向真实场景的深度补全模型，依托奥比中光 Gemini 330 系列双目 3D 相机和深度引擎芯片进行数据采集与验证。LingBot-Vision 作为视觉基座模型，构建了机器人从“看懂”到“看准”的能力链路。

rss · 36Kr Feed · 7月7日 03:26

**背景**: 空间感知模型使机器人能够从 2D 图像理解 3D 环境，这对于导航和操作等任务至关重要。LingBot-Depth 将含噪且不完整的传感器深度数据优化为干净、稠密且具备真实尺度的三维测量结果，从而提升下游视觉任务的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.infoq.cn/article/mqY10ihiZ874id2JDeXu">1.5亿数据！ 蚂蚁灵波发布 空 间 感 知 模 型 LingBot - Depth ... - InfoQ</a></li>
<li><a href="https://finance.sina.cn/tech/2026-01-28/detail-inhivvyy4951308.d.html?fromtech=1&vt=4">蚂蚁灵波 LingBot - Depth 空 间 感 知 模 型 、LingBot-VLA... | 手机新浪网</a></li>
<li><a href="https://developer.aliyun.com/article/1708922">蚂蚁正式开源 LingBot - Depth ...</a></li>

</ul>
</details>

**标签**: `#具身智能`, `#空间感知`, `#机器人视觉`, `#AI模型`, `#蚂蚁集团`

---

<a id="item-13"></a>
## [支付宝 AI 开放平台开启邀测](https://36kr.com/newsflashes/3884959785234689?f=rss) ⭐️ 7.0/10

7 月 7 日，支付宝正式上线 AI 开放平台并开启邀测，商家和开发者可通过其 AI 助手“阿宝”接入 AI 能力，并实现手机、车机、AI 眼镜、IoT 等多终端跨端互联。 此举使支付宝成为中国 AI 生态的关键参与者，让商家无需从零开发即可利用 AI 能力，并触达支付宝 10 亿用户，有望加速金融科技等领域 AI 应用落地。 该平台支持将现有小程序、API 接口和服务能力升级为 AI 可调用的 MCP、Skill 或 Agent 格式，并提供多终端分发的统一管理，且不影响支付宝现有小程序服务。

rss · 36Kr Feed · 7月7日 02:25

**背景**: 支付宝是中国领先的移动支付和数字生活平台。AI 开放平台利用支付宝在身份核验、支付安全和风险防控方面的能力，为 AI 服务提供安全可信的基础设施。MCP（模型上下文协议）是一种允许 AI 模型与外部工具和服务交互的协议。

**标签**: `#AI`, `#Fintech`, `#Alipay`, `#Platform Launch`

---

<a id="item-14"></a>
## [AI 演员 Tilly Norwood 将主演首部电影《Misaligned》](https://www.ithome.com/0/973/436.htm) ⭐️ 7.0/10

由英国制作公司 Particle6 的 AI 部门 Xicoia 创造的 AI 演员 Tilly Norwood 将主演她的首部电影《Misaligned》，这是一部探讨身份认同和 AI 恐惧的喜剧剧情片。影片设定在一个超现实数字世界，由传统电影人与 AI 专家合作制作。 这则新闻凸显了 AI 生成演员与人类演员之间日益紧张的矛盾，美国演员工会 SAG-AFTRA 强烈反对像 Tilly Norwood 这样的合成演员。这部电影可能为 AI 在创意产业中的应用开创先例，引发伦理和劳工方面的担忧。 Tilly Norwood 是由 Particle6 推出的 AI 人才工作室 Xicoia 创造的超写实数字角色。SAG-AFTRA 谴责她是未经同意利用真实演员表演训练的“合成表演者”，而创作者则辩护称她是一件能引发讨论的艺术品。

rss · ITHome Feed · 7月7日 03:16

**背景**: AI 生成演员是利用机器学习在大量人类表演数据上训练出的数字角色。美国最大的演员工会 SAG-AFTRA 一直公开反对这类合成表演者，认为它们威胁就业并贬低人类艺术价值。电影《Misaligned》设定在虚构的“Tilly 宇宙”中，AI 主角在其中挣扎于身份认同和剥削问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/film/2025/sep/30/tilly-norwood-ai-actor-hollywood">Tilly Norwood : how scared should we be of the viral AI ‘ actor ’? | Film</a></li>
<li><a href="https://vocal.media/geeks/sag-aftra-pushes-back-on-controversial-ai-actress-tilly-norwood-no-emotion-no-human-experience">SAG - AFTRA Pushes Back on Controversial AI Actress Tilly Norwood...</a></li>
<li><a href="https://deadline.com/2025/09/eline-van-der-velden-particle6-ai-talent-studio-xicoia-1236555680/">Founder Of AI Indie Particle 6 Launches New AI Talent Studio Xicoia</a></li>

</ul>
</details>

**标签**: `#AI`, `#ethics`, `#entertainment`, `#labor`, `#synthetic actors`

---

<a id="item-15"></a>
## [新加坡在英伟达芯片案中追加洗钱指控](https://www.rfi.fr/cn/%E4%BA%9A%E6%B4%B2/20260706-%E6%B6%89%E8%99%9A%E6%8A%A5%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%8E%BB%E5%90%91-%E6%96%B0%E5%8A%A0%E5%9D%A1%E6%A3%80%E6%96%B9%E5%9C%A8%E8%8B%B1%E4%BC%9F%E8%BE%BE%E8%8A%AF%E7%89%87%E6%A1%88%E4%B8%AD%E6%8F%90%E5%87%BA%E6%96%B0%E6%8C%87%E6%8E%A7) ⭐️ 7.0/10

新加坡检方对一起涉及虚报 AI 服务器去向的案件的关键嫌疑人追加了洗钱指控，这是遏制英伟达芯片非法转运至中国行动的一部分。 这一进展凸显了对规避美国先进 AI 芯片出口管制的法律打击力度加大，可能扰乱供应链并增加科技公司的合规成本。 该案涉及虚报服务器去向以掩盖英伟达 AI 芯片非法转运至中国的行为，此前据报道至少有价值 10 亿美元的芯片被走私。

rss · RFI Chinese · 7月6日 15:52

**背景**: 美国自 2022 年起对向中国出口先进英伟达芯片实施限制，导致走私行为出现。新加坡作为主要科技中心，成为关键转运点，促使当地当局采取执法行动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://qz.com/nvidia-ai-chips-worth-one-billion-smuggled-into-china-">Nvidia AI chips worth $1 billion smuggled into China : report</a></li>
<li><a href="https://www.bbc.com/news/articles/cedy6gl99eno">Nvidia , the chip giant caught between the US and China</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#AI chips`, `#supply chain`, `#geopolitics`, `#legal`

---

<a id="item-16"></a>
## [熊蜂面部表情显示“喜欢”和“不喜欢”](https://www.theguardian.com/environment/2026/jul/07/bees-emotion-like-behaviour-liking-disliking-inner-lives) ⭐️ 7.0/10

一项发表在《美国国家科学院院刊》上的研究使用慢动作视频捕捉到熊蜂的面部运动，例如在品尝甜食后伸出舌头（glossa），以及在尝到不喜欢的味道后摇头，这些行为与哺乳动物中观察到的“喜欢”和“不喜欢”反应一致。 这项研究为昆虫感知提供了新证据，表明蜜蜂可能拥有内心生活和情感状态，这可能对动物福利政策以及我们对跨物种意识的理解产生重要影响。 该研究分析了熊蜂对甜水和普通水的面部表情反应，发现了明显的可测量运动，如伸舌（喜欢）和摇头（不喜欢）。研究人员指出，虽然这些行为类似于哺乳动物的情绪表达，但并不一定证明有意识的情绪。

rss · The Guardian World · 7月6日 19:00

**背景**: 昆虫感知是指昆虫拥有主观体验（如痛苦或快乐）的能力。历史上，昆虫被认为只是简单的反射机器，但最近的研究揭示了它们复杂的行为，如学习、记忆，甚至可能的情感。glossa 是蜜蜂用来摄取花蜜的管状舌头。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.newscientist.com/article/2533149-bumblebee-facial-movements-give-clues-to-their-inner-lives/">Bumblebee facial movements give clues to their inner... | New Scientist</a></li>
<li><a href="https://www.djournal.com/news/national/bumblebees-show-emotions-through-facial-expressions-just-like-mammals/article_c1dc1d20-be58-5f33-9715-f583f22d1532.html">Bumblebees show emotions through facial expressions just like...</a></li>
<li><a href="https://www.archyde.com/do-bumblebees-have-inner-lives-facial-expressions-reveal-preferences/">Do Bumblebees Have Inner Lives? Facial Expressions Reveal...</a></li>

</ul>
</details>

**标签**: `#animal cognition`, `#insect sentience`, `#behavioral science`, `#bumblebees`, `#emotion`

---

<a id="item-17"></a>
## [Vercel CEO 谈将 AI 模型与智能体分离](https://techcrunch.com/2026/07/06/vercel-ceo-guillermo-rauch-on-the-fight-to-split-off-models-from-agents/) ⭐️ 7.0/10

Vercel 首席执行官 Guillermo Rauch 认为，将 AI 模型与智能体分离对于生产优化至关重要，重点在于价格/性能的权衡。 这场架构辩论直接影响企业如何在生产中部署 AI，影响成本、延迟和可扩展性。作为领先平台提供商的 CEO，Rauch 的观点预示着行业方向。 Rauch 强调，在为生产优化时，团队必须评估价格/性能，而不是将模型和智能体视为一体。Vercel 自己的框架 'Eve' 通过将智能体能力映射到文件和文件夹来实现这种分离。

rss · TechCrunch · 7月6日 19:49

**背景**: AI 智能体是使用模型执行任务的自主系统，而模型是底层的神经网络。在生产中，将它们紧密捆绑可能导致效率低下。Vercel 的 Eve 框架将智能体视为一个目录，将运行时（由 Vercel 拥有）与认知内容（由开发者拥有）分离。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://yage.ai/share/vercel-eve-agent-directory-en-20260618.html">Vercel open-sources eve: why "an agent is a directory" is not...</a></li>
<li><a href="https://pub.towardsai.net/vercel-turned-its-file-routing-trick-into-an-ai-agent-framework-e09ff9865d03">Vercel Turned Its File-Routing Trick Into an AI Agent ... | Towards AI</a></li>

</ul>
</details>

**标签**: `#AI`, `#ML`, `#production`, `#agents`, `#Vercel`

---

<a id="item-18"></a>
## [虚假实习内推黑产链条曝光：5000 余份 offer 全是假的](https://www.chinanews.com.cn/sh/2026/07-07/10654207.shtml) ⭐️ 6.0/10

一项调查揭露了一条黑产链条，该链条出售了超过 5000 份来自知名企业的虚假实习内推机会，收取服务费并提供伪造的实习证明。 这种欺诈行为破坏了求职市场的信任，既损害了为虚假机会付费的求职者，也损害了被冒用声誉的公司。 该骗局承诺提供知名公司的线上实习内推，声称轻松完成任务即可获得实习证明，但所有 offer 均为伪造。

rss · China News Service Scroll · 7月7日 03:44

**背景**: 实习内推常被视为进入顶级公司的捷径，导致一些求职者向中介付费。此案凸显了此类未经核实服务的风险。

**标签**: `#fraud`, `#internship`, `#job market`, `#ethics`

---

<a id="item-19"></a>
## [研究生培养不能一刀切](https://www.chinanews.com.cn/edu/2026/07-07/10654106.shtml) ⭐️ 4.0/10

一篇评论文章指出，研究生培养应采用多元评价标准，而非单一的统一尺度。 这一讨论凸显了研究生项目需要个性化培养路径，可能影响大学设计课程和评估学生的方式。 文章批评了当前对所有研究生使用相同标准的趋势，无论其领域或职业目标如何。

rss · China News Service Scroll · 7月7日 03:22

**背景**: 研究生教育通常包括高级课程和研究。一刀切的方法可能忽视不同学科学生的多样化需求。

**标签**: `#education`, `#graduate studies`, `#opinion`

---

<a id="item-20"></a>
## [中国高校为 AI 时代改革创业课程](https://www.chinanews.com.cn/edu/2026/07-07/10654113.shtml) ⭐️ 3.0/10

中国高校正在更新创业课程，要求学生实际创办公司作为期末作业，并邀请真实投资人担任考官。 这一转变反映了 AI 对商业和教育日益增长的影响，旨在让学生更好地应对 AI 时代的真实创业挑战。 文章提到课程改革包括实际创办公司和投资人评估，但未提供具体高校、日期或技术细节。

rss · China News Service Scroll · 7月7日 03:29

**背景**: 中国传统的创业课程通常侧重于理论和商业计划书撰写。新方法强调实践经验以及来自行业专业人士的直接反馈，以适应快速变化的 AI 环境。

**标签**: `#education`, `#entrepreneurship`, `#AI`

---

<a id="item-21"></a>
## [中国红十字会向广西台风灾区运送救灾物资](https://www.chinanews.com.cn/sh/2026/07-07/10654214.shtml) ⭐️ 2.0/10

中国红十字会总会向遭受台风“美莎克”严重影响的广西地区紧急调拨了 5000 个赈济家庭包，物资已抵达并开始分发。 此次调拨为受灾转移群众提供了基本生活保障，体现了人道主义援助在自然灾害应对中的重要作用。 救灾物资包括 5000 个赈济家庭包，每个包含临时安置和生活必需品。此次行动由中国红十字会总会协调。

rss · China News Service Scroll · 7月7日 04:17

**背景**: 2026 年的台风“美莎克”对广西造成严重破坏，导致大规模人员转移。中国红十字会常在灾害发生时提供紧急救援，向受灾群众分发标准化的家庭包。

**标签**: `#humanitarian aid`, `#disaster relief`, `#China`

---

<a id="item-22"></a>
## [甘肃山体滑坡后，自然资源部启动地质灾害防御Ⅲ级响应](https://www.chinanews.com.cn/gn/2026/07-07/10654213.shtml) ⭐️ 2.0/10

7 月 7 日，甘肃省陇南市宕昌县一林区发生山体滑坡，致多人被埋。自然资源部于当日 9 时启动地质灾害防御Ⅲ级响应，并派工作组赴现场指导抢险救援。 此次响应表明地质灾害的严重性以及政府为减少人员伤亡而迅速动员。这凸显了在易发生山体滑坡的山区，灾害防备和响应机制的重要性。 Ⅲ级响应是中国地质灾害防御四级体系中的第三高级别。自然资源部依据《自然资源部地质灾害防御响应工作方案》协调行动。

rss · China News Service Scroll · 7月7日 04:04

**背景**: 中国地质灾害防御响应体系分为四级：Ⅰ级（最严重）至Ⅳ级。Ⅲ级响应针对需要省级和国家协调的重大灾害启动。自然资源部牵头响应，向受灾地区派遣专家和资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.bjd.com.cn/2025/07/27/11248736.shtml">北京 地 质 灾 害 防 御 级 响 应 ！ 洪涝 灾 害 后，记住这些 防 护要点_京报网</a></li>
<li><a href="https://m.jiemian.com/article/14437670_microcontent.html">自然资源部对湖北、贵州启动 地 质 灾 害 防 御 级 响 应 | 界面新闻</a></li>
<li><a href="https://static.cdsb.com/micropub/Articles/202606/6c15f913267faaa3f5b8d6dfff27e359.html">自 然 资 源 部 对安徽湖北湖南贵州启动 地 质 灾 害 防 御 级 响 应</a></li>

</ul>
</details>

**标签**: `#natural disaster`, `#geological hazard`, `#China`

---

<a id="item-23"></a>
## [中国暑期旅游市场列车航班加密供需两旺](https://www.chinanews.com.cn/life/2026/07-07/10654181.shtml) ⭐️ 2.0/10

中国铁路和民航部门加密了旅游列车和特色航线航班，以应对暑期出行需求的激增。 这反映了中国国内旅游业的强劲复苏，表明消费者出行信心增强，有望带动酒店、零售等相关行业。 报道提到“旅游列车频发”和“特色航线加密”，但未提供具体数量或航线信息。

rss · China News Service Scroll · 7月7日 04:01

**背景**: 夏季是中国传统的出行旺季，受学校假期和宜人天气推动。政府通常会调整运力以应对客流高峰。

**标签**: `#travel`, `#tourism`, `#China`

---

<a id="item-24"></a>
## [盲盒消费投诉：销售、质量、退货问题](https://www.chinanews.com.cn/sh/2026/07-07/10654176.shtml) ⭐️ 2.0/10

一篇新闻报道追踪了中国盲盒销售中的消费者投诉，重点指出了限购措施失效、产品质量差以及退货困难等问题。 这很重要，因为盲盒在中国是一种流行的消费品，这些问题影响消费者权益和市场信任。 报道提到了具体问题：商店不遵守购买限制、产品存在质量缺陷以及商家拒绝退货请求。

rss · China News Service Scroll · 7月7日 03:58

**背景**: 盲盒是装有随机玩具或收藏品的密封盒子，类似于电子游戏中的战利品箱。它们在中国已成为一个价值数十亿美元的产业，但因类似赌博的机制和消费者保护问题而面临监管审查。

**标签**: `#consumer issues`, `#blind boxes`, `#China news`

---

<a id="item-25"></a>
## [汛期出行提示：全国公路、铁路、水路最新动态](https://www.chinanews.com.cn/sh/2026/07-07/10654210.shtml) ⭐️ 2.0/10

交通运输部维持强降雨二级防御响应，本报道详细说明了当前汛情对公路、铁路、水路出行的具体影响，包括最新路况、运力调整和出行保障情况。 这一更新对中国汛期出行者至关重要，它提供了关于交通中断和安全措施的实时信息，帮助公众规划行程并避开危险。 报道涵盖了最新路况、铁路运力调整和水路服务变化，但未包含中断的具体数字或技术细节。

rss · China News Service Scroll · 7月7日 03:50

**背景**: 中国的汛期通常为 6 月至 8 月，暴雨可能导致洪水、山体滑坡和交通中断。交通运输部采用分级应急响应机制，二级响应表示情况严重，需要协调行动。

**标签**: `#transportation`, `#weather`, `#news`

---

<a id="item-26"></a>
## [A 股午评：普跌行情，板块分化](https://www.chinanews.com.cn/cj/2026/07-07/10654206.shtml) ⭐️ 2.0/10

超 4700 只个股下跌，三大指数集体收跌，科创 50 收涨；贵金属、券商下跌，半导体硅片、GPU 概念活跃，工程机械上涨。 这份午评反映了市场整体疲软但存在结构性机会，可能影响散户和机构投资者的短期交易决策。 科创 50 逆势上涨，半导体硅片和 GPU 概念交易活跃，表明尽管整体下跌，投资者对科技相关板块仍有兴趣。

rss · China News Service Scroll · 7月7日 03:41

**背景**: A 股是指在中国上海和深圳证券交易所上市的公司股票，以人民币交易。午评提供交易时段的市场表现快照，常影响下午的交易情绪。

**标签**: `#stock market`, `#finance`, `#China`

---

<a id="item-27"></a>
## [近视手术并非人人适合](https://www.chinanews.com.cn/life/2026/07-07/10654120.shtml) ⭐️ 2.0/10

一家中国新闻媒体发布提醒，指出并非所有人都适合接受近视手术，强调术前全面评估的必要性。 这一提醒有助于公众了解近视手术有严格的适应症，可能避免不必要的风险和过高的期望。 文章未具体说明禁忌症，而是作为一般健康建议。它可能针对那些未经过适当医疗咨询就考虑激光眼科手术的人群。

rss · China News Service Scroll · 7月7日 03:36

**背景**: 近视手术（如 LASIK）通过重塑角膜来矫正近视。但候选人必须满足稳定度数、足够角膜厚度和无活动性眼病等条件。许多人并不了解这些要求。

**标签**: `#health`, `#myopia surgery`, `#public awareness`

---

<a id="item-28"></a>
## [体检前的常见错误](https://www.chinanews.com.cn/life/2026/07-07/10654117.shtml) ⭐️ 2.0/10

最近一篇文章指出了人们在体检前常犯的错误，例如空腹超过 16 小时或未经医生建议擅自停药。 这些错误可能导致检测结果不准确，进而引发误诊或不必要的焦虑。了解正确的准备方法有助于确保健康评估的可靠性。 文章特别警告不要空腹时间过长（超过 16 小时）以及未经医嘱擅自停用处方药，因为这两者都可能影响化验结果。

rss · China News Service Scroll · 7月7日 03:35

**背景**: 体检常需空腹以确保血糖和血脂检测的准确性。但过度禁食会引发代谢变化，导致结果失真。同样，突然停用降压药或降糖药等药物可能引起危险的指标波动。

**标签**: `#health`, `#medical checkup`, `#lifestyle`

---