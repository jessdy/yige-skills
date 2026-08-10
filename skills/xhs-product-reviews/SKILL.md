---
name: xhs-product-reviews
description: 拉取商品评价列表，支持排序与仅看有图。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) `GET /v1/xiaohongshu/app_v2/get_product_reviews`。

**何时使用：** 用户要读商品评价原文

## 鉴权

`export YIGE_API_KEY=ak_xxx`（或 `--api-key`），请求头 `Authorization: Bearer <key>`。

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `sku_id` | 是 | 商品 SKU ID |
| `page` | 否 | 页码从0 |
| `sort_strategy_type` | 否 | 0综合/1最新 |
| `share_pics_only` | 否 | 0全部/1仅有图 |

文档：https://docs.tikhub.io/420136405e0

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --sku-id 669ddd44e05f3700011067ed --share-pics-only 1
```

Base：`https://yige.zone`。超时建议 30s。勿泄露 API Key。
