---
name: gzh-account-articles
description: 拉取公众号历史发文列表（单页），支持 offset 游标翻页与文章/视频/音频分栏。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) 公众号接口 `/v1/wechat_mp/v2/fetch_account_articles`，返回结构化 JSON。

**何时使用：** 用户要看某公众号最近发了什么、拉历史文章列表、翻页

**超时：** 微信侧较慢，客户端超时请设 **30 秒**。默认 `raw=false`（精简字段），需要完整上游结构时加 `--raw`。

## 鉴权

1. 打开 [API Key 页面](https://yige.zone/settings/api-keys) 创建密钥
2. 设置环境变量：`export YIGE_API_KEY=ak_xxx`（或传 `--api-key`）
3. 请求头：`Authorization: Bearer <YIGE_API_KEY>`

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `username` | 是 | 公众号 gh_username |
| `page_size` | 否 | 每页 10–20，默认 20 |
| `offset` | 否 | 翻页游标，首页留空；下一页传响应 next_offset |
| `item_show_type` | 否 | 0=文章(默认) / 5=视频 / 7=音频 / 8=贴图 |
| `raw` | 否 | 默认 false（精简）；`--raw` 为 true |

接口文档参考：https://docs.tikhub.io/472974858e0

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --username gh_363b924965e9 --page-size 20
```

Agent 拿到 stdout 的 JSON 后，用 `data` 字段向用户汇报；`content_id` / `comment_id` 等大整数请保持**字符串**，勿转成 Number。

## 常见链路

1. **搜账号** → `gzh-search`（`business_type=account`）拿到 `gh_…`
2. **看资料 / 列表 / 菜单** → `gzh-account-profile` / `gzh-account-articles` / `gzh-account-services`
3. **读文 / 数据 / 评论** → `gzh-article-detail` / `gzh-article-stats` / `gzh-article-comments`
4. **展开回复** → `gzh-comment-replies`（传评论 `content_id`）

## 注意

- Base URL：`https://yige.zone`（勿再使用已下线的 `/story/api/...`）
- 按次计费，请关注控制台余额
- 勿把 API Key 写入仓库或前端
