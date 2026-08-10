---
name: xhs-user-notes
description: 拉取用户已发布笔记列表，支持 cursor 翻页。 需要一格数据 API Key。触发词：小红书用户笔记列表、小红书数据、xhs-user-notes
---

## 简介

小红书用户笔记列表 基于[一格数据](https://yige.zone) 开放接口，把小红书公开数据以结构化 JSON 返回，方便 Agent 与业务系统直接消费。

拉取用户已发布笔记列表，支持 cursor 翻页。

通过本 Skill，你可以：
- 小红书公开数据拉取
- 标准库脚本开箱即用
- 可与搜索/详情/评论编排

适用于：内容创作者、品牌运营、MCN、市场研究 等需要稳定、可编排小红书数据能力的用户。

技术基础：Python 3 标准库（`urllib` / `json`），调用 `https://yige.zone/v1/xiaohongshu/app_v2/get_user_posted_notes`，鉴权使用 Bearer API Key。

## 功能特性

### 核心功能
- **小红书公开数据拉取**
- **标准库脚本开箱即用**
- **可与搜索/详情/评论编排**

### 特色亮点
- App V2 为推荐数据面
- 无播放量/下载量属平台限制
- **⏱️ 超时建议 30 秒**：降低已扣费但未收到响应的风险
- **🔗 可编排**：可与 `xhs-search-notes`、`xhs-image-note-detail`、`xhs-note-comments` 组成完整工作流

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
# 将 skills/xhs-user-notes 放入你的 Agent Skills 目录
```

兼容 Qoder / Codex / Claude Code / OpenClaw 等支持标准 Skill 包的平台。

## 使用指南

### 何时使用
拉取用户已发布笔记列表，支持 cursor 翻页。

### 基础使用（3 步）

#### 第1步：准备输入
向 Agent 说明目标，并提供必要 ID / 链接 / 关键词（见参数表）。

#### 第2步：执行脚本

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --user-id 61b46d790000000010008153
```

#### 第3步：解读结果
脚本向 stdout 打印 JSON。Agent 应优先读取业务字段（通常在 `data`），再用清晰中文向用户汇报；需要原文时再展示关键 JSON 片段。

### 脚本命令速查

| 命令 | 说明 |
|------|------|
| `python scripts/fetch.py -h` | 查看全部参数 |
| `python scripts/fetch.py --user-id 61b46d790000000010008153` | 常用示例 |

### 接口说明

| 项目 | 详情 |
|------|------|
| Method | `GET` |
| Path | `/v1/xiaohongshu/app_v2/get_user_posted_notes` |
| Host | `https://yige.zone` |
| 鉴权 | `Authorization: Bearer <YIGE_API_KEY>` |
| 超时 | 建议 30s |
| 文档 | https://docs.tikhub.io/420136396e0 |

### 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `user_id` | 否 | 见 --help |
| `share_text` | 否 | 见 --help |
| `cursor` | 否 | 见 --help |

### 注意事项
- 偶发 400 可重试
- 翻页参数需按文档透传
- 优先 App V2 接口
- 按次计费，请关注控制台余额
- 勿把 API Key 写入仓库、截图或前端
- 勿再使用已下线的 `/story/api/...` 路径

## 使用场景

### 场景1：选题与拆解
- **角色**：创作者
- **需求**：选题与拆解
- **使用方式**：搜索后拉详情
- **预期收益**：学习爆款结构

### 场景2：种草与舆情监测
- **角色**：品牌
- **需求**：种草与舆情监测
- **使用方式**：按关键词/笔记取数
- **预期收益**：掌握口碑与素材

### 场景3：达人与内容盘点
- **角色**：MCN
- **需求**：达人与内容盘点
- **使用方式**：用户列表+笔记
- **预期收益**：内部内容库

### 场景4：自动分析报告
- **角色**：Agent
- **需求**：自动分析报告
- **使用方式**：多 Skill 组合
- **预期收益**：减少手工拷贝

## 项目架构

### 目录结构
```
xhs-user-notes/
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
| 一格数据 API | `GET /v1/xiaohongshu/app_v2/get_user_posted_notes` |

### 资源索引
- 脚本：`scripts/fetch.py`
- 开放文档：https://docs.tikhub.io/420136396e0
- 控制台密钥：https://yige.zone/settings/api-keys
- 相关 Skill：`xhs-search-notes`、`xhs-image-note-detail`、`xhs-note-comments`

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
