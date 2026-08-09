# Codex Security 路由与交付门禁

安全能力由已安装的官方 `Codex Security` 插件提供。本仓库只决定何时调用，不复制插件实现、扫描提示、脚本或报告格式。

## 何时调用

- 用户要求扫描整个仓库或某个目录：调用 `codex-security:security-scan`。
- 用户要求审查 PR、提交、分支或工作区改动：调用 `codex-security:security-diff-scan`。
- 用户明确要求深度、穷尽或多轮扫描：调用 `codex-security:deep-security-scan`；不要把深扫设为默认交付步骤。
- 用户要求威胁建模、漏洞分诊、修复或加固方案：分别调用 `codex-security:threat-model`、`codex-security:triage-finding`、`codex-security:fix-finding` 或 `codex-security:propose-security-hardening`。
- 开发改动触及认证、授权、租户隔离、密钥、支付、隐私数据、文件上传、路径处理、反序列化、模板执行、SQL、Shell、远程请求或供应链执行时，即使用户没有单独提出安全审查，也在交付前对实际改动调用 `codex-security:security-diff-scan`。

普通文案、样式、测试数据或无安全边界变化的低风险改动不自动扫描。现有工程测试仍然是默认反馈环，安全插件不替代单元测试、类型检查和真实回归。

## 执行边界

1. 只扫描用户拥有或明确授权评估的代码，先解析精确仓库、目录或 Git diff，不擅自扩大范围。
2. 插件在任务启动时加载；若刚完成安装，在新任务中执行首次扫描。
3. 遵循被调用插件 Skill 的预检、证据、覆盖率和报告契约，不手工伪造插件产物。
4. 扫描默认只读。修复代码仍回到本 Skill 的工程循环：建立最小复现、修根因、运行原有测试，再复扫同一范围。
5. 经插件验证为可报告的 Critical 或 High 问题阻断发布和生产部署，直到修复并复扫通过，或用户明确接受风险。Medium 及以下问题随交付报告，不擅自扩大修改范围。
6. 插件不可用或预检未通过时，说明缺失能力和未完成覆盖；不能把普通代码审查冒充 Codex Security 扫描。

交付时给出扫描类型、精确范围、报告路径、覆盖缺口、仍存问题和是否阻断发布。
