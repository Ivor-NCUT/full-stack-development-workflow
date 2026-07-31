---
name: full-stack-requirements
description: 把软件开发需求整理成可独立验收的实现切片。用于新功能、重要交互、架构调整或范围仍模糊的开发任务；先从仓库和现有文档发现事实，再锁定用户目标、接口、边界、测试和不做什么。
---

# 开发需求对齐

1. 读取仓库约定、入口、数据模型、已有 Issue 和测试。
2. 区分可发现事实与业务选择；只询问无法从环境确认且会改变结果的问题。
3. 把需求拆成可独立完成的 Issue，写明使用场景、验收条件、技术边界和不做什么。
4. 无界面任务用架构说明和路由用例对齐，不机械制作 HTML 原型。
5. 用户已明确批准范围时直接建立必要 Issue，不重复设置确认闸门。

输出最小需求单：目标、当前状态、实现切片、公共接口变化、验收、假设。

**2. Task-Based** (best for tool collections)
- Works well when the skill offers different operations/capabilities
- Example: PDF skill with "Quick Start" -> "Merge PDFs" -> "Split PDFs" -> "Extract Text"
- Structure: ## Overview -> ## Quick Start -> ## Task Category 1 -> ## Task Category 2...

