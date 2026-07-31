# GitHub 协作

用于 Issue、分支、提交、PR、合并、冲突和多个 Agent 共同开发。

## 基本纪律

一个任务对应一个 Issue、一个隔离分支或 worktree、一个负责 Agent 和一个 PR。多个 Agent 不在同一工作树的同一分支同时修改；会触碰同一文件的任务按依赖顺序执行。

仓库另有更严格规则时以仓库规则为准。当前环境若禁止 Subagent，则顺序执行，不为了套流程启动 Agent。

## 开始前快照

本地事实使用 `git`：

```bash
git status --short --branch
git remote -v
git branch -vv
git log --oneline --decorate --graph --max-count=12 --all
git diff --stat
git ls-files --others --exclude-standard
```

GitHub 远端事实和变更使用 `gh` / `gh api`：

```bash
gh repo view --json nameWithOwner,defaultBranchRef,url
gh issue list --state open --limit 20
gh pr list --state all --limit 20 --json number,title,state,headRefName,baseRefName,url
```

报告当前分支、远端基线、ahead/behind、未提交文件和活跃 PR。不要用破坏性命令把脏工作区“清干净”。

## Issue

Issue 是任务卡，不是重复抄需求。至少包含：

- 用户可观察目标和使用场景；
- 范围与不做什么；
- 可独立验收的标准；
- 高风险边界、数据和权限；
- 与其他 Issue 的阻塞关系。

切片按端到端行为组织。只有确定需要并行或跨会话时才拆多个 Issue；简单修改保留一个内聚 Issue。

## 分支与 Agent

- 分支命名使用 `codex/<issue-number>-<short-name>` 或仓库既有格式。
- 并行任务使用独立 worktree；禁止两个 Agent 共享未提交文件。
- 一个 Issue 未完成时不顺手扩大到无关功能；新需求先登记。
- 生成物、日志、缓存、`.env`、token、私有数据和本地数据库默认不提交。

## 完成与 PR

提交前检查：

```bash
git status --short
git diff --stat
git diff --name-only
git diff --check
git ls-files --others --exclude-standard
```

运行最窄有意义的测试，再运行受影响的类型检查、构建或完整检查。一个提交保持一个内聚意图。

PR 说明包含：

```markdown
## Summary
- 改了什么
- 为什么

## Verification
- 实际运行的命令和结果

## Notes
- 有意排除的生成物或私有文件
- 风险、回滚和后续项
```

用 `gh pr create` 创建 PR。是否自动合并、需要用户确认或必须等待 CI，服从当前仓库和上级 `AGENTS.md`。

## 审查与合并

- 用 merge-base 固定审查范围，分别检查规格轴和标准轴。
- 一次合并一个 PR；合并后其他重叠分支更新到最新 `main`。
- 不静默 force-push、reset、删除分支或覆盖他人改动。
- 冲突时先读双方 commit、Issue、PR 和测试，理解两个意图；能兼容则保留两者，不能兼容则按当前目标选择并记录取舍，不发明第三种行为。
- 所有冲突解决后运行项目检查，再完成 merge/rebase。
