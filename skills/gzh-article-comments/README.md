# 公众号文章评论 / gzh-article-comments

---

## 简介

拉取文章精选评论（单页），buffer 翻页；可继续用二级回复 Skill 展开楼层。

**核心价值**

- **精选评论列表**
- **buffer 翻页**
- **点赞与精选标记**
- **IP 归属地**

**适用对象**

- 舆情
- 社群运营
- 产品

---

## 功能特性

### 核心功能

- 精选评论列表
- buffer 翻页
- 点赞与精选标记
- IP 归属地

### 特色亮点

- content_id 可喂给 replies

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

- `POST https://yige.zone/v1/wechat_mp/v2/fetch_article_comments`
- 文档：https://docs.tikhub.io/472974853e0

### 常用说法速查

| 意图 | 示例话术 | 效果 |
|------|----------|------|
| 直接取数 | 「用 gzh-article-comments 帮我取数」 | 调用脚本并汇总结果 |
| 串联分析 | 「先搜索再拉详情」 | 自动组合相关 Skill |
| 只要结论 | 「给我结论，不要整段 JSON」 | Agent 摘要关键字段 |

---

## 使用场景

| 场景 | 角色 | 示例问法 | 收益 |
|------|------|----------|------|
| 监测口碑 | 舆情 | 「拉评论」 | 情感分析 |
| 找 UGC 金句 | 运营 | 「筛高赞评论」 | 二次传播 |
| 收集反馈 | 客服 | 「导出留言」 | 问题归类 |
| 评论摘要 | Agent | 「comments→LLM」 | 一句话结论 |

---

## 相关 Skill

`gzh-comment-replies`

更多：https://yige.zone/skills
