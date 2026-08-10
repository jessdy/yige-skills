# 公众号文章列表 / gzh-account-articles

---

## 简介

拉取公众号历史发文单页列表，支持文章/视频/音频分栏与 next_offset 翻页，适合内容日历与选题复盘。

**核心价值**

- **历史发文列表**
- **分栏筛选**
- **offset 游标翻页**
- **标题摘要封面时间**

**适用对象**

- 内容运营
- 编辑
- 数据产品

---

## 功能特性

### 核心功能

- 历史发文列表
- 分栏筛选
- offset 游标翻页
- 标题摘要封面时间

### 特色亮点

- 单页计费可控
- 翻页游标清晰

---

## 使用指南

### 鉴权

```bash
export YIGE_API_KEY=ak_xxx
```

密钥获取：https://yige.zone/settings/api-keys

### 快速开始

```bash
python scripts/fetch.py --username gh_363b924965e9 --page-size 20
```

查看参数：`python scripts/fetch.py -h`

### 接口

- `POST https://yige.zone/v1/wechat_mp/v2/fetch_account_articles`
- 文档：https://docs.tikhub.io/472974858e0

### 常用说法速查

| 意图 | 示例话术 | 效果 |
|------|----------|------|
| 直接取数 | 「用 gzh-account-articles 帮我取数」 | 调用脚本并汇总结果 |
| 串联分析 | 「先搜索再拉详情」 | 自动组合相关 Skill |
| 只要结论 | 「给我结论，不要整段 JSON」 | Agent 摘要关键字段 |

---

## 使用场景

| 场景 | 角色 | 示例问法 | 收益 |
|------|------|----------|------|
| 复盘更新节奏 | 编辑 | 「拉近几页列表」 | 判断更新频率与栏目 |
| 找爆款候选 | 运营 | 「列表后接 stats」 | 定位高阅读文章 |
| 建内容库 | 采集 | 「循环翻页」 | 沉淀标题与链接 |
| 自动选题 | Agent | 「articles→detail」 | 生成摘要周报 |

---

## 相关 Skill

`gzh-article-detail`、`gzh-article-stats`

更多：https://yige.zone/skills
