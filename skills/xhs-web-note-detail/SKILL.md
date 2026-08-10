---
name: xhs-web-note-detail
description: Web V3 笔记详情；需 note_id 与分享链接中的 xsec_token。优先用 App V2 图文/视频详情。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) `GET /v1/xiaohongshu/web_v3/fetch_note_detail`。

**何时使用：** 用户有 note_id+xsec_token，或 App V2 不可用时兜底

## 鉴权

`export YIGE_API_KEY=ak_xxx`（或 `--api-key`），请求头 `Authorization: Bearer <key>`。

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `note_id` | 是 | 笔记 ID |
| `xsec_token` | 是 | 分享链接中的 xsec_token |
| — | — | 无 |

文档：https://docs.tikhub.io/438852168e0

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --note-id xxx --xsec-token yyy
```

Base：`https://yige.zone`。超时建议 30s。勿泄露 API Key。
