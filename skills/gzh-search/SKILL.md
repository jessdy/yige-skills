---
name: gzh-search
description: 通过关键词调用一格数据搜一搜接口，发现公众号账号（gh_username）与文章链接，是后续查资料、拉列表、读正文的入口。 需要一格数据 API Key。触发词：微信搜一搜（公众号/文章）、微信公众号数据、gzh-search
---

## 简介

微信搜一搜（公众号/文章） 基于[一格数据](https://yige.zone) 开放接口，把微信公众号公开数据以结构化 JSON 返回，方便 Agent 与业务系统直接消费。

通过关键词调用一格数据搜一搜接口，发现公众号账号（gh_username）与文章链接，是后续查资料、拉列表、读正文的入口。

通过本 Skill，你可以：
- 关键词综合搜索
- 垂类切换（公众号/文章等）
- 排序与发布时间筛选
- cursor 翻页

适用于：内容运营、舆情监测、行业研究员、Agent 开发者 等需要稳定、可编排微信公众号数据能力的用户。

技术基础：Python 3 标准库（`urllib` / `json`），调用 `https://yige.zone/v1/wechat_search/v2/fetch_search`，鉴权使用 Bearer API Key。

## 功能特性

### 核心功能
- **关键词综合搜索**
- **垂类切换（公众号/文章等）**
- **排序与发布时间筛选**
- **cursor 翻页**

### 特色亮点
- 一次拿到可继续调用的 gh_ 与文章 URL
- 默认 raw=false 精简结构，便于 Agent 消费
- **⏱️ 超时建议 30 秒**：降低已扣费但未收到响应的风险
- **🔗 可编排**：可与 `gzh-account-profile`、`gzh-account-articles`、`gzh-article-detail` 组成完整工作流

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
# 将 skills/gzh-search 放入你的 Agent Skills 目录
```

兼容 Qoder / Codex / Claude Code / OpenClaw 等支持标准 Skill 包的平台。

## 使用指南

### 何时使用
用户只有关键词、不知道 gh_ 或文章链接

### 基础使用（3 步）

#### 第1步：准备输入
向 Agent 说明目标，并提供必要 ID / 链接 / 关键词（见参数表）。

#### 第2步：执行脚本

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --keyword 人民日报 --business-type account
```

#### 第3步：解读结果
脚本向 stdout 打印 JSON。Agent 应优先读取业务字段（通常在 `data`），再用清晰中文向用户汇报；需要原文时再展示关键 JSON 片段。

### 脚本命令速查

| 命令 | 说明 |
|------|------|
| `python scripts/fetch.py -h` | 查看全部参数 |
| `python scripts/fetch.py --keyword 人民日报 --business-type account` | 常用示例 |

### 接口说明

| 项目 | 详情 |
|------|------|
| Method | `POST` |
| Path | `/v1/wechat_search/v2/fetch_search` |
| Host | `https://yige.zone` |
| 鉴权 | `Authorization: Bearer <YIGE_API_KEY>` |
| 超时 | 建议 30s |
| 文档 | https://docs.tikhub.io/472974860e0 |

### 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `keyword` | 是 | 见 --help |
| `business_type` | 否 | all/account/article/…；默认 "account" |
| `sort` | 否 | default/latest/hot；默认 "default" |
| `publish_time` | 否 | all/day/week/half_year；默认 "all" |
| `offset` | 否 | 默认 0 |
| `cursor` | 否 | 翻页游标，首页留空 |

### 注意事项
- 微信搜索本身不分页清晰，多试几次可能结果不同
- 大整数 ID 保持字符串
- 超时建议 30s
- 按次计费，请关注控制台余额
- 勿把 API Key 写入仓库、截图或前端
- 勿再使用已下线的 `/story/api/...` 路径

## 使用场景

### 场景1：找对标公众号
- **角色**：新媒体运营
- **需求**：找对标公众号
- **使用方式**：搜 brand/品类关键词 business_type=account
- **预期收益**：快速得到候选账号列表

### 场景2：找选题参考文
- **角色**：内容策划
- **需求**：找选题参考文
- **使用方式**：搜话题 business_type=article
- **预期收益**：拿到可深入阅读的文章链接

### 场景3：跟踪竞品曝光
- **角色**：竞品监测
- **需求**：跟踪竞品曝光
- **使用方式**：定期搜品牌名+最新排序
- **预期收益**：发现新发文与账号变动

### 场景4：自动补齐账号 ID
- **角色**：Agent 编排
- **需求**：自动补齐账号 ID
- **使用方式**：先 search 再 profile/articles
- **预期收益**：打通完整采集链路

## 项目架构

### 目录结构
```
gzh-search/
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
| 一格数据 API | `POST /v1/wechat_search/v2/fetch_search` |

### 资源索引
- 脚本：`scripts/fetch.py`
- 开放文档：https://docs.tikhub.io/472974860e0
- 控制台密钥：https://yige.zone/settings/api-keys
- 相关 Skill：`gzh-account-profile`、`gzh-account-articles`、`gzh-article-detail`

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
