---
name: xhs-hot-list
description: 获取小红书热榜数据。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) `GET /v1/xiaohongshu/web_v3/fetch_hot_list`。

**何时使用：** 用户要看热榜/热点话题

## 鉴权

`export YIGE_API_KEY=ak_xxx`（或 `--api-key`），请求头 `Authorization: Bearer <key>`。

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| — | — | 见可选 |
| — | — | 无 |

文档：https://tikhub.io/zh/xiaohongshu-api

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py
```

Base：`https://yige.zone`。超时建议 30s。勿泄露 API Key。
