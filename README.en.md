<p align="center">
  <a href="https://yige.zone/?source=github">
    <img src="https://raw.githubusercontent.com/jessdy/yige-skills/main/logo.png" alt="yige.zone" width="220">
  </a>
</p>

<p align="center">
  <b>yige.zone · Agent Skills</b><br>
  <sub>Reusable Agent skills for inspiration, topic research, copywriting, and data review</sub>
</p>

<p align="center">
  <a href="https://github.com/jessdy/yige-skills/blob/main/README.md">中文</a> ·
  <a href="https://github.com/jessdy/yige-skills/blob/main/README.en.md">English</a> ·
  <a href="https://github.com/jessdy/yige-skills/tree/main/skills">Skills directory</a> ·
  <a href="https://yige.zone/?source=github">Website</a> ·
  <a href="https://yige.zone/skills?source=github">Skills Marketplace</a> ·
  <a href="https://yige.zone/docs?source=github">API Docs</a>
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

Skill: Multi-platform copy rewriting / multi-rewrite
Source: https://github.com/jessdy/yige-skills/tree/main/skills/multi-rewrite

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
npx skills add https://github.com/jessdy/yige-skills/tree/main/skills/multi-rewrite
```

Follow the prompts to install into a specific agent folder or globally.

Browse all skills: <https://github.com/jessdy/yige-skills/tree/main/skills>

### SkillHub

Open [SkillHub](https://skillhub.cn/skills) and install by searching for the **Chinese display name** of a skill under `skills/`.

Search examples: `多平台文案改写`, `公众号文案改写`, `PDF 图文提取`

### ClawHub

Browse and install from the official profile: <https://clawhub.ai/jessdy>

## Multi-platform APIs

Full API reference: [yige.zone/docs](https://yige.zone/docs?source=github)

- **Base URL**: `https://yige.zone` (or `https://www.yige.zone`)
- **Auth**: header `Authorization: Bearer <YIGE_API_KEY>`
- **Path prefix**: `/v1/{platform}/...` (e.g. `/v1/douyin/...`, `/v1/xiaohongshu/...`)

Docs are grouped by platform (Douyin, Xiaohongshu, Bilibili, WeChat MP, TikTok, X, etc.) with parameters, examples, and status codes. Get a key: [Yige Hub](https://yige.zone/settings/api-keys?source=github).

## Contributing

Issues and pull requests are welcome for new skills or fixes.

1. Fork this repository
2. Add or edit a subdirectory under `skills/`
3. Ensure `SKILL.md` stands alone, steps are actionable, and dependencies/risks are documented
4. Open a pull request with a short note on motivation and use cases

---

**yige.zone (一格数据)** — Turn repeatable new-media workflows into shareable, evolvable Agent skills.
