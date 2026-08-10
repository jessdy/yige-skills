---
name: xhs-search-images
description: 按关键词搜索小红书图片结果。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) `GET /v1/xiaohongshu/app_v2/search_images`。

**何时使用：** 用户要按关键词搜图片/壁纸素材

## 鉴权

`export YIGE_API_KEY=ak_xxx`（或 `--api-key`），请求头 `Authorization: Bearer <key>`。

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `keyword` | 是 | 搜索关键词 |
| `page` | 否 | 页码从1 |
| `search_id` | 否 | 翻页 |
| `search_session_id` | 否 | 翻页 |
| `word_request_id` | 否 | 翻页 |

文档：https://docs.tikhub.io/420136400e0

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --keyword 壁纸
```

Base：`https://yige.zone`。超时建议 30s。勿泄露 API Key。
