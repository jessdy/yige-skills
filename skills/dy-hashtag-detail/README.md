# 抖音话题详情 / dy-hashtag-detail

---

## 简介

按话题 ch_id 获取话题详情（名称、参与量等），再可用 dy-hashtag-videos 拉作品。

**核心价值**

- 话题详情
- 活动盘点
- 可接作品列表

**适用对象**

- 内容创作者
- 品牌运营
- MCN
- 市场研究

---

## 功能特性

### 核心功能

- 话题详情
- 活动盘点
- 可接作品列表

### 特色亮点

- 挑战赛/话题营销常用
- 与作品列表编排

---

## 使用指南

### 鉴权

```bash
export YIGE_API_KEY=ak_xxx
```

密钥获取：https://yige.zone/settings/api-keys

### 快速开始

```bash
python scripts/fetch.py --ch-id 123456789
```

查看参数：`python scripts/fetch.py -h`

### 接口

- `GET https://yige.zone/v1/douyin/app/v3/fetch_hashtag_detail`
- 文档：https://yige.zone/docs

### 常用说法速查

| 意图 | 示例话术 | 效果 |
|------|----------|------|
| 直接取数 | 「用 dy-hashtag-detail 帮我取数」 | 调用脚本并汇总结果 |
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

`dy-hashtag-videos`、`dy-search-general`

更多：https://yige.zone/skills
