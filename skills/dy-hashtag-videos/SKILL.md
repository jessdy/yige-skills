---
name: dy-hashtag-videos
description: 拉取话题下作品列表，支持排序与 cursor 翻页。需要一格数据 API Key。触发词：抖音话题作品、dy-hashtag-videos
---

## 简介

抖音话题作品列表 基于[一格数据](https://yige.zone) 开放接口，把抖音公开数据以结构化 JSON 返回，方便 Agent 与业务系统直接消费。

按 ch_id 拉取话题作品列表，适合话题营销素材库与热门挑战分析。

通过本 Skill，你可以：
- **话题作品**
- **排序与翻页**
- **素材库构建**

适用于：内容创作者、品牌运营、MCN、市场研究 等需要稳定、可编排抖音数据能力的用户。

技术基础：Python 3 标准库（`urllib` / `json`），调用 `https://yige.zone/v1/douyin/app/v3/fetch_hashtag_video_list`，鉴权使用 Bearer API Key。

## 功能特性

### 核心功能
- **话题作品**
- **排序与翻页**
- **素材库构建**

### 特色亮点
- 营销活动复盘
- 与统计接口编排
- **⏱️ 超时建议 30 秒**：降低已扣费但未收到响应的风险
- **🔗 可编排**：可与 `dy-hashtag-detail`、`dy-video-stats` 组成完整工作流

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
# 将 skills/dy-hashtag-videos 放入你的 Agent Skills 目录
```

兼容 Qoder / Codex / Claude Code / OpenClaw 等支持标准 Skill 包的平台。

## 使用指南

### 何时使用
按 ch_id 拉取话题作品列表，适合话题营销素材库与热门挑战分析。

### 基础使用（3 步）

#### 第1步：准备输入
向 Agent 说明目标，并提供必要 ID / 链接 / 关键词（见参数表）。

#### 第2步：执行脚本

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --ch-id 123456789 --count 10
```

#### 第3步：解读结果
脚本向 stdout 打印 JSON。Agent 应优先读取业务字段（通常在 `data`），再用清晰中文向用户汇报；需要原文时再展示关键 JSON 片段。

### 脚本命令速查

| 命令 | 说明 |
|------|------|
| `python scripts/fetch.py -h` | 查看全部参数 |
| `python scripts/fetch.py --ch-id 123456789 --count 10` | 常用示例 |

### 接口说明

| 项目 | 详情 |
|------|------|
| Method | `GET` |
| Path | `/v1/douyin/app/v3/fetch_hashtag_video_list` |
| Host | `https://yige.zone` |
| 鉴权 | `Authorization: Bearer <YIGE_API_KEY>` |
| 超时 | 建议 30s |
| 文档 | https://yige.zone/docs |

### 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `ch_id` | 是 | 话题 ID |
| `cursor` | 否 | 翻页游标，默认 0 |
| `sort_type` | 否 | 排序类型，默认 0 |
| `count` | 否 | 数量，默认 10 |

### 注意事项
- 先详情后列表更稳妥
- 可再对作品 ID 拉统计
- 按次计费，请关注控制台余额
- 勿把 API Key 写入仓库、截图或前端
- 勿再使用已下线的 `/story/api/...` 路径
- 用户主键多为 `sec_user_id`；播放量请用 `dy-video-stats`

## 使用场景

### 场景1：选题与爆款拆解
- **角色**：创作者
- **需求**：找热门视频并拆解结构
- **使用方式**：热搜/搜索 → 详情 → 统计 → 评论
- **预期收益**：更快产出跟拍与脚本

### 场景2：品牌舆情与口碑
- **角色**：品牌运营
- **需求**：关键词监测与评论洞察
- **使用方式**：搜索视频 + 评论/回复
- **预期收益**：掌握口碑与风险点

### 场景3：达人盘点与选号
- **角色**：MCN / 商务
- **需求**：找达人、看主页与粉丝
- **使用方式**：搜用户 → 资料 → 主页作品 → 统计
- **预期收益**：内部达人库

### 场景4：Agent 自动报告
- **角色**：Agent / 自动化
- **需求**：定时热点与竞品报告
- **使用方式**：多 Skill 编排
- **预期收益**：减少手工拷贝

## 项目架构

### 目录结构
```
dy-hashtag-videos/
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
| 一格数据 API | `GET /v1/douyin/app/v3/fetch_hashtag_video_list` |

### 资源索引
- 脚本：`scripts/fetch.py`
- 接口文档：https://yige.zone/docs
- 控制台密钥：https://yige.zone/settings/api-keys
- 相关 Skill：`dy-hashtag-detail`、`dy-video-stats`

## 常见问答

### 安装相关
**Q: 需要 pip 安装依赖吗？**  
A: 不需要，仅用 Python 标准库。

**Q: 没有 API Key 能用吗？**  
A: 不能。请到 https://yige.zone/settings/api-keys 创建。

### 使用相关
**Q: 为什么详情里没有播放量？**  
A: 抖音普通作品详情通常不含播放量，请使用 `dy-video-stats`。

**Q: 用户 ID 用哪个？**  
A: 优先 `sec_user_id`（可从搜索用户或作品作者字段取得）。

**Q: 返回很大怎么办？**  
A: 先向用户摘要关键字段；需要时再保存完整 JSON。

### 故障排除
**Q: HTTP 401/403？**  
A: 检查 Key 是否有效、是否以 Bearer 传递、余额是否充足。

**Q: HTTP 400 或超时？**  
A: 上游偶发不稳定，请重试并确保超时≥30s；仍失败则稍后重试。

### 安全与许可
**Q: Key 能提交到 Git 吗？**  
A: 不可以。只用环境变量或本地私密配置。
