---
name: gzh-account-articles
description: 拉取公众号历史发文单页列表，支持文章/视频/音频分栏与 next_offset 翻页，适合内容日历与选题复盘。 需要一格数据 API Key。触发词：公众号文章列表、微信公众号数据、gzh-account-articles
---

## 简介

公众号文章列表 基于[一格数据](https://yige.zone) 开放接口，把微信公众号公开数据以结构化 JSON 返回，方便 Agent 与业务系统直接消费。

拉取公众号历史发文单页列表，支持文章/视频/音频分栏与 next_offset 翻页，适合内容日历与选题复盘。

通过本 Skill，你可以：
- 历史发文列表
- 分栏筛选
- offset 游标翻页
- 标题摘要封面时间

适用于：内容运营、编辑、数据产品 等需要稳定、可编排微信公众号数据能力的用户。

技术基础：Python 3 标准库（`urllib` / `json`），调用 `https://yige.zone/v1/wechat_mp/v2/fetch_account_articles`，鉴权使用 Bearer API Key。

## 功能特性

### 核心功能
- **历史发文列表**
- **分栏筛选**
- **offset 游标翻页**
- **标题摘要封面时间**

### 特色亮点
- 单页计费可控
- 翻页游标清晰
- **⏱️ 超时建议 30 秒**：降低已扣费但未收到响应的风险
- **🔗 可编排**：可与 `gzh-article-detail`、`gzh-article-stats` 组成完整工作流

## 一键安装

### 前置条件
- Python 3（推荐 `/usr/bin/python3`）
- 无第三方依赖，仅标准库
- 一格数据 API Key（[获取地址](https://yige.zone/settings/api-keys)）

### 鉴权
本 Skill **需要鉴权**：

```bash
export YIGE_API_KEY=ak_xxx
# 或
python scripts/fetch.py --api-key ak_xxx ...
```

请求头：`Authorization: Bearer <YIGE_API_KEY>`

### 安装方式

```bash
git clone https://github.com/jessdy/yige-skills.git
# 将 skills/gzh-account-articles 放入你的 Agent Skills 目录
```

兼容 Qoder / Codex / Claude Code / OpenClaw 等支持标准 Skill 包的平台。

## 使用指南

### 何时使用
要看某公众号最近发了什么

### 基础使用（3 步）

#### 第1步：准备输入
向 Agent 说明目标，并提供必要 ID / 链接 / 关键词（见参数表）。

#### 第2步：执行脚本

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --username gh_363b924965e9 --page-size 20
```

#### 第3步：解读结果
脚本向 stdout 打印 JSON。Agent 应优先读取业务字段（通常在 `data`），再用清晰中文向用户汇报；需要原文时再展示关键 JSON 片段。

### 脚本命令速查

| 命令 | 说明 |
|------|------|
| `python scripts/fetch.py -h` | 查看全部参数 |
| `python scripts/fetch.py --username gh_363b924965e9 --page-size 20` | 常用示例 |

### 接口说明

| 项目 | 详情 |
|------|------|
| Method | `POST` |
| Path | `/v1/wechat_mp/v2/fetch_account_articles` |
| Host | `https://yige.zone` |
| 鉴权 | `Authorization: Bearer <YIGE_API_KEY>` |
| 超时 | 建议 30s |
| 文档 | https://docs.tikhub.io/472974858e0 |

### 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `username` | 是 | 见 --help |
| `page_size` | 否 | 默认 20 |
| `offset` | 否 | 首页留空；翻页传 next_offset |
| `item_show_type` | 否 | 0文章/5视频/7音频/8贴图 |

### 注意事项
- page_size 范围 10-20
- 首页 offset 留空
- 末页看 is_end
- 按次计费，请关注控制台余额
- 勿把 API Key 写入仓库、截图或前端
- 勿再使用已下线的 `/story/api/...` 路径

## 使用场景

### 场景1：复盘更新节奏
- **角色**：编辑
- **需求**：复盘更新节奏
- **使用方式**：拉近几页列表
- **预期收益**：判断更新频率与栏目

### 场景2：找爆款候选
- **角色**：运营
- **需求**：找爆款候选
- **使用方式**：列表后接 stats
- **预期收益**：定位高阅读文章

### 场景3：建内容库
- **角色**：采集
- **需求**：建内容库
- **使用方式**：循环翻页
- **预期收益**：沉淀标题与链接

### 场景4：自动选题
- **角色**：Agent
- **需求**：自动选题
- **使用方式**：articles→detail
- **预期收益**：生成摘要周报

## 项目架构

### 目录结构
```
gzh-account-articles/
├── SKILL.md           # 本文件（给 Agent 的完整说明书）
├── README.md          # 用户向导读
└── scripts/
    └── fetch.py       # 调用一格数据接口的 CLI
```

### 核心模块

| 模块 | 文件 | 说明 |
|------|------|------|
| 技能说明 | `SKILL.md` | 触发条件、参数、场景与编排建议 |
| 调用脚本 | `scripts/fetch.py` | 标准库 HTTP 客户端，打印 JSON |

### 技术栈

| 技术 | 用途 |
|------|------|
| Python 3 | 运行环境 |
| urllib | HTTP 请求 |
| 一格数据 API | `POST /v1/wechat_mp/v2/fetch_account_articles` |

### 资源索引
- 脚本：`scripts/fetch.py`
- 开放文档：https://docs.tikhub.io/472974858e0
- 控制台密钥：https://yige.zone/settings/api-keys
- 相关 Skill：`gzh-article-detail`、`gzh-article-stats`

## 常见问答

### 安装相关
**Q: 需要 pip 安装依赖吗？**  
A: 不需要，仅用 Python 标准库。

**Q: 没有 API Key 能用吗？**  
A: 不能。请到 https://yige.zone/settings/api-keys 创建。

### 使用相关
**Q: 返回很大怎么办？**  
A: 先向用户摘要关键字段；需要时再保存完整 JSON。

**Q: 和相关 Skill 怎么配合？**  
A: 按「发现 → 详情 → 互动/商业」链路组合，例如搜索后取 ID 再拉详情。

### 故障排除
**Q: HTTP 401/403？**  
A: 检查 Key 是否有效、是否以 Bearer 传递、余额是否充足。

**Q: HTTP 400 或超时？**  
A: 上游偶发不稳定，请重试并确保超时≥30s；仍失败则稍后重试。

### 安全与许可
**Q: Key 能提交到 Git 吗？**  
A: 不可以。只用环境变量或本地私密配置。
