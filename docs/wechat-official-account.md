# GitHub Actions + WeChat Official Account

This setup runs Horizon every day at 08:00 Asia/Shanghai, collects domestic
and international news candidates, uses AI scoring and deduplication, keeps up
to 36 selected items, publishes the generated Chinese digest to GitHub Pages,
and creates a WeChat Official Account article from the same digest.

## Files To Add

Copy these files into the same paths in the repository:

- .github/workflows/daily-wechat-news.yml
- data/config.wechat-news.example.json
- scripts/publish_wechat.py
- docs/wechat-official-account.md

## GitHub Secrets

Add these in Settings -> Secrets and variables -> Actions -> Secrets:

- DEEPSEEK_API_KEY: DeepSeek API key. To use OpenAI or Claude instead, update
  the ai block in data/config.wechat-news.example.json.
- WECHAT_APP_ID: WeChat Official Account AppID.
- WECHAT_APP_SECRET: WeChat Official Account AppSecret.
- WECHAT_THUMB_MEDIA_ID: Permanent image media_id from the official account
  media library. WeChat draft articles require a cover image.

## GitHub Variables

Optional variables in Settings -> Secrets and variables -> Actions -> Variables:

- WECHAT_PUBLISH_MODE: draft by default. Set to publish to call WeChat's publish API.
- WECHAT_AUTHOR: article author, default Horizon.
- WECHAT_CONTENT_SOURCE_URL: Read original URL, usually the GitHub Pages home page.
- WECHAT_DIGEST: article digest. If empty, the script derives it from the digest text.
- RSSHUB_BASE: RSSHub base URL, default https://rsshub.app. A self-hosted RSSHub
  instance is recommended if the public service is unstable.

## First Test

1. Keep WECHAT_PUBLISH_MODE as draft.
2. Manually run Daily WeChat News from the GitHub Actions page.
3. Check the workflow artifact and the WeChat draft box.
4. After the draft content looks stable, set WECHAT_PUBLISH_MODE to publish.

## Notes

filtering.max_items controls the final 36-item cap. The domestic, international,
and tech/finance groups are upper bounds, not hard quotas. If one group has too
few high-quality items on a given day, Horizon can publish fewer items or let
other groups fill the digest instead of forcing low-quality content.
