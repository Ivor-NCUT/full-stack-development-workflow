# Zeabur 交付

用于 Zeabur 部署、配置、巡检、排障和生产验收。具体命令和接口调用由已安装的 `zeabur-*` Skill 提供，本参考只负责选择工具和统一安全流程。

## 不变量

- 始终使用 `npx zeabur@latest`，不用其他 Zeabur CLI 安装。
- 先通过只读命令解析项目、服务、环境和部署 ID；后续使用精确 ID，不用名称猜目标。
- 不输出密钥、完整环境变量、数据库密码、私有日志或用户数据。
- 修改前备份配置、文件或数据，并写清回滚目标。
- 控制面超时或 `unexpected EOF` 后先回读状态、文件大小、哈希、部署或服务状态；请求可能已经落地，禁止盲目重复。
- 删除项目、服务、域名记录、数据或服务器，以及租用服务器、购买域名等资金动作，必须再次确认精确目标和影响。

## 工具选择

| 任务 | 调用 |
|---|---|
| 登录与身份 | `zeabur-auth` |
| 创建项目、列服务 | `zeabur-project-create`、`zeabur-service-list` |
| 部署代码、Dockerfile | `zeabur-deploy`、`zeabur-dockerfile` |
| 模板创建、部署、备份、发布 | `zeabur-template`、`zeabur-template-deploy`、`zeabur-template-backup`、`zeabur-template-publish` |
| 环境变量和轻量服务更新 | `zeabur-variables`、`zeabur-update-service` |
| 日志、指标、容器命令、重启 | `zeabur-deployment-logs`、`zeabur-service-metric`、`zeabur-service-exec`、`zeabur-restart` |
| 数据库和对象存储 | `zeabur-database`、`zeabur-object-storage` |
| 域名绑定、DNS、注册 | `zeabur-domain-url`、`zeabur-domain-dns`、`zeabur-domain-register` |
| 迁移、端口、启动顺序 | `zeabur-migration`、`zeabur-port-mismatch`、`zeabur-startup-order` |
| 专用服务器 | `zeabur-server-catalog`、`zeabur-server-list`、`zeabur-server-rent`、`zeabur-server-ssh` |
| AI Hub 与邮件 | `zeabur-ai-hub`、`zeabur-email` |
| 删除服务或项目 | `zeabur-service-delete`、`zeabur-project-delete` |

同时命中多个任务时只先调用解决当前阻塞的 Skill。例如端口错误先用 `zeabur-port-mismatch`，不要先重启；变量配置错误先用 `zeabur-variables`，不要整仓重部署。

## 部署循环

1. 读取仓库部署说明、端口、启动命令、持久化、迁移和必需变量。
2. 运行本地最窄验证，锁定精确提交或制品。
3. 只读列出目标项目、服务、当前部署、域名和依赖。
4. 备份受影响配置或持久化数据，定义回滚版本。
5. 选择最窄动作：变量更新优于重部署，单服务更新优于全项目重建。
6. 部署后检查控制面状态、运行日志、健康端点、进程数、端口、依赖连接和一个关键业务探针。
7. 验证持久化和重启行为；失败时恢复备份并复验。

“命令返回成功”不等于上线成功。必须回读真实运行状态。

## 常见根因优先级

- 代理超时或无法访问：先核对应用监听端口与平台代理端口。
- 服务启动后立即崩溃：检查必需变量、启动命令、依赖就绪和迁移。
- 数据重启后丢失：检查持久卷、数据库或对象存储，不用重启掩盖。
- 数据库 connection refused：检查启动顺序和健康依赖。
- 一直等待 migration：检查是否需要独立 migrator 或迁移锁。
- 重定向、CORS、回调错误：检查公开域名、协议和尾斜杠。
- CPU、内存或延迟异常：先看指标和日志，再决定扩容或修代码。

交付记录至少包含项目/服务 ID、部署版本、备份位置、验证命令与结果、健康状态和回滚方式。
