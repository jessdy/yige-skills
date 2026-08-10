---
name: xhs-pgy-note-detail
description: 获取蒲公英侧商业笔记详情。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) `POST /v1/xiaohongshu/pgy/get_note_detail`。

**何时使用：** 分析商业合作笔记详情

## 鉴权

`export YIGE_API_KEY=ak_xxx`（或 `--api-key`），请求头 `Authorization: Bearer <key>`。

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `note_id` | 是 | 笔记 ID |
| — | — | 无 |

文档：https://docs.tikhub.io/479321008e0

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --note-id 697c0eee000000000a03c308
```

Base：`https://yige.zone`。超时建议 30s。勿泄露 API Key。
