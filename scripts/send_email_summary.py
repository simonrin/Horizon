"""Send the latest generated Horizon summary by email."""

from __future__ import annotations

import argparse
import os
import smtplib
import ssl
from datetime import datetime
from email.message import EmailMessage
from pathlib import Path


def env_required(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def env_bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
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


def build_message(summary_path: Path, lang: str) -> EmailMessage:
    mail_to = env_required("MAIL_TO")
    mail_from = os.getenv("SMTP_FROM") or env_required("SMTP_USERNAME")
    subject_prefix = os.getenv("MAIL_SUBJECT_PREFIX", "Horizon Daily News")
    today = datetime.now().strftime("%Y-%m-%d")

    body = summary_path.read_text(encoding="utf-8").strip()
    if not body:
        raise SystemExit(f"Generated summary is empty: {summary_path}")

    message = EmailMessage()
    message["From"] = mail_from
    message["To"] = mail_to
    message["Subject"] = f"{subject_prefix} {today}"
    message.set_content(body)

    message.add_attachment(
        body.encode("utf-8"),
        maintype="text",
        subtype="markdown",
        filename=summary_path.name,
    )
    message["X-Horizon-Lang"] = lang
    return message


def send(message: EmailMessage) -> None:
    host = env_required("SMTP_HOST")
    port = int(os.getenv("SMTP_PORT", "587"))
    username = env_required("SMTP_USERNAME")
    password = env_required("SMTP_PASSWORD")
    use_ssl = env_bool("SMTP_USE_SSL", port == 465)
    starttls = env_bool("SMTP_STARTTLS", not use_ssl)

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
