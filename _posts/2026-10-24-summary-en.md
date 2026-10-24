---
layout: default
title: "Horizon Summary: 2026-10-24 (EN)"
date: 2026-10-24
lang: en
---

> From 25 items, 11 important content pieces were selected

---

1. [Moonshot AI Releases Kimi K3.1 Pro and Highspeed Variant](#item-1) ⭐️ 8.0/10
2. [GPU-unlock exploits firmware to boost FP/BF16 issue rates on RTX 3000](#item-2) ⭐️ 8.0/10
3. [Blogger Demonstrates Successful iPhone Hack, Sparking Security Debate](#item-3) ⭐️ 8.0/10
4. [Around a dozen banking apps now explicitly permit GrapheneOS](#item-4) ⭐️ 7.0/10
5. [Brotli RCE 'HTTP2Shell' affects many HTTP libraries and apps](#item-5) ⭐️ 7.0/10
6. [OBS Studio 33 Released with Updated CEF and Security Fixes](#item-6) ⭐️ 7.0/10
7. [Twelve Years of Distributed SQLite: A Practitioner's Retrospective](#item-7) ⭐️ 7.0/10
8. [FreeDNS: Long-Lived Free Dynamic DNS Service Discussed on Hacker News](#item-8) ⭐️ 6.0/10
9. [2018 Essay on Quantum Confusion Sparks HN Debate](#item-9) ⭐️ 6.0/10
10. [Local Wikipedia shows nearby articles within a half-hour walk](#item-10) ⭐️ 6.0/10
11. [Apple Music's 404 Page Hides Playable iPod with Brick Game](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Moonshot AI Releases Kimi K3.1 Pro and Highspeed Variant](https://www.kimi.ai/blog/kimi-k3-1-pro) ⭐️ 8.0/10

Moonshot AI released Kimi K3.1 Pro, the first model in its new K3.1 series and its most capable 3T-class open-weight model to date, featuring a 1-million-token context window, alongside Kimi K3.1 Pro Highspeed, which delivers 2-3x the speed for more responsive applications. This release strengthens the competitive position of open-weight Chinese models against proprietary frontier systems, offering developers a high-capability, long-context option with a faster variant for latency-sensitive workloads. The lively Hacker News discussion also highlights growing scrutiny of model behavior, marketing practices, and safety tradeoffs in the open-weight ecosystem. K3.1 Pro is a post-trained version of Kimi K3 with the same architecture but a much larger post-training budget, and it is priced at $1.39 per million input tokens and $13 per million output tokens on OpenRouter. The Highspeed variant trades a couple of percentage points of quality for a 2-3x latency reduction, and community testing on a Pac-Man benchmark placed it around Sonnet 5.5 for price-performance.

hackernews · Jowsey · Oct 23, 16:59 · [Discussion](https://news.ycombinator.com/item?id=50212065)

**Background**: Moonshot AI is a Chinese AI lab known for its Kimi series of large language models, and open-weight models are those whose trained parameters are publicly released so others can download, run, and fine-tune them. Kimi K3 was a 2.8-trillion-parameter open-weight multimodal reasoning model, and K3.1 Pro builds on it through additional post-training rather than architectural changes. A 1-million-token context window lets the model process very long documents or codebases in a single prompt, while the Highspeed variant targets applications where response latency matters more than marginal quality gains.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-1-pro-quickstart">Kimi K3.1 Pro - Kimi API Platform</a></li>
<li><a href="https://www.yottalabs.ai/post/kimi-k3-1-pro-specs-price-open-weights-benchmarks">Kimi K3.1 Pro: Specs, Price, Open Weights Date, and ...</a></li>
<li><a href="https://openrouter.ai/moonshotai/kimi-k3">Kimi K3 - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**Discussion**: Commenters reported that the model's reasoning traces sometimes identify it as Kimi by Moonshot and sometimes as ChatGPT, and reference an 'evaluator' or phantom instruction lines, raising questions about self-awareness quirks. Others flagged Moonshot's 'creators campaign' docs as a way to spot potentially paid boosters, and debated the removal of cybersecurity data—questioning how much is just standard software knowledge and whether such filtering meaningfully limits misuse versus simply slowing capability growth.

**Tags**: `#llm`, `#ai-models`, `#moonshot-ai`, `#ai-safety`, `#open-source-ai`

---

<a id="item-2"></a>
## [GPU-unlock exploits firmware to boost FP/BF16 issue rates on RTX 3000](https://github.com/Zagitta/gpu-unlock) ⭐️ 8.0/10

A new tool called GPU-unlock, developed by Zagitta, exploits a buffer overflow vulnerability in the GPU booter firmware to unlock higher FP/BF16 instruction issue rates on Nvidia RTX 3000 consumer GPUs, bringing them closer to professional-card performance. It is packaged as a standalone UEFI module that chainloads into the OS, avoiding the need to patch the Nvidia driver. This is significant because it allows consumer GPUs to achieve performance levels previously reserved for professional cards, potentially offering up to 47–59% throughput gains in BF16 workloads like AI inference. It democratizes access to higher compute performance for researchers and enthusiasts without expensive hardware upgrades. The exploit relies on a classic buffer overflow in the booter that enables Return Oriented Programming (ROP) to execute custom code. However, users must run their cards hotter and may need to increase the power limit to 450W, which exceeds stock cooler capabilities, and the mod can be stacked with the existing p2p mod for additional benefits.

hackernews · fragebogen · Oct 24, 09:58 · [Discussion](https://news.ycombinator.com/item?id=50219700)

**Background**: Nvidia consumer GPUs typically have artificially limited FP/BF16 instruction issue rates compared to professional cards, even though the underlying hardware may support higher throughput. The GPU booter is a firmware component that initializes the GPU during boot, and vulnerabilities in it can be exploited to bypass these limits. UEFI modules are pre-boot executables that can modify system behavior before the operating system loads, making them a powerful vector for such modifications.

<details><summary>References</summary>
<ul>
<li><a href="https://agihunt.info/en/p/1a16a6415784a1108768c363c83">RTX 30-series GPU Unlock tested: up to 59%… · AGI Hunt</a></li>

</ul>
</details>

**Discussion**: The community response is largely positive, with testers confirming the results and the author answering questions. Commenters note practical caveats such as increased heat and power requirements, and mention that the mod can be stacked with a p2p mod for additional card-to-card speed improvements. Some also point out that the benefits are workload-dependent, as training is often memory-bandwidth bound.

**Tags**: `#gpu`, `#nvidia`, `#firmware-exploit`, `#hardware`, `#performance`

---

<a id="item-3"></a>
## [Blogger Demonstrates Successful iPhone Hack, Sparking Security Debate](https://blog.calif.io/p/iphone) ⭐️ 8.0/10

A blog post by Calif details a successful hack of an iPhone, showcasing multiple exploit techniques that achieve arbitrary code execution and potentially root access. The post, accompanied by demos, quickly rose to the top of Hacker News with over 1,000 points and 650 comments. This demonstration highlights ongoing vulnerabilities in iOS, even as Apple markets Lockdown Mode as an extreme protection for high-risk users. It fuels the debate on whether such protections are sufficient against sophisticated exploit chains and raises questions about jailbreak persistence and Apple's ability to patch. The hack appears to involve multiple attack vectors, including iMessage attachment processing and PDF rendering, reminiscent of previous exploit chains like ForcedEntry used by Pegasus. Community members question whether Lockdown Mode would mitigate these specific exploits and whether root access can be maintained across updates.

hackernews · pavel_lishin · Oct 23, 16:21 · [Discussion](https://news.ycombinator.com/item?id=50211474)

**Background**: iOS jailbreaking involves exploiting vulnerabilities to bypass Apple's restrictions and gain root access, often using kernel or userland exploits. Lockdown Mode is an optional extreme protection feature that limits certain apps and web content to reduce attack surface, but its real-world effectiveness against advanced exploits is still debated. Exploit chains like BLASTPASS and ForcedEntry have shown that iPhones can be compromised without user interaction, often via zero-click vectors like iMessage.

<details><summary>References</summary>
<ul>
<li><a href="https://support.apple.com/en-us/105120">About Lockdown Mode - Apple Support</a></li>
<li><a href="https://en.wikipedia.org/wiki/IOS_jailbreaking">iOS jailbreaking - Wikipedia</a></li>
<li><a href="https://projectzero.google/2019/08/a-very-deep-dive-into-ios-exploit.html">A very deep dive into iOS Exploit chains found in the wild - Project Zero</a></li>

</ul>
</details>

**Discussion**: Commenters expressed admiration for the demos, with some wishing for root access on their own devices and others questioning whether Lockdown Mode would help. Concerns were raised about iOS's susceptibility to PDF-based exploits and whether such hacks could prevent Apple from pushing updates.

**Tags**: `#iPhone`, `#security`, `#exploit`, `#jailbreak`, `#iOS`

---

<a id="item-4"></a>
## [Around a dozen banking apps now explicitly permit GrapheneOS](https://grapheneos.social/@GrapheneOS/117492375462459244) ⭐️ 7.0/10

GrapheneOS announced that around a dozen banking apps have begun explicitly permitting its official builds, a shift from the previous norm where banking apps often blocked or restricted the privacy-focused Android OS. This marks growing acceptance of hardened Android distributions by financial institutions, potentially reducing a major barrier to GrapheneOS adoption for privacy-conscious users who need mobile banking. The support applies only to official GrapheneOS builds; self-built versions are still blocked by remote attestation, and some apps may have limited functionality such as NFC payments not working.

hackernews · privacyishuman · Oct 24, 01:15 · [Discussion](https://news.ycombinator.com/item?id=50217495)

**Background**: GrapheneOS is an open-source Android-based operating system focused on security and privacy, officially supported on Google Pixel devices. Banking apps often use hardware-backed remote attestation to verify device integrity, which can flag custom ROMs as untrusted. Remote attestation relies on cryptographic certificates signed by a hardware root of trust to confirm the OS hasn't been tampered with.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>
<li><a href="https://source.android.com/docs/security/features/keystore/attestation">Key and ID attestation - Security | Android Open Source Project Hardware-Backed Android Key Attestation Security - Guardsquare Implement hardware-backed attestation for digital credentials Dynamic Security Policies with Android Hardware Attestation ... Implement Android Hardware-Backed Key Attestation: A Hands-On ... How does device attestation work on Android devices</a></li>
<li><a href="https://grapheneos.org/">GrapheneOS: the private and secure mobile OS</a></li>

</ul>
</details>

**Discussion**: Commenters debated the trade-offs: some resented banks effectively requiring users to provide secure hardware, while others noted that only official builds work due to attestation. Several users reported that most banking apps now function on GrapheneOS, though NFC payments often remain unavailable, and some questioned the irony of banking apps having their own security bugs.

**Tags**: `#GrapheneOS`, `#mobile security`, `#privacy`, `#banking apps`, `#remote attestation`

---

<a id="item-5"></a>
## [Brotli RCE 'HTTP2Shell' affects many HTTP libraries and apps](https://www.aikido.dev/blog/python-packages-vulnerable-node2shell-brotli-cve-2026-111497) ⭐️ 7.0/10

A critical remote code execution vulnerability in Brotli decompression, tracked as CVE-2026-111497 and originally dubbed Node2Shell, has been rebranded HTTP2Shell after researchers found it affects numerous HTTP libraries and applications beyond Node.js, including Python packages using brotli or brotlicffi. The flaw allows an attacker to execute arbitrary code by sending a specially crafted Brotli-compressed request body to a vulnerable server. This vulnerability has a broad blast radius because Brotli is widely used for HTTP compression, and many popular frameworks and libraries may be exposed if they decompress request bodies. Organizations running affected software need to identify and patch vulnerable components urgently to prevent remote code execution attacks. The vulnerability resides in the Brotli decompression code bundled with affected libraries and runtimes, so fixing it requires updating the specific component (e.g., Node.js runtime or Python brotli package) to a patched version. Notably, the flaw was reportedly reported and fixed in February but not recognized as a security issue until now, and some commenters question how many implementations actually support Brotli-compressed request bodies in common configurations.

hackernews · theanonymousone · Oct 24, 08:06 · [Discussion](https://news.ycombinator.com/item?id=50219177)

**Background**: Brotli is a lossless data compression algorithm developed by Google, commonly used to compress HTTP responses and sometimes requests to reduce bandwidth. Many programming languages and frameworks include Brotli support, either natively or via third-party libraries, which means a flaw in the decompression logic can propagate across a wide ecosystem. Remote code execution (RCE) is a severe class of vulnerability where an attacker can run arbitrary commands on a target system, often leading to full compromise.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aikido.dev/blog/node2shell-nodejs-brotli-rce-cve-2026-111497">Node 2 Shell : Node.js Brotli vulnerability allows remote code execution...</a></li>
<li><a href="https://www.imperva.com/blog/node2shell-from-brotli-data-to-remote-code-execution/">Node2Shell: From Brotli Data to Remote Code Execution | Imperva</a></li>
<li><a href="https://en.wikipedia.org/wiki/Brotli">Brotli - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters criticized the name HTTP2Shell as overly broad and meaningless, with some preferring Brotli2Shell or Broccoli2Shell to better reflect the actual issue. Others questioned the disclosure process, noting the vulnerability was reported and fixed in February but not recognized as important until now, and expressed annoyance at the sensationalism while urging people to patch and move on.

**Tags**: `#security`, `#vulnerability`, `#brotli`, `#http`, `#rce`

---

<a id="item-6"></a>
## [OBS Studio 33 Released with Updated CEF and Security Fixes](https://github.com/obsproject/obs-studio/releases/tag/33.0.0) ⭐️ 7.0/10

OBS Studio has released version 33.0.0, which notably updates the embedded Chromium Embedded Framework (CEF) from version 127/6533 to 150/7871. This update addresses security vulnerabilities that had been exploited in the wild. This release is significant because it finally patches a two-year-old CEF version that had known remote code execution (RCE) exploits, improving security for the widely-used open-source streaming and recording tool. The update affects all OBS users, particularly those on Windows, macOS, and Linux who rely on the software for live production. The CEF update from 127 to 150 brings the embedded browser component up to date with modern Chromium security patches, but users should verify plugin compatibility as major CEF jumps can affect browser-based sources and integrations. The release also includes other unspecified fixes and improvements typical of a major version bump.

hackernews · pentagrama · Oct 24, 04:49 · [Discussion](https://news.ycombinator.com/item?id=50218430)

**Background**: OBS Studio (Open Broadcaster Software) is a free, open-source, cross-platform application for live streaming and screen recording, widely used by content creators, educators, and professionals. It uses Chromium Embedded Framework (CEF) to render browser-based elements such as alerts, overlays, and web sources within scenes. CEF is based on Chromium, so outdated versions can inherit known browser security vulnerabilities, including remote code execution flaws.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OBS_Studio">OBS Studio - Wikipedia</a></li>
<li><a href="https://github.com/obsproject/obs-studio/releases">Releases · obsproject/ obs - studio</a></li>

</ul>
</details>

**Discussion**: Community comments are largely positive, with users praising OBS for reliability over alternatives like Zoom for recording lectures, and sharing creative setups such as using HDMI capture with OBS. One commenter highlighted VDO.ninja as a lightweight complementary tool for low-latency video, while another specifically welcomed the CEF update as a long-overdue fix for RCE exploits that had been reported in the media.

**Tags**: `#OBS Studio`, `#streaming`, `#open-source`, `#video-recording`, `#Hacker News`

---

<a id="item-7"></a>
## [Twelve Years of Distributed SQLite: A Practitioner's Retrospective](https://philipotoole.com/twelve-years-of-distributed-sqlite/) ⭐️ 7.0/10

Philip O'Toole published a reflective blog post looking back on twelve years of building distributed SQLite systems, which sparked a Hacker News discussion with 330 points and 50 comments. The retrospective highlights the maturation of distributed SQLite as a viable alternative to traditional database servers, and the community discussion reveals practical tradeoffs between replication strategies and SQLite versus Postgres for modern applications. The discussion compared approaches like rqlite (consensus-based), Litestream (S3 sync), Cloudflare D1 (SQL wrapper over Durable Objects), and Paxos-based multi-master systems using WAL replication, with commenters noting D1's reliability issues and SQLite's SQL feature limitations.

hackernews · otoolep · Oct 24, 01:16 · [Discussion](https://news.ycombinator.com/item?id=50217500)

**Background**: SQLite is an embedded database engine that lacks built-in replication, so distributed SQLite systems add replication through methods like consensus algorithms, write-ahead log (WAL) shipping, or file system sync. Projects like rqlite, Litestream, and Cloudflare D1 aim to provide global distribution and high availability while preserving SQLite's simplicity.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sqliteforum.com/p/replication-strategies-for-sqlite">SQLite Replication Strategies for Distributed Applications</a></li>
<li><a href="https://docs.fly.io/litefs">LiteFS - Distributed SQLite - Fly.io</a></li>
<li><a href="https://www.ofsecman.io/post/postmortem-5-000-incident-in-10-seconds-due-to-cloudflare-d1">How Cloudflare D 1 Burned $5,000 in 10 Seconds Without Warning .</a></li>

</ul>
</details>

**Discussion**: Commenters shared mixed views: some reported Cloudflare D1 as unreliable in production and noted a D1 developer's advice to prefer Durable Objects storage; others described building Paxos-based multi-master SQLite with WAL replication; and one argued that with AI agents, managing Postgres is now easy enough that SQLite's limitations make a full database server more appealing for remote use.

**Tags**: `#sqlite`, `#distributed-systems`, `#databases`, `#replication`, `#hacker-news`

---

<a id="item-8"></a>
## [FreeDNS: Long-Lived Free Dynamic DNS Service Discussed on Hacker News](https://freedns.afraid.org/) ⭐️ 6.0/10

A Hacker News discussion highlighted FreeDNS (freedns.afraid.org), a free dynamic DNS service that has been operating for nearly two decades, with users sharing their long-term experiences and raising security concerns about its absence from the Public Suffix List. FreeDNS remains a popular choice for hobbyists and small-scale projects needing free DNS hosting, and the discussion underscores the importance of security considerations like Public Suffix List inclusion for shared domain services. The main technical concern is that FreeDNS domains are not on the Public Suffix List, which can lead to cookie security issues because browsers may allow cookies to be set on the shared parent domain instead of isolated subdomains; users also noted the service's static interface and compared it to alternatives like dns.he.net and nic.eu.org.

hackernews · esher · Oct 24, 15:20 · [Discussion](https://news.ycombinator.com/item?id=50222133)

**Background**: Dynamic DNS (DDNS) allows a domain name to be automatically updated with a changing IP address, which is useful for accessing home networks or devices remotely. The Public Suffix List (PSL) is a catalog of domain suffixes under which anyone can register names, and it helps browsers enforce security boundaries for cookies and other web features. FreeDNS is a free service that offers both dynamic and static DNS hosting, including the ability to create subdomains under domains contributed by other users.

<details><summary>References</summary>
<ul>
<li><a href="https://freedns.afraid.org/">FreeDNS - Free DNS - Dynamic DNS - Static DNS subdomain and ...</a></li>
<li><a href="https://publicsuffix.org/">Public Suffix List</a></li>
<li><a href="https://www.radware.com/cyberpedia/application-delivery/dynamic-dns/">Dynamic DNS ( DDNS ): How it Works, Benefits & Security Risks</a></li>

</ul>
</details>

**Discussion**: Commenters generally praised FreeDNS for its longevity and reliability, with some using it for 15-20 years, but also pointed out the missing Public Suffix List listing as a security pain point and suggested alternatives like nic.eu.org for free domains and dns.he.net for backup DNS.

**Tags**: `#DNS`, `#free services`, `#security`, `#Public Suffix List`, `#Hacker News`

---

<a id="item-9"></a>
## [2018 Essay on Quantum Confusion Sparks HN Debate](https://www.southampton.ac.uk/~doug/quantum_physics/index.html) ⭐️ 6.0/10

A 2018 essay by a University of Southampton author expressing confusion about quantum physics interpretations was reposted and discussed on Hacker News, garnering 223 points and 153 comments. The discussion focused on the Many Worlds interpretation versus the Copenhagen interpretation, the nature of scientific models, and recommended learning resources. The discussion highlights ongoing public and expert fascination with the foundational questions of quantum mechanics, particularly the divide between the Many Worlds and Copenhagen interpretations. It also underscores how community forums like Hacker News serve as venues for informal science education and debate about the limits of models. Commenters debated whether the Many Worlds interpretation is more satisfactory than Copenhagen, with one physicist expressing minority skepticism about Many Worlds. Others emphasized that all models are wrong but some are useful, and shared book recommendations such as 'Picturing Quantum Processes' by Bob Coecke and 'Basic Concepts of Quantum Mechanics' by L. V. Tarasov.

hackernews · rramadass · Oct 24, 09:53 · [Discussion](https://news.ycombinator.com/item?id=50219666)

**Background**: Quantum mechanics is a fundamental theory in physics that describes nature at the smallest scales, but its mathematical formalism allows for multiple interpretations that attempt to explain how the theory corresponds to reality. The Copenhagen interpretation, historically dominant, posits that the wavefunction collapses upon measurement, while the Many Worlds interpretation, formalized by Hugh Everett, asserts that the universal wavefunction is objectively real and that all possible outcomes are physically realized in a branching multiverse. These interpretations are empirically indistinguishable, leading to ongoing philosophical debate.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Many-worlds_interpretation">Many - worlds interpretation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Interpretations_of_quantum_mechanics">Interpretations of quantum mechanics - Wikipedia</a></li>
<li><a href="https://plato.stanford.edu/entries/qm-manyworlds/">Many - Worlds Interpretation of Quantum Mechanics (Stanford...)</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion was lively and substantive, with commenters debating the merits of the Many Worlds interpretation versus Copenhagen, and one physicist noting they are in the minority for finding Many Worlds difficult to accept. Others argued that quantum mechanics is just a model, like attention in neural networks, and shared personal learning journeys and book recommendations.

**Tags**: `#quantum-physics`, `#science-communication`, `#many-worlds`, `#hackernews-discussion`, `#physics-education`

---

<a id="item-10"></a>
## [Local Wikipedia shows nearby articles within a half-hour walk](https://edjefferson.com/localwiki/) ⭐️ 6.0/10

A developer created Local Wikipedia, a web app that displays Wikipedia articles about places within a half-hour walk from the user's current location. The project was shared on Hacker News, where it received 1497 points and 240 comments. This project highlights how geolocation can make Wikipedia more personally relevant, sparking discussions about proximity bias and the desire for customizable search radii. It also demonstrates the appeal of simple, accessible side projects that leverage existing APIs. The app is essentially a wrapper around Wikipedia's built-in 'nearby' feature, as noted by commenters who found identical results. Users also pointed out that distances are shown in yards for European locations, which some found inappropriate.

hackernews · sohkamyung · Oct 22, 23:01 · [Discussion](https://news.ycombinator.com/item?id=50202285)

**Background**: Wikipedia offers a geolocation API that allows querying articles by coordinates, enabling apps to show place-related content. Isochrone mapping, which calculates areas reachable within a given travel time, is a common technique for proximity-based services. Proximity bias refers to the tendency to favor information or people that are physically close.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/W3C_Geolocation_API">W3C Geolocation API - Wikipedia</a></li>
<li><a href="https://stackoverflow.com/questions/4191165/wikipedia-api-for-geolocations">Wikipedia API for geolocations - Stack Overflow</a></li>
<li><a href="https://horizonmapper.com/isochrone-map-generator">Free Isochrone Map Generator | Drive, Walk & Cycle</a></li>

</ul>
</details>

**Discussion**: Commenters shared mixed reactions: some noted that nearby articles felt more pertinent due to proximity, while others criticized the fixed half-hour radius as impractical for rural areas and suggested making it configurable. A few pointed out that similar apps already exist, and one joked about the use of yards for European distances.

**Tags**: `#Wikipedia`, `#geolocation`, `#side-project`, `#proximity`, `#web-app`

---

<a id="item-11"></a>
## [Apple Music's 404 Page Hides Playable iPod with Brick Game](https://music.apple.com/this-url-doesnt-exist) ⭐️ 6.0/10

Apple Music's web 404 error page now features a playable replica of the first-generation iPod, complete with a working click wheel and a hidden Brick game, discovered on the 25th anniversary of the iPod's announcement. This whimsical Easter egg showcases Apple's playful side and taps into nostalgia for the iconic iPod, generating significant engagement and discussion on Hacker News. The Brick game is accessed by going to Settings > About and holding the center button for 5 seconds; the Easter egg was spotted by Kian and Alex Greenland, and some users report it only works with an Apple Music subscription.

hackernews · frizlab · Oct 23, 12:28 · [Discussion](https://news.ycombinator.com/item?id=50207910)

**Background**: The iPod was first announced by Apple in October 2001 and revolutionized portable music with its click wheel interface. The click wheel, introduced on the iPod mini in 2004 and later on the fourth-generation iPod, became an iconic and satisfying user interface. Apple discontinued the iPod line in 2022, but its legacy lives on through such Easter eggs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.macrumors.com/2026/10/23/apple-music-has-a-hidden-ipod-you-can-play-with/">Apple Music Has a Hidden iPod You Can Play With - MacRumors</a></li>
<li><a href="https://www.ithinkdiff.com/apple-music-ipod-easter-egg-404-page/">Apple Music iPod Easter Egg Hides on Its 404 Page</a></li>
<li><a href="https://www.notebookcheck.net/Apple-Music-s-404-page-hides-a-playable-first-generation-iPod-with-a-Brick-game.1432111.0.html">Apple Music’s 404 page hides a playable first-generation iPod ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed nostalgia for the click wheel and praised Apple's rare whimsy, while one noted the irony of engineers dealing with elevated 404 rates and another pointed out the subscription requirement.

**Tags**: `#Apple Music`, `#Easter egg`, `#UI design`, `#nostalgia`, `#Hacker News`

---