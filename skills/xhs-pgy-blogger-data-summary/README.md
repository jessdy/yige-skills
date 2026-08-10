# 蒲公英博主数据概览 / xhs-pgy-blogger-data-summary

---

## 简介

账号维度数据概览（报价预估、内容占比、粉丝增长等）。

**核心价值**

- **蒲公英商业数据查询**
- **结构化 JSON 输出**
- **可与选号链路编排**

**适用对象**

- 品牌投放
- MCN
- 选号 BD
- 效果分析

---

## 功能特性

### 核心功能

- 蒲公英商业数据查询
- 结构化 JSON 输出
- 可与选号链路编排

### 特色亮点

- 面向投放前评估的商业数据面
- 与公开内容 Skill 互补

---

## 使用指南

### 鉴权

```bash
export YIGE_API_KEY=ak_xxx
```

密钥获取：https://yige.zone/settings/api-keys

### 快速开始

```bash
python scripts/fetch.py --user-id 5c668b3e0000000012021605
```

查看参数：`python scripts/fetch.py -h`

### 接口

- `POST https://yige.zone/v1/xiaohongshu/pgy/get_blogger_data_summary`
- 文档：https://docs.tikhub.io/479321012e0

### 常用说法速查

| 意图 | 示例话术 | 效果 |
|------|----------|------|
| 直接取数 | 「用 xhs-pgy-blogger-data-summary 帮我取数」 | 调用脚本并汇总结果 |
| 串联分析 | 「先搜索再拉详情」 | 自动组合相关 Skill |
| 只要结论 | 「给我结论，不要整段 JSON」 | Agent 摘要关键字段 |

---

## 使用场景

| 场景 | 角色 | 示例问法 | 收益 |
|------|------|----------|------|
| 投放前评估达人 | 品牌 | 「传入博主 user_id 查询」 | 降低选号风险 |
| 达人盘点评级 | MCN | 「批量拉取核心指标」 | 内部评级体系 |
| 对比报价与表现 | 媒介 | 「结合详情与核心数据」 | 优化预算分配 |
| 生成选号一页纸 | Agent | 「多接口汇总结论」 | 节省人工整理 |

---

## 相关 Skill

`xhs-pgy-blogger-detail`、`xhs-pgy-blogger-core-data`、`xhs-search-users`

更多：https://yige.zone/skills
