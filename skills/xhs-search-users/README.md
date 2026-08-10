# 小红书搜索用户 / xhs-search-users

---

## 简介

按关键词搜索小红书用户/博主。

**核心价值**

- **小红书公开数据拉取**
- **标准库脚本开箱即用**
- **可与搜索/详情/评论编排**

**适用对象**

- 内容创作者
- 品牌运营
- MCN
- 市场研究

---

## 功能特性

### 核心功能

- 小红书公开数据拉取
- 标准库脚本开箱即用
- 可与搜索/详情/评论编排

### 特色亮点

- App V2 为推荐数据面
- 无播放量/下载量属平台限制

---

## 使用指南

### 鉴权

```bash
export YIGE_API_KEY=ak_xxx
```

密钥获取：https://yige.zone/settings/api-keys

### 快速开始

```bash
python scripts/fetch.py --keyword 美妆博主
```

查看参数：`python scripts/fetch.py -h`

### 接口

- `GET https://yige.zone/v1/xiaohongshu/app_v2/search_users`
- 文档：https://docs.tikhub.io/420136399e0

### 常用说法速查

| 意图 | 示例话术 | 效果 |
|------|----------|------|
| 直接取数 | 「用 xhs-search-users 帮我取数」 | 调用脚本并汇总结果 |
| 串联分析 | 「先搜索再拉详情」 | 自动组合相关 Skill |
| 只要结论 | 「给我结论，不要整段 JSON」 | Agent 摘要关键字段 |

---

## 使用场景

| 场景 | 角色 | 示例问法 | 收益 |
|------|------|----------|------|
| 选题与拆解 | 创作者 | 「搜索后拉详情」 | 学习爆款结构 |
| 种草与舆情监测 | 品牌 | 「按关键词/笔记取数」 | 掌握口碑与素材 |
| 达人与内容盘点 | MCN | 「用户列表+笔记」 | 内部内容库 |
| 自动分析报告 | Agent | 「多 Skill 组合」 | 减少手工拷贝 |

---

## 相关 Skill

`xhs-search-notes`、`xhs-image-note-detail`、`xhs-note-comments`

更多：https://yige.zone/skills
