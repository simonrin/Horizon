---
layout: default
title: "Horizon Summary: 2026-08-13 (ZH)"
date: 2026-08-13
lang: zh
---

> 从 376 条内容中筛选出 1 条重要资讯。

---

1. [Tailscale 将数据库损坏追溯到 16 年前的 SQLite WAL-Reset 漏洞](#item-1) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [Tailscale 将数据库损坏追溯到 16 年前的 SQLite WAL-Reset 漏洞](https://tailscale.com/blog/sqlite-wal-reset-bug) ⭐️ 9.0/10

Tailscale 公开详细说明了他们如何将反复出现的数据库损坏事件追溯到 16 年前的 SQLite 漏洞，该漏洞现已被正式命名为 WAL-Reset 漏洞。该漏洞影响 SQLite 3.7.0 至 3.51.2 版本，并在 2026 年 3 月 13 日发布的 SQLite 3.51.3 中修复。 这一发现意义重大，因为它表明即使是像 SQLite 这样成熟且广泛使用的软件，也可能隐藏着微妙且长期存在的漏洞，在特定条件下导致数据损坏。调试过程也凸显了资助开源工具的价值，因为 Tailscale 对自定义 SQLite VFS shim 的投资帮助隔离了竞态条件。 该漏洞是 SQLite WAL（预写日志）模式下的一个数据竞态，即使在单写入者设计下，当多个连接并发使用时也可能发生。Tailscale 在确定根本原因之前经历了 19 次损坏事件，并且在调查过程中还发现了第二个独立的过期表达式索引漏洞。

hackernews · ropbear · 8月12日 14:22 · [社区讨论](https://news.ycombinator.com/item?id=49272832)

**背景**: SQLite 是一种广泛使用的嵌入式数据库，支持 WAL 模式以提高并发性和性能。在 WAL 模式下，更改会先追加到 WAL 文件中，然后再检查点写入主数据库文件。WAL-Reset 漏洞涉及 WAL 重置过程中的竞态条件，可能导致数据库损坏。Tailscale 使用 SQLite 作为其 tailnet 的控制平面数据库，损坏由其备份管道检测到。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tailscale.com/blog/sqlite-wal-reset-bug">How Tailscale helped find the SQLite WAL-Reset bug</a></li>
<li><a href="https://byteiota.com/sqlite-wal-bug-tailscale-found-it-after-19-corruptions/">SQLite WAL Bug: Tailscale Found It After 19 Corruptions</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区称赞了这篇文章详细的调试叙述以及公司资助开源开发的决定。评论者指出，即使 SQLite 拥有庞大的测试套件（9200 万行测试），漏洞仍然可能漏过，有些人希望 Tailscale 能继续通过支持合同支持 SQLite。

**标签**: `#SQLite`, `#database`, `#debugging`, `#open-source`, `#Tailscale`

---