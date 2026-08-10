---
name: xhs-pgy-fans-summary
description: 博主粉丝量级、活跃/互动/阅读粉丝等概览。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) `POST /v1/xiaohongshu/pgy/get_blogger_fans_summary`。

**何时使用：** 评估粉丝质量与活跃度

## 鉴权

`export YIGE_API_KEY=ak_xxx`（或 `--api-key`），请求头 `Authorization: Bearer <key>`。

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `user_id` | 是 | 博主 user_id |
| — | — | 无 |

文档：https://docs.tikhub.io/479321013e0

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --user-id 5c668b3e0000000012021605
```

Base：`https://yige.zone`。超时建议 30s。勿泄露 API Key。
