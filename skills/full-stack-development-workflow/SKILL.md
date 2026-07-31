---
name: full-stack-development-workflow
description: 公司级全栈开发主路由。用于长程或跨阶段的软件开发、产品实现、Bug 修复、代码审查、重构、部署与上线验收；根据当前状态只选择需求对齐、Issue 实现、根因调试、质量审查或部署验收中的一个专家。用户明确点名其他开发 Skill 时尊重点名，不替代平台工具。
---

# 全栈开发

先读仓库约定、现有 Issue、代码和运行状态，再决定当前唯一阶段。不要复制专家的完整方法，也不要预先制造一条固定流水线。

## 路由

| 当前结果 | 调用 |
|---|---|
| 把模糊需求变成可验收切片 | `full-stack-requirements` |
| 实现已确认 Issue | `full-stack-implementation` |
| 复现故障并修复根因 | `full-stack-debugging` |
| 审查风险、兼容性和坏味道 | `full-stack-quality-review` |
| 发布、迁移或云端回归 | `full-stack-deployment` |

## 边界

- 先读取并遵循 `codex-dev-good-taste`；Ponytail 激活时采用其最小实现阶梯。
- Skill 本身的创建、归类和进化由 `agent-skill-evolution-workflow` 主持，本 Skill 只提供工程实现原则。
- GitHub、Zeabur、飞书等操作继续调用现有专用 Skill，不复制连接器。
- 用户已给出明确范围和执行授权时直接推进；仅在缺少高影响业务选择、权限或不可逆操作前暂停。

每个阶段结束时留下：真实产物、最小检查、Issue/版本状态、阻塞项和下一阶段。前一阶段未通过，不假装进入下一阶段。

