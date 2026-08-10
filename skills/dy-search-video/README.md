# 抖音搜索视频 / dy-search-video

---

## 简介

关键词搜索抖音视频（POST V2）。翻页请透传 cursor、search_id、backtrace。

**核心价值**

- 关键词搜视频
- 多维筛选
- 可编排详情/统计

**适用对象**

- 内容创作者
- 品牌运营
- MCN
- 市场研究

---

## 功能特性

### 核心功能

- 关键词搜视频
- 多维筛选
- 可编排详情/统计

### 特色亮点

- 选题与竞品监测入口
- POST JSON 体

---

## 使用指南

### 鉴权

```bash
export YIGE_API_KEY=ak_xxx
```

密钥获取：https://yige.zone/settings/api-keys

### 快速开始

```bash
python scripts/fetch.py --keyword 猫咪 --sort-type 1
```

查看参数：`python scripts/fetch.py -h`

### 接口

- `POST https://yige.zone/v1/douyin/search/fetch_video_search_v2`
- 文档：https://yige.zone/docs

### 常用说法速查

| 意图 | 示例话术 | 效果 |
|------|----------|------|
| 直接取数 | 「用 dy-search-video 帮我取数」 | 调用脚本并汇总结果 |
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

`dy-search-video`、`dy-video-detail`、`dy-user-profile`、`dy-video-comments`、`dy-search-general`、`dy-search-suggest`

更多：https://yige.zone/skills
