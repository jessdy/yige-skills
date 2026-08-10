---
name: xhs-image-note-detail
description: 根据 note_id 或分享链接获取图文笔记正文、图片、互动数据与作者信息。需要一格数据 API Key。
---

## 简介

调用[一格数据](https://yige.zone) 小红书接口 `GET /v1/xiaohongshu/app_v2/get_image_note_detail`，返回结构化 JSON。

**何时使用：** 用户给了图文笔记链接或 note_id，要读正文/图片/点赞收藏

**超时：** 建议客户端超时 **30 秒**。若偶发 400，可重试几次。

## 鉴权

1. 打开 [API Key 页面](https://yige.zone/settings/api-keys) 创建密钥
2. `export YIGE_API_KEY=ak_xxx`（或 `--api-key`）
3. 请求头：`Authorization: Bearer <YIGE_API_KEY>`

## 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| （见可选） | — | `note_id`/`user_id` 与 `share_text` 通常二选一 |
| `note_id` | 否 | 笔记 ID，优先 |
| `share_text` | 否 | 笔记分享链接 |

接口文档参考：https://docs.tikhub.io/420136391e0

## 用法

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --note-id 697c0eee000000000a03c308
```

Agent 拿到 stdout 的 JSON 后，用 `data` 向用户汇报。图文详情用 `xhs-image-note-detail`，视频用 `xhs-video-note-detail`；类型不确定时可先搜笔记再按返回 type 选择。

## 常见链路

1. **搜内容** → `xhs-search-notes` / `xhs-search-suggest`
2. **找人** → `xhs-search-users` → `xhs-user-info` → `xhs-user-notes`
3. **读笔记** → `xhs-image-note-detail` 或 `xhs-video-note-detail`
4. **看评论** → `xhs-note-comments` → `xhs-note-sub-comments`
5. **首页发现** → `xhs-homefeed`

## 注意

- Base URL：`https://yige.zone`（勿使用已下线的 `/story/api/...`）
- 按次计费；勿把 API Key 写入仓库或前端
- 小红书不提供播放量/下载量字段
