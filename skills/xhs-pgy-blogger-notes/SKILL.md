---
name: xhs-pgy-blogger-notes
description: 拉取蒲公英侧博主笔记表现明细。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) `POST /v1/xiaohongshu/pgy/get_blogger_notes`。

**何时使用：** 分析达人笔记阅读/互动表现

## 鉴权

`export YIGE_API_KEY=ak_xxx`（或 `--api-key`），请求头 `Authorization: Bearer <key>`。

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `user_id` | 是 | 博主 user_id |
| `page_number` | 否 | 页码从1 |
| `page_size` | 否 | 1-100 |
| `note_type` | 否 | 0全部/1图文/2视频 |
| `order_type` | 否 | 1阅读/2互动/3最新 |
| `advertise_switch` | 否 | 1全部/0自然 |

文档：https://docs.tikhub.io/479321008e0

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --user-id 5c668b3e0000000012021605 --order-type 2
```

Base：`https://yige.zone`。超时建议 30s。勿泄露 API Key。
