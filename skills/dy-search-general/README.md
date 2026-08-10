# 抖音综合搜索 / dy-search-general

---

## 简介

综合搜索（视频/用户等混合结果）。不确定类型时先用本 Skill，再分流到详情接口。

**核心价值**

- 综合搜索
- 多类型结果
- 筛选与翻页

**适用对象**

- 内容创作者
- 品牌运营
- MCN
- 市场研究

---

## 功能特性

### 核心功能

- 综合搜索
- 多类型结果
- 筛选与翻页

### 特色亮点

- 不确定类型时的入口
- 可再细分到视频/用户 Skill

---

## 使用指南

### 鉴权

```bash
export YIGE_API_KEY=ak_xxx
```

密钥获取：https://yige.zone/settings/api-keys

### 快速开始

```bash
python scripts/fetch.py --keyword 人工智能 --sort-type 0
```

查看参数：`python scripts/fetch.py -h`

### 接口

- `POST https://yige.zone/v1/douyin/search/fetch_general_search_v2`
- 文档：https://yige.zone/docs

### 常用说法速查

| 意图 | 示例话术 | 效果 |
|------|----------|------|
| 直接取数 | 「用 dy-search-general 帮我取数」 | 调用脚本并汇总结果 |
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

`dy-search-video`、`dy-search-user`、`dy-search-suggest`

更多：https://yige.zone/skills
