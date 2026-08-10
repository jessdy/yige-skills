---
name: xhs-pgy-blogger-list
description: 按品牌广告主 ID 与粉丝区间筛选蒲公英博主列表。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) `POST /v1/xiaohongshu/pgy/get_blogger_list`。

**何时使用：** 品牌方选号，按粉丝量筛选达人

## 鉴权

`export YIGE_API_KEY=ak_xxx`（或 `--api-key`），请求头 `Authorization: Bearer <key>`。

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `brand_user_id` | 是 | 品牌方/广告主用户 ID |
| `page_num` | 否 | 页码 |
| `page_size` | 否 | 1-100 |
| `fans_number_lower` | 否 | 粉丝下限 |
| `fans_number_upper` | 否 | 粉丝上限 |

文档：https://docs.tikhub.io/479321008e0

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --brand-user-id 5dcfa5370000000001006030 --fans-number-lower 10000 --fans-number-upper 1000000
```

Base：`https://yige.zone`。超时建议 30s。勿泄露 API Key。
