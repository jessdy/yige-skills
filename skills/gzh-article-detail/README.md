# 公众号文章详情 / gzh-article-detail

---

## 简介

根据文章 URL 拉取正文、标题、作者、封面、发布时间与合集信息，适合摘要、归档与改写上游。

**核心价值**

- **正文纯文本/HTML 结构**
- **标题作者封面**
- **发布时间**
- **合集信息**

**适用对象**

- 内容创作者
- 归档系统
- AI 应用

---

## 功能特性

### 核心功能

- 正文纯文本/HTML 结构
- 标题作者封面
- 发布时间
- 合集信息

### 特色亮点

- 短链/长链均可
- content_text 便于 LLM

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

- `POST https://yige.zone/v1/wechat_mp/v2/fetch_article_detail`
- 文档：https://docs.tikhub.io/472974851e0

### 常用说法速查

| 意图 | 示例话术 | 效果 |
|------|----------|------|
| 直接取数 | 「用 gzh-article-detail 帮我取数」 | 调用脚本并汇总结果 |
| 串联分析 | 「先搜索再拉详情」 | 自动组合相关 Skill |
| 只要结论 | 「给我结论，不要整段 JSON」 | Agent 摘要关键字段 |

---

## 使用场景

| 场景 | 角色 | 示例问法 | 收益 |
|------|------|----------|------|
| 拆解爆文结构 | 创作者 | 「拉详情」 | 二次创作参考 |
| 入库正文 | 归档 | 「定时抓取」 | 知识库建设 |
| 摘要/翻译 | AI | 「detail→模型」 | 自动日报 |
| 核对发布信息 | 运营 | 「看作者与时间」 | 内容质检 |

---

## 相关 Skill

`gzh-article-stats`、`gzh-article-comments`、`wechat-rewrite`

更多：https://yige.zone/skills
