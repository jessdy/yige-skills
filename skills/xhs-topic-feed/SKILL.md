---
name: xhs-topic-feed
description: 拉取话题下笔记列表，支持最热/最新与游标翻页。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) `GET /v1/xiaohongshu/app_v2/get_topic_feed`。

**何时使用：** 用户要浏览某话题下的笔记

## 鉴权

`export YIGE_API_KEY=ak_xxx`（或 `--api-key`），请求头 `Authorization: Bearer <key>`。

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `page_id` | 是 | 话题页面 ID |
| `sort` | 否 | trend=最热(默认) / time=最新 |
| `cursor_score` | 否 | 翻页字段 |
| `last_note_id` | 否 | 翻页 |
| `last_note_ct` | 否 | 翻页 |
| `session_id` | 否 | 翻页保持 |
| `first_load_time` | 否 | 翻页保持 |

文档：https://docs.tikhub.io/420136408e0

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --page-id 5c1cc866febed9000184b7c1 --sort trend
```

Base：`https://yige.zone`。超时建议 30s。勿泄露 API Key。
