---
layout: default
title: "Horizon Summary: 2026-06-15 (ZH)"
date: 2026-06-15
lang: zh
---

> 从 297 条内容中筛选出 28 条重要资讯。

---

1. [里约热内卢自称自研的大语言模型被揭露为现有模型的加权合并](#item-1) ⭐️ 8.0/10
2. [清华团队揭示记忆重激活如何调控睡眠](#item-2) ⭐️ 8.0/10
3. [Anthropic 全球停供最新 AI 模型](#item-3) ⭐️ 8.0/10
4. [AI 加速中国“人造太阳”聚变研究](#item-4) ⭐️ 7.0/10
5. [智源院长王仲远：世界模型四条路，VLA 不会死](#item-5) ⭐️ 7.0/10
6. [世航智能创纪录融资 10 亿元，海洋机器人赛道升温](#item-6) ⭐️ 7.0/10
7. [SK 海力士本月将出货 HBM4E 样品](#item-7) ⭐️ 7.0/10
8. [谷歌与 UCSD 将旧 Pixel 手机改造成低成本数据中心](#item-8) ⭐️ 7.0/10
9. [中国电动自行车变速器初创公司洛梵狄完成 B+轮融资](#item-9) ⭐️ 6.0/10
10. [网件起诉 TP-Link 虚假宣传为美国公司](#item-10) ⭐️ 6.0/10
11. [计算机历史博物馆从德国仓库回收 2000 余件文物](#item-11) ⭐️ 6.0/10
12. [黑灯工厂：中国年轻人就业的威胁？](#item-12) ⭐️ 6.0/10
13. [英国首相斯塔默宣布对 16 岁以下青少年实施‘澳大利亚加强版’社交媒体禁令](#item-13) ⭐️ 6.0/10
14. [远程医疗公司在减肥药使用中的双重角色引发担忧](#item-14) ⭐️ 6.0/10
15. [Anthropic 暂停模型访问，印度反思 AI 未来](#item-15) ⭐️ 6.0/10
16. [FBI 建造模拟小镇用于网络攻击演练](#item-16) ⭐️ 6.0/10
17. [中国加速地下管网更新，纳入“六网”战略](#item-17) ⭐️ 5.0/10
18. [黑土地保护会议展示中国进展](#item-18) ⭐️ 5.0/10
19. [半固态凝胶电池为全固态电池提供实用过渡方案](#item-19) ⭐️ 5.0/10
20. [公安部公布 10 起网络谣言典型案例](#item-20) ⭐️ 4.0/10
21. [新一轮厄尔尼诺现象已宣布，可能成为超级厄尔尼诺](#item-21) ⭐️ 4.0/10
22. [中国推动铁路旅游融合，2030 年前打造 160 列以上旅游列车](#item-22) ⭐️ 3.0/10
23. [湖北推动非遗融入日常生活](#item-23) ⭐️ 3.0/10
24. [神舟二十三号乘组在轨第三周动态](#item-24) ⭐️ 2.0/10
25. [青年农机手赋能现代农业](#item-25) ⭐️ 2.0/10
26. [前 5 个月中国铁路多项指标创新高](#item-26) ⭐️ 2.0/10
27. [A 股周一开盘普涨，三大指数集体高开](#item-27) ⭐️ 2.0/10
28. [央行开展 4250 亿元 7 天期逆回购操作](#item-28) ⭐️ 2.0/10

---

<a id="item-1"></a>
## [里约热内卢自称自研的大语言模型被揭露为现有模型的加权合并](https://github.com/nex-agi/Nex-N2/issues/4) ⭐️ 8.0/10

一项 GitHub 问题分析显示，里约热内卢市政府发布的 Rio-3.5-Open-397B（自称是 Qwen3.5 的自研微调版本）实际上是约 60%的 Nex-N2 Pro 和 40%的 Qwen3.5-397B-A17B 的加权合并，所有层的每个权重张量都符合 0.6/0.4 的混合比例。 这引发了对政府资助 AI 项目透明度和归属问题的严重担忧，因为该模型被宣传为原创作品，却未披露其源自现有开源模型，可能误导公众和研究社区。 分析发现，Rio 模型中的每个权重张量在数千个标准差范围内，与 Nex-N2 Pro 和 Qwen3.5 的 0.6/0.4 混合结果完全一致，覆盖所有 60 层和每个网络组件，这无法用微调或蒸馏来解释。

hackernews · unrvl22 · 6月14日 15:37 · [社区讨论](https://news.ycombinator.com/item?id=48528371)

**背景**: 模型合并是一种将两个或多个预训练模型的权重组合成一个模型的技术，无需额外训练，常用方法包括线性插值或 SLERP。这种方法可以提升性能，但在发布衍生模型时需要适当归属。Rio 模型被声称是 Qwen3.5 的微调版本，但证据表明它只是一个简单的加权合并。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2212.09849">[2212.09849] Dataless Knowledge Fusion by Merging Weights of Language Models</a></li>
<li><a href="https://nerdleveltech.com/nex-n2-pro-open-weight-coding-benchmarks">Nex-N2-Pro: Open-Weight Coder vs GPT-5.5 (2026)</a></li>

</ul>
</details>

**社区讨论**: 社区评论对缺乏披露表示怀疑和担忧，有人指出该模型可能原本计划包含蒸馏但上传版本遗漏了。其他人则强调深度学习模型的鲁棒性，简单的权重插值就能带来性能提升。

**标签**: `#LLM`, `#model merging`, `#open source`, `#ethics`, `#reproducibility`

---

<a id="item-2"></a>
## [清华团队揭示记忆重激活如何调控睡眠](https://www.ithome.com/0/964/240.htm) ⭐️ 8.0/10

清华大学团队在《科学》杂志发表研究，表明睡眠中的记忆重激活能主动调控睡眠质量，负向记忆促进觉醒，正向记忆促进睡眠。 这一发现解释了压力导致睡眠不佳的原因，并将记忆印迹细胞确定为抑郁症相关睡眠障碍的潜在治疗靶点，为治疗开辟了新途径。 研究团队利用小鼠发现，基底外侧杏仁核中的负向记忆印迹细胞在非快速眼动睡眠中自发重激活，增加向觉醒的转换，而正向记忆印迹细胞则促进睡眠维持。

rss · ITHome Feed · 6月15日 01:49

**背景**: 睡眠分为非快速眼动和快速眼动阶段，记忆巩固发生在睡眠期间。基底外侧杏仁核是参与情绪记忆的脑区。这项研究揭示了一种双向机制：记忆不仅在睡眠中巩固，还主动塑造睡眠结构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ebiotrade.com/newsf/2026-6/20260612091456831.htm">生命学院钟毅团队与合作者揭示 记 忆 重 激 活 调节睡眠的神经机制 - 生物通</a></li>
<li><a href="https://zh.wikipedia.org/zh-hans/杏仁核">杏仁核 - 维基百科，自由的百科全书 - zh.wikipedia.org</a></li>
<li><a href="https://zh.wikipedia.org/zh-hans/非快速動眼睡眠">非快速动眼睡眠 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**标签**: `#neuroscience`, `#sleep research`, `#memory`, `#Science publication`, `#brain mechanisms`

---

<a id="item-3"></a>
## [Anthropic 全球停供最新 AI 模型](https://www.dw.com/zh/%E5%92%8C%E4%B8%AD%E5%9B%BD%E6%9C%89%E5%85%B3-anthropic%E6%9C%80%E6%96%B0ai%E6%A8%A1%E5%9E%8B%E5%85%A8%E7%90%83%E6%96%AD%E4%BE%9B/a-77543796?maca=chi-rss-chi-all-1127-rdf) ⭐️ 8.0/10

6 月 12 日，Anthropic 根据美国商务部的国家安全指令，暂停了所有用户对其最新 AI 模型 Claude Mythos 5 和 Claude Fable 5 的访问权限。 此举凸显了 AI 发展与国家安全之间日益紧张的矛盾，可能限制全球对尖端 AI 的访问，并促使欧盟加速推动技术自主。 白宫怀疑与中国有关的组织可能利用这些模型，因此突然实施全球禁令。欧盟正在评估影响，并强调相关措施不应歧视合作伙伴。

rss · DW Chinese · 6月14日 10:25

**背景**: Anthropic 是一家领先的 AI 公司，以其 Claude 系列闻名。Mythos 5 和 Fable 5 是其最先进的模型，其中 Mythos 5 仅限于网络安全和科学研究。美国越来越多地使用出口管制来防止对手获取敏感 AI 技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5?pubDate=20260613">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://decrypt.co/370556/anthropic-rolls-out-claude-mythos-5-ai-model-safer-fable-public">Anthropic Rolls Out Claude Mythos 5 AI Model —Along... - Decrypt</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_States_export_controls_on_AI_chips_and_semiconductors">United States export controls on AI chips and semiconductors</a></li>

</ul>
</details>

**标签**: `#AI`, `#Geopolitics`, `#Anthropic`, `#National Security`, `#Tech Regulation`

---

<a id="item-4"></a>
## [AI 加速中国“人造太阳”聚变研究](https://www.chinanews.com.cn/gn/2026/06-14/10640315.shtml) ⭐️ 7.0/10

中关村学院与中关村人工智能研究院的研究人员正在利用强化学习、生成式模型和自进化智能体来加速可控核聚变研究，旨在解决等离子体诊断、预测和不稳定性控制等问题。 如果成功，AI 驱动的聚变将让清洁、丰富的能源更接近现实，有助于应对全球能源挑战并减少对化石燃料的依赖。 该团队构建了“物理+数据”双轮驱动的技术核心，利用强化学习进行等离子体控制，利用生成式模型进行设计优化，这与 DeepMind 和 IBM 在聚变研究中的最新进展类似。

rss · China News Service China · 6月14日 11:25

**背景**: 可控核聚变旨在通过将轻原子核在极端温度和压力下融合，在地球上复制太阳的能量产生方式。托卡马克和仿星器是常见的反应堆设计，但维持稳定的等离子体仍是一大挑战。AI，尤其是强化学习，在控制等离子体行为和优化反应堆设计方面已显示出潜力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nuclear_fusion">Nuclear fusion - Wikipedia</a></li>
<li><a href="https://deepmind.google/blog/accelerating-fusion-science-through-learned-plasma-control/">Accelerating fusion science through learned plasma control</a></li>
<li><a href="https://research.ibm.com/blog/fusion-plasma-ai-model">A new AI model for probing fusion plasma behavior - IBM Research</a></li>

</ul>
</details>

**标签**: `#AI`, `#nuclear fusion`, `#reinforcement learning`, `#energy`, `#research`

---

<a id="item-5"></a>
## [智源院长王仲远：世界模型四条路，VLA 不会死](https://36kr.com/p/3853016586359817?f=rss) ⭐️ 7.0/10

智源研究院院长王仲远将当前世界模型研究分为四类：以语言为中心、以像素为中心、以三维结构为中心和以视觉表征为中心。他认为 VLA 模型不会消亡，但世界模型才是真正的未来方向。 这一分类厘清了世界模型研究领域碎片化的现状，帮助 AI 和机器人社区理解不同方法之间的权衡。作为领先的非营利研究机构负责人，王仲远的观点预示着未来几年资源和注意力的可能投向。 智源研究院正在探索第五种方法，将语言和视觉表征融合到统一的潜空间中，所有模态被压缩后按需解码。王仲远指出，世界模型目前处于类似深度学习 2012 年前后的阶段，尚无明确基准或主导范式。

rss · 36Kr Feed · 6月15日 01:50

**背景**: 世界模型旨在让 AI 系统理解物理世界的动态、因果关系和常识，这是当前大语言模型和视觉-语言-动作（VLA）模型所缺乏的。它们被认为是推进具身智能的关键，因为机器人必须与物理世界交互并推理。主要方法包括视频生成模型（如 Sora）、3D 重建模型（如 World Labs 的 Marble）以及预测架构（如 Meta 的 V-JEPA）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vision-language-action_model">Vision–language–action model - Wikipedia</a></li>
<li><a href="https://ai.meta.com/blog/v-jepa-yann-lecun-ai-model-video-joint-embedding-predictive-architecture/">V-JEPA: The next step toward advanced machine intelligence</a></li>
<li><a href="https://marble.worldlabs.ai/">Marble</a></li>

</ul>
</details>

**标签**: `#world model`, `#embodied AI`, `#VLA`, `#AI research`, `#robotics`

---

<a id="item-6"></a>
## [世航智能创纪录融资 10 亿元，海洋机器人赛道升温](https://36kr.com/p/3853011900142848?f=rss) ⭐️ 7.0/10

海洋具身智能公司「世航智能」完成 A 轮融资，金额超过 10 亿元人民币，创下全球海洋机器人领域单轮融资纪录。投资方包括摩尔线程、昆仑芯、Vertex Growth，以及金沙江创投朱啸虎等。 这笔创纪录的投资表明市场对海洋机器人这一高难度但高价值领域的强烈信心。世航的技术有望变革船舶清洗、海上风电维护、海底巡检等水下作业，减少对潜水员和大型装备的依赖。 世航的「沧穹 CEORION」具身大模型在仿真中任务成功率超过 90%，在未见环境中的零样本适应能力超过 70%。其机器人已完成超千艘大型船舶养护作业，2026 年上半年订单金额超过 10 亿元。

rss · 36Kr Feed · 6月15日 01:50

**背景**: 海洋机器人面临极端挑战：低光照、高浑浊度、强洋流、通信受限、高压和腐蚀。传统水下作业依赖潜水员或大型装备，成本高且风险大。具身智能将感知、推理和动作集成于单一系统，使机器人能在复杂环境中自主作业。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.chinaventure.com.cn/news/114-20260327-390683.html">独家 | 三百家机构，盯上一个 海 洋 机器人 | 投中网</a></li>
<li><a href="https://pdf.dfcfw.com/pdf/H301_AP202510031755113354_1.pdf">Survey on Embodied AI, Liu Yang, et.al》中国银河证券研究院</a></li>

</ul>
</details>

**标签**: `#marine robotics`, `#funding`, `#embodied intelligence`, `#underwater robots`

---

<a id="item-7"></a>
## [SK 海力士本月将出货 HBM4E 样品](https://36kr.com/newsflashes/3853695838016515?f=rss) ⭐️ 7.0/10

SK 海力士正准备最早于本月向主要客户交付 HBM4E 样品，并计划于明年实现量产。 这标志着高带宽内存发展路线图中的关键一步，将直接影响下一代 AI 和机器学习硬件的性能。 样品交付时间紧迫，因为客户测试和优化必须在今年下半年完成，以便明年启动量产。

rss · 36Kr Feed · 6月15日 00:22

**背景**: HBM（高带宽内存）是一种通过垂直堆叠 DRAM 芯片实现高带宽和低功耗的内存类型，对 AI 加速器和 GPU 至关重要。HBM4E 是 HBM4 的增强版本，预计将提供比 HBM3E 更高的带宽和容量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://biz.chosun.com/en/en-it/2026/03/17/KMCM2WMLBRHI7LGRQMLJ2FZAXQ/">Samsung unveils fastest HBM 4 E at US GTC, tightens... - CHOSUNBIZ</a></li>
<li><a href="https://m-en.yna.co.kr/view/AEN20260316009051320?section=economy-finance/economy">(LEAD) Samsung unveils HBM 4 E sample; Nvidia CEO highlights closer...</a></li>

</ul>
</details>

**标签**: `#HBM`, `#SK Hynix`, `#memory`, `#AI hardware`, `#semiconductor`

---

<a id="item-8"></a>
## [谷歌与 UCSD 将旧 Pixel 手机改造成低成本数据中心](https://www.ithome.com/0/964/204.htm) ⭐️ 7.0/10

加州大学圣地亚哥分校（UCSD）的研究人员与谷歌合作，将废弃的 Pixel 智能手机改造成数据中心通用计算集群，以极低的成本实现了与服务器 CPU 相当的单核性能。 这种方法为预算有限的机构提供了一种可持续且经济高效的替代方案，通过赋予旧手机作为计算节点的第二次生命来减少电子垃圾。它可能使学校和小型研究实验室更容易获得计算资源。 研究团队拆除了屏幕、电池等非必要组件，安装标准 Linux 发行版，并部署 Kubernetes 进行容器编排。基准测试显示，25-50 部旧手机的总算力相当于一台双路服务器 CPU。

rss · ITHome Feed · 6月14日 23:56

**背景**: 隐含碳排放（Embodied Carbon）指设备制造过程中产生的碳排放，涵盖其整个生命周期。标准性能评估公司（SPEC）提供标准化的基准测试来比较计算系统性能。Kubernetes 是一个开源的容器编排平台，广泛应用于数据中心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Standard_Performance_Evaluation_Corporation">Standard Performance Evaluation Corporation - Wikipedia</a></li>
<li><a href="https://kubernetes.io/zh-cn/docs/home/">Kubernetes 文档 | Kubernetes</a></li>
<li><a href="http://www.tanpaifang.com/tanguwen/2023/0323/95610.html">什么是隐含碳（Embodied Carbon）？_碳排放交易网——全球领先的碳市场...</a></li>

</ul>
</details>

**标签**: `#sustainability`, `#data center`, `#recycling`, `#edge computing`, `#Kubernetes`

---

<a id="item-9"></a>
## [中国电动自行车变速器初创公司洛梵狄完成 B+轮融资](https://36kr.com/p/3853252135654660?f=rss) ⭐️ 6.0/10

中国电动自行车变速器初创公司洛梵狄已完成数千万元 B+轮融资，投资方包括国泰海通、达晨财智和广州黄埔科创母基金。资金将用于研发、产能扩张和全球销售网络建设，重点开发下一代智能内变速器，扭矩可达 200Nm。 本轮融资标志着中国供应商正在挑战禧玛诺、博世等巨头在电动自行车变速器市场的长期垄断。洛梵狄的高扭矩智能变速器可帮助电动自行车品牌实现产品差异化，并加速全球电动自行车的普及。 洛梵狄的 UHT（超大扭矩）技术将其智能内变速器的输入扭矩上限提升至 200Nm，而禧玛诺主流产品为 85Nm，enviolo HD 为 100Nm。该系统通过 AI 算法在毫秒级内自动换挡，可提升续航里程达 30%。

rss · 36Kr Feed · 6月15日 01:30

**背景**: 内变速器将传动机构置于后轮花鼓内部，相比外变速器维护更少且不受天气影响。在电动自行车中应用日益广泛，欧洲高端车型渗透率已超 40%。然而，传统内变速器难以承受现代电动自行车电机的高扭矩，限制了性能和耐用性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.lofandi.com/">内变速器, 自动内三速, 内五速, 自行车锁, 智能刹车锁 – 洛梵狄</a></li>
<li><a href="https://www.36kr.com/p/2896203538225793">突破eBike硬核壁垒技术，这家广东公司要抢千亿老牌外企垄断市场丨潜伏...</a></li>
<li><a href="https://enviolo.com/">Enviolo - Stepless Bicycle Transmissions and Automatic ...</a></li>

</ul>
</details>

**标签**: `#eBike`, `#hardware`, `#funding`, `#transmission`, `#startup`

---

<a id="item-10"></a>
## [网件起诉 TP-Link 虚假宣传为美国公司](https://www.ithome.com/0/964/232.htm) ⭐️ 6.0/10

网件于 2026 年 6 月 11 日对 TP-Link 提起反诉，指控 TP-Link 虚假宣称自己是美国公司，导致网件损失数千万美元销售额。TP-Link 回应称该反诉不准确且歪曲事实。 这场法律战凸显了对外国制造网络设备日益增长的国家安全担忧，并可能重塑美国路由器市场的营销实践。结果可能影响消费者信任以及美国本土品牌与外资品牌之间的竞争。 网件长达 49 页的反诉书指出，尽管 TP-Link 声称于 2024 年剥离中国业务，但其仍是一家从中国子公司采购研发和制造的中国公司。TP-Link 美国官网称其总部位于加州尔湾，且不向中国大陆客户销售产品。

rss · ITHome Feed · 6月15日 01:30

**背景**: 2026 年 3 月，FCC 以国家安全风险为由，禁止在美国销售新的外国制造 Wi-Fi 路由器，网件和 Eero 获得临时豁免。TP-Link 此前于 2025 年 11 月起诉网件，指控其发起抹黑运动导致 TP-Link 损失超过 10 亿美元销售额。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wired.com/story/us-government-foreign-made-router-ban-explained/">What You Need to Know About the Foreign-Made Router Ban in ...</a></li>
<li><a href="https://www.cnet.com/home/internet/the-fcc-just-banned-the-sale-of-new-foreign-made-wifi-routers-but-two-major-brands-have-already-gained-an-exemption/">Netgear and Eero Get Exemption From FCC's Ban of New Foreign ...</a></li>
<li><a href="https://cybernews.com/news/tp-link-lawsuit-netgear-orchestrating-smear-campaign/">TP-Link sues Netgear over alleged smear campaign | Cybernews</a></li>

</ul>
</details>

**标签**: `#networking`, `#legal`, `#business`, `#TP-Link`, `#Netgear`

---

<a id="item-11"></a>
## [计算机历史博物馆从德国仓库回收 2000 余件文物](https://www.ithome.com/0/964/208.htm) ⭐️ 6.0/10

计算机历史博物馆（CHM）回顾了其最大规模的复古计算文物回收行动，从德国卡斯特罗普-劳克塞尔的一座废弃仓库中发掘出 2000 多件物品，装满了 7 辆重型半挂卡车。 这批藏品保存了从 20 世纪 30 年代到 80 年代的稀有计算历史，包括冷战时期的东欧集团机型，丰富了 CHM 的馆藏，用于研究和教育。 这批藏品由亚琛工业大学的一位教授收集，2006 年经当地税务顾问爆料后发现。清理工作曾因附近发现一枚未爆炸的二战炸弹而短暂中断。

rss · ITHome Feed · 6月15日 00:19

**背景**: 位于加州山景城的计算机历史博物馆是世界上最大的计算历史博物馆。此次回收是其最大规模的一次收购，跨越多个计算时代，包括罕见的大型机、小型机和存储介质。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/computer-history-museum-recalls-astonishing-retro-haul-recovered-from-abandoned-german-warehouse-over-2-000-artifacts-spanning-the-1930s-to-1980s-required-seven-tractor-trailers-after-a-wwii-bomb-scare">Computer History Museum recalls ‘astonishing’ retro haul ...</a></li>

</ul>
</details>

**标签**: `#computer history`, `#retro computing`, `#museum`, `#artifact recovery`

---

<a id="item-12"></a>
## [黑灯工厂：中国年轻人就业的威胁？](https://www.dw.com/zh/%E9%BB%91%E7%81%AF%E5%B7%A5%E5%8E%82-%E7%85%A7%E4%B8%8D%E4%BA%AE%E4%B8%AD%E5%9B%BD%E5%B9%B4%E8%BD%BB%E4%BA%BA%E7%9A%84%E5%B0%B1%E4%B8%9A%E4%B9%8B%E8%B7%AF/a-77527764?maca=chi-rss-chi-all-1127-rdf) ⭐️ 6.0/10

德国之声的一篇分析质疑，中国快速推广的“黑灯工厂”（全自动化、无人工厂）是否正在削弱年轻人的就业前景，因为自动化正在取代制造业中的人力劳动。 这很重要，因为中国在推动人工智能和机器人技术领先地位的同时，正面临青年失业危机；技术进步与就业创造之间的张力可能影响该国的经济和社会稳定。 文章指出，格力等公司在实施黑灯工厂后，工厂员工从 1 万人减少到 1000 人；据行业估计，中国目前生产了全球 40%以上的机器人。

rss · DW Chinese · 6月14日 07:08

**背景**: “黑灯工厂”是指完全自动化的制造设施，可以在极少或无人值守的情况下运行，通常使用机器人和人工智能。中国将机器人和人工智能作为产业升级战略的重点投资领域，但这引发了关于就业替代的担忧，尤其是对进入劳动力市场的年轻工人。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://36kr.com/p/1319989636202889">黑 灯 工 厂 、无人 工 厂 只是巨头进军 工 业互联网的“样板间”？ -36氪</a></li>
<li><a href="http://paper.people.com.cn/rmrb/images/2024-05/29/18/rmrb2024052918.pdf">CHJZKRMRB18B20240529C</a></li>
<li><a href="https://www.engineering.org.cn/sscae/EN/PDF/10.15302/J-SSCAE-2026.01.021">我 国 高档数控 机 床与 机 器 人 产 业 十年发展回顾与展望</a></li>

</ul>
</details>

**标签**: `#AI`, `#automation`, `#employment`, `#China`, `#robotics`

---

<a id="item-13"></a>
## [英国首相斯塔默宣布对 16 岁以下青少年实施‘澳大利亚加强版’社交媒体禁令](https://www.theguardian.com/uk-news/2026/jun/14/starmer-to-announce-australia-plus-ban-on-social-media-for-under-16s) ⭐️ 6.0/10

英国首相基尔·斯塔默将宣布禁止 16 岁以下青少年使用 TikTok、Instagram 和 X 等主要社交媒体应用，并对游戏应用施加额外限制，防止其与陌生人聊天。 这标志着英国在线安全监管的重大升级，可能为其他国家树立先例，并迫使科技公司实施更严格的年龄验证和内容审核。 这项被称为‘澳大利亚加强版’的禁令超越了澳大利亚现行法律，还对 16 岁以下青少年的游戏应用功能进行限制，例如移除与陌生人聊天的功能。

rss · The Guardian World · 6月14日 21:42

**背景**: 目前，主要社交媒体平台的最低年龄为 13 岁，但英国没有官方政府规定的年龄限制。此举是在对儿童心理健康和在线安全的担忧日益加剧的背景下做出的，澳大利亚已于 2024 年通过了类似的 16 岁以下青少年禁令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/uk-news/2026/jun/14/what-is-uk-introducing-australia-plus-social-media-ban-how-will-it-work">Why is the UK launching an ‘ Australia plus ’ social media ban and...</a></li>
<li><a href="https://www.reuters.com/legal/litigation/uk-pm-starmer-set-ban-harmful-social-media-under-16s-2026-06-08/">UK PM Starmer set to ban 'harmful' social media for under-16s | Reuters</a></li>

</ul>
</details>

**标签**: `#social media`, `#regulation`, `#UK policy`, `#youth safety`

---

<a id="item-14"></a>
## [远程医疗公司在减肥药使用中的双重角色引发担忧](https://www.npr.org/2026/06/14/nx-s1-5805984/glp1-telehealth-weight-loss-drugs) ⭐️ 6.0/10

像 Vida Health 这样的远程医疗公司正在为服用 Wegovy 和 Zepbound 等减肥药的患者提供生活方式支持计划，同时雇主也要求它们控制这些昂贵药物的支出。 这种双重角色造成了利益冲突，可能损害患者护理，因为远程医疗提供者可能为了达到节省成本的目标而限制药物获取。初级保健医生担心这一趋势会破坏医患关系，并可能导致治疗不足。 生活方式支持计划包括虚拟辅导和健康计划，旨在减少对处方的依赖。雇主正在利用远程医疗将减肥药覆盖与健康计划捆绑，作为基于价值的福利策略。

rss · NPR News · 6月14日 09:00

**背景**: 像 GLP-1 激动剂（如 Wegovy、Zepbound）这样的减肥药非常有效但价格昂贵，每月费用超过 1000 美元。提供健康保险的雇主正在寻求在不取消覆盖的情况下管理这些成本的方法。远程医疗公司介入提供临床支持和成本控制机制，但这种双重任务引发了伦理问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.npr.org/2026/06/14/nx-s1-5805984/glp1-telehealth-weight-loss-drugs">Telehealth companies limit who gets weight loss drugs : NPR</a></li>
<li><a href="https://www.mcknightsseniorliving.com/news/telehealth-giants-pairing-obesity-drugs-with-weight-loss-programs-to-prevent-overreliance-on-prescriptions/">Telehealth giants pairing obesity drugs with weight-loss programs to...</a></li>
<li><a href="https://www.linkedin.com/pulse/how-employers-leveraging-direct-telehealth-control-rob-gillespie--xusde">How Employers Are Leveraging Direct Telehealth to Control Rising...</a></li>

</ul>
</details>

**标签**: `#telehealth`, `#obesity drugs`, `#healthcare`, `#employer benefits`

---

<a id="item-15"></a>
## [Anthropic 暂停模型访问，印度反思 AI 未来](https://techcrunch.com/2026/06/13/as-anthropic-suspends-access-to-new-models-india-debates-its-ai-future/) ⭐️ 6.0/10

Anthropic 已暂停在印度对其最新 AI 模型的访问，这引发了印度国内关于其 AI 战略及自主必要性的大讨论。 这一事件凸显了依赖外国 AI 模型的地缘政治风险，可能加速印度推动自主研发基础模型和 AI 基础设施。 据报道，此次暂停源于美国指令，印度科技领袖现在呼吁国内研发和开源模型以减少依赖。

rss · TechCrunch · 6月14日 03:00

**背景**: Anthropic 是一家领先的 AI 公司，以其 Claude 系列大型语言模型闻名，这些模型采用宪法 AI 进行安全训练。印度一直在推进 AI 自主，已有 12 家公司利用 38000 块 GPU 以补贴价格开发基础模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model) - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/posts/satyendra_india-accelerates-ai-self-reliance-12-companies-activity-7383183623908319233-adMM">India 's AI self - reliance : 12 companies lead foundation... | LinkedIn</a></li>
<li><a href="https://economictimes.indiatimes.com/tech/artificial-intelligence/anthropics-fable-5-takedown-triggers-india-inc-push-for-ai-self-reliance/articleshow/131698077.cms">Anthropic’s Fable 5 takedown triggers India Inc push for AI ...</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#Anthropic`, `#India`, `#geopolitics`

---

<a id="item-16"></a>
## [FBI 建造模拟小镇用于网络攻击演练](https://www.theverge.com/tech/949648/fbi-fake-town-cyberattacks-kinetic-cyber-range) ⭐️ 6.0/10

FBI 在阿拉巴马州亨茨维尔开设了一个占地 22000 平方英尺的模拟小镇，名为 Kinetic Cyber Range，用于模拟网络攻击以进行培训。 该设施为 FBI 特工及合作伙伴提供了逼真的实践环境，用于练习应对网络威胁，弥合了课堂学习与现实事件之间的差距。 该小镇包括便利店、加油站、医院和带家具的房屋，所有设施通过 200 多台服务器连接，以模拟真实的数字基础设施。

rss · The Verge · 6月14日 20:35

**背景**: FBI 的 Kinetic Cyber Range 仿照弗吉尼亚州匡提科著名的战术训练设施 Hogan's Alley 建造，但专注于网络犯罪。它让受训者体验物理与数字威胁交织的真实场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fbi.gov/news/stories/inside-the-fbis-kinetic-cyber-range">Inside the FBI ’s Kinetic Cyber Range — FBI</a></li>
<li><a href="https://xeber.world/en/article/fbi-cyber-range-a-fake-town-built-for-cyberattack-simulation-training-bd6c18">FBI Cyber Range : Fake Town Built for Cyberattack Simulation Training</a></li>
<li><a href="https://cybernews.com/cybercrime/fbi-kinetic-cyber-range-training/">First look at the FBI 's "Kinetic Cyber Range " | Cybernews</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#FBI`, `#training`, `#simulation`

---

<a id="item-17"></a>
## [中国加速地下管网更新，纳入“六网”战略](https://www.chinanews.com.cn/sh/2026/06-15/10640505.shtml) ⭐️ 5.0/10

中国正在实施一项国家战略，对老化的地下管网进行更新改造，涵盖供水、燃气、排水、供热等管线，作为更广泛的“六张网”基础设施计划的一部分。目标是在“十五五”期间改造约 77 万公里管线。 老化的地下管网导致漏损、内涝和频繁的道路开挖，威胁城市安全和日常生活。这一大规模更新改造旨在使城市“生命线”现代化，提高防洪能力，为数亿居民提供可靠的公用事业服务。 该计划涉及燃气管道约 20 万公里、排水管道约 17.5 万公里、供水管道约 17.5 万公里、污水管道约 10 万公里、供热管道约 12 万公里。传感器、人工智能和智能监控系统等先进技术正在部署，以实时检测泄漏和预测故障。

rss · China News Service Scroll · 6月15日 01:58

**背景**: 中国拥有世界上规模最大的地下管网，但许多管道已超过设计寿命，导致漏损和排水不足。暴雨期间的城市内涝已成为紧迫问题。“六张网”计划是一项国家战略，旨在升级交通、水、能源和地下管网等基础设施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.online.sh.cn/news/gb/content/2026-06/11/content_10459222.htm">建设“好房子”，改造老旧小区、老旧街区厂区…… 城 市 更新聚焦23...</a></li>
<li><a href="https://news.cri.cn/20260612/125dcd84-b918-44fc-85c1-dc62c6eb09cd.html">一线调研丨地下管网加速焕新升级 让城市“里子”更扎实</a></li>
<li><a href="https://www.sohu.com/a/895304529_121123903">事关地下管网更新改造，住建部发布新一批城市公共供水管网漏损治理可...</a></li>

</ul>
</details>

**标签**: `#infrastructure`, `#urban planning`, `#civil engineering`, `#China`

---

<a id="item-18"></a>
## [黑土地保护会议展示中国进展](https://www.chinanews.com.cn/gn/2026/06-14/10640336.shtml) ⭐️ 5.0/10

300 余位中外专家齐聚长春，参加第六届黑土地保护利用国际会议暨 FAO 国际黑土联盟年会，围绕黑土地健康培育、产能提升、智慧农业发展和生态屏障建设展开研讨。 此次会议是两大黑土地国际学术会议首次联合举办，彰显了中国在黑土地保护和可持续农业方面的领导地位，对全球粮食安全和气候韧性至关重要。 会议由中国科学院东北地理与农业生态研究所主办，联合国粮农组织国际黑土联盟、世界黑土联合会等协办，会期为 6 月 12 日至 15 日。

rss · China News Service China · 6月14日 12:50

**背景**: 黑土地是地球上最肥沃的土壤之一，但面临集约化耕作导致的退化。中国于 2021 年启动“黑土粮仓”科技会战，组织全国 98 家单位、1300 余名科研人员开展黑土地保护与修复科技攻关。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://www.jl.xinhuanet.com/20260613/10ba3b3dbc0948f1907a8b5204427404/c.html">第六届黑土地保护利用国际会议暨FAO国际黑土联盟第七届年会在长春召开...</a></li>
<li><a href="https://www.jl.gov.cn/yaowen/202606/t20260614_3642538.html">两大黑土地国际学术会议首度牵手 大会开幕式在长举办</a></li>
<li><a href="https://www.ncsti.gov.cn/kjdt/kjrd/202606/t20260609_249229.html">“ 黑 土 粮 仓 ” 科 技 会 战 交出5年“成绩单”</a></li>

</ul>
</details>

**标签**: `#agriculture`, `#soil conservation`, `#environmental science`, `#conference`

---

<a id="item-19"></a>
## [半固态凝胶电池为全固态电池提供实用过渡方案](https://www.theverge.com/column/948594/solid-state-batteries-semi-solid-state) ⭐️ 5.0/10

The Verge 的 Thomas Ricker 指出，全固态电池尚未具备商业可行性，而半固态（凝胶）电池作为一种更安全、更实用的中间方案，已开始进入市场。 这很重要，因为电池行业迫切需要比锂离子电池更安全、能量密度更高的替代品，而半固态凝胶电池无需等待全固态电池的突破即可提供渐进式改进。 半固态电池采用凝胶状电解质，相比液态电解质降低了热失控风险，同时比真正的全固态电池更易制造。文章指出，挥发性液态电解质会起火，而半固态凝胶则不会。

rss · The Verge · 6月14日 12:00

**背景**: 锂离子电池主导着便携式电子设备和电动汽车市场，但由于使用易燃液态电解质而存在安全风险。全固态电池用固态电解质替代液态电解质，有望实现更高的能量密度和安全性，但在制造、界面稳定性和长期性能方面面临挑战。半固态电池采用混合凝胶电解质作为过渡方案，在降低生产难度的同时提供部分固态电池的优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/column/948594/solid-state-batteries-semi-solid-state">Solid - state batteries still aren’t ready, but gels are | The Verge</a></li>
<li><a href="https://www.nature.com/articles/s41560-023-01208-9">Challenges in speeding up solid-state battery development</a></li>
<li><a href="https://axial.acs.org/energy/solid-state-battery-advancements-challenges-and-industry-impacts">Solid-State Battery Advancements, Challenges, and Industry ...</a></li>

</ul>
</details>

**标签**: `#batteries`, `#solid-state`, `#energy storage`, `#technology`

---

<a id="item-20"></a>
## [公安部公布 10 起网络谣言典型案例](https://www.chinanews.com.cn/gn/2026/06-15/10640436.shtml) ⭐️ 4.0/10

2026 年 6 月 15 日，公安部网安局公布了 10 起打击整治网络谣言违法犯罪的典型案例，展示了持续的执法行动。 这一公告凸显了中国政府对规范网络言论和打击虚假信息的持续关注，影响了中国的互联网治理和用户行为。 这些案例从公众举报中选出，代表了网络谣言犯罪的典型模式，但摘要中未披露具体技术细节或法律处罚。

rss · China News Service China · 6月15日 00:10

**背景**: 中国的网络谣言可能导致社会不稳定，一直是执法重点。公安部定期公布此类案例以震慑违法行为并教育公众。

**标签**: `#cybersecurity`, `#law enforcement`, `#China`, `#online rumors`

---

<a id="item-21"></a>
## [新一轮厄尔尼诺现象已宣布，可能成为超级厄尔尼诺](https://www.bbc.com/zhongwen/articles/cly0ne5y8x5o/trad?at_medium=RSS&at_campaign=rss) ⭐️ 4.0/10

美国机构宣布热带太平洋出现新一轮厄尔尼诺现象，近几个月海面温度急剧上升。许多预测显示，这次事件可能形成“超级”厄尔尼诺，甚至可能是有记录以来最强之一。 厄尔尼诺事件会显著扰乱全球天气模式，在世界各地引发干旱、洪水等极端天气。超级厄尔尼诺可能对农业、水资源和生态系统造成严重影响，影响数十亿人口。 超级厄尔尼诺事件定义为太平洋部分海域海面温度比平均水平高出 2°C 或以上。上一次超级厄尔尼诺发生在 2015-2016 年，导致随后几年墨西哥湾飓风强度增强。

rss · BBC Chinese · 6月14日 03:12

**背景**: 厄尔尼诺是一种气候模式，表现为赤道太平洋海域异常升温，影响全球天气。通常每 2-7 年发生一次，持续 9-12 个月。相反相位拉尼娜则带来降温。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Super_El_Niño_events">Super El Niño events - Wikipedia</a></li>
<li><a href="https://www.aol.com/articles/super-el-ni-o-coming-223525902.html">Is a Super El Niño Coming in 2026? Here’s What Scientists Are... - AOL</a></li>

</ul>
</details>

**标签**: `#climate`, `#El Niño`, `#environment`

---

<a id="item-22"></a>
## [中国推动铁路旅游融合，2030 年前打造 160 列以上旅游列车](https://www.chinanews.com.cn/sh/2026/06-15/10640459.shtml) ⭐️ 3.0/10

中国宣布多项措施促进铁路与旅游融合发展，包括加快铁路基础设施旅游化改造、打造游客专属候车区、鼓励社会资本参与旅游列车设施改造，目标到 2030 年打造 160 列以上铁路旅游列车专用车组。 该政策旨在利用广泛的铁路网络促进国内旅游和经济增长，可能使旅行更加便捷和吸引游客。 措施包括设置便捷换乘通道，鼓励各类社会资本参与旅游列车设备设施改造。目标是在 2030 年前打造 160 列以上旅游列车。

rss · China News Service Scroll · 6月15日 01:17

**背景**: 中国拥有庞大的铁路网络，将旅游与铁路服务融合被视为促进国内旅游的一种方式。其他国家也有类似举措，如瑞士和日本的观光列车线路。

**标签**: `#policy`, `#railway`, `#tourism`, `#infrastructure`

---

<a id="item-23"></a>
## [湖北推动非遗融入日常生活](https://www.chinanews.com.cn/sh/2026/06-15/10640447.shtml) ⭐️ 3.0/10

湖北省于 2026 年 6 月 14 日启动文化遗产活动，展示近 100 项非物质文化遗产项目和 200 余件文创产品，旨在将非遗融入日常生活。 该活动通过让公众接触非遗，有助于保护和振兴非物质文化遗产，促进文化欣赏并为当地手工艺人创造经济机会。 活动以“非遗，让生活更美好”为主题，在黄冈举行，并与文化和自然遗产日消夏购物月同步，展示了近 100 项代表性非遗项目。

rss · China News Service Scroll · 6月15日 01:01

**背景**: 非物质文化遗产包括代代相传的传统、表演艺术、手工艺和知识。湖北拥有丰富的文化遗产，此类活动旨在将这些项目从博物馆带入日常生活。

**标签**: `#cultural heritage`, `#event`, `#China`

---

<a id="item-24"></a>
## [神舟二十三号乘组在轨第三周动态](https://www.chinanews.com.cn/gn/2026/06-15/10640497.shtml) ⭐️ 2.0/10

神舟二十三号乘组（指令长朱杨柱、航天员张志远、载荷专家黎家盈）已在轨工作生活三周，近期完成了日常维护和科学实验等任务。 此次任务首次有来自港澳地区的第四批航天员执行飞行，彰显了中国航天计划的扩展与国际合作。例行更新确认了乘组健康状况良好、任务稳步推进。 乘组中黎家盈是中国首位从港澳地区选拔的女性载荷专家。任务于 2026 年 5 月 24 日在酒泉由长征二号 F 火箭发射升空。

rss · China News Service Scroll · 6月15日 01:55

**背景**: 神舟是中国载人飞船系列。神舟二十三号任务属于中国空间站建造与运营阶段。乘组将在天宫空间站驻留约六个月。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.qq.com/rain/a/20260524V08WDT00">news.qq.com/rain/a/20260524V08WDT00</a></li>
<li><a href="https://news.xmnn.cn/gnxw/202605/t20260523_430318.html">神二十三乘组确定： 朱 杨 柱 、 张 志 远 、 黎 家 盈 _新闻频道_厦门网</a></li>

</ul>
</details>

**标签**: `#space`, `#astronauts`, `#China`

---

<a id="item-25"></a>
## [青年农机手赋能现代农业](https://www.chinanews.com.cn/gn/2026/06-15/10640491.shtml) ⭐️ 2.0/10

文章讨论了推动组织管理规范化、作业接单网络化、农机调配共享化，以赋能青年农机手。 这一举措可以提高效率并吸引年轻人从事农业，支持中国的农业现代化目标。 重点在于三个方面：管理规范化、作业接单网络化和农机调配共享化，共同旨在优化农机使用。

rss · China News Service Scroll · 6月15日 01:51

**背景**: 中国农业面临劳动力老龄化和机械化效率低的问题。青年农机手通过数字化工具和共享服务被视为现代化的关键。

**标签**: `#agriculture`, `#China`, `#modernization`

---

<a id="item-26"></a>
## [前 5 个月中国铁路多项指标创新高](https://www.chinanews.com.cn/cj/2026/06-15/10640487.shtml) ⭐️ 2.0/10

据国铁集团消息，今年 1 至 5 月，中国铁路客货运量均创历史新高。 这表明中国经济活动活跃，铁路运营高效，反映了国家交通基础设施的绩效。 该报告涵盖客运和货运量，1 至 5 月期间多项指标均创历史新高。

rss · China News Service Scroll · 6月15日 01:49

**背景**: 铁路是中国重要的运输方式，用于客运和货运物流。国铁集团定期发布运营数据以监测经济趋势。

**标签**: `#railway`, `#transportation`, `#China`

---

<a id="item-27"></a>
## [A 股周一开盘普涨，三大指数集体高开](https://www.chinanews.com.cn/cj/2026/06-15/10640477.shtml) ⭐️ 2.0/10

周一 A 股三大指数集体高开，超 3600 只个股上涨，贵金属、海运、航空板块领涨，煤炭、油气、航天军工板块下跌。 这一市场走势反映了短期投资者情绪和板块轮动，可能影响交易者和基金经理的投资组合策略。但作为常规每日行情，对长期科技或工程趋势意义有限。 上证指数、深证成指和创业板指均高开。贵金属板块大涨，煤炭板块领跌，油气、航天军工板块紧随其后。

rss · China News Service Scroll · 6月15日 01:40

**背景**: A 股市场包括在上海和深圳交易所交易的股票。每日市场波动受经济数据、政策变化和全球事件影响，但单日涨跌往往是噪音而非长期趋势信号。

**标签**: `#finance`, `#stock market`, `#China`

---

<a id="item-28"></a>
## [央行开展 4250 亿元 7 天期逆回购操作](https://www.chinanews.com.cn/cj/2026/06-15/10640467.shtml) ⭐️ 2.0/10

2026 年 6 月 15 日，中国人民银行以固定利率 1.40%开展了 4250 亿元 7 天期逆回购操作，全额满足了一级交易商的需求。 此次操作表明央行维持银行体系短期流动性稳定的意图，对金融市场运行和经济活动至关重要。 操作采用固定利率、数量招标方式，1.40%的利率与当前 7 天期逆回购政策利率一致，该利率自 2024 年起成为主要短期政策利率。

rss · China News Service Scroll · 6月15日 01:35

**背景**: 逆回购是央行向一级交易商购买有价证券并约定 7 天后卖回的短期流动性调节工具。一级交易商是获准与央行直接交易的金融机构。该工具用于向银行体系注入流动性并引导短期利率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.thepaper.cn/newsDetail_forward_33299336">分析｜时隔22个月公开市场7天期逆回购操作量为零，释放了什么信号_金...</a></li>
<li><a href="https://finance.sina.com.cn/jryx/bank/2026-06-12/doc-iniccfxx0269708.shtml">央行今日开展3930亿元7天期逆回购操作_新浪财经_新浪网</a></li>
<li><a href="https://baike.baidu.com/item/7天期逆回购操作/67171684">7天期逆回购操作_百度百科</a></li>

</ul>
</details>

**标签**: `#finance`, `#central bank`, `#monetary policy`

---