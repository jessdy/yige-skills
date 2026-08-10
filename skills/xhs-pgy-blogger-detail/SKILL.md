---
name: xhs-pgy-blogger-detail
description: 获取蒲公英博主资料、粉丝、合作报价等。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) `POST /v1/xiaohongshu/pgy/get_blogger_detail`。

**何时使用：** 品牌选号，要看达人蒲公英详情与报价

## 鉴权

`export YIGE_API_KEY=ak_xxx`（或 `--api-key`），请求头 `Authorization: Bearer <key>`。

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `user_id` | 是 | 蒲公英博主 user_id |
| — | — | 无 |

文档：https://docs.tikhub.io/479321008e0

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --user-id 5c668b3e0000000012021605
```

Base：`https://yige.zone`。超时建议 30s。勿泄露 API Key。
