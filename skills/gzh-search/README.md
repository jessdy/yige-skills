# 微信搜一搜（公众号/文章） / gzh-search

---

## 简介

通过关键词调用一格数据搜一搜接口，发现公众号账号（gh_username）与文章链接，是后续查资料、拉列表、读正文的入口。

**核心价值**

- **关键词综合搜索**
- **垂类切换（公众号/文章等）**
- **排序与发布时间筛选**
- **cursor 翻页**

**适用对象**

- 内容运营
- 舆情监测
- 行业研究员
- Agent 开发者

---

## 功能特性

### 核心功能

- 关键词综合搜索
- 垂类切换（公众号/文章等）
- 排序与发布时间筛选
- cursor 翻页

### 特色亮点

- 一次拿到可继续调用的 gh_ 与文章 URL
- 默认 raw=false 精简结构，便于 Agent 消费

---

## 使用指南

### 鉴权

```bash
export YIGE_API_KEY=ak_xxx
```

密钥获取：https://yige.zone/settings/api-keys

### 快速开始

```bash
python scripts/fetch.py --keyword 人民日报 --business-type account
```

查看参数：`python scripts/fetch.py -h`

### 接口

- `POST https://yige.zone/v1/wechat_search/v2/fetch_search`
- 文档：https://docs.tikhub.io/472974860e0

### 常用说法速查

| 意图 | 示例话术 | 效果 |
|------|----------|------|
| 直接取数 | 「用 gzh-search 帮我取数」 | 调用脚本并汇总结果 |
| 串联分析 | 「先搜索再拉详情」 | 自动组合相关 Skill |
| 只要结论 | 「给我结论，不要整段 JSON」 | Agent 摘要关键字段 |

---

## 使用场景

| 场景 | 角色 | 示例问法 | 收益 |
|------|------|----------|------|
| 找对标公众号 | 新媒体运营 | 「搜 brand/品类关键词 business_type=account」 | 快速得到候选账号列表 |
| 找选题参考文 | 内容策划 | 「搜话题 business_type=article」 | 拿到可深入阅读的文章链接 |
| 跟踪竞品曝光 | 竞品监测 | 「定期搜品牌名+最新排序」 | 发现新发文与账号变动 |
| 自动补齐账号 ID | Agent 编排 | 「先 search 再 profile/articles」 | 打通完整采集链路 |

---

## 相关 Skill

`gzh-account-profile`、`gzh-account-articles`、`gzh-article-detail`

更多：https://yige.zone/skills
