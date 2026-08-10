---
name: xhs-creator-inspiration
description: 拉取创作者中心推荐灵感流。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) `GET /v1/xiaohongshu/app_v2/get_creator_inspiration_feed`。

**何时使用：** 创作者要找选题灵感、推荐灵感流

## 鉴权

`export YIGE_API_KEY=ak_xxx`（或 `--api-key`），请求头 `Authorization: Bearer <key>`。

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| — | — | 见可选 |
| `cursor` | 否 | 翻页如 r_1 |
| `tab` | 否 | 标签默认0 |

文档：https://docs.tikhub.io/420136409e0

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py
```

Base：`https://yige.zone`。超时建议 30s。勿泄露 API Key。
