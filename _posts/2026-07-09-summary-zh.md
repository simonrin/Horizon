---
layout: default
title: "Horizon Summary: 2026-07-09 (ZH)"
date: 2026-07-09
lang: zh
---

> 从 376 条内容中筛选出 28 条重要资讯。

---

1. [TypeScript 7.0 发布，通过 Go 重写实现 10 倍速度提升](#item-1) ⭐️ 9.0/10
2. [国家医保局曝光药企伪造医生联名信干扰集采](#item-2) ⭐️ 8.0/10
3. [陈立泉获国家最高科技奖，引领中国锂电池领跑世界](#item-3) ⭐️ 8.0/10
4. [贲德获 2025 年度国家最高科学技术奖](#item-4) ⭐️ 8.0/10
5. [蚂蚁灵波开源实时世界模型 LingBot-World 2.0](#item-5) ⭐️ 8.0/10
6. [国家超算互联网核心节点正式上线](#item-6) ⭐️ 8.0/10
7. [华为确认 2025 年实现高速 L3，欢迎特斯拉 FSD 入华](#item-7) ⭐️ 8.0/10
8. [首次直接观测到海底扩张过程](#item-8) ⭐️ 8.0/10
9. [OpenAI 发布全双工语音模型，支持实时翻译](#item-9) ⭐️ 8.0/10
10. [昇视唯盛完成数亿元 B 轮融资，打造智能焊接机器人](#item-10) ⭐️ 7.0/10
11. [物理 AI 公司深度智控获数亿元融资，打造能源基础设施大脑](#item-11) ⭐️ 7.0/10
12. [泽塔聚变完成数亿元天使轮融资](#item-12) ⭐️ 7.0/10
13. [内存短缺推动 DDR4 和 DDR3 价格飙升](#item-13) ⭐️ 7.0/10
14. [英特尔 Arc Pro B70 在 AI 推理中达 2320.76 token/s，超越 RTX 5090D](#item-14) ⭐️ 7.0/10
15. [法国监管机构警告 Meta 支付新闻使用费](#item-15) ⭐️ 7.0/10
16. [中国工信部警告 Claude Code 存在安全漏洞](#item-16) ⭐️ 7.0/10
17. [美国议员调查美企日益使用中国 AI 模型](#item-17) ⭐️ 7.0/10
18. [研究：澳大利亚在售儿童沙释放石棉纤维](#item-18) ⭐️ 7.0/10
19. [EmTech AI 2026 聚焦 AI 平台崛起](#item-19) ⭐️ 7.0/10
20. [NHTSA 要求自动驾驶公司停止干扰急救人员](#item-20) ⭐️ 7.0/10
21. [中国极端天气风险远超认知与基础设施应对能力](#item-21) ⭐️ 6.0/10
22. [魏炳波院士三十余载“造锅煮饭”助力中国空间材料科学](#item-22) ⭐️ 6.0/10
23. [上海芯片初创企业沐曦与曦智取得里程碑](#item-23) ⭐️ 5.0/10
24. [青海 50MW 光热电站四年发电 5.82 亿千瓦时](#item-24) ⭐️ 5.0/10
25. [两院院士热议“科技三会”指明方向](#item-25) ⭐️ 5.0/10
26. [2025 年度国家科技奖呈现新特点](#item-26) ⭐️ 4.0/10
27. [海南自贸港样板间推进教育科技人才一体发展](#item-27) ⭐️ 3.0/10
28. [雄安新区启动全域通办政务服务](#item-28) ⭐️ 3.0/10

---

<a id="item-1"></a>
## [TypeScript 7.0 发布，通过 Go 重写实现 10 倍速度提升](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) ⭐️ 9.0/10

微软宣布 TypeScript 7.0 正式版发布，该版本将编译器完全用 Go 语言重写，在 VS Code 等大型代码库上实现了高达 11.9 倍的速度提升。 这一巨大的性能提升使 TypeScript 在大型项目上显著加快，将构建时间从分钟级缩短到秒级，从而提升开发者生产力并促进更广泛的采用。 Go 移植版是对现有 TypeScript 代码库的忠实翻译，保持了与 6.0 版本的语义兼容性，并通过了十年积累的测试套件。编译器现在利用原生代码速度和共享内存并行处理。

hackernews · DanRosenwasser · 7月8日 16:06 · [社区讨论](https://news.ycombinator.com/item?id=48833715)

**背景**: TypeScript 是 JavaScript 的超集，添加了可选的静态类型检查，帮助开发者尽早发现错误。之前的编译器本身是用 TypeScript 编写的，在大型代码库上可能较慢。通过用 Go（一种具有高效并发能力的编译语言）重写，微软实现了巨大的速度提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/">Announcing TypeScript 7.0 - TypeScript - devblogs.microsoft.com</a></li>
<li><a href="https://devblogs.microsoft.com/typescript/typescript-native-port/">A 10x Faster TypeScript - TypeScript - devblogs.microsoft.com</a></li>
<li><a href="https://github.com/microsoft/typescript-go">GitHub - microsoft/typescript-go: Staging repo for ...</a></li>

</ul>
</details>

**社区讨论**: 社区反应极为积极，许多人称赞团队的工程壮举。一些用户对性能提升表示兴奋，并指出在过渡期间维护两个代码库的难度。还有少数用户对 JSDoc 类型语法的持续支持表示赞赏。

**标签**: `#TypeScript`, `#performance`, `#programming languages`, `#Microsoft`, `#compiler`

---

<a id="item-2"></a>
## [国家医保局曝光药企伪造医生联名信干扰集采](https://www.chinanews.com.cn/jk/2026/07-09/10655783.shtml) ⭐️ 8.0/10

2026 年 7 月 7 日，国家医保局披露某进口原研药企伪造了一份由 31 家医院 78 名医生联署的专家建议函，试图影响第 12 批集采的品种遴选。诺华、雅培、拜耳已对此作出回应。 该事件直接损害了中国药品集中带量采购制度的公正性，该制度旨在通过公平竞争降低药价。这可能会削弱公众对集采流程以及在中国运营的跨国药企的信任。 国家医保局未点名具体药企，但指出伪造函件旨在影响第 12 批集采定品的专家咨询环节。诺华、雅培、拜耳三家公司均已发表声明，否认参与或承诺配合调查。

rss · China News Service Scroll · 7月9日 03:26

**背景**: 中国的药品集中带量采购（集采）是一种基于采购量的招标项目，通过承诺大量采购量来压低中标药价。流程中包括专家咨询环节以遴选适宜药品。原研药是指拥有专利的创新药，仿制药则是价格更低的仿制品；自 2018 年以来，集采已大幅降低药品费用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ailegal.baidu.com/legalarticle/qadetail?id=619c08a931966a250219">国家医保集采步骤讲解-法行宝-法律解答</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/81815954676">国家医保集采流程了解 - 知乎专栏</a></li>
<li><a href="https://news.qq.com/rain/a/20251013A07UYF00">原研药和仿制药，效果一样吗？_腾讯新闻</a></li>

</ul>
</details>

**标签**: `#pharmaceutical regulation`, `#centralized procurement`, `#healthcare policy`, `#ethics`, `#China`

---

<a id="item-3"></a>
## [陈立泉获国家最高科技奖，引领中国锂电池领跑世界](https://www.chinanews.com.cn/gn/2026/07-08/10655525.shtml) ⭐️ 8.0/10

中国科学院物理研究所院士陈立泉因在锂电池研究和产业化方面的开创性贡献，荣获 2025 年度国家最高科学技术奖。 该奖项表彰了陈立泉半个世纪的基础性工作，使中国在电动汽车电池生产领域领先全球，新能源汽车产销量连续 11 年保持全球第一。 陈立泉团队研制出中国第一块固态锂电池和第一块液态锂电池，并积极推动技术产业化。国家最高科学技术奖是中国最高科学荣誉，奖金为 800 万元。

rss · China News Service China · 7月8日 14:03

**背景**: 锂电池是可充电储能设备，广泛应用于电动汽车和电子产品。固态锂电池使用固态电解质代替液态电解质，具有更高的安全性和能量密度，但面临离子电导率低等挑战。陈立泉被誉为中国锂电池产业的奠基人和开拓者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/国家最高科学技术奖/621338">国家最高科学技术奖 - 百度百科 2025年度国家科学技术奖揭晓 - 中国科学技术协会 国家科学技术奖励工作办公室 - nosta.gov.cn 258项！2025年度国家科学技术奖，获奖数量揭晓_腾讯新闻 2025年度国家科学技术奖揭晓，陈立泉和贲德获最高奖，上海获奖数量创... Top Stories</a></li>
<li><a href="https://www.sohu.com/a/1047394357_120863305">258项获奖！两人获最高科技奖，2025年度国家科学技术奖揭晓</a></li>

</ul>
</details>

**标签**: `#lithium batteries`, `#China`, `#science award`, `#energy storage`, `#EV industry`

---

<a id="item-4"></a>
## [贲德获 2025 年度国家最高科学技术奖](https://www.chinanews.com.cn/gn/2026/07-08/10655524.shtml) ⭐️ 8.0/10

著名雷达专家贲德荣获 2025 年度国家最高科学技术奖，以表彰他在机载脉冲多普勒雷达、相控阵雷达和天基监视雷达技术方面的奠基性贡献。 该奖项凸显了中国在雷达技术方面的战略进步，这对国防和监视系统至关重要。贲德的工作显著提升了中国在陆海空天预警探测领域的能力。 贲德被誉为中国机载脉冲多普勒雷达的奠基者、相控阵雷达的主要开创者和天基监视雷达的先行者。他的贡献塑造了中国多域雷达预警探测体系的发展。

rss · China News Service China · 7月8日 14:01

**背景**: 脉冲多普勒雷达利用多普勒效应从杂波中检测运动目标，实现现代空战中的超视距交战。相控阵雷达通过电子方式控制波束指向，实现快速扫描和多目标跟踪。天基监视雷达部署在卫星上，用于全球监测。贲德的工作覆盖了这三个关键领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.qq.com/rain/a/20260708A04KI700">国家最高科技奖获得者贲德：为中国战机打造超视距“火眼金睛”</a></li>
<li><a href="https://baike.baidu.com/item/天基监视雷达新技术/22153837">天基监视雷达新技术_百度百科</a></li>

</ul>
</details>

**标签**: `#radar technology`, `#defense`, `#national award`, `#engineering`, `#surveillance`

---

<a id="item-5"></a>
## [蚂蚁灵波开源实时世界模型 LingBot-World 2.0](https://36kr.com/newsflashes/3887867035532038?f=rss) ⭐️ 8.0/10

蚂蚁灵波科技开源了 LingBot-World 2.0，这是一个实时交互世界模型，首次在世界模型中引入 Agent 机制，支持小时级实时生成和 720p/60fps 高清输出。 此次开源通过提供可自托管的高保真交互世界模型，显著推动了 AI 驱动的仿真和机器人训练，降低了游戏、影视预演、数字孪生和具身智能领域开发者和研究者的门槛。 LingBot-World 2.0 在 Apache 2.0 许可下完全开源，无需等待列表即可立即使用，并且可以自托管。它提供与 Genie 3 相当的能力，能够从简单输入生成交互式、符合物理规律的游戏环境，无需 3D 建模或资产管线。

rss · 36Kr Feed · 7月9日 03:42

**背景**: 世界模型是基于观察和动作预测环境动态的 AI 系统，是推理和规划的核心认知机制。Agent 机制使模型能够在模拟世界中自主探索和交互，使其适用于需要预测环境模型的具身 AI 智能体训练。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/robbyant/lingbot-world">GitHub - Robbyant/lingbot-world: Advancing Open-source World ...</a></li>
<li><a href="https://lingbot-world.net/">LingBot-World | Open Source World Model for Game Development ...</a></li>
<li><a href="https://www.lingbot-world.org/">LingBot-World | Open Source AI World Model - Free Deploy</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#world model`, `#robotics`, `#simulation`

---

<a id="item-6"></a>
## [国家超算互联网核心节点正式上线](https://36kr.com/newsflashes/3887797387344387?f=rss) ⭐️ 8.0/10

2026 年 7 月 9 日，国家超算互联网核心节点在郑州正式上线运行，可对外提供超过 10 万张国产 AI 加速卡算力，成为该平台接入的最大规模单体国产 AI 算力资源池。 这一里程碑显著提升了中国的国家计算基础设施，实现了全国异构算力资源的统一调度，并将资源利用率从不足 50%提升至满载，对大规模 AI 训练和科学计算至关重要。 该核心节点采用中科曙光的 scaleX 万卡超集群系统，支持多品牌国产加速卡混合部署，并可灵活扩展至十万卡甚至百万卡规模。它还集成了与河南省科学院联合研发的 6 万卡 AI for Science（科学智能）计算集群。

rss · 36Kr Feed · 7月9日 02:32

**背景**: 国家超算互联网是一项国家倡议，旨在连接全国的超算中心和智算中心，提供统一的计算服务。核心节点位于郑州，总建筑面积约 16 万平方米，作为资源调度和管理的运营枢纽。该节点于 2026 年 2 月 5 日启动试运行，截至 2026 年 5 月，平台已连接全国 30 余家超算与智算中心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.qq.com/rain/a/20260709A03VDU00">刚刚，国家超算互联网核心节点正式上线_腾讯新闻</a></li>
<li><a href="https://www.scnet.cn/home/subject/hxjd/index.html">国家超算互联网核心节点 - 超算互联网</a></li>
<li><a href="https://baike.baidu.com/item/国家超算互联网核心节点/63648019">国家超算互联网核心节点 - 百度百科</a></li>

</ul>
</details>

**标签**: `#supercomputing`, `#AI infrastructure`, `#China`, `#national computing`, `#HPC`

---

<a id="item-7"></a>
## [华为确认 2025 年实现高速 L3，欢迎特斯拉 FSD 入华](https://www.ithome.com/0/974/346.htm) ⭐️ 8.0/10

华为智能驾驶解决方案产品线总裁李文广确认，从技术上讲，明年高速场景即可进入 L3 自动驾驶时代，今年将进行试点，随后常态化准入。他还表示特别欢迎特斯拉 FSD 入华同场竞技。 这标志着中国自动驾驶竞赛的一个重要里程碑，华为计划在 2025 年实现高速 L3 商业化，可能加速行业普及。对特斯拉 FSD 的欢迎凸显了华为的信心以及对订阅制商业模式的推动。 华为明年在自动驾驶领域的投入将超过 200 亿元，今年下半年发布的部分高端车型将为高速 L3 进行硬件预埋。李文广还透露，华为正与三大保险公司合作推出泊车权益和智驾权益。

rss · ITHome Feed · 7月9日 02:13

**背景**: L3 级自动驾驶允许系统在特定场景（如高速）下接管驾驶，但驾驶员需随时准备接管。华为乾崑智驾 ADS 是中国领先的自动驾驶系统，已搭载于超过 170 万辆汽车，最新版本采用云端世界引擎与车端世界行为模型架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/1912622682484220704">华为乾崑ADS智驾方案简析 - 知乎</a></li>
<li><a href="https://www.163.com/dy/article/KF1LARRF055394Y9.html">华为L3商业化提速：七城高速实测全面启动，2026年规模落地|自动驾驶|...</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/27715963789">L3级自动驾驶：技术突破与商业化进程全解析 - 知乎</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#Huawei`, `#L3`, `#Tesla FSD`, `#AI`

---

<a id="item-8"></a>
## [首次直接观测到海底扩张过程](https://www.nytimes.com/2026/07/08/science/oceans-geology-seafloor.html) ⭐️ 8.0/10

科学家首次直接观测到海底扩张过程，证实了板块构造理论的一个关键方面。 这一直接观测验证了板块构造的基本机制——此前仅被推断而从未被直接目睹，可能改进对地球地质活动和海底演化的模型。 该观测由科学家完成，并于 2026 年 7 月 8 日在《纽约时报》上报道，记录了海底板块的扩张过程。

rss · The New York Times World · 7月8日 18:28

**背景**: 海底扩张是指在大洋中脊处，随着板块分离，新洋壳形成的过程。它是板块构造理论的关键组成部分，但由于深海环境难以进入，此前从未被直接观测到。

**标签**: `#geology`, `#oceanography`, `#plate tectonics`, `#seafloor spreading`

---

<a id="item-9"></a>
## [OpenAI 发布全双工语音模型，支持实时翻译](https://techcrunch.com/2026/07/08/openai-releases-new-voice-models-for-more-natural-live-conversations/) ⭐️ 8.0/10

OpenAI 发布了名为 GPT-Live 的新型全双工语音模型，使 ChatGPT 能够同时说话和聆听，从而实现更自然的实时对话和实时翻译。 这一突破消除了以往语音助手的轮流说话限制，使 AI 对话更接近人类交流，并实现无缝的实时跨语言翻译，可能改变多语言环境下的沟通方式。 GPT-Live 语音模式是一项全双工升级，可在移动端和网页端使用，专为处理实时翻译而设计，模型必须在生成输出的同时处理输入的语音。

rss · TechCrunch · 7月8日 17:00

**背景**: 传统的语音助手以半双工模式运行，即一次只能听或说，导致尴尬的停顿。全双工通信允许双方同时说话，是人类对话的关键特征。实时翻译一直是 AI 的目标，但以往的系统需要先将语音转录为文本再翻译，增加了延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://venturebeat.com/technology/openai-launches-gpt-live-a-full-duplex-voice-upgrade-that-lets-chatgpt-talk-more-like-a-person">OpenAI launches GPT-Live, a full-duplex voice upgrade that ...</a></li>
<li><a href="https://www.technobezz.com/news/openai-launches-gpt-live-voice-mode-for-simultaneous-listening-and-speaking">OpenAI Launches GPT-Live Voice Mode for Simultaneous ...</a></li>
<li><a href="https://aitoolly.com/ai-news/article/2026-07-09-openai-unveils-new-voice-models-featuring-simultaneous-speaking-and-listening-for-enhanced-live-tran">OpenAI New Voice Models: Simultaneous Speak and Listen</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#voice models`, `#AI`, `#real-time translation`, `#NLP`

---

<a id="item-10"></a>
## [昇视唯盛完成数亿元 B 轮融资，打造智能焊接机器人](https://36kr.com/p/3887871679347208?f=rss) ⭐️ 7.0/10

中国初创公司昇视唯盛宣布完成数亿元 B 轮融资，由上海半导体产投和金桥基金领投，资金将用于升级焊接具身智能大脑并扩大产能。 本轮融资凸显了工业制造领域对具身智能的旺盛需求，尤其是在焊接这一劳动力缺口严重的场景。昇视唯盛的技术有望大幅减少对熟练焊工的依赖，提升钢构、船舶等行业的效率。 昇视唯盛声称其焊接机器人每台可替代 1.5 至 2 名焊工，投资回报周期为 1-1.5 年。公司采用自研的“大脑”（基于千万级焊接数据训练的多模态 AI）和“小脑”（实时运动控制系统）来处理复杂非标焊接任务。

rss · 36Kr Feed · 7月9日 03:48

**背景**: 具身智能是指拥有物理实体并能与环境交互的 AI 系统，例如机器人。焊接是制造业中关键但危险的工艺，中国面临严重的劳动力短缺，注册焊工平均年龄超过 45 岁。传统焊接自动化需要大量编程，无法适应非标场景，这为 AI 驱动的解决方案创造了市场机会。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.36kr.com/p/3878315095470083">巨头接踵入场，具身智能大战开打 - 36氪</a></li>
<li><a href="https://baike.baidu.com/item/焊接机器人/6027642">焊接机器人_百度百科</a></li>
<li><a href="http://www.3srobotics.com/">3Srobotics - 上海昇视唯盛科技有限公司</a></li>

</ul>
</details>

**标签**: `#embodied AI`, `#industrial robotics`, `#welding`, `#funding`, `#manufacturing`

---

<a id="item-11"></a>
## [物理 AI 公司深度智控获数亿元融资，打造能源基础设施大脑](https://36kr.com/p/3887726503688968?f=rss) ⭐️ 7.0/10

物理 AI 企业深度智控（DeepCtrls）完成数亿元人民币 B 轮融资，由晶科能源、国投创新等领投，红杉中国、源码资本等老股东跟投。 本轮融资凸显了物理 AI 在优化能源基础设施中的重要性，这对全球脱碳和 AI 驱动的自动化至关重要。深度智控的技术有望大幅降低工业和智算中心的能耗。 深度智控自研的 PhyAI 引擎将物理机理与 AI 深度耦合，实现了 L4/L5 级自主控制，模型泛化误差低于 3%。公司已服务超过 360 家头部企业客户，包括台积电、腾讯、字节跳动等。

rss · 36Kr Feed · 7月9日 01:20

**背景**: 物理 AI 是指能够理解并与物理世界交互的 AI 系统，区别于纯数字 AI。深度智控将其应用于能源系统，实现供暖、制冷和用电的自主优化。公司由李辉博士于 2018 年创立，他曾任职于清华大学和美国劳伦斯伯克利国家实验室。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/物理AI/65039806">物理AI_百度百科</a></li>
<li><a href="https://zgeo.net/news/deepctrls-physical-ai-funding-2026">深度智控获数亿融资，物理AI引擎PhyAI驱动能源基础设施重塑 | 智脑时...</a></li>
<li><a href="https://www.163.com/dy/article/KA7KQG3O0538H7TD.html">深度智控李辉携PhyAI引擎亮相世界青年科学家论坛|人工智能|phyai|李辉...</a></li>

</ul>
</details>

**标签**: `#physical AI`, `#energy infrastructure`, `#funding`, `#industrial AI`, `#deep tech`

---

<a id="item-12"></a>
## [泽塔聚变完成数亿元天使轮融资](https://36kr.com/newsflashes/3887808277871112?f=rss) ⭐️ 7.0/10

中国可控核聚变企业泽塔聚变完成了数亿元天使轮融资，由北京市绿色能源和低碳产业投资基金领投，多家机构跟投。资金将用于 Z 箍缩聚变-裂变混合堆的研发和工程落地。 这笔大额投资表明市场对 Z 箍缩和混合堆等替代聚变路线的信心增强，可能加速商用聚变能源的实现。同时也凸显了中国对突破性清洁能源技术的日益重视。 泽塔聚变正在开发 Z 箍缩聚变-裂变混合堆，通过电流压缩等离子体并结合裂变包层来倍增能量输出。公司计划将资金用于迭代研发、工程体系搭建和人才梯队扩容。

rss · 36Kr Feed · 7月9日 02:43

**背景**: Z 箍缩是一种等离子体约束方式，利用强电流压缩并加热等离子体以达到聚变条件。聚变-裂变混合堆利用聚变中子引发非裂变材料（如铀-238）的裂变，可能实现更高的能量增益并减少核废料。该路线不如托卡马克成熟，但近期实验进展使其重新受到关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Z-pinch">Z-pinch - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fusion-fission_hybrid_reactor">Fusion-fission hybrid reactor</a></li>

</ul>
</details>

**标签**: `#fusion energy`, `#funding`, `#startup`, `#Z-pinch`, `#clean energy`

---

<a id="item-13"></a>
## [内存短缺推动 DDR4 和 DDR3 价格飙升](https://www.ithome.com/0/974/432.htm) ⭐️ 7.0/10

DDR4 8Gb 合约价预计 2026 年第三季度环比上涨 50%，DDR3 每 Gb 价格已倒挂高于 DDR5，DDR3 4Gb 为 3.19 美元/Gb，而 DDR5 16Gb 为 2.94 美元/Gb。 此次价格上涨标志着严重的 DRAM 供应短缺，可能影响数据中心、企业级 SSD 以及仍依赖 DDR3 和 DDR4 内存的旧系统的硬件成本。 短缺是由企业级 SSD 需求增长（每 1TB NAND 需要 1GB DRAM）以及主要制造商逐步停产 DDR4 所驱动。供需缺口可能持续长达两年。

rss · ITHome Feed · 7月9日 03:44

**背景**: DRAM 是一种易失性存储器，用于计算机和服务器的临时数据存储。DDR4 和 DDR3 是较老的代际，而 DDR5 是最新标准。企业级 SSD 通常使用 DRAM 作为缓存以提高性能，特别是在 AI 和数据中心使用的高容量硬盘中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://siliconanalysts.com/market-data/dram-ddr4-price">DDR4 8Gb Contract & Spot Price — Historical Data & Chart ...</a></li>
<li><a href="https://siliconanalysts.com/analysis/ddr4-historic-price-inversion-2025">DDR4's Historic Inversion: How a $1.63 Chip Became $12.76 in ...</a></li>
<li><a href="https://www.ramght.com/market-focus-dram-q2-2026-price-analysis_n28">Market Focus: DRAM – Q2 2026 Price Analysis-ramght.com</a></li>

</ul>
</details>

**标签**: `#DRAM`, `#memory pricing`, `#hardware`, `#supply chain`, `#enterprise SSD`

---

<a id="item-14"></a>
## [英特尔 Arc Pro B70 在 AI 推理中达 2320.76 token/s，超越 RTX 5090D](https://www.ithome.com/0/974/422.htm) ⭐️ 7.0/10

在蓝戟（GUNNIR）的基准测试中，4 卡英特尔 Arc Pro B70 配置在 DeepSeek R1-Distill Qwen 32B FP16 模型上实现了高达 2320.76 token/s 的吞吐量，在高并发（128-512）下超越了英伟达 RTX 5090D 和 RTX 4090D。 这一结果挑战了英伟达在 AI 推理领域的主导地位，表明英特尔的工作站 GPU 在高吞吐场景下可以超越顶级英伟达显卡，可能为 LLM 服务提供更具成本效益的选择。 测试使用每配置 4 张显卡，Arc Pro B70 配备 32GB VRAM 和 GDDR6 ECC 内存。在并发 128 时，B70 比 RTX 5090D 快 8.6%，比 RTX 4090D 快 34.2%；在并发 256 时，分别快 7.5% 和 48.7%。

rss · ITHome Feed · 7月9日 03:19

**背景**: Token/s 吞吐量衡量模型在并发请求下每秒生成的 token 数量，是 LLM 推理效率的关键指标。DeepSeek R1 是 2025 年 1 月发布的开源推理模型，以远低于 OpenAI o1 的成本达到相近性能。英特尔 Arc Pro B70 是基于 Battlemage 架构的工作站 GPU，于 2026 年 3 月推出，配备 32GB 显存。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-R1">deepseek-ai/DeepSeek-R1 · Hugging Face</a></li>
<li><a href="https://www.intel.com/content/www/us/en/products/sku/245797/intel-arc-pro-b70-graphics/specifications.html">Intel® Arc™ Pro B70 Graphics</a></li>

</ul>
</details>

**标签**: `#AI inference`, `#GPU benchmark`, `#Intel Arc`, `#DeepSeek`, `#LLM`

---

<a id="item-15"></a>
## [法国监管机构警告 Meta 支付新闻使用费](https://www.rfi.fr/cn/%E6%AC%A7%E6%B4%B2/20260708-%E6%B3%95%E5%9B%BD%E7%AB%9E%E4%BA%89%E7%9B%91%E7%AE%A1%E6%9C%BA%E6%9E%84%E5%90%91meta%E5%8F%91%E5%87%BA%E8%AD%A6%E5%91%8A) ⭐️ 7.0/10

2026 年 7 月 8 日，法国竞争管理局要求 Meta 在 15 天内提出付款计划，并与法国媒体团体重启谈判，以支付自 2025 年起积欠的新闻内容使用费。 这一强制行动凸显了监管机构对科技巨头向新闻出版商支付内容费用的压力日益增大，可能为其他地区的类似纠纷树立先例。 该命令要求 Meta 在 15 天内遵守，所涉费用可追溯至 2025 年。法国竞争管理局是一个独立的行政机构，负责监管反竞争行为。

rss · RFI Chinese · 7月8日 20:44

**背景**: 法国竞争管理局（Autorité de la concurrence）是执行法国竞争法的独立机构。近年来，它积极参与涉及数字平台和新闻出版商的案件，特别是关于根据邻接权使用新闻内容的报酬问题。此案之前，法国曾对谷歌采取过类似行动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rfi.fr/cn/欧洲/20260708-法国竞争监管机构向meta发出警告">法国竞争监管机构向Meta发出警告 - RFI - 法国国际广播电台</a></li>
<li><a href="https://zh.wikipedia.org/wiki/竞争管理局">竞争管理局 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**标签**: `#Meta`, `#regulation`, `#competition law`, `#news content`, `#France`

---

<a id="item-16"></a>
## [中国工信部警告 Claude Code 存在安全漏洞](https://www.rfi.fr/cn/%E4%B8%AD%E5%9B%BD/20260708-%E4%B8%AD%E5%9B%BD%E5%B7%A5%E4%BF%A1%E9%83%A8%E8%AD%A6%E7%A4%BAclaude-code%E5%AD%98%E5%AE%89%E5%85%A8%E9%9A%90%E6%82%A3) ⭐️ 7.0/10

中国工信部下属的国家网络安全威胁和漏洞信息共享平台（NVDB）检测到 AI 编程工具 Claude Code 存在安全漏洞，该漏洞可能未经用户同意将包括位置和身份识别信息在内的敏感数据传输至 Anthropic 的服务器。 这一来自主要政府机构的官方警告凸显了人们对 AI 编程工具数据隐私和安全性的日益担忧，可能影响全球范围内此类工具的信任度和采用率，尤其是在受监管行业。 该漏洞被描述为一个后门，可能将敏感信息发送到远程服务器。NVDB 未具体说明受影响的 Claude Code 版本，但该警告适用于该工具在中国的使用。

rss · RFI Chinese · 7月8日 20:36

**背景**: Claude Code 是 Anthropic 开发的 AI 编程助手，帮助开发者编写、审查和调试代码。NVDB 是中国工信部运营的国家网络安全漏洞库，负责跟踪和披露漏洞。此次警告之前，2026 年 3 月曾发生 Anthropic 通过 npm 意外泄露 51.2 万行 Claude Code 源代码的事件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/07/08/china-anthropic-ai-claude-code-backdoor-security-threat.html">China warns about AI risks with Anthropic's Claude Code - CNBC</a></li>
<li><a href="https://www.globaltimes.cn/page/202607/1365448.shtml">China issues warning over backdoor security risks in ...</a></li>
<li><a href="https://cybernews.com/ai-news/china-backdoor-security-alert-anthropics-claude-code/">China warns of 'backdoor' security risk in Anthropic's Claude ...</a></li>

</ul>
</details>

**标签**: `#security`, `#AI`, `#Claude Code`, `#privacy`, `#vulnerability`

---

<a id="item-17"></a>
## [美国议员调查美企日益使用中国 AI 模型](https://www.rfi.fr/cn/%E7%A7%91%E6%8A%80%E4%B8%8E%E6%96%87%E5%8C%96/20260708-%E7%BE%8E%E8%AE%AE%E5%91%98%E8%B0%83%E6%9F%A5%E7%BE%8E%E4%BC%81%E6%97%A5%E7%9B%8A%E5%B9%BF%E6%B3%9B%E4%BD%BF%E7%94%A8%E4%B8%AD%E5%9B%BDai%E6%A8%A1%E5%9E%8B-%E7%BE%8E%E5%9B%BD%E5%8A%A1%E9%99%A2-%E8%AF%A5%E6%83%85%E5%86%B5%E5%BC%95%E5%8F%91%E4%B8%A5%E9%87%8D%E5%85%B3%E5%88%87) ⭐️ 7.0/10

美国议员已启动调查，关注美国企业日益广泛使用中国 AI 模型，并援引国家安全关切。美国国务院对此趋势表示严重关切。 这项调查可能导致新的法规限制美国企业使用中国 AI 模型，从而重塑全球 AI 供应链。它凸显了美中科技竞争的加剧以及中国模型日益增长的成本优势。 DeepSeek、阿里巴巴的 Qwen、月之暗面的 Kimi 和稀宇科技等中国模型在 OpenRouter 等平台上越来越受欢迎。调查针对爱彼迎和 Cursor（Anysphere）等使用这些模型的公司。

rss · RFI Chinese · 7月8日 10:47

**背景**: 人工智能已成为美中竞争的核心领域，双方都在争夺主导地位。中国 AI 模型在缩小与美国同类产品性能差距的同时，提供了显著更低的成本，这使其对美国开发者和企业具有吸引力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.aibase.com/zh/news/29465">美国企业“弃用”头部AI：中国模型凭借高性价比突围</a></li>
<li><a href="https://www.163.com/dy/article/L1C33P720511D6RL.html">美国盯上中国开源 AI 模型：Airbnb、Cursor 被调查|爱彼迎|cursor_网...</a></li>

</ul>
</details>

**标签**: `#AI`, `#geopolitics`, `#US-China competition`, `#regulation`

---

<a id="item-18"></a>
## [研究：澳大利亚在售儿童沙释放石棉纤维](https://www.theguardian.com/australia-news/2026/jul/09/contaminated-childrens-play-sand-sold-in-australia-can-release-toxic-airborne-asbestos-research-finds) ⭐️ 7.0/10

奥克兰理工大学的一项新研究发现，90% 的工艺沙样品在玩耍时会释放出空气中的石棉纤维，这与澳大利亚监管机构此前声称风险较低的说法相矛盾。 这一发现具有重大的公共卫生意义，因为儿童尤其容易受到石棉暴露的影响，石棉可能导致日后患间皮瘤等疾病。这也削弱了官方安全评估的可信度，并可能导致更严格的监管。 该研究测试了在澳大利亚销售的工艺沙产品，发现 90% 的样品在模拟玩耍过程中向空气中释放了石棉纤维。ACCC 此前曾表示这些产品风险较低，但新研究表明空气中的纤维可能被释放。

rss · The Guardian World · 7月8日 15:00

**背景**: 石棉是一种天然矿物，因其耐热性和耐久性曾被广泛用于建筑和消费品。当含石棉的材料被扰动时，微小的纤维会飘散到空气中，如果被吸入，可能导致肺癌、间皮瘤和石棉肺等严重疾病。自 2025 年底以来，受石棉污染的儿童沙在澳大利亚和新西兰引起了越来越多的关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phcc.org.nz/briefing/asbestos-contaminated-childrens-play-sand-assessing-mitigating-and-preventing-risk">Asbestos-contaminated children’s play sand: Assessing ...</a></li>
<li><a href="https://www.sbs.com.au/news/article/new-health-advice-issued-after-asbestos-found-in-kids-play-sand/e2gc116j7">New health advice issued after asbestos found in kids' play ...</a></li>
<li><a href="https://biologyinsights.com/how-far-does-asbestos-travel-in-the-air/">How Far Does Asbestos Travel in the Air? - Biology Insights</a></li>

</ul>
</details>

**标签**: `#public health`, `#asbestos`, `#Australia`, `#consumer safety`, `#environmental hazard`

---

<a id="item-19"></a>
## [EmTech AI 2026 聚焦 AI 平台崛起](https://www.technologyreview.com/2026/07/08/1140223/emtech-ai-2026-the-rise-of-the-ai-platform/) ⭐️ 7.0/10

在 EmTech AI 2026 上，MIT Technology Review 报道称，AI 平台的崛起是一个关键趋势，标志着从独立 AI 模型向集成环境开发和管理 AI 应用的转变。 这一趋势表明 AI 正在成熟为基于平台的生态系统，使企业能够更高效地构建、部署和扩展 AI 解决方案，从而加速 AI 在各行业的采用。 会议于 2026 年 4 月 21-23 日在马萨诸塞州剑桥市的 MIT Media Lab 举行，商业领袖分享了利用生成式 AI 的见解。AI 平台集成了数据管理、模型训练、部署和监控等工具。

rss · MIT Technology Review · 7月8日 16:26

**背景**: AI 平台是一个集成的技术环境，提供设计、定制和管理智能应用所需的一切。它通常包括自动化、MLOps 和预测分析能力。EmTech AI 是 MIT Technology Review 举办的年度会议，聚焦 AI 领导力和实际应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://event.technologyreview.com/emtech-ai-2026">EmTech AI 2026 in Cambridge, MA</a></li>
<li><a href="https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-an-ai-platform">What is an AI platform? | Microsoft Azure</a></li>
<li><a href="https://www.redhat.com/en/topics/ai/what-is-an-ai-platform">What is an AI platform? - Red Hat</a></li>

</ul>
</details>

**标签**: `#AI`, `#platforms`, `#industry trends`, `#MIT Technology Review`

---

<a id="item-20"></a>
## [NHTSA 要求自动驾驶公司停止干扰急救人员](https://techcrunch.com/2026/07/08/feds-demand-autonomous-vehicle-companies-stop-interfering-with-first-responders/) ⭐️ 7.0/10

美国国家公路交通安全管理局（NHTSA）要求自动驾驶公司停止干扰急救人员，并指出紧急场景并非“边缘情况”。 这一监管行动可能迫使自动驾驶公司将应急响应场景置于系统优先地位，从而提升急救人员和公众的安全。这也标志着 NHTSA 的立场转变，不再将此类情况视为罕见例外，而是作为强制性运营要求。 NHTSA 明确否定了行业将紧急场景视为“边缘情况”（即不可预测的罕见事件）的表述。该机构的要求表明，自动驾驶车辆必须将处理与警车、消防车和救护车的互动作为核心功能来设计。

rss · TechCrunch · 7月8日 21:49

**背景**: 自动驾驶车辆依靠传感器和人工智能进行导航，但它们在处理紧急车辆靠近、路障或事故现场等异常情况时常常遇到困难。行业历来将此类场景归类为难以测试和验证的“边缘情况”。NHTSA 的新立场挑战了这一分类，强调紧急场景足够常见，需要系统性解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nhtsa.gov/vehicle-safety/automated-vehicles-safety">Automated Vehicle Safety | NHTSA</a></li>
<li><a href="https://www.linkedin.com/pulse/edge-cases-autonomous-vehicles-road-full-autonomy-from-moyin-ikuseru-xetve">Edge Cases in Autonomous Vehicles: The road to ... - LinkedIn</a></li>

</ul>
</details>

**标签**: `#autonomous vehicles`, `#regulation`, `#safety`, `#NHTSA`

---

<a id="item-21"></a>
## [中国极端天气风险远超认知与基础设施应对能力](https://www.chinanews.com.cn/ll/2026/07-09/10655767.shtml) ⭐️ 6.0/10

一篇评论指出，中国极端天气事件增多，如 2026 年 6 月塔克拉玛干沙漠洪水及 400 毫米等降水量线北移，但公众风险意识和防洪基础设施未能同步提升。 这一差距暴露了应对巨灾的脆弱性，威胁公共安全和经济稳定，凸显了在气候变化背景下加强风险沟通和基础设施适应的紧迫性。 评论特别提到 2026 年 6 月塔克拉玛干沙漠洪水和 400 毫米等降水量线北移，指出部分干部群众风险意识不足，城市及山区防汛能力不足。

rss · China News Service Scroll · 7月9日 03:29

**背景**: 400 毫米等降水量线是中国重要的气候分界线，传统上划分半湿润区和半干旱区。其北移表明气候正在变化，给先前较干旱地区带来更多降雨。塔克拉玛干沙漠是中国最大的沙漠，2026 年 6 月因极端降雨遭遇前所未有的洪水，凸显了气候变化下极端天气的不可预测性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.news.cn/politics/20260624/a524080b70d7453087c2d7a0420aa69f/c.html">气象专家：塔克拉玛干沙漠洪水何来 - 新华网</a></li>
<li><a href="https://news.qq.com/rain/a/20260616A09QLI00">真的“雨带北移”了？对话中国科学院气象专家：400毫米等降水量线有向北...</a></li>
<li><a href="https://news.qq.com/rain/a/20260623A07M9N00">塔克拉玛干沙漠发洪水了！3小时下完一年的雨，到底是好事还是坏事？_...</a></li>

</ul>
</details>

**标签**: `#climate change`, `#extreme weather`, `#risk management`, `#China`

---

<a id="item-22"></a>
## [魏炳波院士三十余载“造锅煮饭”助力中国空间材料科学](https://www.chinanews.com.cn/gn/2026/07-08/10655487.shtml) ⭐️ 6.0/10

一篇人物特写介绍了魏炳波院士三十余年来在中国空间材料科学领域的开创性工作，包括其团队制备的难熔合金样品在中国空间站成功完成在轨实验。 魏炳波的工作使中国在空间材料研究方面实现了自主能力，减少了对国外设施的依赖，并提升了中国在微重力材料科学领域的地位。 魏炳波团队制备了 10 余种数百个高性能难熔合金样品，在中国空间站无容器材料科学实验柜进行了 6 批次在轨实验，其中钨合金实验尤为亮眼，钨的熔点高达 3422°C。

rss · China News Service China · 7月8日 13:51

**背景**: 空间材料科学，又称微重力材料科学，研究微重力条件下的材料加工规律及新型材料制备。该学科始于 20 世纪 70 年代，涵盖晶体生长与金属/复合材料制备等领域。中国空间站为此类实验提供了独特平台，这些实验在地球上因重力引起的对流和沉降而难以进行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.sciencenet.cn/htmlnews/2026/7/567883.shtm">魏炳波院士助中国空间材料科学破局—新闻—科学网</a></li>
<li><a href="https://www.sohu.com/a/1047684014_121443915">三十余载“造锅煮饭”，魏炳波院士助中国空间材料科学破局</a></li>

</ul>
</details>

**标签**: `#space materials science`, `#China`, `#academic profile`, `#materials research`

---

<a id="item-23"></a>
## [上海芯片初创企业沐曦与曦智取得里程碑](https://www.chinanews.com.cn/cj/2026/07-09/10655787.shtml) ⭐️ 5.0/10

成立于 2020 年的 GPU 芯片初创企业沐曦集成电路已累计销售超过 5.5 万颗芯片，部署于 10 余个智算集群；而源自麻省理工学院实验室的光子芯片企业曦智科技于 2026 年 4 月在港交所上市，成为“全球 AI 硅光芯片第一股”。 这些成就凸显了中国初创企业在 GPU 和硅光芯片等关键 AI 硬件领域的快速进步，有望减少对外国供应商的依赖，并推动国内 AI 基础设施建设。 沐曦的 GPU 已部署于 10 余个智算集群，曦智的硅光芯片技术可将 AI 计算集群的延迟降低近 90%，并兼容多个主流大模型。

rss · China News Service Scroll · 7月9日 03:27

**背景**: GPU 是 AI 训练和推理的核心硬件，而硅光芯片利用光而非电信号传输数据，具有更高速度和更低功耗。沐曦采用无晶圆厂模式，专注于 GPU 设计与软件生态；曦智（Lightelligence）则开发用于 AI 工作负载的光子集成电路。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/en/item/Muxi+Integrated+Circuit+(Shanghai)+Co.,+Ltd./948916">Muxi Integrated Circuit (Shanghai) Co., Ltd._Baiduwiki</a></li>
<li><a href="https://en.chipsourcetek.com/Industry-News/6813.html">Xizhi Technology, the world's first AI silicon photonics chip ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lightelligence">Lightelligence - Wikipedia</a></li>

</ul>
</details>

**标签**: `#GPU`, `#photonic chip`, `#AI`, `#startup`, `#China`

---

<a id="item-24"></a>
## [青海 50MW 光热电站四年发电 5.82 亿千瓦时](http://www.chinanews.com.cn/tp/hd2011/2026/07-09/1197645.shtml) ⭐️ 5.0/10

青海中控德令哈 50MW 塔式光热电站四年累计实际发电量达 5.82 亿千瓦时，验证了塔式熔盐储能光热技术的可靠性。 这一里程碑证明了中国大规模熔盐储能光热发电的商业可行性，支持了国家的能源转型和电网稳定。 该电站位于青海德令哈，总装机容量 50 兆瓦，是中国第一座大规模商业化运营的太阳能热发电站。通过持续优化运行策略和提升系统效率，实现了 5.82 亿千瓦时的发电量。

rss · China News Service Scroll · 7月9日 03:23

**背景**: 塔式光热电站利用成千上万面定日镜将太阳光聚焦到塔顶的吸热器上，加热熔盐以储存热能。储存的热量即使在无阳光时也能发电，实现 24 小时连续供电。该技术对于克服太阳能的间歇性至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/443465930">科普百篇系列（126） 我国的“熔盐塔式光热发电技术”全球瞩目</a></li>
<li><a href="https://wenku.baidu.com/view/2466e5cc4293daef5ef7ba0d4a7302768f996f5a.html">熔盐塔式光热电站工作原理及优缺点详解_百度文库</a></li>
<li><a href="https://baike.baidu.com/item/太阳能塔式发电/2439281">太阳能塔式发电_百度百科</a></li>

</ul>
</details>

**标签**: `#solar energy`, `#renewable energy`, `#CSP`, `#China`

---

<a id="item-25"></a>
## [两院院士热议“科技三会”指明方向](https://www.chinanews.com.cn/gn/2026/07-09/10655758.shtml) ⭐️ 5.0/10

中国科学院和中国工程院院士高度评价“科技三会”，认为其为建设世界科技强国指明了战略方向，并强调人工智能驱动的创新。 这一高层表态标志着国家将优先发展人工智能和基础研究，可能加速中国的技术自立和全球竞争力。 “科技三会”指全国科技大会、国家科学技术奖励大会和两院院士大会，分别于 2024 年和 2026 年召开。

rss · China News Service China · 7月9日 03:11

**背景**: “科技三会”首次于 2016 年召开，习近平主席在会上提出了到 2050 年建成世界科技强国的“三步走”战略。这些会议是颁发国家科技奖和制定政策方向的平台。最近的讨论强调人工智能是研究范式变革的驱动力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ncsti.gov.cn/kjdt/ztbd/qgkjsh/index_1.html">全国“科技三会”</a></li>
<li><a href="https://baike.baidu.com/item/科技三会/19699559">科技三会_百度百科</a></li>
<li><a href="https://www.ncsti.gov.cn/kjdt/kjrd/202512/t20251210_231693.html">2025国是论坛上，专家提出—— 以人工智能技术驱动创新范式变革</a></li>

</ul>
</details>

**标签**: `#China`, `#science policy`, `#technology`, `#innovation`, `#AI`

---

<a id="item-26"></a>
## [2025 年度国家科技奖呈现新特点](https://www.chinanews.com.cn/gn/2026/07-09/10655570.shtml) ⭐️ 4.0/10

据中新网 2026 年 7 月 9 日报道，2025 年度国家科学技术奖呈现出新的特点。 这些奖项反映了中国科技政策的演变方向，预示着研究重点和评审标准的变化。 该报道为常规新闻，未提供具体技术细节，仅概述了奖项的总体趋势，未披露具体获奖者或指标。

rss · China News Service China · 7月8日 23:27

**背景**: 国家科学技术奖是中国对科学成就的最高荣誉，通常每年公布一次，涵盖自然科学、技术发明和科学技术进步等类别。

**标签**: `#science policy`, `#China`, `#awards`

---

<a id="item-27"></a>
## [海南自贸港样板间推进教育科技人才一体发展](https://www.chinanews.com.cn/sh/2026/07-09/10655781.shtml) ⭐️ 3.0/10

2026 年 7 月 8 日，海南自贸港“样板间”儋州市宣布推出“1+3+N”教育科技人才一体发展政策体系，以促进产业高质量发展。 这一一体化发展模式旨在加速培育新质生产力、壮大产业集群，为中国自贸港建设中的其他地区提供示范。 “1+3+N”体系包括一个总体方案、三大行动计划及多项配套措施，涵盖教育改革、科技创新和人才引进。

rss · China News Service Scroll · 7月9日 03:26

**背景**: 儋州市被定位为海南自贸港的“工业心脏”和“样板间”。“十五五”期间重点任务是壮大产业集群、培育新质生产力。该政策与国家推进教育科技人才一体发展的战略部署相一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.chinanews.com/sh/2026/07-09/10655781.shtml">海南自贸港“样板间”推进教育科技人才一体发展-中新网</a></li>
<li><a href="https://www.danzhou.gov.cn/danzhou/jdhy/xwfbh/202511/t20251120_3974248.html">实录丨奋力打造海南自贸港“样板间”系列新闻发布会 深化制度集成创新 ...</a></li>
<li><a href="https://www.moe.gov.cn/jyb_xwfb/s5147/202605/t20260522_1437327.html">一体推进教育科技人才发展 - 中华人民共和国教育部政府门户网站</a></li>

</ul>
</details>

**标签**: `#policy`, `#regional development`, `#education`, `#talent`

---

<a id="item-28"></a>
## [雄安新区启动全域通办政务服务](https://www.chinanews.com.cn/gn/2026/07-09/10655732.shtml) ⭐️ 3.0/10

自 2026 年 7 月 9 日起，雄安新区实施政务服务“全域通办”，居民和企业可在区域内任一服务点办理行政事项。 这项改革大幅减少了出行和等待时间，提升了当地居民和企业的便利性，并为新建城区的行政一体化树立了典范。 改革包括市县同权、异地代收、多地联办、京雄同城四种办理模式。首批 24 项新区本级高频事项可多点办理，625 个北京市级事项可在雄安服务大厅收件。

rss · China News Service China · 7月9日 02:32

**背景**: 雄安新区是国家级重大发展项目，旨在疏解北京非首都功能。“全域通办”允许政务服务在区域内不同行政层级和地点办理，依托数字平台和城际协调。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.cctv.com/2026/07/09/ARTI5WJOOKo3fCHT7Jgtj1JD260709.shtml">雄安新区政务服务实现“全域通办”_新闻频道_央视网 (cctv.com)</a></li>
<li><a href="https://www.beijing.gov.cn/ywdt/zwzt/jjjyth/jjyw/202607/t20260703_4746337.html">雄安政务服务“全域通办” 北京的事多点可办_津冀要闻_首都之窗_北京市...</a></li>
<li><a href="https://news.bjd.com.cn/2026/07/09/11853527.shtml">雄安新区政务服务实现“全域通办”_京报网</a></li>

</ul>
</details>

**标签**: `#government services`, `#China`, `#administrative reform`

---