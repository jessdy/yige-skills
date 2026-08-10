# 公众号评论二级回复 / gzh-comment-replies

---

## 简介

展开某条一级评论下的二级回复，支持分页或一次拉全。

**核心价值**

- **二级回复列表**
- **all_pages 一次拉全**
- **翻页 offset**

**适用对象**

- 舆情
- 社区运营

---

## 功能特性

### 核心功能

- 二级回复列表
- all_pages 一次拉全
- 翻页 offset

### 特色亮点

- 与 comments 形成完整楼层

---

## 使用指南

### 鉴权

```bash
export YIGE_API_KEY=ak_xxx
```

密钥获取：https://yige.zone/settings/api-keys

### 快速开始

```bash
python scripts/fetch.py --url "https://mp.weixin.qq.com/s/…" --content-id 12109128638545265979
```

查看参数：`python scripts/fetch.py -h`

### 接口

- `POST https://yige.zone/v1/wechat_mp/v2/fetch_comment_replies`
- 文档：https://docs.tikhub.io/472974854e0

### 常用说法速查

| 意图 | 示例话术 | 效果 |
|------|----------|------|
| 直接取数 | 「用 gzh-comment-replies 帮我取数」 | 调用脚本并汇总结果 |
| 串联分析 | 「先搜索再拉详情」 | 自动组合相关 Skill |
| 只要结论 | 「给我结论，不要整段 JSON」 | Agent 摘要关键字段 |

---

## 使用场景

| 场景 | 角色 | 示例问法 | 收益 |
|------|------|----------|------|
| 深挖争议楼层 | 舆情 | 「传 content_id」 | 完整对话链 |
| 官方回复检查 | 运营 | 「看回复内容」 | 质检口径 |
| 互动结构 | 研究 | 「抽样楼层」 | 分析传播 |
| 楼层摘要 | Agent | 「replies→摘要」 | 减少噪声 |

---

## 相关 Skill

`gzh-article-comments`

更多：https://yige.zone/skills
