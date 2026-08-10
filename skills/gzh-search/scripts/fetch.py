#!/usr/bin/env python3
"""Call Yige WeChat MP API. Auth via YIGE_API_KEY env or --api-key."""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

BASE = os.environ.get("YIGE_API_BASE", "https://yige.zone").rstrip("/")
TIMEOUT = 30


def post(path: str, body: dict, api_key: str) -> dict:
    url = f"{BASE}{path}"
    data = json.dumps(body, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "yige-skills/gzh",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            raw = resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        print(f"HTTP {e.code}: {err_body}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Request failed: {e}", file=sys.stderr)
        sys.exit(1)
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        print(raw)
        sys.exit(1)


def resolve_key(cli_key: str | None) -> str:
    key = (cli_key or os.environ.get("YIGE_API_KEY") or "").strip()
    if not key:
        print(
            "Missing API key. Set YIGE_API_KEY or pass --api-key. "
            "Get one at https://yige.zone/settings/api-keys",
            file=sys.stderr,
        )
        sys.exit(1)
    return key


def add_common(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--api-key", default=None, help="Override YIGE_API_KEY")
    parser.add_argument(
        "--raw",
        action="store_true",
        help="Return raw upstream payload (default: raw=false, simplified)",
    )


def main() -> None:
    p = argparse.ArgumentParser(description="微信搜一搜（公众号/文章）")
    add_common(p)
    p.add_argument("--keyword", required=True)
    p.add_argument("--business-type", default="account", help="all/account/article/…")
    p.add_argument("--sort", default="default", help="default/latest/hot")
    p.add_argument("--publish-time", default="all", help="all/day/week/half_year")
    p.add_argument("--offset", type=int, default=0)
    p.add_argument("--cursor", default="", help="翻页游标，首页留空")
    args = p.parse_args()
    api_key = resolve_key(args.api_key)
    body = {
        "keyword": args.keyword,
        "business_type": args.business_type,
        "sort": args.sort,
        "publish_time": args.publish_time,
        "offset": args.offset,
        "raw": bool(args.raw),
    }
    if args.cursor:
        body["cursor"] = args.cursor
    result = post("/v1/wechat_search/v2/fetch_search", body, api_key)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
