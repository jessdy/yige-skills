---
name: xhs-creator-hot-inspiration
description: 拉取创作者热点灵感列表。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) `GET /v1/xiaohongshu/app_v2/get_creator_hot_inspiration_feed`。

**何时使用：** 创作者要看当下热点灵感

## 鉴权

`export YIGE_API_KEY=ak_xxx`（或 `--api-key`），请求头 `Authorization: Bearer <key>`。

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| — | — | 见可选 |
| `cursor` | 否 | 翻页 |

文档：https://docs.tikhub.io/420136410e0

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py
```

Base：`https://yige.zone`。超时建议 30s。勿泄露 API Key。
