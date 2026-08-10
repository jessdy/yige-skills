---
name: xhs-homefeed-categories
description: 获取首页推荐分类频道列表，供 homefeed 的 category 参数使用。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) `GET /v1/xiaohongshu/web_v3/fetch_homefeed_categories`。

**何时使用：** 用户要按频道刷首页，需先拿分类 ID

## 鉴权

`export YIGE_API_KEY=ak_xxx`（或 `--api-key`），请求头 `Authorization: Bearer <key>`。

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| — | — | 见可选 |
| — | — | 无 |

文档：https://docs.tikhub.io/438852176e0

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py
```

Base：`https://yige.zone`。超时建议 30s。勿泄露 API Key。
