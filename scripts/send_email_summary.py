"""Send the latest generated Horizon summary by email."""

from __future__ import annotations

import argparse
import html
import os
import re
import smtplib
import ssl
from datetime import datetime
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path


def env_required(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def env_bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None or not value.strip():
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def latest_summary(lang: str) -> Path:
    summary_dir = Path("data/summaries")
    candidates = sorted(
        summary_dir.glob(f"*-{lang}.md"),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )
    if not candidates:
        raise SystemExit(f"No generated summary found in {summary_dir} for lang={lang!r}")
    return candidates[0]


def strip_markdown(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\x60{3}.*?\x60{3}", "", text, flags=re.DOTALL)
    text = re.sub(r"<details>.*?</details>", "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<a\s+id=["\'][^"\']+["\']\s*></a>', "", text, flags=re.IGNORECASE)
    text = re.sub(
        r'<a\s+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>',
        lambda match: f"{strip_markdown(match.group(2))} ({match.group(1)})",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    text = re.sub(r"</?(?:ul|ol|li|summary|p|br)[^>]*>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (\2)", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"__([^_]+)__", r"\1", text)
    text = re.sub(r"\x60([^\x60]+)\x60", r"\1", text)
    text = re.sub(r"^\s{0,3}#{1,6}\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*>\s?", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*[-*_]{3,}\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return html.unescape(text).strip()


def split_paragraphs(text: str) -> list[str]:
    return [paragraph.strip() for paragraph in re.split(r"\n\s*\n", text) if paragraph.strip()]


def split_generated_summary(markdown: str) -> tuple[str, str, list[dict[str, str]]]:
    text = markdown.replace("\r\n", "\n").replace("\r", "\n")
    first_heading = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    title = first_heading.group(1).strip() if first_heading else "Horizon Daily News"

    intro_match = re.search(r"^>\s*(.+)$", text, flags=re.MULTILINE)
    intro = intro_match.group(1).strip() if intro_match else ""

    parts = re.split(r'\n\s*<a\s+id=["\']item-(\d+)["\']\s*></a>\s*\n', text, flags=re.IGNORECASE)
    items: list[dict[str, str]] = []

    for i in range(1, len(parts), 2):
        block = parts[i + 1].strip()
        header = re.search(r"^##\s+(.+)$", block, flags=re.MULTILINE)
        if not header:
            continue

        header_text = header.group(1).strip()
        title_match = re.match(r"\[([^\]]+)\]\(([^)]+)\)\s*(.*)", header_text)
        if title_match:
            item_title = title_match.group(1).strip()
            url = title_match.group(2).strip()
            score = title_match.group(3).strip()
        else:
            item_title = strip_markdown(header_text)
            url_match = re.search(r"https?://\S+", header_text)
            url = url_match.group(0).rstrip(")") if url_match else ""
            score = ""

        body = block[header.end() :].strip()
        body = strip_markdown(body)
        items.append(
            {
                "title": strip_markdown(item_title),
                "url": url,
                "score": strip_markdown(score),
                "body": body,
            }
        )

    return strip_markdown(title), strip_markdown(intro), items


def build_plain_email_body(markdown: str) -> str:
    title, intro, items = split_generated_summary(markdown)
    if not items:
        return strip_markdown(markdown)

    lines = [title]
    if intro:
        lines.extend(["", intro])
    lines.append("")

    for index, item in enumerate(items, start=1):
        heading = f"{index}. {item['title']}"
        if item["score"]:
            heading = f"{heading} {item['score']}"
        lines.append(heading)
        if item["url"]:
            lines.append(f"链接/跳转: {item['url']}")

        paragraphs = split_paragraphs(item["body"])
        if paragraphs:
            lines.extend(["", f"重点: {paragraphs[0]}"])
            if len(paragraphs) > 1:
                lines.extend(["", *paragraphs[1:]])
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def link_icons(url: str) -> str:
    if not url:
        return ""
    safe_url = html.escape(url, quote=True)
    return (
        f' <a href="{safe_url}" title="原文链接" '
        'style="color:#2563eb;text-decoration:none;font-size:16px;">🔗</a>'
        f' <a href="{safe_url}" title="跳转打开" '
        'style="color:#2563eb;text-decoration:none;font-size:16px;">↗</a>'
    )


def html_paragraph(text: str, *, muted: bool = False) -> str:
    escaped = html.escape(text)
    color = "#64748b" if muted else "#0f172a"
    return (
        f'<p style="margin:8px 0 0 0;color:{color};font-size:15px;'
        f'line-height:1.65;">{escaped}</p>'
    )


def build_html_email_body(markdown: str) -> str:
    title, intro, items = split_generated_summary(markdown)
    if not items:
        return f"<pre>{html.escape(strip_markdown(markdown))}</pre>"

    item_cards: list[str] = []
    for index, item in enumerate(items, start=1):
        paragraphs = split_paragraphs(item["body"])
        key_point = paragraphs[0] if paragraphs else ""
        details = paragraphs[1:]

        score_html = ""
        if item["score"]:
            score_html = (
                '<span style="margin-left:8px;color:#f59e0b;font-size:13px;'
                f'font-weight:600;">{html.escape(item["score"])}</span>'
            )

        detail_html = "".join(html_paragraph(paragraph, muted=True) for paragraph in details)

        key_html = ""
        if key_point:
            key_html = (
                '<div style="margin-top:12px;padding:12px 14px;'
                'background:#fff7ed;border-left:4px solid #f97316;'
                'border-radius:8px;color:#7c2d12;font-size:15px;line-height:1.65;">'
                '<strong>重点：</strong>'
                f'{html.escape(key_point)}'
                '</div>'
            )

        item_cards.append(
            '<section style="margin:18px 0;padding:18px 18px;'
            'border:1px solid #e2e8f0;border-radius:14px;background:#ffffff;">'
            '<h2 style="margin:0;color:#0f172a;font-size:18px;line-height:1.45;">'
            f'<span style="color:#2563eb;">{index}.</span> '
            f'<strong>{html.escape(item["title"])}</strong>'
            f'{link_icons(item["url"])}'
            f'{score_html}'
            '</h2>'
            f'{key_html}'
            f'{detail_html}'
            '</section>'
        )

    intro_html = ""
    if intro:
        intro_html = (
            '<p style="margin:8px 0 0 0;color:#475569;font-size:15px;'
            f'line-height:1.6;">{html.escape(intro)}</p>'
        )

    return (
        '<!doctype html><html><body style="margin:0;padding:0;'
        'background:#f8fafc;font-family:-apple-system,BlinkMacSystemFont,'
        'Segoe UI,Arial,"Microsoft YaHei",sans-serif;">'
        '<main style="max-width:760px;margin:0 auto;padding:24px 14px;">'
        '<header style="padding:20px 18px;background:#0f172a;'
        'border-radius:16px;color:white;">'
        f'<h1 style="margin:0;font-size:24px;line-height:1.35;">{html.escape(title)}</h1>'
        f'{intro_html}'
        '</header>'
        f'{"".join(item_cards)}'
        '</main></body></html>'
    )


def build_message(summary_path: Path, lang: str) -> EmailMessage:
    mail_to = env_required("MAIL_TO")
    mail_address = os.getenv("SMTP_FROM") or env_required("SMTP_USERNAME")
    mail_from = formataddr(("News", mail_address))
    subject_prefix = os.getenv("MAIL_SUBJECT_PREFIX", "Horizon Daily News")
    today = datetime.now().strftime("%Y-%m-%d")

    raw_body = summary_path.read_text(encoding="utf-8").strip()
    if not raw_body:
        raise SystemExit(f"Generated summary is empty: {summary_path}")

    plain_body = build_plain_email_body(raw_body)
    html_body = build_html_email_body(raw_body)

    message = EmailMessage()
    message["From"] = mail_from
    message["To"] = mail_to
    message["Subject"] = f"{subject_prefix} {today}"
    message.set_content(plain_body)
    message.add_alternative(html_body, subtype="html")
    message["X-Horizon-Lang"] = lang
    return message


def send(message: EmailMessage) -> None:
    host = env_required("SMTP_HOST")
    port = int(os.getenv("SMTP_PORT", "587"))
    username = env_required("SMTP_USERNAME")
    password = env_required("SMTP_PASSWORD")
    use_ssl = env_bool("SMTP_USE_SSL", port == 465)
    starttls = env_bool("SMTP_STARTTLS", not use_ssl and port != 25)

    if use_ssl:
        with smtplib.SMTP_SSL(host, port, context=ssl.create_default_context()) as server:
            server.login(username, password)
            server.send_message(message)
        return

    with smtplib.SMTP(host, port) as server:
        server.ehlo()
        if starttls:
            server.starttls(context=ssl.create_default_context())
            server.ehlo()
        server.login(username, password)
        server.send_message(message)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lang", default="zh")
    parser.add_argument("--summary", type=Path)
    args = parser.parse_args()

    summary_path = args.summary or latest_summary(args.lang)
    message = build_message(summary_path, args.lang)
    send(message)
    print(f"Sent {summary_path} to {message['To']}")


if __name__ == "__main__":
    main()
