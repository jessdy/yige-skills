# 公众号文章互动数据 / gzh-article-stats

---

## 简介

拉取阅读量、点赞、在看、分享、收藏、评论数等核心互动指标，是公众号最重要的注意力信号。

**核心价值**

- **阅读/点赞/在看/分享/收藏/评论**
- **精简计数模式**

**适用对象**

- 数据分析
- 内容运营
- 投放评估

---

## 功能特性

### 核心功能

- 阅读/点赞/在看/分享/收藏/评论
- 精简计数模式

### 特色亮点

- 阅读量比公开点赞更能反映打开意愿

---

## 使用指南

### 鉴权

```bash
export YIGE_API_KEY=ak_xxx
```

密钥获取：https://yige.zone/settings/api-keys

### 快速开始

```bash
python scripts/fetch.py --url "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"
```

查看参数：`python scripts/fetch.py -h`

### 接口

- `POST https://yige.zone/v1/wechat_mp/v2/fetch_article_stats`
- 文档：https://docs.tikhub.io/472974852e0

### 常用说法速查

| 意图 | 示例话术 | 效果 |
|------|----------|------|
| 直接取数 | 「用 gzh-article-stats 帮我取数」 | 调用脚本并汇总结果 |
| 串联分析 | 「先搜索再拉详情」 | 自动组合相关 Skill |
| 只要结论 | 「给我结论，不要整段 JSON」 | Agent 摘要关键字段 |

---

## 使用场景

| 场景 | 角色 | 示例问法 | 收益 |
|------|------|----------|------|
| 爆款复盘 | 运营 | 「stats 对比多篇」 | 找出高阅读题材 |
| 评估合作效果 | 投放 | 「核对阅读量」 | 结算依据 |
| 注意力分析 | 研究 | 「批量 stats」 | 行业基准 |
| 周报指标 | Agent | 「articles→stats」 | 自动表格 |

---

## 相关 Skill

`gzh-article-detail`、`gzh-account-articles`

更多：https://yige.zone/skills
