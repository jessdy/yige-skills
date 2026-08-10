---
name: xhs-web-user-info
description: Web V3 用户主页信息。优先用 App V2 xhs-user-info。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) `GET /v1/xiaohongshu/web_v3/fetch_user_info`。

**何时使用：** 需要 Web 面用户资料时

## 鉴权

`export YIGE_API_KEY=ak_xxx`（或 `--api-key`），请求头 `Authorization: Bearer <key>`。

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `user_id` | 是 | 用户 ID |
| — | — | 无 |

文档：https://docs.tikhub.io/438852177e0

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --user-id 61b46d790000000010008153
```

Base：`https://yige.zone`。超时建议 30s。勿泄露 API Key。
