# Full Stack Development Workflow

公司级研发 MOE Agent Skill。一个薄路由负责判断当前开发阶段，五个专家分别负责需求对齐、实现、调试、审查和部署验收。

## 安装

```bash
node tools/install.mjs
```

默认安装到 `${CODEX_HOME:-~/.codex}/skills`。已有真实目录不会被删除；只有同源符号链接会被幂等复用。

## 验证

```bash
python3 tools/validate_project.py .
python3 -m unittest discover -s tests -v
```
Company-level MOE Agent Skill for requirements, implementation, debugging, review, and deployment.
