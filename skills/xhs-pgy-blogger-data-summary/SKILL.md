---
name: xhs-pgy-blogger-data-summary
description: 账号维度数据概览（报价预估、内容占比、粉丝增长等）。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) `POST /v1/xiaohongshu/pgy/get_blogger_data_summary`。

**何时使用：** 快速看达人概览与同行对比

## 鉴权

`export YIGE_API_KEY=ak_xxx`（或 `--api-key`），请求头 `Authorization: Bearer <key>`。

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `user_id` | 是 | 博主 user_id |
| — | — | 无 |

文档：https://docs.tikhub.io/479321012e0

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --user-id 5c668b3e0000000012021605
```

Base：`https://yige.zone`。超时建议 30s。勿泄露 API Key。
