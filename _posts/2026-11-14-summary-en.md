---
layout: default
title: "Horizon Summary: 2026-11-14 (EN)"
date: 2026-11-14
lang: en
---

> From 24 items, 13 important content pieces were selected

---

1. [Lovable apps leak passport details and 200K private messages](#item-1) ⭐️ 8.0/10
2. [TorchTitan scales 1T-parameter MoE to 1,300 tokens/s per GPU on 384 GH200s](#item-2) ⭐️ 8.0/10
3. [PyPI launches redesigned project pages highlighting security signals](#item-3) ⭐️ 7.0/10
4. [EFF Warns Tech Companies Are Redefining Privacy Again](#item-4) ⭐️ 7.0/10
5. [ICML 2027 introduces two-stage review and reciprocal reviewer rules](#item-5) ⭐️ 7.0/10
6. [Developer trains tiny transformer to predict personal blood sugar](#item-6) ⭐️ 7.0/10
7. [KDE Documentary Sparks Nostalgic Community Discussion](#item-7) ⭐️ 6.0/10
8. [Google Antigravity adds /teamwork multi-agent collaboration for science and engineering](#item-8) ⭐️ 6.0/10
9. [Terminactory: A Rust Terminal Factory Game with AI Agent Integration](#item-9) ⭐️ 6.0/10
10. [Interactive site compares all 13 versions of Monkey Island side by side](#item-10) ⭐️ 6.0/10
11. [Italy fines Meta $887M over Android users' data access](#item-11) ⭐️ 6.0/10
12. [Should short-horizon price forecasting papers benchmark against market-implied forecasts?](#item-12) ⭐️ 6.0/10
13. [Reddit User Seeks Ethical Alternatives to Kaggle Over Biometric Verification](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Lovable apps leak passport details and 200K private messages](https://www.crissyfield.de/research/lovable-en/) ⭐️ 8.0/10

Security research published on crissyfield.de reveals that apps built with the Lovable AI app builder expose sensitive data, including passport details and over 200,000 private messages, due to insecure default configurations. The issue stems from missing or misconfigured Supabase Row Level Security (RLS) policies in generated apps, allowing unauthorized access to database records. This incident highlights the systemic risk of AI-generated apps that prioritize speed over security, potentially affecting thousands of non-technical users who are unaware of the privacy implications. It also raises questions about platform responsibility, as both Lovable and Supabase face scrutiny for default settings that leave data exposed. The vulnerabilities are easy to exploit, requiring only basic inspection of network calls in a browser, and are widespread because many Lovable apps use Supabase with permissive defaults. A related Supabase discussion suggests that a fix for new projects was deployed on October 30, but existing projects may still be affected.

hackernews · armcat · Nov 14, 17:43 · [Discussion](https://news.ycombinator.com/item?id=50499017)

**Background**: Lovable is an AI-powered app builder that generates full-stack React and Supabase applications from natural-language prompts, enabling users without coding skills to create web apps quickly. Supabase is an open-source Firebase alternative that provides a Postgres database, authentication, and APIs; its security model relies on Row Level Security (RLS) policies to restrict data access. When RLS is not properly configured, the public API key (anon key) can allow anyone to read or write data, a common pitfall in AI-generated apps.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/lovable-ai-app-builder-customer-data/">Lovable AI App Builder Reportedly Exposes Thousands of ...</a></li>
<li><a href="https://dappasol.com/guides/lovable-security-vulnerabilities/">Lovable Security Vulnerabilities: Is It Safe? (2026)</a></li>
<li><a href="https://aithinkerlab.com/lovable-ai-security-vulnerabilities-vibe-hacking/">Lovable AI Security Vulnerabilities: 16 Flaws From 30 Days of ...</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree that AI-generated apps are easy targets due to insecure defaults and the sheer volume of such apps, with some drawing analogies to letting unlicensed people fly passenger planes. A key point of debate is Supabase's culpability: one commenter argues that Supabase's permissive defaults, a deliberate onboarding tradeoff, are partly to blame, while others note that similar breaches have hit other platforms like Railway.

**Tags**: `#security`, `#AI-generated apps`, `#data breach`, `#Supabase`, `#privacy`

---

<a id="item-2"></a>
## [TorchTitan scales 1T-parameter MoE to 1,300 tokens/s per GPU on 384 GH200s](https://www.reddit.com/r/MachineLearning/comments/1xvce5h/scaling_to_1t_moe_on_torchtitan_p/) ⭐️ 8.0/10

A team working with TorchTitan and PyTorch maintainers optimized training of a ~1T-parameter Mixture-of-Experts model to achieve ~1,300 tokens/s per GPU on 384 GH200 GPUs, a 14X improvement over their starting point. They shared lessons on parallelism strategies, including choosing FSDP plus expert parallelism over pipeline parallelism, and performance tuning techniques. This demonstrates that PyTorch-native tooling like TorchTitan can scale to trillion-parameter MoE models on modern hardware, providing a practical blueprint for large-scale training. The lessons on parallelism and memory optimization are valuable for practitioners pushing the limits of distributed training. The team used 384-way FSDP with 4-way expert parallelism kept within a node, and avoided pipeline parallelism to reduce step latency. Key optimizations included full activation checkpointing (4X speedup), offloading activations to Grace CPU over the 900 GB/s C2C link, and using the Muon optimizer instead of Adam to fit 64k-token sequences.

reddit · r/MachineLearning · /u/f14-bertolotti · Nov 13, 16:28

**Background**: Mixture-of-Experts (MoE) is a technique where multiple expert networks specialize in different parts of the input space, allowing models to have many parameters while keeping compute per token manageable. TorchTitan is a PyTorch-native platform for large-scale training, and GH200 is a GPU from NVIDIA that combines a Grace CPU and Hopper GPU with high-bandwidth interconnect, used in the JUPITER supercomputer. FSDP (Fully Sharded Data Parallel) shards model weights across GPUs, while expert parallelism assigns different experts to different GPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/pytorch/torchtitan">GitHub - pytorch/torchtitan: A PyTorch native platform for ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://spotgpus.com/compare/h200-sxm-vs-gh200">H200 vs GH 200 : specs, price per hour, which to rent (2026) | SpotGPUs</a></li>

</ul>
</details>

**Tags**: `#large-scale-training`, `#mixture-of-experts`, `#PyTorch`, `#distributed-training`, `#GPU-optimization`

---

<a id="item-3"></a>
## [PyPI launches redesigned project pages highlighting security signals](https://blog.pypi.org/posts/2026-11-06-ui-updates-complete/) ⭐️ 7.0/10

PyPI has rolled out redesigned project pages that prominently display security signals such as provenance attestations, making it easier for users to see whether a release was built and published through a trusted pipeline. Because PyPI is critical infrastructure for the Python ecosystem, surfacing provenance directly on project pages could encourage wider adoption of trusted publishing and help developers spot supply-chain risks before installing a package. The provenance signals are based on PEP 740 attestations and Sigstore-style keyless signing, but they primarily detect tampered releases of formerly benign projects rather than flagging intentionally malicious packages from the start.

hackernews · rbanffy · Nov 14, 15:40 · [Discussion](https://news.ycombinator.com/item?id=50497892)

**Background**: Provenance attestations are verifiable records of how and where a package was built, often tied to a CI/CD identity via OIDC. Sigstore's keyless signing uses short-lived certificates from Fulcio and an append-only transparency log called Rekor, eliminating long-lived signing keys. PyPI's trusted publishing lets maintainers upload packages directly from CI providers without storing API tokens.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.pypi.org/using-pypi/package-security/provenance/">Checking Provenance ( package origin) - PyPI User Documentation</a></li>
<li><a href="https://docs.sigstore.dev/cosign/signing/overview/">Overview - Sigstore</a></li>
<li><a href="https://matrixgard.com/blog/npm-pypi-provenance-attestation-supply-chain-2026/">Valid Provenance , Malicious Package: What Attestations Buy You</a></li>

</ul>
</details>

**Discussion**: Commenters welcomed the increased visibility of provenance but debated its limits: some worried that trust is becoming centralized around big cloud CI providers and creating lock-in, while others noted that provenance detects tampered entries, not malicious projects, and asked for trusted publishing to support reusable workflows.

**Tags**: `#pypi`, `#supply-chain-security`, `#sigstore`, `#python`, `#provenance`

---

<a id="item-4"></a>
## [EFF Warns Tech Companies Are Redefining Privacy Again](https://www.eff.org/deeplinks/2026/11/tech-companies-are-trying-shift-entire-concept-privacy-again) ⭐️ 7.0/10

The Electronic Frontier Foundation published an analysis arguing that tech companies are once again attempting to shift the entire concept of privacy, a topic that sparked a Hacker News discussion with 342 points and 133 comments. This matters because the redefinition of privacy by tech companies can weaken legal protections and normalize surveillance, affecting everyday users and workers who face AI recording in meetings and monitoring tools. The EFF article is part of its ongoing advocacy for user privacy and free expression, and the community discussion highlights practical concerns like AI notetakers recording professional meetings and the difficulty of opting out without risking employment.

hackernews · gslin · Nov 14, 12:45 · [Discussion](https://news.ycombinator.com/item?id=50496602)

**Background**: The Electronic Frontier Foundation (EFF) is a leading nonprofit founded in 1990 that defends civil liberties in the digital world through litigation, policy analysis, and activism. Tech companies have increasingly introduced features like AI notetakers and workplace monitoring, which raise questions about consent and data collection. The Universal Declaration of Human Rights, Article 12, protects against arbitrary interference with privacy, a principle often cited in these debates.

<details><summary>References</summary>
<ul>
<li><a href="https://www.eff.org/about">About EFF | Electronic Frontier Foundation</a></li>
<li><a href="https://www.eff.org/issues/privacy">Privacy | Electronic Frontier Foundation</a></li>

</ul>
</details>

**Discussion**: Commenters expressed frustration with the ubiquity of AI recording in professional settings, with one asking how to minimize exposure when opting out seems impossible. Others cited the UN Universal Declaration of Human Rights and compared current recording products to the backlash against Google Glass, while some suggested practical strategies like using throwaway identities and supporting organizations like EFF.

**Tags**: `#privacy`, `#AI`, `#surveillance`, `#EFF`, `#tech policy`

---

<a id="item-5"></a>
## [ICML 2027 introduces two-stage review and reciprocal reviewer rules](https://www.reddit.com/r/MachineLearning/comments/1xvkxbj/icml_2027_changes_d/) ⭐️ 7.0/10

ICML 2027's Call for Papers introduces a two-stage review process where area chairs decide whether a paper proceeds to full review, with any first-stage rejection requiring confirmation by a senior area chair and authors receiving a short justification by February 23. It also caps authors at 20 submissions, requires each paper to name a reciprocal reviewer from its author list (max 6 papers per reviewer), mandates program committee service for anyone with 3 or more submissions, and limits each author to at most one paper with no eligible reciprocal reviewer. These changes directly target the submission explosion and reviewer overload that have strained major ML conferences for years, and they could set a precedent for other venues like ICLR and IJCAI that are also experimenting with reciprocal reviewing. Authors, especially those with many coauthors who cannot review, will face new constraints on how many papers they can submit. The first-stage rejection is subject to a senior area chair check, which may mitigate concerns about quick area chair reads missing good papers, but the policy still gives area chairs significant gatekeeping power. The per-author cap of 20 submissions and the requirement that anyone with 3 or more submissions serve on the program committee tie authorship volume directly to reviewing duty, and non-compliant papers may be desk rejected.

reddit · r/MachineLearning · /u/Gravitist · Nov 13, 21:53

**Background**: ICML is one of the premier international conferences on machine learning, and in recent years its submission numbers have grown rapidly, putting immense pressure on the volunteer reviewer pool. Many conferences have responded with policies such as reciprocal reviewing, where authors are required to review for the conference, and ICLR 2027 and IJCAI 2027 have adopted similar reciprocal review requirements. The two-stage review process is a mechanism to screen out clearly out-of-scope or low-quality submissions early, reducing the burden on full reviewers.

<details><summary>References</summary>
<ul>
<li><a href="https://icml.cc/">2027 Conference</a></li>
<li><a href="https://iclr.cc/Conferences/2027/AuthorGuidelines">ICLR 2027 Author Guidelines</a></li>
<li><a href="https://2027.ijcai.org/reciprocal-review-policy/">Reciprocal Review Policy – IJCAI 2027</a></li>

</ul>
</details>

**Discussion**: The Reddit poster finds the changes a reasonable fix for out-of-control reviewer load and agrees that tying authorship volume to reviewing duty is fair, but worries that a quick first-stage area chair read could miss good papers, though the senior area chair check helps. They ask whether this will push the problem elsewhere.

**Tags**: `#machine-learning`, `#peer-review`, `#academic-publishing`, `#conference-policy`, `#ICML`

---

<a id="item-6"></a>
## [Developer trains tiny transformer to predict personal blood sugar](https://www.reddit.com/r/MachineLearning/comments/1xvja5n/i_have_trained_a_model_to_predict_my_blood_sugar_p/) ⭐️ 7.0/10

A developer trained a 31,253-parameter encoder-only transformer on synthetic continuous glucose monitor (CGM) data from 1 million simulated type 1 diabetics, then fine-tuned it with LoRA on 115 days of personal CGM data (80 for training, 35 for testing). The model predicts blood glucose up to 2 hours ahead, performs infilling and backcasting, and shows emergent time-of-day awareness with context windows of 48 hours or more. This project demonstrates that a very small, personally fine-tuned transformer can achieve competitive blood glucose prediction, suggesting that personalized health forecasting may not require massive models or datasets. It also explores counterfactual reasoning over insulin and carbohydrate inputs, which could eventually support safer daily diabetes management decisions. The model uses a variable context window of 3.5 to 7.0 days, is trained in Kovatchev risk space with DILATE, MSE, and pinball losses combined via learned Kendall-Gal weights, and still underperforms the developer at predicting hypoglycemia within the next 30 minutes. The counterfactual reasoning capability has not yet been formally benchmarked.

reddit · r/MachineLearning · /u/0xdeadf1sh · Nov 13, 20:48

**Background**: Continuous glucose monitors (CGMs) are wearable devices that track glucose levels in interstitial fluid 24 hours a day, generating dense time-series data. LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning technique that freezes pre-trained weights and injects small trainable matrices, making it possible to adapt models on limited personal data. Encoder-only transformers, such as BERT, are well-suited for understanding and forecasting tasks on sequential data like CGM traces.

<details><summary>References</summary>
<ul>
<li><a href="https://my.clevelandclinic.org/health/articles/continuous-glucose-monitoring-cgm">Continuous Glucose Monitoring ( CGM ): What It Is</a></li>
<li><a href="https://en.wikipedia.org/wiki/LoRA_(machine_learning)">LoRA (machine learning) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Transformer_(deep_learning)">Transformer (deep learning) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#healthcare`, `#time-series`, `#transformers`, `#personalization`

---

<a id="item-7"></a>
## [KDE Documentary Sparks Nostalgic Community Discussion](https://tube.kockatoo.org/w/fFinNHfanLT7aBEb2B8y4c) ⭐️ 6.0/10

A documentary video chronicling the history of the KDE desktop environment has been released, prompting community members to share reminiscences about KDE's early days, its evolution, and the challenges faced during the KDE 4 era. The documentary highlights the cultural and historical significance of KDE, one of the oldest and most influential open-source desktop projects, and fosters community reflection on its achievements and struggles. The video is hosted on tube.kockatoo.org, a PeerTube instance, and the discussion reached 275 points with 52 comments on a news aggregator, indicating strong interest among long-time users.

hackernews · mrkn1 · Nov 14, 13:43 · [Discussion](https://news.ycombinator.com/item?id=50496976)

**Background**: KDE is a free and open-source desktop environment for Linux and other Unix-like systems, founded in 1996 by Matthias Ettrich. Its flagship product, Plasma, is known for its high customizability and is widely used in distributions like Fedora KDE and Kubuntu. Over the years, KDE has faced challenges such as the rocky transition to KDE 4, but has evolved into a stable and feature-rich ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://linux.fandom.com/wiki/KDE_Plasma">KDE Plasma | Linux Wiki | Fandom</a></li>
<li><a href="https://kde.org/">Home - KDE Community</a></li>
<li><a href="https://kde.org/plasma-desktop/">Plasma is KDE 's desktop environment . Simple by default, powerful...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed nostalgia and appreciation for KDE's journey, with many sharing personal stories of using KDE since the early days. Some recalled the instability of KDE 4 but praised the community's perseverance and the eventual success of Plasma, while others highlighted early applications like Amarok and Konqueror as reasons they switched to Linux.

**Tags**: `#kde`, `#open-source`, `#linux`, `#desktop-environment`, `#documentary`

---

<a id="item-8"></a>
## [Google Antigravity adds /teamwork multi-agent collaboration for science and engineering](https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/) ⭐️ 6.0/10

Google Research published a blog post detailing results from Antigravity's /teamwork feature, a multi-agent system where teams of AI agents collaborate, critique, and iterate over hours or days to solve open problems in mathematics, chemistry, systems software, and ML engineering. The /teamwork command is available on paid plans across the Antigravity App and CLI. This signals Google's push toward role-based multi-agent workflows in its agent-first development platform, potentially enabling faster R&D by letting domain experts guide autonomous agent teams. It also intensifies competition with Anthropic's Claude dynamic workflows and OpenAI's Codex in the emerging AI agent tooling market. The /teamwork command is limited to paid plans on the Antigravity App and CLI, and the blog post focuses on research results rather than step-by-step usage guidance. Community members noted that Antigravity lacks an auto mode and trails Claude Code and Codex in some workflow features.

hackernews · acossta · Nov 14, 13:20 · [Discussion](https://news.ycombinator.com/item?id=50496811)

**Background**: Google Antigravity is an agent-first software development platform released in November 2025 alongside the Gemini 3 model, functioning as an IDE where AI agents write, run, and test code with varying autonomy. Multi-agent systems (MAS) built on large language models let groups of agents coordinate and solve complex tasks collectively, moving from isolated models to collaboration-centric approaches. The /teamwork feature applies this paradigm to long-horizon science and engineering problems.

<details><summary>References</summary>
<ul>
<li><a href="https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/">Advancing science & engineering with Antigravity ’s / teamwork</a></li>
<li><a href="https://antigravity.google/docs/teamwork/">Teamwork agent teams (/ teamwork ) | Google Antigravity Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Antigravity">Google Antigravity - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Reaction was mixed: some commenters were enthusiastic about team-based agent workflows and cited related research on adaptive multi-agent harnesses, while others questioned how /teamwork differs from Claude's dynamic workflows and criticized the post for not explaining practical usage. One commenter said the post 'doesn't tell me how to use it,' and another noted Antigravity feels behind Claude Code and Codex in features like auto mode.

**Tags**: `#multi-agent-systems`, `#AI-agents`, `#Google-Research`, `#developer-tools`, `#LLM-workflows`

---

<a id="item-9"></a>
## [Terminactory: A Rust Terminal Factory Game with AI Agent Integration](https://gitlab.com/snipedbywifi/terminactory) ⭐️ 6.0/10

Developer snipedbywifi released Terminactory, a terminal-native idle factory game written in Rust using the ratatui library, on GitLab. The game integrates with AI coding agents via Claude Code hooks, allowing agents to send 'telegrams' (progress messages) that appear in-game while the player manages their factory. This project showcases a novel use of AI agent hooks to create a secondary in-game notification system, blending productivity with entertainment. It also demonstrates how terminal-based games can serve as a lightweight, always-available distraction during long-running agent tasks, potentially inspiring similar integrations in other tools. The game includes standard factory mechanics like building, deleting, and earning measurement, plus unexpected features such as a fake in-game browser with a wiki, forums, extensive lore, and a research graph for unlocking items. It is hosted on GitLab and the developer acknowledges heavy AI assistance in its creation.

hackernews · snipedbywifi · Nov 14, 14:05 · [Discussion](https://news.ycombinator.com/item?id=50497132)

**Background**: Ratatui is a Rust library for building terminal user interfaces (TUIs), forked from tui-rs in 2023 to continue its development. Claude Code hooks are automation triggers that allow custom scripts to run at specific points in the AI coding assistant's workflow. Idle factory games are a subgenre where players build and optimize production chains, often with minimal active interaction.

<details><summary>References</summary>
<ul>
<li><a href="https://ratatui.rs/">Ratatui | Ratatui</a></li>
<li><a href="https://github.com/ratatui/ratatui">GitHub - ratatui / ratatui : A Rust crate for cooking up terminal user ...</a></li>
<li><a href="https://www.aitmpl.com/hooks/">39+ Claude Code Hooks : Automation Triggers & Scripts</a></li>

</ul>
</details>

**Discussion**: Commenters questioned whether the terminal-only aspect is enough of a value proposition compared to games like Factorio, and noted the reinvention of local mail systems akin to NetHack. Others asked about the ubiquity of mining/smelting themes in factory games and suggested adding Nerd Fonts icon support.

**Tags**: `#rust`, `#ratatui`, `#terminal-ui`, `#game-development`, `#ai-agents`

---

<a id="item-10"></a>
## [Interactive site compares all 13 versions of Monkey Island side by side](https://monkeyisland.pages.dev/) ⭐️ 6.0/10

An interactive web showcase lets users drag and compare screenshots from all 13 versions of the classic point-and-click game 'The Secret of Monkey Island' side by side. The site, styled with a Borland Turbo Vision UI look, highlights differences across platforms and graphics modes such as CGA, EGA, and VGA. The comparison offers a tangible look at how the same game was adapted across platforms with vastly different graphical capabilities, from 4-color CGA to VGA and CD-ROM versions. It also sparks nostalgia and appreciation for the ingenuity of artists and developers working under tight hardware constraints. The site covers 13 distinct versions, including the original 1990 releases on Amiga, MS-DOS, Atari ST, and Macintosh, later ports to FM Towns and Mega-CD, and the 2009 Special Edition remake. Users can drag a slider to compare screenshots, making differences in color palette and resolution immediately visible.

hackernews · maximilianburke · Nov 14, 04:23 · [Discussion](https://news.ycombinator.com/item?id=50493904)

**Background**: The Secret of Monkey Island is a 1990 point-and-click adventure game developed by Lucasfilm Games (later LucasArts) and built on the SCUMM engine, which powered many of the studio's classic adventures. Early PC graphics modes like CGA (4 colors), EGA (16 colors), and VGA (256 colors) imposed severe constraints on artists, and ports to platforms like the Amiga and FM Towns offered different palettes and sound capabilities. The game was later remade in 2009 with updated graphics and voiceovers for PC, Xbox 360, PS3, and iOS.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Monkey_Island">Monkey Island - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/SCUMM">SCUMM - Wikipedia</a></li>
<li><a href="https://news.e-ink.me/en/archive/2026-11-13/article/the-secret-of-monkey-island-all-13-versions-side-by-side">The Secret of Monkey Island: all 13 versions side by side</a></li>

</ul>
</details>

**Discussion**: Commenters shared nostalgic memories of growing up with CGA graphics, with some recalling how 'cold' the cyan-magenta palette felt compared to the warmer EGA/VGA era. Others praised the artistry required to create compelling visuals with only four colors, and several reminisced about playing the game on Hercules monitors, Amiga floppies, and the Borland Turbo Vision-style UI of the site.

**Tags**: `#retro-computing`, `#game-development`, `#graphics`, `#nostalgia`, `#history`

---

<a id="item-11"></a>
## [Italy fines Meta $887M over Android users' data access](https://www.reuters.com/world/italy-fines-meta-887-million-over-android-users-data-access-2026-11-14/) ⭐️ 6.0/10

Italy's data protection regulator fined Meta €805 million (about $887 million) for allegedly accessing Android users' photos and videos without proper consent, and ordered the company to change its photo-sharing feature. This is the largest fine ever issued by Italy's data protection authority and highlights the growing scrutiny of Big Tech's data practices under GDPR, potentially setting a precedent for how consent is interpreted for mobile app permissions across the EU. The fine amounts to about 0.47% of Meta's global revenue, and Meta maintains that users must grant permission on their device before the feature operates and can change that permission at any time; the exact mechanism of the alleged unauthorized access remains unclear from the article.

hackernews · giuliomagnifico · Nov 14, 13:48 · [Discussion](https://news.ycombinator.com/item?id=50497009)

**Background**: GDPR requires companies to obtain explicit consent before collecting or processing personal data, including photos and videos. Android's scoped storage system controls which files apps can access, and apps must request specific permissions to read media files created by other apps. Italy's data protection authority (Garante) has been active in enforcing GDPR against tech companies, and this fine is part of a broader European trend of large privacy penalties.

<details><summary>References</summary>
<ul>
<li><a href="https://www.politico.eu/article/italy-hits-meta-with-e805m-fine-over-privacy-law-violation/">Italy hits Meta with €805m fine over privacy law violation</a></li>
<li><a href="https://developer.android.com/training/data-storage/shared/media">Access media files from shared storage | App data and files | Android ...</a></li>
<li><a href="https://gdprlocal.com/gdpr-compliance-for-apps/">GDPR Compliance for Apps: A Complete Guide - GDPR Local</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters questioned the evidence behind the fine, with some asking how Meta accessed photos without consent and others noting that users must grant permission, suggesting consent was given at some point. Some also doubted whether such fines are actually paid and discussed the overall high volume of EU tech fines.

**Tags**: `#privacy`, `#gdpr`, `#meta`, `#regulation`, `#android`

---

<a id="item-12"></a>
## [Should short-horizon price forecasting papers benchmark against market-implied forecasts?](https://www.reddit.com/r/MachineLearning/comments/1xw6fk9/should_shorthorizon_price_forecasting_papers/) ⭐️ 6.0/10

A Reddit discussion on r/MachineLearning questions whether short-horizon price forecasting papers should compare against market-implied forecasts (e.g., options implied volatility, prediction markets) and evaluate interval coverage instead of only naive baselines and point-forecast RMSE. If adopted, this would raise the bar for financial ML evaluation, forcing models to demonstrate value beyond publicly available market information and to account for uncertainty—critical for risk-sensitive applications like crypto trading. The poster notes that most papers only report point-forecast RMSE and rarely compare against options-implied ranges or crowd forecasts, and asks whether data access or missing literature explains this gap; no comments were provided to gauge community response.

reddit · r/MachineLearning · /u/happypeanut-t · Nov 14, 16:23

**Background**: Market-implied forecasts are expectations derived from traded prices, such as options implied volatility (which reflects the market's view of future price range) or prediction market odds. Interval coverage measures how often a forecast's predicted range actually contains the true outcome, e.g., an 80% interval should contain the outcome 80% of the time. Short-horizon price forecasting papers often use deep learning models like transformers and LSTMs and benchmark against simple baselines like ARIMA or random walk.

<details><summary>References</summary>
<ul>
<li><a href="https://www.investopedia.com/terms/i/iv.asp">Exploring Implied Volatility and Options Pricing - Investopedia</a></li>
<li><a href="https://www.federalreserve.gov/econres/feds/kalshi-and-the-rise-of-macro-markets.htm">The Fed - Kalshi and the Rise of Macro Markets</a></li>
<li><a href="https://r-statistics.co/Checking-Prediction-Interval-Coverage.html">The Expert Edge in Forecasting Like a Pro Lesson 7: Checking ...</a></li>

</ul>
</details>

**Tags**: `#forecasting`, `#machine-learning`, `#evaluation-methods`, `#financial-ml`, `#uncertainty-quantification`

---

<a id="item-13"></a>
## [Reddit User Seeks Ethical Alternatives to Kaggle Over Biometric Verification](https://www.reddit.com/r/MachineLearning/comments/1xw6d7n/ethical_alternatives_to_kaggle_d/) ⭐️ 6.0/10

A Reddit user on r/MachineLearning posted a discussion questioning Kaggle's mandatory biometric verification, which they claim is required even just to submit a solution to a competition, and asked the community for ethical alternative platforms for ML competitions. This raises a legitimate privacy and ethics concern about identity verification requirements on major ML platforms, which could affect many practitioners who want to participate in competitions without submitting biometric data. It also highlights a growing demand for alternative competition platforms that prioritize user privacy. The user specifically objects to mandatory biometric verification through a 'controversial vendor' for competition submission, not just for prize collection, and seeks platforms to have fun with state-of-the-art (SOTA) or quasi-SOTA models. The post is a discussion/opinion piece, so its value depends on community responses suggesting alternatives.

reddit · r/MachineLearning · /u/nico_25 · Nov 14, 16:20

**Background**: Kaggle is a popular platform for machine learning competitions, datasets, and notebooks. Biometric verification involves using physiological or behavioral characteristics, such as facial recognition or fingerprint scans, to verify identity, and some platforms require it to prevent fraud and bot accounts. SOTA (state-of-the-art) refers to the best-performing models currently available for a given task.

<details><summary>References</summary>
<ul>
<li><a href="https://www.datasource.ai/en/data-science-articles/11-kaggle-alternatives-in-data-science-competitions">11 Kaggle Alternatives in Data Science Competitions</a></li>
<li><a href="https://deepnote.com/alternatives/kaggle">The 7 best Kaggle alternatives for 2026</a></li>
<li><a href="https://www.digitalocean.com/community/tutorials/exploring-sota-guide-to-cutting-edge-ai-models">Exploring SOTA: A Guide to Cutting-Edge AI Models</a></li>

</ul>
</details>

**Tags**: `#kaggle`, `#privacy`, `#ml-competitions`, `#ethics`, `#community-discussion`

---