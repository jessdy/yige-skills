---
name: xhs-product-detail
description: 根据 sku_id 获取商品价格、规格、库存与描述。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) `GET /v1/xiaohongshu/app_v2/get_product_detail`。

**何时使用：** 用户有 sku_id，要看商品详情

## 鉴权

`export YIGE_API_KEY=ak_xxx`（或 `--api-key`），请求头 `Authorization: Bearer <key>`。

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `sku_id` | 是 | 商品 SKU ID |
| — | — | 无 |

文档：https://docs.tikhub.io/420136403e0

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --sku-id 669ddd44e05f3700011067ed
```

Base：`https://yige.zone`。超时建议 30s。勿泄露 API Key。
