---
name: gzh-article-stats
description: 拉取阅读量、点赞、在看、分享、收藏、评论数等核心互动指标，是公众号最重要的注意力信号。 需要一格数据 API Key。触发词：公众号文章互动数据、微信公众号数据、gzh-article-stats
---

## 简介

公众号文章互动数据 基于[一格数据](https://yige.zone) 开放接口，把微信公众号公开数据以结构化 JSON 返回，方便 Agent 与业务系统直接消费。

拉取阅读量、点赞、在看、分享、收藏、评论数等核心互动指标，是公众号最重要的注意力信号。

通过本 Skill，你可以：
- 阅读/点赞/在看/分享/收藏/评论
- 精简计数模式

适用于：数据分析、内容运营、投放评估 等需要稳定、可编排微信公众号数据能力的用户。

技术基础：Python 3 标准库（`urllib` / `json`），调用 `https://yige.zone/v1/wechat_mp/v2/fetch_article_stats`，鉴权使用 Bearer API Key。

## 功能特性

### 核心功能
- **阅读/点赞/在看/分享/收藏/评论**
- **精简计数模式**

### 特色亮点
- 阅读量比公开点赞更能反映打开意愿
- **⏱️ 超时建议 30 秒**：降低已扣费但未收到响应的风险
- **🔗 可编排**：可与 `gzh-article-detail`、`gzh-account-articles` 组成完整工作流

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
# 将 skills/gzh-article-stats 放入你的 Agent Skills 目录
```

兼容 Qoder / Codex / Claude Code / OpenClaw 等支持标准 Skill 包的平台。

## 使用指南

### 何时使用
要评估某篇文章表现

### 基础使用（3 步）

#### 第1步：准备输入
向 Agent 说明目标，并提供必要 ID / 链接 / 关键词（见参数表）。

#### 第2步：执行脚本

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --url "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"
```

#### 第3步：解读结果
脚本向 stdout 打印 JSON。Agent 应优先读取业务字段（通常在 `data`），再用清晰中文向用户汇报；需要原文时再展示关键 JSON 片段。

### 脚本命令速查

| 命令 | 说明 |
|------|------|
| `python scripts/fetch.py -h` | 查看全部参数 |
| `python scripts/fetch.py --url "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"` | 常用示例 |

### 接口说明

| 项目 | 详情 |
|------|------|
| Method | `POST` |
| Path | `/v1/wechat_mp/v2/fetch_article_stats` |
| Host | `https://yige.zone` |
| 鉴权 | `Authorization: Bearer <YIGE_API_KEY>` |
| 超时 | 建议 30s |
| 文档 | https://docs.tikhub.io/472974852e0 |

### 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `url` | 是 | 见 --help |

### 注意事项
- 部分账号可能隐藏部分指标
- 按次计费，请关注控制台余额
- 勿把 API Key 写入仓库、截图或前端
- 勿再使用已下线的 `/story/api/...` 路径

## 使用场景

### 场景1：爆款复盘
- **角色**：运营
- **需求**：爆款复盘
- **使用方式**：stats 对比多篇
- **预期收益**：找出高阅读题材

### 场景2：评估合作效果
- **角色**：投放
- **需求**：评估合作效果
- **使用方式**：核对阅读量
- **预期收益**：结算依据

### 场景3：注意力分析
- **角色**：研究
- **需求**：注意力分析
- **使用方式**：批量 stats
- **预期收益**：行业基准

### 场景4：周报指标
- **角色**：Agent
- **需求**：周报指标
- **使用方式**：articles→stats
- **预期收益**：自动表格

## 项目架构

### 目录结构
```
gzh-article-stats/
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
| 一格数据 API | `POST /v1/wechat_mp/v2/fetch_article_stats` |

### 资源索引
- 脚本：`scripts/fetch.py`
- 开放文档：https://docs.tikhub.io/472974852e0
- 控制台密钥：https://yige.zone/settings/api-keys
- 相关 Skill：`gzh-article-detail`、`gzh-account-articles`

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
