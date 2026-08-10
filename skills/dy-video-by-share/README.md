# 抖音分享链接解析作品 / dy-video-by-share

---

## 简介

粘贴抖音分享文案或链接，解析出作品详情；适合用户只给链接、没有 aweme_id 的场景。

**核心价值**

- 分享链接一键解析
- 无需事先知道 aweme_id
- 可接评论/统计链路

**适用对象**

- 内容创作者
- 品牌运营
- MCN
- 市场研究

---

## 功能特性

### 核心功能

- 分享链接一键解析
- 无需事先知道 aweme_id
- 可接评论/统计链路

### 特色亮点

- 适合聊天场景直接贴链
- 播放量仍建议用 dy-video-stats

---

## 使用指南

### 鉴权

```bash
export YIGE_API_KEY=ak_xxx
```

密钥获取：https://yige.zone/settings/api-keys

### 快速开始

```bash
python scripts/fetch.py --share-url "https://v.douyin.com/xxxxx/"
```

查看参数：`python scripts/fetch.py -h`

### 接口

- `GET https://yige.zone/v1/douyin/app/v3/fetch_one_video_by_share_url`
- 文档：https://yige.zone/docs

### 常用说法速查

| 意图 | 示例话术 | 效果 |
|------|----------|------|
| 直接取数 | 「用 dy-video-by-share 帮我取数」 | 调用脚本并汇总结果 |
| 串联分析 | 「先搜索再拉详情和播放量」 | 自动组合相关 Skill |
| 只要结论 | 「给我结论，不要整段 JSON」 | Agent 摘要关键字段 |

---

## 使用场景

| 场景 | 角色 | 示例问法 | 收益 |
|------|------|----------|------|
| 选题与拆解 | 创作者 | 「搜关键词并拆爆款」 | 学习爆款结构 |
| 舆情监测 | 品牌 | 「拉评论看看口碑」 | 掌握风险与金句 |
| 达人盘点 | MCN | 「搜用户再拉主页作品」 | 内部达人库 |
| 自动报告 | Agent | 「多 Skill 组合出日报」 | 减少手工拷贝 |

---

## 相关 Skill

`dy-video-detail`、`dy-video-stats`、`dy-video-comments`

更多：https://yige.zone/skills
