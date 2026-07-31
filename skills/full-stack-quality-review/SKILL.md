---
name: full-stack-quality-review
description: 审查代码改动的正确性、兼容性、安全性和维护成本。用于代码审查、合并前检查、架构回顾或重构验收；先列会导致错误或回退的具体问题，再检查测试、文档和不必要复杂度。
---

# 代码质量审查

按严重程度输出可操作发现，给出精确文件和行号。重点检查：

- 输入边界、安全和数据丢失风险；
- 公共接口与旧行为兼容；
- 状态来源、重复逻辑和特殊分支；
- 测试是否真正覆盖改动；
- 架构文档是否与代码一致。

没有可操作问题时明确说没有发现，不为凑数量输出风格偏好。
**2. Task-Based** (best for tool collections)
- Works well when the skill offers different operations/capabilities
- Example: PDF skill with "Quick Start" -> "Merge PDFs" -> "Split PDFs" -> "Extract Text"
- Structure: ## Overview -> ## Quick Start -> ## Task Category 1 -> ## Task Category 2...

