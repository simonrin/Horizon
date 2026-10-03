---
layout: default
title: "Horizon Summary: 2026-10-03 (EN)"
date: 2026-10-03
lang: en
---

> From 25 items, 11 important content pieces were selected

---

1. [Aleph Alpha Releases Kolibri, a Sovereign Open-Weight LLM](#item-1) ⭐️ 8.0/10
2. [Court Backs EFF: Utah VPN Law Is Technically Impossible](#item-2) ⭐️ 8.0/10
3. [C++ Insights Visualizes Compiler Transformations of C++ Code](#item-3) ⭐️ 7.0/10
4. [Newgrounds Nostalgia and Ruffle's Flash Preservation Success](#item-4) ⭐️ 7.0/10
5. [Cloudflare Launches OHTTP Gateway for Privacy-Preserving HTTP](#item-5) ⭐️ 7.0/10
6. [arXiv caps submissions at two per month per submitter](#item-6) ⭐️ 7.0/10
7. [NeurIPS 2026 Paper Achieves Topological Out-of-Domain Generalization in Dynamical Systems](#item-7) ⭐️ 7.0/10
8. [FLEET adds reward-aware memory and MCTS to Best-of-N generation](#item-8) ⭐️ 7.0/10
9. [Apple Releases Pass Designer Tool for Apple Wallet Passes](#item-9) ⭐️ 6.0/10
10. [Reddit user recommends free monograph 'The Principles of Diffusion Models'](#item-10) ⭐️ 6.0/10
11. [Reddit post questions whether robot demos with hand-tracking gaps should be kept](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Aleph Alpha Releases Kolibri, a Sovereign Open-Weight LLM](https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/) ⭐️ 8.0/10

Aleph Alpha released Kolibri, an English-German Mixture-of-Experts reasoning model with 78B total and 3B active parameters, up to 1M token context, and open weights under the Apache 2.0 license. The release includes an unusually transparent technical report and abstention training that teaches the model to say "I don't know" when answers aren't in context. Kolibri positions itself as a sovereign, mission-critical model for European enterprises and public-sector users who need EU AI Act compliance without vendor lock-in. Its transparent report and abstention training could raise expectations for openness and hallucination mitigation across the open-weight LLM ecosystem. The model uses a Mixture-of-Experts architecture with 78B total and 3B active parameters, supports up to 1M tokens of context, and was trained with abstention data plus the Merlin-Arthur protocol to reduce hallucinations. It is available on Hugging Face, and community members have hosted free chat demos and run third-party benchmarks.

hackernews · bastitx · Oct 3, 09:36 · [Discussion](https://news.ycombinator.com/item?id=49942706)

**Background**: Aleph Alpha is a German AI company known for sovereign AI solutions aimed at European enterprises and governments. Open-weight models let anyone download and run the model locally, which is important for organizations that must keep data within their own infrastructure. Abstention training is a technique that teaches a model to decline answering when it lacks sufficient information, rather than guessing and hallucinating.

<details><summary>References</summary>
<ul>
<li><a href="https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/">Kolibri Has Landed: A Sovereign Open - Weight Model — Aleph Alpha</a></li>
<li><a href="https://huggingface.co/Aleph-Alpha/Kolibri-1">Aleph - Alpha / Kolibri -1 · Hugging Face</a></li>
<li><a href="https://digg.com/tech/jpbv7q3x">Aleph Alpha releases Kolibri , an open-weight English-German AI...</a></li>

</ul>
</details>

**Discussion**: Commenters praised the technical report as an unprecedented tutorial-level guide to building a modern agentic LLM, with a training team member answering questions and noting the team formed less than a year ago. Others highlighted free hosted demos and third-party benchmarks, while critics noted that Qwen3 27B outperformed Kolibri on German benchmarks and questioned the "sovereign" label given Aleph Alpha's Cohere takeover.

**Tags**: `#LLM`, `#open-weight`, `#Aleph Alpha`, `#agentic AI`, `#hallucination mitigation`

---

<a id="item-2"></a>
## [Court Backs EFF: Utah VPN Law Is Technically Impossible](https://www.eff.org/deeplinks/2026/10/court-agrees-eff-utahs-vpn-law-demands-technical-impossibility) ⭐️ 8.0/10

A court has agreed with the Electronic Frontier Foundation (EFF) that Utah's law requiring platforms to block VPN traffic is technically impossible to comply with. Under the law, platforms face an impossible choice: block all VPN traffic nationwide or withdraw access from Utah entirely. This ruling is a significant legal and technical development with broad implications for internet regulation and privacy, as it sets a precedent against technically unfeasible censorship mandates. It could influence how other US states and countries approach VPN restrictions and age-verification laws. The law, known as SB 73, would require platforms to assume any single IP address could be operating a VPN or proxy, effectively burdening the rights of users. Reliably detecting VPN traffic is difficult because anyone can proxy through a random hosting provider, and deep packet inspection is not foolproof.

hackernews · hn_acker · Oct 1, 22:23 · [Discussion](https://news.ycombinator.com/item?id=49927754)

**Background**: The Electronic Frontier Foundation (EFF) is a US-based nonprofit digital rights group founded in 1990 that defends privacy and free expression online. VPNs (virtual private networks) encrypt and tunnel internet traffic, making it hard for networks to identify or block them. Utah became the first US state to target VPNs with a strict age-verification law, prompting legal challenges over technical feasibility.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VPN_blocking">VPN blocking - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters debated whether VPN detection is even technically possible, with some noting that anyone can proxy through a hosting provider. Others questioned the truism that 'the internet will always route around censorship,' pointing to Iran, China, and Kashmir as examples where censorship has advanced. Some argued the real motivation behind such laws is broader government control rather than blocking adult content.

**Tags**: `#VPN`, `#internet censorship`, `#privacy`, `#law`, `#EFF`

---

<a id="item-3"></a>
## [C++ Insights Visualizes Compiler Transformations of C++ Code](https://github.com/andreasfertig/cppinsights) ⭐️ 7.0/10

C++ Insights, a Clang-based source-to-source transformation tool hosted on GitHub by Andreas Fertig, shows developers how their C++ source code is rewritten by the compiler. It reveals implicit constructs such as range-based for loops, structured bindings, and auto-generated special member functions, and now uses Clang 20. C++ is notorious for implicit behavior that is invisible in the source, so a tool that exposes compiler-generated code helps developers debug, learn the language, and reason about performance. It is especially valuable for teaching and for engineers who want to understand what the standard actually requires the compiler to do. C++ Insights performs source-to-source transformation rather than showing assembly, so its output remains readable C++ that maps closely to the original code. It is built on Clang, meaning its fidelity depends on the Clang version it tracks, and it focuses on language-level transformations rather than runtime value changes.

hackernews · rramadass · Oct 1, 23:53 · [Discussion](https://news.ycombinator.com/item?id=49928361)

**Background**: Compilers do much more than translate code literally: they desugar range-based for loops into iterator loops, expand lambdas into closure classes, generate copy/move constructors and destructors, and insert implicit conversions. These transformations are defined by the C++ standard but are usually invisible to the programmer. C++ Insights makes them explicit by producing an equivalent, expanded version of the source that a human can read.

**Discussion**: Commenters were enthusiastic, with one noting they had long wondered "what is the compiler thinking" in C++. Others shared related projects, including a C++-to-Clang-to-JS transpiler for stepping through value changes and a language-agnostic tool called Benzi, while one user asked for a lambda capture example because that is where compiler magic is most visible.

**Tags**: `#C++`, `#compiler`, `#developer-tools`, `#code-visualization`, `#programming`

---

<a id="item-4"></a>
## [Newgrounds Nostalgia and Ruffle's Flash Preservation Success](https://www.newgrounds.com/) ⭐️ 7.0/10

A Hacker News discussion about Newgrounds.com drew 398 upvotes and 116 comments, with early creators and users sharing nostalgic stories and praising Ruffle for making old Flash games playable again. One commenter noted they could now play a Flash game they uploaded 15 years ago, which they had assumed was lost forever. This highlights the cultural impact of Newgrounds as a pioneering platform for user-generated games and animation, and demonstrates how Ruffle's emulation is successfully preserving a significant portion of early internet gaming history that would otherwise be lost. It also underscores the ongoing efforts to archive and maintain access to Flash content after Adobe Flash's end-of-life. Ruffle is an Adobe Flash Player emulator written in Rust that targets both desktop and web via WebAssembly, and it has been adopted by many Flash preservation sites. The discussion includes personal anecdotes from early contributors like Tom Fulp using friends as characters, and the community's emotional connection to the site's legacy.

hackernews · azhenley · Oct 3, 00:55 · [Discussion](https://news.ycombinator.com/item?id=49940394)

**Background**: Newgrounds is an American entertainment website founded by Tom Fulp in 1995, and in 2000 it became the first Flash website with an automated submission system, hosting countless user-made games and animations. Adobe Flash was discontinued at the end of 2020, threatening to make much of this content unplayable, but projects like Ruffle aim to preserve it by emulating Flash in modern browsers.

**Discussion**: The overall sentiment is highly nostalgic and appreciative, with users sharing personal stories of creating and playing Flash games on Newgrounds, praising Ruffle for reviving lost content, and reflecting on how the site's community-driven era contrasts with today's more commercial platforms. Some express a sense of loss for the unique online culture of that time.

**Tags**: `#Newgrounds`, `#Flash`, `#Game Preservation`, `#Ruffle`, `#Community`

---

<a id="item-5"></a>
## [Cloudflare Launches OHTTP Gateway for Privacy-Preserving HTTP](https://blog.cloudflare.com/announcing-cloudflare-ohttp-gateway/) ⭐️ 7.0/10

Cloudflare announced an Oblivious HTTP (OHTTP) gateway service that separates client identity from request content using a relay and gateway architecture. The service allows developers to route encrypted HTTP requests through Cloudflare's relay while running their own gateway, so no single entity sees both the sender's IP and the request payload. As a major CDN that already sits in front of a large portion of the web, Cloudflare offering OHTTP infrastructure could make privacy-preserving HTTP practical for mainstream developers. It may accelerate adoption of the IETF OHTTP standard for use cases like analytics, update checks, and API calls where users want anonymity without a full VPN or Tor. OHTTP uses a relay to strip client IP information and a gateway to handle cryptographic encapsulation and decapsulation, so the application server only sees plain HTTP. Cloudflare offers its relay (formerly Privacy Gateway) and lets developers run their own gateway, which is recommended when application servers are hosted off Cloudflare.

hackernews · est · Oct 3, 03:15 · [Discussion](https://news.ycombinator.com/item?id=49941091)

**Background**: Oblivious HTTP (OHTTP) is an IETF protocol designed to enable anonymous HTTP transactions by ensuring no single party can see both the request content and the sender's IP address. It builds on binary HTTP and is related to other privacy-preserving protocols like Oblivious DNS over HTTPS. The architecture typically involves a client, a relay, a gateway, and a target server, with encryption ensuring that the relay only sees ciphertext and the gateway only sees the client's IP, not the plaintext request.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Oblivious_HTTP">Oblivious HTTP - Wikipedia</a></li>
<li><a href="https://blog.cloudflare.com/announcing-cloudflare-ohttp-gateway/">Announcing Cloudflare OHTTP Gateway – expanding... | Cloudflare Blog</a></li>
<li><a href="https://ietf-wg-ohai.github.io/oblivious-http/draft-ietf-ohai-ohttp.html">Oblivious HTTP</a></li>

</ul>
</details>

**Discussion**: Commenters raised concerns about centralizing privacy through Cloudflare, with some preferring to share their IP with the website they visit rather than a large tech company. Others shared practical use cases, such as private desktop software checking for updates, and questioned whether encryption could be handled directly by the origin server instead of a separate gateway.

**Tags**: `#privacy`, `#OHTTP`, `#Cloudflare`, `#networking`, `#web-infrastructure`

---

<a id="item-6"></a>
## [arXiv caps submissions at two per month per submitter](https://www.reddit.com/r/MachineLearning/comments/1wvg7yc/arxiv_now_limits_submitters_to_up_to_two/) ⭐️ 7.0/10

arXiv has implemented a new rate-limit policy that restricts each submitter to a maximum of two submissions per calendar month across all categories, effective from October 1, 2026. The change was announced on the official arXiv blog and has sparked extensive discussion in the Machine Learning community on Reddit. arXiv is the central preprint platform for machine learning and AI research, so this policy directly affects how researchers disseminate their work and could slow the pace of publication for prolific authors. It represents a significant shift in how a key scholarly infrastructure handles the surge of AI-generated content. The limit applies to all categories and includes rejected submissions, meaning even papers that are not accepted still count toward the monthly quota. The policy is part of arXiv's broader effort to manage a record 40,363 submissions in September 2026, which the platform attributes partly to AI tools straining volunteer moderators.

reddit · r/MachineLearning · /u/Nunki08 · Oct 2, 00:47

**Background**: arXiv is a free, open-access preprint server that hosts nearly 2.4 million scholarly articles in fields such as physics, mathematics, and computer science. Preprints are versions of papers shared publicly before formal peer review, and arXiv has become the de facto standard for rapid dissemination in machine learning and AI. In recent years, the platform has struggled with a flood of low-quality or AI-generated submissions, prompting it to introduce measures like endorsement requirements for first-time posters and now monthly submission caps.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/">arXiv has updated its rate limit policy for all submitters.</a></li>
<li><a href="https://cybernews.com/ai-news/arxiv-limits-researchers-to-two-papers-a-month/">arXiv submission limit targets AI slop as paper flood... | Cybernews</a></li>
<li><a href="https://arxiv.org/">arXiv .org e- Print archive</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion reflects a mix of support for curbing AI-generated spam and concern about the impact on legitimate researchers who collaborate across multiple projects. Some commenters worry about unintended consequences for early-career researchers, while others suggest workarounds such as coordinating submissions with co-authors.

**Tags**: `#arXiv`, `#research-publishing`, `#machine-learning`, `#academic-policy`, `#community-discussion`

---

<a id="item-7"></a>
## [NeurIPS 2026 Paper Achieves Topological Out-of-Domain Generalization in Dynamical Systems](https://www.reddit.com/r/MachineLearning/comments/1wvwodf/topological_outofdomain_generalization_in/) ⭐️ 7.0/10

A NeurIPS 2026 preprint (arXiv:2606.22969) introduces a modified hierarchical dynamical systems reconstruction (DSR) model that achieves topological out-of-domain generalization (OODG), correctly predicting bifurcations and beyond-bifurcation dynamics without explicit knowledge of control parameters during training. The authors mathematically identify failure modes in previous hierarchical DSR models and fix them using feature-splitting and physical sparsity priors, testing the approach on shallow PLRNNs and Neural ODEs. This work addresses a fundamental challenge in dynamical systems reconstruction and time series forecasting—predicting novel dynamical regimes when a system crosses a tipping point—with potential impact on climate science, neuroscience (e.g., epileptic seizures), and medicine (e.g., sepsis). It pushes beyond current models that rely on statistical regularities and cannot extrapolate to unseen regimes. The method is generic and works for both discrete and continuous time RNNs, specifically tested on shallow PLRNNs and Neural ODEs. The key innovation is inferring the dynamical system jointly with control parameters, using feature-splitting and physical sparsity priors to correct failure modes in previous hierarchical DSR models.

reddit · r/MachineLearning · /u/DangerousFunny1371 · Oct 2, 15:25

**Background**: Dynamical systems reconstruction (DSR) aims to learn the underlying equations of a system from time series data. Topological out-of-domain generalization (OODG) refers to predicting qualitative changes in system behavior, such as bifurcations, when a control parameter crosses a critical value. Bifurcations occur when a small smooth change in a parameter causes a sudden qualitative change in system behavior, and are common in climate, brain, and physiological systems.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.22969">Topological Out - of - Domain Generalization in Dynamical Systems ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bifurcation_(dynamical_systems)">Bifurcation (dynamical systems)</a></li>

</ul>
</details>

**Tags**: `#dynamical systems`, `#out-of-domain generalization`, `#time series forecasting`, `#NeurIPS`, `#machine learning`

---

<a id="item-8"></a>
## [FLEET adds reward-aware memory and MCTS to Best-of-N generation](https://www.reddit.com/r/MachineLearning/comments/1wvs12j/adding_memory_to_search_instead_of_sampling_in/) ⭐️ 7.0/10

The authors of FLEET introduced an algorithm that enhances Best-of-N generation by attributing external rewards to specific tokens and using modified Monte Carlo Tree Search (MCTS) to adjust logits during subsequent runs. Tested on GSM8K and LiveCodeBench v6 easy split with Llama 3.2 3B, FLEET matched the sampling baseline with half the iterations on GSM8K and improved LiveCodeBench score from 0.59 to 0.69 while reaching the baseline in only 9 iterations versus 32. This work addresses a fundamental inefficiency in reward maximization tasks where repetitive sampling is blind to rewards, potentially making LLM inference and search more efficient. It could benefit researchers and practitioners working on reinforcement learning, language model decoding, and search-based generation. FLEET tracks logits with high entropy and varentropy as branching points, stores normalized hidden states in a vector store with reward history, and uses cosine similarity for retrieval; the metadata store can be preserved as a prior for other tasks or to enrich SFT/RL, and sequential execution is not required as it can be passed as a lookup table.

reddit · r/MachineLearning · /u/Helpful_Minimum_2214 · Oct 2, 12:04

**Background**: Best-of-N generation is a common technique where N candidate outputs are sampled and the one with the highest reward is selected, but it is inefficient because sampling is unaware of rewards. Monte Carlo Tree Search (MCTS) is a search algorithm that balances exploration and exploitation, often used in decision-making tasks. Entropy measures uncertainty in a probability distribution, and varentropy measures the variability of information content, helping identify uncertain tokens.

**Tags**: `#machine-learning`, `#reinforcement-learning`, `#monte-carlo-tree-search`, `#language-models`, `#sampling`

---

<a id="item-9"></a>
## [Apple Releases Pass Designer Tool for Apple Wallet Passes](https://developer.apple.com/pass-designer/) ⭐️ 6.0/10

Apple has launched Pass Designer, a dedicated tool on its developer site for constructing and customizing Apple Wallet passes in the PKPass format. The tool lets developers edit semantic tags directly in the UI and view semantic and non-semantic passes side by side. The tool lowers the barrier for businesses and developers to create Wallet passes, which could increase adoption of digital tickets, loyalty cards, and coupons on iOS. It also reignites debate about whether Apple should support cross-platform pass standards instead of platform-specific workflows. Pass Designer supports editing semantic tags in the UI and comparing semantic versus non-semantic passes, and it can automatically generate pass content. However, it remains an Apple-only workflow, and community members note that free web-based PKPass wizards already exist.

hackernews · soheilpro · Oct 2, 19:06 · [Discussion](https://news.ycombinator.com/item?id=49937276)

**Background**: Apple Wallet passes use the PKPass file format, a digital version of a physical ticket, boarding pass, coupon, or loyalty card that can be stored in the Wallet app on iOS devices. Developers previously had to hand-craft the underlying JSON and asset bundles or rely on third-party tools, so a first-party visual designer is a notable convenience. The discussion also touches on LLMs, which make building well-defined tools like this much faster than before.

<details><summary>References</summary>
<ul>
<li><a href="https://walletwallet.alen.ro/blog/pkpass-file/">PKPASS File: The Complete Reference for Apple Wallet 's File Format</a></li>
<li><a href="https://docs.fileformat.com/misc/pkpass/">PKPASS File Format - Apple Wallet Pass</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree the tool is useful but not technically novel, with one noting it is exactly the kind of software that was hard to prioritize before LLMs and trivial to build now. Others point out free web-based PKPass wizards already exist, wish for semantic barcode-area support to brighten only the scanner region on HDR displays, and criticize Apple for not agreeing on a joint standard with Google so passes only need to be made once.

**Tags**: `#Apple Wallet`, `#Pass Designer`, `#PKPass`, `#LLM`, `#Cross-platform`

---

<a id="item-10"></a>
## [Reddit user recommends free monograph 'The Principles of Diffusion Models'](https://www.reddit.com/r/MachineLearning/comments/1wwtpg6/the_principles_of_diffusion_models_by_lai_et_al/) ⭐️ 6.0/10

A Reddit user (u/DenoisedNeuron) posted a strong recommendation for the freely available monograph 'The Principles of Diffusion Models' by Lai et al., praising its balance of mathematical rigor and intuition. The post notes the book targets researchers, graduate students, and practitioners with basic deep learning knowledge, and includes dedicated appendices for deeper mathematical study. Diffusion models have become a dominant paradigm in generative AI, but their mathematical foundations (ELBO, score matching, SDEs) can be daunting for newcomers. A freely available, well-structured monograph lowers the barrier to entry and could help more researchers and practitioners understand and build upon these models. The reviewer notes that a strong background in information and probability theory plus a solid understanding of DDPMs helped them get more out of the book, though prior specialization in diffusion models is not required. The full text is available for free on the book's official website.

reddit · r/MachineLearning · /u/DenoisedNeuron · Oct 3, 18:04

**Background**: Diffusion models are generative models that learn to gradually denoise data starting from pure noise, as popularized by Ho et al.'s 2020 paper 'Denoising Diffusion Probabilistic Models' (DDPM). Their training and sampling rely on mathematical concepts such as the evidence lower bound (ELBO), score matching, and stochastic differential equations, which are often covered in advanced machine learning courses.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2006.11239">[2006.11239] Denoising Diffusion Probabilistic Models</a></li>
<li><a href="https://learnopencv.com/denoising-diffusion-probabilistic-models/">InDepth Guide to Denoising Diffusion Probabilistic Models DDPM</a></li>
<li><a href="https://www.udemy.com/course/diffusion-models-deep-dive-theory-to-practice/">Diffusion Models Deep Dive: Theory to Practice</a></li>

</ul>
</details>

**Tags**: `#diffusion-models`, `#generative-ai`, `#machine-learning`, `#book-review`, `#research`

---

<a id="item-11"></a>
## [Reddit post questions whether robot demos with hand-tracking gaps should be kept](https://www.reddit.com/r/MachineLearning/comments/1ww5ijc/r_would_you_keep_a_robot_demonstration_if_hand/) ⭐️ 6.0/10

A Reddit post on r/MachineLearning raises a nuanced evaluation issue in robot learning: when hand tracking drops out during a critical contact phase (e.g., inserting a plug into a socket), episode-level metrics like recall can mask the failure. The author proposes reporting pose error and coverage together, with coverage broken down by approach, contact, and withdrawal phases, plus the longest consecutive gap during contact. This matters because imitation learning and robot demonstration pipelines depend on accurate hand pose labels during contact-rich manipulation, and aggregate metrics can hide exactly the moments that determine task success. If practitioners cannot tell whether an episode's contact-phase labels are usable, they may train on corrupted data or discard valuable demonstrations unnecessarily. The post references MEgoVista, whose Table 3 reports detection precision, recall, and F1 alongside reconstruction errors, and whose Section 4.4 describes an evaluation protocol that assigns an error to missed detections instead of excluding them. The author notes that the blank HaPTIC row in that table means the method failed to produce valid output in multi-person capture scenes, not that it had a brief tracking dropout.

reddit · r/MachineLearning · /u/Klutzy_Cap8492 · Oct 2, 21:18

**Background**: Robot learning from demonstration often uses human motion capture or egocentric video to collect training data, where hand pose must be tracked accurately even under occlusion. Hand tracking systems can lose the hand when it is occluded by objects or the body, creating gaps in pose labels precisely during contact events like insertion. Evaluation metrics such as recall and pose error are commonly used to judge tracker quality, but they may not reveal where in an episode the failures occur.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.16684">MEgoVista : Multi-view Ego-aware Motion Estimation for Metric...</a></li>
<li><a href="https://theaterfi.re/post/3727489">[R] Would you keep a robot demonstration if hand tracking missed...</a></li>

</ul>
</details>

**Tags**: `#robot learning`, `#hand tracking`, `#evaluation metrics`, `#demonstration data`, `#occlusion`

---