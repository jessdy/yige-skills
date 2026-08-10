<p align="center">
  <a href="https://yige.zone/?source=github">
    <img src="https://raw.githubusercontent.com/jessdy/yige-skills/main/logo.png" alt="一格数据" width="220">
  </a>
</p>

<p align="center">
  <b>一格数据 · Agent Skills</b><br>
  <sub>面向灵感、选题、文案创作与数据复盘的可复用 Agent 技能合集</sub>
</p>

<p align="center">
  <a href="https://github.com/jessdy/yige-skills/blob/main/README.md">中文</a> ·
  <a href="https://github.com/jessdy/yige-skills/blob/main/README.en.md">English</a> ·
  <a href="https://github.com/jessdy/yige-skills/tree/main/skills">Skills 目录</a> ·
  <a href="https://yige.zone/?source=github">官网</a> ·
  <a href="https://yige.zone/skills?source=github">Skills 市场</a> ·
  <a href="https://yige.zone/docs?source=github">API 文档</a>
</p>

---

本仓库由 **一格数据（[yige.zone](https://yige.zone/)）** 维护，收录多枚 Agent Skill。每个技能以 `SKILL.md` 为核心，可与 Cursor、Claude Code、OpenClaw 等支持 Agent Skills 的工具配合使用。

## 目录

- [仓库结构](#仓库结构)
- [技能目录约定](#技能目录约定)
- [身份认证](#身份认证)
- [如何使用 Skill](#如何使用-skill)
- [多平台 API](#多平台-api)
- [参与贡献](#参与贡献)

## 仓库结构

```text
.
├── README.md          # 中文说明
├── README.en.md       # English README
├── logo.png           # 品牌标识
└── skills/            # 技能（每个子目录一枚）
    └── <skill-name>/
        ├── SKILL.md
        └── …          # scripts / references / assets（可选）
```

## 技能目录约定

每个技能是一个**独立子文件夹**，且至少包含：

| 文件 | 说明 |
| --- | --- |
| `SKILL.md` | 技能入口：YAML frontmatter + 正文（触发条件、步骤、约束、示例等） |

建议在 `SKILL.md` 的 frontmatter 中提供清晰元信息，便于检索与导入：

```yaml
---
name: Example Skill
description: 一句话说明技能适用场景与能力边界（建议具体，避免空泛）。
---
```

可选目录：`references/`、`scripts/`、`assets/`，与 `SKILL.md` 同级存放，保持单技能自包含、使用相对路径引用。

## 身份认证

所有 API 请求都需要有效的 API Key。

请前往 [一格数据 Hub](https://yige.zone/settings/api-keys?source=github) 获取，并配置环境变量：

```bash
export YIGE_API_KEY="ak_xxxx..."
```

## 如何使用 Skill

### 本地 / Cursor

将需要的技能目录复制到所用工具的 skills 目录（如 Cursor 的 user skills，或项目内 `.cursor/skills/`），或通过客户端「添加技能」入口指向该子文件夹。

### Agent 安装提示词

直接告诉智能体（OpenClaw / WorkBuddy / Qoder 等）：

```text
请帮我在当前工作区检查并安装以下 Agent Skill。

Skill：多平台文案改写 / multi-rewrite
源码地址：https://github.com/jessdy/yige-skills/tree/main/skills/multi-rewrite

请按顺序执行：
1. 检查本项目是否已安装该 Skill
2. 访问上述 GitHub 地址，阅读 SKILL.md / README，确认安装步骤与依赖
3. 若未安装：将 Skill 安装到本项目适用的目录（优先沿用已有 skills 路径）
4. 若已安装：对比远程内容，按需更新并说明变更
5. 完成后告知：安装路径、如何触发该 Skill、简短使用示例

网络受限时可尝试 git clone 或 curl；有歧义或冲突时先询问我。
```

### skills CLI

```bash
# 安装 skills CLI
npx skills init

# 浏览仓库并选择安装
npx skills add jessdy/yige-skills

# 安装指定技能
npx skills add https://github.com/jessdy/yige-skills/tree/main/skills/multi-rewrite
```

按提示安装到指定 Agent 目录，或安装为全局技能。

更多技能见仓库目录：<https://github.com/jessdy/yige-skills/tree/main/skills>

### SkillHub

访问 [SkillHub](https://skillhub.cn/skills)，搜索 `skills/` 目录中对应技能的中文名安装。

搜索示例：`多平台文案改写`、`公众号文案改写`、`PDF 图文提取`

### ClawHub

访问官方主页安装：<https://clawhub.ai/jessdy>

## 多平台 API

完整接口文档见：[yige.zone/docs](https://yige.zone/docs?source=github)

- **Base URL**：`https://yige.zone`（或 `https://www.yige.zone`）
- **鉴权**：请求头 `Authorization: Bearer <YIGE_API_KEY>`
- **路径前缀**：`/v1/{platform}/...`（如 `/v1/douyin/...`、`/v1/xiaohongshu/...`）

文档内按平台分组（抖音 / 小红书 / Bilibili / 公众号 / TikTok / X 等），含请求参数、示例与状态码说明。获取密钥：[一格数据 Hub](https://yige.zone/settings/api-keys?source=github)。

## 参与贡献

欢迎通过 Issue / Pull Request 贡献新技能或修正现有技能。

1. Fork 本仓库
2. 在 `skills/` 下新增或修改对应子目录
3. 确保 `SKILL.md` 可独立理解、步骤可执行、依赖与风险有说明
4. 发起 Pull Request，并在描述中简要说明变更动机与适用场景

---

**一格数据（yige.zone）** — 将可重复的新媒体工作流沉淀为可分享、可演进的 Agent 技能。
