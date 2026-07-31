---
name: full-stack-debugging
description: 复现软件故障并在共享根因处修复。用于报错、测试失败、线上异常、性能回退或行为不一致；追踪症状路径和所有相关调用方，以一处根因修复覆盖兄弟路径，并留下回归检查。
---

# 根因调试

1. 收集精确错误、触发条件、影响面和最近变更。
2. 建立最小复现，搜索目标函数及全部调用方。
3. 区分传输噪声、配置错误、状态源冲突和代码缺陷。
4. 在最小共享边界修复，不在每个调用方堆 guard。
5. 运行复现检查和受影响测试；无法复现时明确缺少的证据。

输出根因、修复位置、验证结果和仍存在的风险，不把重启或一次成功响应当作根因修复。

**2. Task-Based** (best for tool collections)
- Works well when the skill offers different operations/capabilities
- Example: PDF skill with "Quick Start" -> "Merge PDFs" -> "Split PDFs" -> "Extract Text"
- Structure: ## Overview -> ## Quick Start -> ## Task Category 1 -> ## Task Category 2...

