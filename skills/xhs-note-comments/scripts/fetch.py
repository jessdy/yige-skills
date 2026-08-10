#!/usr/bin/env python3
"""Call Yige Xiaohongshu API. Auth via YIGE_API_KEY env or --api-key."""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

BASE = os.environ.get("YIGE_API_BASE", "https://yige.zone").rstrip("/")
TIMEOUT = 30


def request(method: str, path: str, api_key: str, *, params: dict | None = None, body: dict | None = None) -> dict:
    url = f"{BASE}{path}"
    if params:
        clean = {k: v for k, v in params.items() if v is not None and v != ""}
        if clean:
            url = f"{url}?{urllib.parse.urlencode(clean)}"
    data = None
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
        "User-Agent": "yige-skills/xhs",
    }
    if body is not None:
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, method=method.upper(), headers=headers)
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


PATH = "/v1/xiaohongshu/app_v2/get_note_comments"


def main() -> None:
    p = argparse.ArgumentParser(description="小红书笔记评论")
    add_common(p)
    p.add_argument("--note-id", default="")
    p.add_argument("--share-text", default="")
    p.add_argument("--cursor", default="")
    p.add_argument("--index", type=int, default=0)
    p.add_argument("--page-area", default="UNFOLDED")
    p.add_argument("--sort-strategy", default="latest_v2")
    args = p.parse_args()
    api_key = resolve_key(args.api_key)
    if not args.note_id and not args.share_text:
        p.error("需要 --note-id 或 --share-text 之一")
    params = {
        "note_id": args.note_id or None,
        "share_text": args.share_text or None,
        "cursor": args.cursor or None,
        "index": args.index,
        "pageArea": args.page_area,
        "sort_strategy": args.sort_strategy,
    }
    result = request("GET", PATH, api_key, params=params)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
