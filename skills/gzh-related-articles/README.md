# 公众号关联文章 / gzh-related-articles

---

## 简介

拉取文章底部关联/推荐阅读；未开启关联时返回空。

**核心价值**

- **关联文章列表**

**适用对象**

- 内容策略
- SEO/内链分析

---

## 功能特性

### 核心功能

- 关联文章列表

### 特色亮点

- 观察账号内链与选题簇

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

- `POST https://yige.zone/v1/wechat_mp/v2/fetch_related_articles`
- 文档：https://docs.tikhub.io/472974855e0

### 常用说法速查

| 意图 | 示例话术 | 效果 |
|------|----------|------|
| 直接取数 | 「用 gzh-related-articles 帮我取数」 | 调用脚本并汇总结果 |
| 串联分析 | 「先搜索再拉详情」 | 自动组合相关 Skill |
| 只要结论 | 「给我结论，不要整段 JSON」 | Agent 摘要关键字段 |

---

## 使用场景

| 场景 | 角色 | 示例问法 | 收益 |
|------|------|----------|------|
| 分析内容簇 | 策略 | 「related」 | 发现系列选题 |
| 补齐内链 | 运营 | 「对照自己菜单」 | 优化推荐 |
| 扩链爬取 | 采集 | 「related→detail」 | 扩大语料 |
| 相关推荐卡片 | Agent | 「展示给用户」 | 提升完读 |

---

## 相关 Skill

`gzh-article-detail`

更多：https://yige.zone/skills
