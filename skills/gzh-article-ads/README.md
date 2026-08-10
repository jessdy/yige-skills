# 公众号文章广告 / gzh-article-ads

---

## 简介

拉取文中/文末广告位信息；无广告时返回空，适合商业化与竞品广告分析。

**核心价值**

- **广告位解析**

**适用对象**

- 商业化
- 媒介
- 竞品

---

## 功能特性

### 核心功能

- 广告位解析

### 特色亮点

- 识别投放痕迹

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

- `POST https://yige.zone/v1/wechat_mp/v2/fetch_article_ad`
- 文档：https://docs.tikhub.io/472974856e0

### 常用说法速查

| 意图 | 示例话术 | 效果 |
|------|----------|------|
| 直接取数 | 「用 gzh-article-ads 帮我取数」 | 调用脚本并汇总结果 |
| 串联分析 | 「先搜索再拉详情」 | 自动组合相关 Skill |
| 只要结论 | 「给我结论，不要整段 JSON」 | Agent 摘要关键字段 |

---

## 使用场景

| 场景 | 角色 | 示例问法 | 收益 |
|------|------|----------|------|
| 竞品广告盘点 | 媒介 | 「抽查多篇」 | 判断投放节奏 |
| 评估版位 | 商业化 | 「看广告结构」 | 优化接广 |
| 广告形态 | 研究 | 「采样」 | 行业报告 |
| 标记是否接广 | Agent | 「写入元数据」 | 过滤语料 |

---

## 相关 Skill

`gzh-article-detail`

更多：https://yige.zone/skills
