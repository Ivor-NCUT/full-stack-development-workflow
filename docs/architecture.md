# Architecture

`full-stack-development-workflow` 是唯一可发现入口。需求、实现、调试、审查和部署共享同一组工程原则，因此不再作为五个独立 Skill 竞争触发。

主入口只保留任务判断和统一执行循环，细节按需加载三份一层参考：

- `engineering-principles.md`：从需求到代码、调试、测试和审查。
- `github-collaboration.md`：Issue、分支、PR、合并与多 Agent 工作区。
- `zeabur-delivery.md`：Zeabur 工具路由、部署安全与生产验证。

参考文件提供流程和安全边界，不复制连接器实现。GitHub 远端操作使用 `gh` / `gh api`；Zeabur 操作调用已安装的 `zeabur-*` Skills。

Skill 生命周期任务由 `agent-skill-evolution-workflow` 主持。若任务同时涉及 Skill 与代码，本仓库只提供工程实现与验证原则。
