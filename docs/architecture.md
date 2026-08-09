# Architecture

`full-stack-development-workflow` 是唯一可发现入口。需求、实现、调试、审查和部署共享同一组工程原则，因此不再作为五个独立 Skill 竞争触发。

主入口只保留任务判断和统一执行循环，细节按需加载五份一层参考：

- `engineering-principles.md`：从需求到代码、调试、测试和审查。
- `ponytail-integration.md`：实现、重构和审查时的最小正确实现阶梯，以及外部插件的降级与 Hook 信任边界。
- `security-review.md`：Codex Security 插件路由、高风险改动识别和发布门禁。
- `github-collaboration.md`：Issue、分支、PR、合并与多 Agent 工作区。
- `zeabur-delivery.md`：Zeabur 工具路由、部署安全与生产验证。

参考文件提供流程和安全边界，不复制连接器或外部插件实现。Ponytail 保持为可选的外部 Codex 插件：父 Skill 在编码任务中按需使用它，未安装时执行同一能力阶梯；仓库不静默安装插件或信任生命周期 Hook。安全扫描调用已安装的 `codex-security:*` Skills；多阶段人工配置仅在 `wizard` 已安装且确有重复价值时路由。GitHub 远端操作使用 `gh` / `gh api`；Zeabur 操作调用已安装的 `zeabur-*` Skills。

Skill 生命周期任务由 `agent-skill-evolution-workflow` 主持。若任务同时涉及 Skill 与代码，本仓库只提供工程实现与验证原则。
