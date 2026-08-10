---
name: xhs-user-faved-notes
description: 拉取用户公开收藏的笔记列表，cursor 翻页。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) `GET /v1/xiaohongshu/app_v2/get_user_faved_notes`。

**何时使用：** 用户要看某账号公开收藏了哪些笔记

## 鉴权

`export YIGE_API_KEY=ak_xxx`（或 `--api-key`），请求头 `Authorization: Bearer <key>`。

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| — | — | 见可选 |
| `user_id` | 否 | 用户 ID 优先 |
| `share_text` | 否 | 用户分享链接 |
| `cursor` | 否 | 翻页：上一页最后一条 note_id |

文档：https://docs.tikhub.io/420136397e0

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --user-id 5a8cf39111be10466d285d6b
```

Base：`https://yige.zone`。超时建议 30s。勿泄露 API Key。
