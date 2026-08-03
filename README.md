# Full Stack Development Workflow

公司级研发职能 Agent Skill。一个深入口贯穿需求、设计、实现、调试、审查、GitHub 协作和 Zeabur 交付；通用原则按需加载，不再拆成五个抢路由的阶段 Skill。

## 结构

- `skills/full-stack-development-workflow`：唯一可发现入口。
- `skills/full-stack-development-workflow/references/engineering-principles.md`：工程、架构、测试、调试和审查。
- `skills/full-stack-development-workflow/references/ponytail-integration.md`：Ponytail 的按需编码决策、降级与 Hook 审阅边界。
- `skills/full-stack-development-workflow/references/github-collaboration.md`：Issue、分支、PR 与多 Agent 协作。
- `skills/full-stack-development-workflow/references/zeabur-delivery.md`：Zeabur 工具选择、部署和生产验收。

Zeabur 的具体操作仍调用已安装的 `zeabur-*` Skill，本仓库不复制平台连接器。

## 可选的 Ponytail 编码能力

全栈入口会在实现、重构和代码审查中按需应用 Ponytail 的能力阶梯：不做、复用现有、标准库、原生平台、已装依赖、一行、最小实现。它不会跳过安全、数据保护、错误处理、可访问性或验证，也不会在只读、规划或平台操作中抢路由。

Ponytail 是外部 Codex 插件，不随本仓库安装器静默安装或复制。需要插件级自动激活时，按其官方说明安装：

```bash
codex plugin marketplace add DietrichGebert/ponytail
codex plugin add ponytail@ponytail
```

随后在 Codex 的 `/hooks` 中审阅并信任其两个生命周期 Hook。没有该插件时，本 Skill 仍执行相同的最小正确实现阶梯。

## 安装

```bash
node tools/install.mjs
```

默认安装到 `${CODEX_HOME:-~/.codex}/skills`。安装器会移除本仓库早期五个阶段 Skill 的同源符号链接；其他链接和真实目录不会被删除。

## 验证

```bash
python3 tools/validate_project.py .
python3 -m unittest discover -s tests -v
```
核心内容来自用户授权的 `codex-dev-good-taste`、`multi-agent-github-workflow`、已安装 Zeabur Skills，并吸收 `mattpocock/skills` 与 [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) 中 MIT 许可的工程思想；完整来源见 `knowledge/sources.jsonl`。
