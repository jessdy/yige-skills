---
name: xhs-topic-info
description: 根据 page_id 获取话题名称、浏览量、讨论数等。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) `GET /v1/xiaohongshu/app_v2/get_topic_info`。

**何时使用：** 用户要查看某个话题/标签页信息

## 鉴权

`export YIGE_API_KEY=ak_xxx`（或 `--api-key`），请求头 `Authorization: Bearer <key>`。

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `page_id` | 是 | 话题页面 ID |
| `note_id` | 否 | 来源笔记 ID，可选 |

文档：https://docs.tikhub.io/420136407e0

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --page-id 5c1cc866febed9000184b7c1
```

Base：`https://yige.zone`。超时建议 30s。勿泄露 API Key。
