# 公众号服务菜单 / gzh-account-services

---

## 简介

查询公众号底部自定义菜单/服务入口结构，未配置则返回空菜单。

**核心价值**

- **自定义菜单结构**
- **服务入口解析**

**适用对象**

- 产品
- 运营
- 体验分析

---

## 功能特性

### 核心功能

- 自定义菜单结构
- 服务入口解析

### 特色亮点

- 一眼看清导流布局

---

## 使用指南

### 鉴权

```bash
export YIGE_API_KEY=ak_xxx
```

密钥获取：https://yige.zone/settings/api-keys

### 快速开始

```bash
python scripts/fetch.py --username gh_363b924965e9
```

查看参数：`python scripts/fetch.py -h`

### 接口

- `POST https://yige.zone/v1/wechat_mp/v2/fetch_account_services`
- 文档：https://docs.tikhub.io/472974859e0

### 常用说法速查

| 意图 | 示例话术 | 效果 |
|------|----------|------|
| 直接取数 | 「用 gzh-account-services 帮我取数」 | 调用脚本并汇总结果 |
| 串联分析 | 「先搜索再拉详情」 | 自动组合相关 Skill |
| 只要结论 | 「给我结论，不要整段 JSON」 | Agent 摘要关键字段 |

---

## 使用场景

| 场景 | 角色 | 示例问法 | 收益 |
|------|------|----------|------|
| 对标菜单设计 | 产品 | 「查竞品菜单」 | 优化自家入口 |
| 检查活动入口 | 运营 | 「确认菜单是否更新」 | 避免过期链接 |
| 梳理用户路径 | 体验 | 「解析菜单树」 | 画用户旅程 |
| 结构化导出 | Agent | 「写入配置表」 | 自动化对账 |

---

## 相关 Skill

`gzh-account-profile`

更多：https://yige.zone/skills
