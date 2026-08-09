<p align="center">
  <a href="https://yige.zone/?source=github">
    <img src="./logo.png" alt="yige.zone" width="220">
  </a>
</p>

<p align="center">
  <b>yige.zone · Agent Skills</b><br>
  <sub>Reusable Agent skills for inspiration, topic research, copywriting, and data review</sub>
</p>

<p align="center">
  <a href="./README.md">中文</a> ·
  <a href="./README.en.md">English</a> ·
  <a href="https://yige.zone/?source=github">Website</a> ·
  <a href="https://yige.zone/skills?source=github">Skills Marketplace</a> ·
  <a href="https://yige.zone/apis?source=github">API Docs</a>
</p>

---

This repository is maintained by **yige.zone (一格数据)** and hosts Agent Skills centered on `SKILL.md`. They work with tools that support Agent Skills, such as Cursor, Claude Code, and OpenClaw.

## Contents

- [Repository layout](#repository-layout)
- [Skill directory conventions](#skill-directory-conventions)
- [Authentication](#authentication)
- [How to use skills](#how-to-use-skills)
- [Multi-platform APIs](#multi-platform-apis)
- [Contributing](#contributing)

## Repository layout

```text
.
├── README.md          # Chinese README
├── README.en.md       # This file
├── logo.png           # Brand mark
└── skills/            # One skill per subdirectory
    └── <skill-name>/
        ├── SKILL.md
        └── …          # scripts / references / assets (optional)
```

## Skill directory conventions

Each skill lives in its **own subdirectory** and must include at least:

| File | Purpose |
| --- | --- |
| `SKILL.md` | Skill entry: YAML frontmatter + body (triggers, steps, constraints, examples, etc.) |

Use clear frontmatter in `SKILL.md` for discovery and platform import:

```yaml
---
name: Example Skill
description: One sentence on when to use the skill and what it does (be specific).
---
```

Optional folders such as `references/`, `scripts/`, and `assets/` may sit next to `SKILL.md`. Keep each skill self-contained and use relative paths.

## Authentication

All API requests require a valid API Key.

Get one from [Yige Hub](https://yige.zone/settings/api-keys?source=github), then set:

```bash
export YIGE_API_KEY="ak_xxxx..."
```

## How to use skills

### Local / Cursor

Copy the skill folder into your client’s skills directory (e.g. Cursor user skills or project `.cursor/skills/`), or use the client’s “Add skill” flow and point it at that subdirectory.

### Agent install prompt

Tell your agent (OpenClaw / WorkBuddy / Qoder, etc.):

```text
Please help me check and install the following Agent Skill in the current workspace.

Skill: Xiaohongshu Latest Hot Notes / xiaohongshu-realtime-search
Source: https://github.com/jessdy/yige-skills/tree/main/skills/xiaohongshu-realtime-search

Please follow these steps in order:
1. Check whether this Skill is already installed in the project
2. Visit the GitHub URL above, read SKILL.md / README, and confirm installation steps and dependencies
3. If not installed: install the Skill to the appropriate directory for this project (prefer reusing existing skills paths)
4. If already installed: compare with the remote version, update as needed, and explain any changes
5. When done, report: installation path, how to trigger this Skill, and a brief usage example

If network access is limited, try git clone or curl; ask me first if anything is ambiguous or conflicts arise.
```

### skills CLI

```bash
# Install the skills CLI
npx skills init

# Browse the repo and pick a skill
npx skills add jessdy/yige-skills

# Install a specific skill
npx skills add https://github.com/jessdy/yige-skills/tree/main/skills/seedance-video-gen
```

Follow the prompts to install into a specific agent folder or globally.

### SkillHub

Open [SkillHub](https://skillhub.cn/skills) and install by searching for the **Chinese display name** of a skill under `skills/`.

Search examples: `公众号爆款文章查询`, `抖音每日最具影响力账号`

### ClawHub

Browse and install from the official profile: <https://clawhub.ai/user/yige-data>

## Multi-platform APIs

Full docs: [yige.zone/apis](https://yige.zone/apis?source=github)

Docs include request headers, parameters, response shapes, request/response examples, and common status codes.

### Douyin

- [Get content details (Premium)](https://yige.zone/apis/douyin/0OT1E306)
- [Get account info (Premium)](https://yige.zone/apis/douyin/XUT4CECZ)
- [Search accounts by keyword (Premium)](https://yige.zone/apis/douyin/P5CHB3BZ)
- [Search content by keyword (Premium)](https://yige.zone/apis/douyin/774OBKK0)
- [Get account content list (Premium)](https://yige.zone/apis/douyin/QEQLCKD6)
- [Search AI content by keyword (Premium)](https://yige.zone/apis/douyin/I8P3HTVH)

### Xiaohongshu (RED)

- [Get account info (Premium)](https://yige.zone/apis/xiaohongshu/4IVIDHEN)
- [Get content details (Premium)](https://yige.zone/apis/xiaohongshu/KR1LPTBF)
- [Search accounts by keyword (Premium)](https://yige.zone/apis/xiaohongshu/439NFLBD)
- [Search content by keyword (Premium)](https://yige.zone/apis/xiaohongshu/384C6W6B)
- [Search AI content by keyword (Premium)](https://yige.zone/apis/xiaohongshu/047JJ3UA)

### WeChat Official Accounts

- [Get account info (Premium)](https://yige.zone/apis/gongzhonghao/6C4A77XR)
- [Get article by content UUID (Premium)](https://yige.zone/apis/gongzhonghao/XEO0QQNF)
- [Search accounts by keyword (Premium)](https://yige.zone/apis/gongzhonghao/DNVPQZEZ)
- [Search articles by keyword (Premium)](https://yige.zone/apis/gongzhonghao/PW97QFBS)
- [Get account article list (Premium)](https://yige.zone/apis/gongzhonghao/XNV30XZ3)
- [Get article by URL (Premium)](https://yige.zone/apis/gongzhonghao/VUTTKTP6)
- [Search AI-generated articles by keyword (Premium)](https://yige.zone/apis/gongzhonghao/IE0887SO)

### Bilibili

- [Get content details (Premium)](https://yige.zone/apis/bilibili/TIN1NMTZ)
- [Get account info (Premium)](https://yige.zone/apis/bilibili/EH53TOT7)
- [Search accounts by keyword (Premium)](https://yige.zone/apis/bilibili/ZXJLJQ21)
- [Search content by keyword (Premium)](https://yige.zone/apis/bilibili/LEN9QXR3)
- [Get account content list (Premium)](https://yige.zone/apis/bilibili/VPA67I98)

### Toutiao

- [Get account content list (Realtime)](https://yige.zone/apis/jinritoutiao/28CFGF5I)
- [Get content details (Realtime)](https://yige.zone/apis/jinritoutiao/PAB6Z75Y)

### TikTok

- [Search accounts by keyword](https://yige.zone/apis/tool-tiktok/20070019)

### AI search

- [Kimi text search](https://yige.zone/apis/tool-ai-search/USDIOVU23)
- [Doubao text search](https://yige.zone/apis/tool-ai-search/I9R9LIDL)
- [DeepSeek text search](https://yige.zone/apis/tool-ai-search/KGX4SDXQ)

### AI tools

- [GPT image generation](https://yige.zone/apis/tool/HUV4KRFQ)
- [Doubao image generation](https://yige.zone/apis/tool/7OM96HCF)
- [Doubao video generation](https://yige.zone/apis/tool/ER2ATHKI)
- [Upload image](https://yige.zone/apis/tool/FXDGJO1V)
- [Upload video / image / audio](https://yige.zone/apis/tool/6L178PZD)
- [Short video downloader](https://yige.zone/apis/tool/AWUTFI4V)

### More platforms

- [Coming soon](https://yige.zone/apis)

## Contributing

Issues and pull requests are welcome for new skills or fixes.

1. Fork this repository
2. Add or edit a subdirectory under `skills/`
3. Ensure `SKILL.md` stands alone, steps are actionable, and dependencies/risks are documented
4. Open a pull request with a short note on motivation and use cases

---

**yige.zone (一格数据)** — Turn repeatable new-media workflows into shareable, evolvable Agent skills.
