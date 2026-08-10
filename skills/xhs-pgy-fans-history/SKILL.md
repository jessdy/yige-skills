---
name: xhs-pgy-fans-history
description: 博主粉丝增长历史趋势。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) `POST /v1/xiaohongshu/pgy/get_blogger_fans_history`。

**何时使用：** 看粉丝增减趋势

## 鉴权

`export YIGE_API_KEY=ak_xxx`（或 `--api-key`），请求头 `Authorization: Bearer <key>`。

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `user_id` | 是 | 博主 user_id |
| `date_type` | 否 | 1近7天/2近30天/3近90天 |

文档：https://docs.tikhub.io/479321008e0

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --user-id 5c668b3e0000000012021605 --date-type 2
```

Base：`https://yige.zone`。超时建议 30s。勿泄露 API Key。
