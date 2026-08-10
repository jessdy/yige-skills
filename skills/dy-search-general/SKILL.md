---
name: dy-search-general
description: 抖音综合搜索 V2，返回视频/用户等多类型结果，支持筛选与翻页透传。需要一格数据 API Key。触发词：抖音综合搜索、dy-search-general
---

## 简介

抖音综合搜索 基于[一格数据](https://yige.zone) 开放接口，把抖音公开数据以结构化 JSON 返回，方便 Agent 与业务系统直接消费。

综合搜索（视频/用户等混合结果）。不确定类型时先用本 Skill，再分流到详情接口。

通过本 Skill，你可以：
- **综合搜索**
- **多类型结果**
- **筛选与翻页**

适用于：内容创作者、品牌运营、MCN、市场研究 等需要稳定、可编排抖音数据能力的用户。

技术基础：Python 3 标准库（`urllib` / `json`），调用 `https://yige.zone/v1/douyin/search/fetch_general_search_v2`，鉴权使用 Bearer API Key。

## 功能特性

### 核心功能
- **综合搜索**
- **多类型结果**
- **筛选与翻页**

### 特色亮点
- 不确定类型时的入口
- 可再细分到视频/用户 Skill
- **⏱️ 超时建议 30 秒**：降低已扣费但未收到响应的风险
- **🔗 可编排**：可与 `dy-search-video`、`dy-search-user`、`dy-search-suggest` 组成完整工作流

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
# 将 skills/dy-search-general 放入你的 Agent Skills 目录
```

兼容 Qoder / Codex / Claude Code / OpenClaw 等支持标准 Skill 包的平台。

## 使用指南

### 何时使用
综合搜索（视频/用户等混合结果）。不确定类型时先用本 Skill，再分流到详情接口。

### 基础使用（3 步）

#### 第1步：准备输入
向 Agent 说明目标，并提供必要 ID / 链接 / 关键词（见参数表）。

#### 第2步：执行脚本

```bash
export YIGE_API_KEY=ak_xxx
python scripts/fetch.py --keyword 人工智能 --sort-type 0
```

#### 第3步：解读结果
脚本向 stdout 打印 JSON。Agent 应优先读取业务字段（通常在 `data`），再用清晰中文向用户汇报；需要原文时再展示关键 JSON 片段。

### 脚本命令速查

| 命令 | 说明 |
|------|------|
| `python scripts/fetch.py -h` | 查看全部参数 |
| `python scripts/fetch.py --keyword 人工智能 --sort-type 0` | 常用示例 |

### 接口说明

| 项目 | 详情 |
|------|------|
| Method | `POST` |
| Path | `/v1/douyin/search/fetch_general_search_v2` |
| Host | `https://yige.zone` |
| 鉴权 | `Authorization: Bearer <YIGE_API_KEY>` |
| 超时 | 建议 30s |
| 文档 | https://yige.zone/docs |

### 参数

| 参数 | 必填 | 说明 |
|------|------|------|
| `keyword` | 是 | 搜索关键词 |
| `cursor` | 否 | 翻页游标，默认 0 |
| `sort_type` | 否 | 0综合 1最多点赞 2最新 |
| `publish_time` | 否 | 发布时间筛选 |
| `filter_duration` | 否 | 时长过滤 |
| `content_type` | 否 | 内容类型 |
| `search_id` | 否 | 翻页透传 |
| `backtrace` | 否 | 翻页透传 |

### 注意事项
- 结果类型混合，Agent 需按字段分流
- 专搜视频用 dy-search-video 更稳
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
dy-search-general/
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
| 一格数据 API | `POST /v1/douyin/search/fetch_general_search_v2` |

### 资源索引
- 脚本：`scripts/fetch.py`
- 接口文档：https://yige.zone/docs
- 控制台密钥：https://yige.zone/settings/api-keys
- 相关 Skill：`dy-search-video`、`dy-search-user`、`dy-search-suggest`

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
