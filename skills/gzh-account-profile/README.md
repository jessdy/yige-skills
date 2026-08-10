# 公众号资料查询 / gzh-account-profile

---

## 简介

根据 gh_username 拉取公众号资料页：昵称、简介、头像、服务类型等，适合账号建档与对标分析。

**核心价值**

- **资料页基础信息**
- **昵称/简介/头像**
- **服务类型与状态**

**适用对象**

- 账号运营
- BD 选号
- 数据分析

---

## 功能特性

### 核心功能

- 资料页基础信息
- 昵称/简介/头像
- 服务类型与状态

### 特色亮点

- 输入只需 gh_…
- 可与搜一搜串联

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

- `POST https://yige.zone/v1/wechat_mp/v2/fetch_account_profile`
- 文档：https://docs.tikhub.io/472974857e0

### 常用说法速查

| 意图 | 示例话术 | 效果 |
|------|----------|------|
| 直接取数 | 「用 gzh-account-profile 帮我取数」 | 调用脚本并汇总结果 |
| 串联分析 | 「先搜索再拉详情」 | 自动组合相关 Skill |
| 只要结论 | 「给我结论，不要整段 JSON」 | Agent 摘要关键字段 |

---

## 使用场景

| 场景 | 角色 | 示例问法 | 收益 |
|------|------|----------|------|
| 建档对标账号 | 运营 | 「传入 gh_」 | 得到标准资料字段 |
| 核实账号真实性 | BD | 「查资料与封禁状态」 | 降低合作踩坑 |
| 补全展示信息 | Agent | 「search→profile」 | 列表页展示更完整 |
| 批量画像 | 研究 | 「循环多个 gh_」 | 构建账号库 |

---

## 相关 Skill

`gzh-search`、`gzh-account-articles`、`gzh-account-services`

更多：https://yige.zone/skills
