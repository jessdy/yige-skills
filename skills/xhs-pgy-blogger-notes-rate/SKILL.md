---
name: xhs-pgy-blogger-notes-rate
description: 博主笔记转化率/报价相关表现。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) `POST /v1/xiaohongshu/pgy/get_blogger_notes_rate`。

**何时使用：** 评估达人笔记转化效率

## 鉴权

`export YIGE_API_KEY=ak_xxx`（或 `--api-key`），请求头 `Authorization: Bearer <key>`。

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `user_id` | 是 | 博主 user_id |
| `note_type` | 否 | 1图文/2视频/3全部 |
| `date_type` | 否 | 1/2/3 |
| `advertise_switch` | 否 | 1/0 |

文档：https://docs.tikhub.io/479321008e0

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --user-id 5c668b3e0000000012021605
```

Base：`https://yige.zone`。超时建议 30s。勿泄露 API Key。
