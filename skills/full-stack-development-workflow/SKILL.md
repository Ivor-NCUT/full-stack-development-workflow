---
name: full-stack-development-workflow
description: 公司级全栈开发职能入口。用于需求澄清、产品与架构设计、代码实现、测试、Bug 与性能诊断、代码审查、GitHub Issue/分支/PR/多 Agent 协作，以及 Zeabur 部署和生产验收。一个 Skill 贯穿完整开发任务，按需读取工程原则、GitHub 协作或 Zeabur 交付参考；Skill 自身的创建与迭代仍由 agent-skill-evolution-workflow 主持。
---

# 全栈开发

把开发视为一个连续问题，而不是五个互相抢路由的阶段 Skill。先理解真实目标和代码流，再使用最短可靠路径完成、验证和交付。

## 开始前

1. 读取适用的 `AGENTS.md`、仓库文档、当前分支、工作区改动、Issue 和测试。
2. 区分可从环境发现的事实、需要用户决定的业务选择和需要额外权限的外部动作。
3. 用户已经明确目标、范围或要求直接执行时直接推进，不重复设置确认闸门。
4. 保护用户未提交改动；不把密钥、业务数据、日志和生成物误提交。

## 按需读取

- 写代码、设计模块、调试、测试或审查：读取 [references/engineering-principles.md](references/engineering-principles.md)。
- 开始实现、重构或代码审查：读取 [references/ponytail-integration.md](references/ponytail-integration.md)，按需调用已安装的 Ponytail 能力。
- 创建 Issue、分支、PR、合并或安排多个 Agent：读取 [references/github-collaboration.md](references/github-collaboration.md)。
- 部署、巡检或排查 Zeabur：读取 [references/zeabur-delivery.md](references/zeabur-delivery.md)，再调用对应的已安装 `zeabur-*` Skill。

只读取当前任务需要的参考，不把三份参考机械串成固定流水线。

## 统一执行循环

1. 定义用户可观察的成功结果和当前基线。
2. 找到完整调用链、稳定接口、真实约束和最小改动位置。
3. 需要拆分时按端到端行为建立纵向 Issue；一次只推进一个可验收切片。
4. 优先复用现有代码、标准库、平台能力和已安装依赖，再写最少新代码。
5. 非平凡逻辑留下能捕获真实失败的最小检查；Bug 先建立可变红的反馈环。
6. 完成后分别检查“是否符合需求”和“是否符合工程标准”，同步受影响文档。
7. 涉及远端或生产时使用精确 ID、可恢复备份和回读证据；控制面报错先查状态再重试。

## 边界

- Skill 生命周期任务由 `agent-skill-evolution-workflow` 主持；本入口提供工程实现与验证能力。
- 飞书、Zeabur、GitHub、数据库和邮箱等平台能力继续由专用工具执行，本仓库只提供选择和安全工作流。
- Ponytail 是可选的外部编码能力，不是第二个可发现入口；未安装时仍执行其能力阶梯，不静默安装或信任其 Hook。
- 没有真实需求时不提前制造接口、专家、服务或部署。
- 不可逆操作、资金、真实用户、生产数据和新增权限必须保留明确授权。

交付时留下真实产物、验证命令与结果、Issue/PR/版本状态、回滚点和仍存在的风险。
