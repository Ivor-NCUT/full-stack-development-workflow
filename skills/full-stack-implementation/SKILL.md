---
name: full-stack-implementation
description: 按已确认 GitHub Issue 完成最小正确实现。用于目标、边界和验收条件已经明确的代码任务；先读完整调用链，复用现有结构、标准库、平台能力和已安装依赖，再写必要代码与最小回归检查。
---

# 开发实现

1. 确认工作区状态、目标 Issue、贡献规范和受影响调用方。
2. 按 Ponytail 阶梯寻找最短可靠实现；不增加假想抽象。
3. 一次只推进当前 Issue，发现新需求只登记，不顺手扩张。
4. 非平凡逻辑留下一个能失败的最小检查。
5. 同步受影响的架构文档和公共接口说明。
6. 验证通过后更新并关闭 Issue；失败则保留可复现证据。

禁止覆盖用户未提交改动，禁止为通过测试而改变未授权业务行为。

**2. Task-Based** (best for tool collections)
- Works well when the skill offers different operations/capabilities
- Example: PDF skill with "Quick Start" -> "Merge PDFs" -> "Split PDFs" -> "Extract Text"
- Structure: ## Overview -> ## Quick Start -> ## Task Category 1 -> ## Task Category 2...

