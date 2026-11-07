---
layout: default
title: "Horizon Summary: 2026-11-07 (EN)"
date: 2026-11-07
lang: en
---

> From 17 items, 11 important content pieces were selected

---

1. [Undocumented macOS daemons build personal knowledge graph since 2022](#item-1) ⭐️ 8.0/10
2. [Libghostty 1.0 Released with Stable C ABI](#item-2) ⭐️ 8.0/10
3. [Microsoft Research's AI Frontiers group ends as John Langford exits](#item-3) ⭐️ 7.0/10
4. [Apple's iOS keyboard has a 'grey list' of words it won't help you spell](#item-4) ⭐️ 7.0/10
5. [Coldframe honeypot mimics supermarket fridge controllers to study attacks](#item-5) ⭐️ 7.0/10
6. [Need for Speed Underground 2 Revived Online in the Browser](#item-6) ⭐️ 7.0/10
7. [Law firm runs entirely on free software, sparking debate](#item-7) ⭐️ 7.0/10
8. [Blogger Builds $8 Linux Computer, Sparks Discussion on Cheap SBCs](#item-8) ⭐️ 6.0/10
9. [Retrospective on Borland Turbo Pascal 7 sparks nostalgia and debate](#item-9) ⭐️ 6.0/10
10. [Ancient DNA confirms Goths' Scandinavian origin myth](#item-10) ⭐️ 6.0/10
11. [Nilay Patel: AI products don't justify their costs](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Undocumented macOS daemons build personal knowledge graph since 2022](https://8rank.ai/game/apple-intelligence-personal-knowledge-graph) ⭐️ 8.0/10

A researcher has revealed that every Mac since macOS 13 (2022) ships with two undocumented daemons, knowledgeconstructiond and intelligenceplatformd, that build a personal knowledge graph about the user and their relationships. The system aggregates contacts, inferred family ties, locations, and communication patterns, and can merge data across devices linked to the same Apple ID. This raises significant privacy and ethical concerns because a hidden system profiles users and their social circles without explicit consent, and the data could potentially be accessed by forensic tools or malicious actors. It also highlights the tension between Apple's on-device intelligence features and user transparency. The knowledge graph includes inferred family relationships based on a kinship scorecard, and community reports confirm that data from work and personal Macs can be merged once the system identifies the same user. The daemons are undocumented, and there is no user-facing way to view or delete the graph.

hackernews · infwhispers · Nov 7, 09:46 · [Discussion](https://news.ycombinator.com/item?id=50403097)

**Background**: Apple Intelligence, introduced at WWDC 2024, relies on on-device foundation models to provide personalized assistance, such as understanding which 'James' you mean when you ask Siri to text someone. To do this, macOS maintains a semantic knowledge graph of your contacts, locations, and activities. The daemons knowledgeconstructiond and intelligenceplatformd are part of this infrastructure, but their existence and data collection were previously undisclosed.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50403097">Every Mac comes with an ( undocumented ) family member classifier</a></li>
<li><a href="https://www.privacyaffairs.com/macos-knowledge-graph/">macOS Knowledge Graph: What Your Mac Infers About Your Family</a></li>
<li><a href="https://www.worldcybernews.com/articles/1884">macOS Builds Undocumented Personal Knowledge Graph Since ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed a mix of fascination and concern: some found the data useful if opt-in, while others raised social and ethical worries about constant recording of conversations. One user reported that the system merged knowledge graphs from their work and personal Macs, picking up Slack channels from work even though Slack wasn't used on the personal machine. The author of the research also joined the discussion to answer questions.

**Tags**: `#privacy`, `#macOS`, `#Apple Intelligence`, `#knowledge graph`, `#surveillance`

---

<a id="item-2"></a>
## [Libghostty 1.0 Released with Stable C ABI](https://mitchellh.com/writing/libghostty-1-0) ⭐️ 8.0/10

Mitchell Hashimoto released libghostty-vt 1.0 on November 6, 2026, marking both the library and its C ABI as stable. The library is a portable, high-performance C library for terminal emulation extracted from the core of the Ghostty terminal. A stable ABI means developers can embed a full terminal emulator into their applications without worrying about breaking changes in future updates. This has already led to adoption by major projects like JetBrains IDEs, which replaced JediTerm with libghostty, and a wave of new terminals and agentic coding tools. The library is written in Zig but exposes a carefully designed C ABI, using techniques like opaque handles and enum-keyed getters and setters to avoid leaking implementation details. The 1.0 release emphasizes backward compatibility and distribution, with the latter involving trust and human curation.

hackernews · mfiguiere · Nov 6, 23:30 · [Discussion](https://news.ycombinator.com/item?id=50399933)

**Background**: Ghostty is a terminal emulator created by Mitchell Hashimoto, known for its performance and native UI. Libghostty is the core terminal emulation logic extracted from Ghostty, allowing other applications to reuse it instead of writing their own terminal emulator. Zig is a systems programming language that emphasizes performance, simplicity, and metaprogramming, and it can export C-compatible APIs.

<details><summary>References</summary>
<ul>
<li><a href="https://mitchellh.com/writing/libghostty-1-0">Libghostty 1.0 – Mitchell Hashimoto</a></li>
<li><a href="https://blog.jetbrains.com/platform/2026/10/jetbrains-terminal-now-uses-ghostty/">The Terminal in JetBrains IDEs Now Runs on libghostty - The...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters praised Mitchell for not promoting his own competing product Rex in the announcement, showing respect. Some were surprised by the emphasis on backward compatibility, noting that migrations are often mechanical and well-suited for AI agents, while others highlighted the importance of distribution and trust. Developers shared positive experiences using libghostty in projects like neomacs and Android, and one commenter found the API design lessons useful for their own Zig project.

**Tags**: `#terminal-emulator`, `#zig`, `#c-abi`, `#open-source`, `#developer-tools`

---

<a id="item-3"></a>
## [Microsoft Research's AI Frontiers group ends as John Langford exits](https://hunch.net/?p=13764006) ⭐️ 7.0/10

Microsoft Research's AI Frontiers group has been declared ended, and prominent machine learning researcher John Langford is leaving the organization. The news was reported by Business Examiner and sparked extensive discussion on Hacker News. This signals a broader industry shift away from exploratory AI research toward scaling transformer-based models, potentially reducing long-term innovation and diversity in AI methods. It affects researchers, academic collaborations, and the overall AI ecosystem's ability to pursue fundamental breakthroughs. John Langford is a partner researcher at Microsoft Research New York City known for his work in machine learning theory and reinforcement learning. The AI Frontiers group focused on fundamental advances in AI, and its dissolution reflects Microsoft's prioritization of product-oriented AI development.

hackernews · srean · Nov 7, 18:02 · [Discussion](https://news.ycombinator.com/item?id=50406563)

**Background**: Microsoft Research, founded in 1991, has long operated like an academic lab, allowing researchers to publish openly and pursue long-term projects. The AI Frontiers group was one of its labs focused on frontier AI research, including efficient language models and agentic systems. In recent years, the AI industry has concentrated heavily on scaling transformer models, which are the architecture behind large language models like GPT-4.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/John_Langford_(computer_scientist)">John Langford (computer scientist) - Wikipedia</a></li>
<li><a href="https://www.microsoft.com/en-us/research/lab/ai-frontiers/">Microsoft Research AI Frontiers - Microsoft Research</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree that large companies are now prioritizing transformer-based scaling over exploratory research, with one noting Meta fired its previous head of exploratory AI. Some express concern that over-investment in hardware for frontier models may not align with future breakthroughs in efficiency and open models, raising doubts about AI valuations. Others point out the article's reference to Digg as an outdated source.

**Tags**: `#AI research`, `#Microsoft Research`, `#industry trends`, `#LLM scaling`, `#research funding`

---

<a id="item-4"></a>
## [Apple's iOS keyboard has a 'grey list' of words it won't help you spell](https://www.theguardian.com/technology/2026/nov/06/struggling-to-spell-male-chauvinist-pig-apple-grey-list-means-your-iphone-wont-help-you) ⭐️ 7.0/10

New research reported by The Guardian reveals that Apple's iOS keyboard maintains a 'grey list' of over 100,000 words and phrases—such as 'male chauvinist pig'—that it will not autocomplete or swipe-type, though users can still type them manually. This affects hundreds of millions of iPhone users and raises questions about soft censorship and platform control over language, while also fueling broader criticism of iOS keyboard quality compared to rivals like Gboard. The list is called a 'grey list' because it only restricts predictive and swipe input, not manual typing, and it is multilingual with tens of thousands of entries; Apple has not publicly disclosed the list or its criteria.

hackernews · user_7832 · Nov 7, 17:06 · [Discussion](https://news.ycombinator.com/item?id=50406111)

**Background**: iOS keyboards use machine learning to predict and autocorrect words as you type, and swipe typing (QuickPath) suggests words based on finger gestures. Platform makers like Apple and Google filter certain words from suggestions to avoid offensive or harmful content, but the scope and transparency of such filtering are often unclear.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/nov/06/struggling-to-spell-male-chauvinist-pig-apple-grey-list-means-your-iphone-wont-help-you">Struggling to spell ‘male chauvinist pig’? Apple ’s grey list means your...</a></li>
<li><a href="https://gizmodo.com/ios-apparently-maintains-a-list-of-4500-phrases-it-wont-autocomplete-2000836374">iOS Apparently Maintains a List of 4,500+ Phrases It Won't ...</a></li>
<li><a href="https://www.digitaltrends.com/phones/apples-iphone-keyboard-has-a-hidden-list-of-words-it-refuses-to-suggest-and-some-entries-are-surprising/">Apple's iPhone keyboard has a hidden list of words it refuses ...</a></li>

</ul>
</details>

**Discussion**: Commenters debated whether this constitutes soft coercion or a reasonable design choice, with some arguing that not predicting controversial phrases is not censorship since users can still type them, while others criticized iOS keyboard quality and noted that Gboard likely does something similar.

**Tags**: `#Apple`, `#iOS`, `#keyboard`, `#censorship`, `#privacy`

---

<a id="item-5"></a>
## [Coldframe honeypot mimics supermarket fridge controllers to study attacks](https://github.com/hedgerow-dev/coldframe) ⭐️ 7.0/10

A developer released Coldframe, a single-file Python honeypot that convincingly impersonates Danfoss AK-SM 800A and Dixell XWEB refrigeration controllers. The honeypot uses only the standard library and has already been fingerprinted by Shodan as real devices, attracting generic scanners and Shodan's crawler. This project highlights the vulnerability of internet-exposed industrial control systems in critical infrastructure like supermarkets, where security is often an afterthought. It also raises questions about the reliability of Shodan data for identifying real devices versus honeypots. Coldframe meticulously replicates real device fingerprints, including header order, page titles, certificate fields, and TLS versions, and it recognizes exploit attempts such as CVE-2025-41450 and the Danfoss 'code of the day' login bypass. Default logins open a fake dashboard with defrost buttons to observe attacker behavior beyond initial access.

hackernews · hedgerow-dev · Nov 7, 17:27 · [Discussion](https://news.ycombinator.com/item?id=50406292)

**Background**: Honeypots are decoy systems designed to attract and analyze attacks. Danfoss AK-SM 800A and Dixell XWEB are real refrigeration controllers used in supermarkets to monitor and control cooling systems, and they are often exposed online. Shodan is a search engine for internet-connected devices, frequently used by researchers and attackers to find vulnerable systems.

<details><summary>References</summary>
<ul>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2025-41450">NVD - CVE - 2025 - 41450</a></li>
<li><a href="https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/">Danfoss security advisories | Danfoss</a></li>
<li><a href="https://webapps2.copeland.com/ci/dixell-xweb/index.htm">Dixell XWEB Evo</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about relying on Shodan data, noting that many devices found there are already honeypots or compromised. The author acknowledged that supermarkets lack security teams and suggested vendors should provide secure defaults, while another commenter questioned whether the recent refrigeration incidents were actually large-scale hacks.

**Tags**: `#honeypot`, `#IoT security`, `#industrial control systems`, `#Shodan`, `#critical infrastructure`

---

<a id="item-6"></a>
## [Need for Speed Underground 2 Revived Online in the Browser](https://nfsu2.xyz/) ⭐️ 7.0/10

A fan-made project at nfsu2.xyz has brought Need for Speed Underground 2 online in the browser, allowing players to race the 2004 classic with multiplayer support directly on the web. The site uses WebGPU to render the game and has quickly gained popularity, drawing 619 points and 180 comments on Hacker News. This project demonstrates how WebGPU and reverse engineering can make decades-old games playable online without installation, potentially inspiring similar browser-based revivals of other abandonware titles. It also reignites debates about the legality and sustainability of fan-driven game preservation. The game runs in the browser via WebGPU, and Linux users reportedly need to enable unsafe WebGPU features in Chromium to get it working. The site is fan-operated and hosts copyrighted content without authorization, raising takedown concerns as it gains attention.

hackernews · fluxusars · Nov 7, 09:36 · [Discussion](https://news.ycombinator.com/item?id=50403052)

**Background**: WebGPU is a modern web API that lets browsers access the system's GPU for high-performance graphics and computation, enabling complex 3D games to run in a web page. Need for Speed Underground 2, released in 2004, is no longer sold or supported by its publisher, placing it in the category of 'abandonware'—software that is out of commerce but still legally protected by copyright. Fan projects that reverse engineer and host such games often operate in a legal gray area, tolerated by some publishers but vulnerable to takedown requests.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebGPU">WebGPU - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Abandonware">Abandonware - Wikipedia</a></li>
<li><a href="https://www.howtogeek.com/829307/what-is-abandonware-and-is-it-legal/">What Is " Abandonware " and Is it Legal ?</a></li>

</ul>
</details>

**Discussion**: Commenters are impressed by the technical feat and the nostalgia factor, with many sharing memories of playing the game in the mid-2000s. However, some raise concerns about the site's legality and the ethics of soliciting donations for copyrighted content, while others hope the project is left alone since the game is no longer commercially available.

**Tags**: `#WebGPU`, `#game preservation`, `#abandonware`, `#browser gaming`, `#reverse engineering`

---

<a id="item-7"></a>
## [Law firm runs entirely on free software, sparking debate](https://decoded.legal/blog/2026/11/running-a-law-firm-on-free-software-2026-edition/) ⭐️ 7.0/10

A UK-based law firm, decoded.legal, published a detailed 2026 edition blog post describing how it operates its entire practice using only free software, from document drafting to billing and client management. The post has sparked a community discussion on Hacker News with 83 comments about the practicality and risks of this approach. This case study demonstrates that a professional services firm can avoid vendor lock-in and proprietary software costs, challenging the assumption that Microsoft Word and other commercial tools are indispensable in legal practice. It also highlights broader debates about interoperability, AI vendor vertical integration, and professional norms in the legal industry. The firm's setup relies on free software alternatives for document creation, email, and practice management, though specific tools are not detailed in the summary. Community members raise concerns about interoperability risks if other lawyers need to step in, and one commenter notes that a respected open source lawyer called not using Word 'malpractice' at a legal workshop.

hackernews · DeepLogin · Nov 7, 09:39 · [Discussion](https://news.ycombinator.com/item?id=50403066)

**Background**: Free software, as defined by the Free Software Foundation, grants users the freedom to run, study, share, and modify software, and is a matter of liberty rather than price. Vendor lock-in occurs when an organization becomes dependent on a single vendor's technology, making migration difficult and costly. In the legal industry, Microsoft Word and Outlook are standard tools, and many firms use practice management software like Clio for billing and case management.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gnu.org/philosophy/free-sw.en.html">What is Free Software? - GNU Project - Free Software Foundation</a></li>
<li><a href="https://www.superblocks.com/blog/vendor-lock">What Is Vendor Lock-In? Cloud Examples + How to Avoid It</a></li>
<li><a href="https://lawyerist.com/reviews/law-practice-management-software/">Best Law Practice Management Software Reviews (2026)</a></li>

</ul>
</details>

**Discussion**: Commenters express a mix of envy and skepticism: one lawyer stuck in a big firm laments bloated, buggy mandated software, while another warns that law firms using AI tools like Harvey are enabling vendor vertical integration and losing competitive edge. Others question the practicality of a lawyer focusing on IT, raise concerns about continuity if the lawyer is unavailable, and debate whether not using Word constitutes malpractice.

**Tags**: `#free-software`, `#legal-tech`, `#open-source`, `#workflow`, `#vendor-lock-in`

---

<a id="item-8"></a>
## [Blogger Builds $8 Linux Computer, Sparks Discussion on Cheap SBCs](http://thelittleengineerthatcould.blogspot.com/2022/12/the-8-linux-computer.html) ⭐️ 6.0/10

A blog post from 2022 describes building a Linux computer for just $8, likely using a low-cost chip, and has recently resurfaced on Hacker News with 161 points and 67 comments. This project highlights the extreme low end of Linux-capable hardware, showing how hobbyists can repurpose cheap components, and the discussion compares alternatives like the Ox64 and LicheeRV Nano, reflecting broader interest in affordable single-board computers for embedded and IoT projects. The $8 computer likely relies on a minimal system-on-chip with limited peripherals, and commenters note trade-offs such as poor documentation, lack of USB support, and outdated kernels on similar cheap boards.

hackernews · zenincognito · Nov 7, 14:00 · [Discussion](https://news.ycombinator.com/item?id=50404599)

**Background**: A single-board computer (SBC) is a complete computer built on a single circuit board, often used for education, prototyping, or embedded control. Linux can run on low-cost ARM-based chips, but support for peripherals and software updates varies widely. Hobbyists often seek out cheap boards to repurpose for projects, balancing cost against functionality and community support.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Single-board_computer">Single-board computer</a></li>
<li><a href="https://en.wikipedia.org/wiki/Embedded_system">Embedded system - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters shared mixed experiences: one criticized the Ox64 for poor peripheral support and outdated kernel, while another praised the LicheeRV Nano (SG2002) as a better value at $15-20 with USB OTG and GPIO. Others noted that the main appeal of such cheap boards is their small size and convenient GPIO rather than pure cost, and recalled the $5 Raspberry Pi Zero.

**Tags**: `#Linux`, `#embedded`, `#low-cost hardware`, `#SBC`, `#hobbyist`

---

<a id="item-9"></a>
## [Retrospective on Borland Turbo Pascal 7 sparks nostalgia and debate](https://kevinboone.me/tpwin.html) ⭐️ 6.0/10

A blog post by Kevin Boone reflects on Borland Turbo Pascal 7, its design, and its influence, prompting a Hacker News discussion with over 70 comments where developers shared personal memories and debated modern software development skills. The discussion highlights how Turbo Pascal's fast compilation and integrated environment set a standard for developer productivity, and raises concerns about the loss of low-level skills in an increasingly abstracted and AI-assisted industry. Turbo Pascal 7, released in 1992 for MS-DOS, was the last version and was accompanied by the more feature-rich Borland Pascal; it was later superseded by Delphi for Windows development. Commenters also referenced articles like "Things Turbo Pascal is Smaller Than" and "A Personal History of Compilation Speed" to illustrate its efficiency.

hackernews · andsoitis · Nov 7, 16:06 · [Discussion](https://news.ycombinator.com/item?id=50405678)

**Background**: Turbo Pascal was a software development system created by Borland in the 1980s that bundled a compiler and an integrated development environment (IDE) for the Pascal language on CP/M and MS-DOS. It was renowned for its fast compilation, elegant syntax, and affordable price, making it a popular choice for hobbyists and professionals alike. Turbo Pascal played a key role in popularizing Pascal and influenced later tools like Delphi.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Turbo_Pascal">Turbo Pascal - Wikipedia</a></li>
<li><a href="https://news.ycombinator.com/item?id=50405678">They don't make 'em like that any more: Borland Turbo Pascal ...</a></li>

</ul>
</details>

**Discussion**: Commenters shared nostalgic stories, such as writing their first sold programs in Turbo Pascal and creating DOS games as teenagers. Some agreed with the article's concern that few developers today could build something like Turbo Pascal, while others expressed hope that AI might help compensate for the growing depth of abstraction in computing.

**Tags**: `#Turbo Pascal`, `#software history`, `#compilers`, `#programming tools`, `#Hacker News`

---

<a id="item-10"></a>
## [Ancient DNA confirms Goths' Scandinavian origin myth](https://www.science.org/content/article/barbarian-tribe-s-mythic-origin-story-true-ancient-dna-reveals) ⭐️ 6.0/10

Ancient DNA analysis of skeletons across Europe has provided evidence that the Goths, a Germanic tribe, originated in Scandinavia before migrating south and eventually sacking Rome. This confirms a mythic origin story that had been recounted for centuries but was often dismissed by historians. This finding bolsters the reliability of oral traditions and myths as historical sources, and it may prompt reevaluation of other ancient origin stories. It also demonstrates the power of ancient DNA to resolve long-standing historical debates. The study analyzed genomes from Gothic-era skeletons and compared them with modern and ancient populations, revealing genetic links to Scandinavia. However, the exact timing and scale of the migration, as well as the degree of continuity with later Gothic populations, remain areas of active research.

hackernews · benbreen · Nov 7, 04:54 · [Discussion](https://news.ycombinator.com/item?id=50401740)

**Background**: The Goths were a Germanic people who played a major role in the fall of the Western Roman Empire. According to their own legend, recorded by the 6th-century historian Jordanes, they originated in Scandinavia, specifically from the island of Gotland. However, historians have long debated this claim, with some arguing that the Goths actually originated on the continent. Ancient DNA studies have become a powerful tool for tracing human migrations and resolving such debates.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Herodotus">Herodotus - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Origin_of_the_Goths">Origin of the Goths - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Goths">Goths - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters drew parallels to Herodotus, noting that many of his 'wild claims' have been vindicated by modern research, and questioned why the Gothic origin story was ever doubted given Scandinavia's place names like Gotland and Gothenburg. Others discussed the etymology of words like 'helmet' in Spanish and Italian, and pointed out that Swedish Gothlanders have long embraced this origin myth.

**Tags**: `#archaeology`, `#ancient-dna`, `#history`, `#science-news`, `#genetics`

---

<a id="item-11"></a>
## [Nilay Patel: AI products don't justify their costs](https://simonwillison.net/2026/Nov/6/nilay-patel/) ⭐️ 6.0/10

In a clip from The Vergecast episode "Big Tech lost big in the 2026 election," Nilay Patel argued that AI products are not good enough to justify their environmental, economic, and societal costs, and that the industry's spending far outpaces real benefits. Patel's critique adds a prominent media voice to the growing debate over an AI bubble, questioning whether massive data center investments and agent hype can deliver commensurate value to users and society. Patel specifically called out AI overviews, deepfake "slop," and AI agents as examples of underwhelming products, and linked the costs to political corruption; the quote was surfaced by Simon Willison, who tagged it with slop, generative-ai, and ai-ethics.

rss · Simon Willison · Nov 6, 17:13

**Background**: The AI industry is spending tens of billions on data centers that consume large amounts of water and energy, while companies like OpenAI and Google face questions about whether revenue will ever catch up. AI agents, which are autonomous software systems powered by large language models, have been heavily promoted but often fail to meet expectations in real-world use. Patel's comments reflect a broader skepticism about AI hype and its societal costs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.foodandwaterwatch.org/2025/04/09/artificial-intelligence-water-climate/">Artificial Intelligence: Big Tech’s Big Threat to Our Water and Climate</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-agents">What are AI agents? - IBM</a></li>
<li><a href="https://qz.com/sam-altman-ai-bubble-open-ai-warning">OpenAI CEO Sam Altman says an AI bubble is forming</a></li>

</ul>
</details>

**Tags**: `#AI industry`, `#AI economics`, `#tech criticism`, `#AI hype`, `#commentary`

---