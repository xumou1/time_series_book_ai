# Skills 跨工具调用指南（Codex / Claude Code / 其他 agent）

> 我们的两个科研 skill（`ts-research-application`、`ts-research-method`）是**自包含的 Markdown playbook**，带标准 YAML frontmatter（`name` + `description`），不依赖任何专有 API——**任何能读取指令文件的 agent 工具都可以调用**。本指南覆盖主流工具。

## Skill 文件位置

| 位置 | 用途 |
|---|---|
| `C:\Users\jshmx\AppData\Roaming\reasonix\skills\<name>\SKILL.md` | Reasonix 原生（`run_skill` 或 `/名`） |
| `C:\Users\jshmx\.claude\skills\<name>\SKILL.md` | Claude Code 原生（已复制好） |
| 工作区 `literature/` | 配套资源：文献清单、文献索引.md、KNOWLEDGE-*.md（所有工具共享） |

## ① Claude Code（已配置，最简单）

Skill 已复制到 `~/.claude/skills/`，**直接可用**：

- **自动触发**：Claude Code 根据 description 自动匹配合适 skill；
- **手动调用**：对话中直接说"用 ts-research-application 开始这个课题"，或 `/ts-research-application`（若 CLI 支持斜杠）；
- **传参**：在对话里说明覆盖项，如"root 用 D:\research\loadforecast，focus 能源"。

## ② Codex（OpenAI CLI）

三种方式任选：

- **方案 A（推荐）· 项目级 AGENTS.md**：在项目根建 `AGENTS.md`，写入：
  ```markdown
  # 时间序列科研任务
  如需进行时间序列应用/方法改进研究，请先读取并严格遵循：
  - C:\Users\jshmx\AppData\Roaming\reasonix\skills\ts-research-application\SKILL.md
  - C:\Users\jshmx\AppData\Roaming\reasonix\skills\ts-research-method\SKILL.md
  配套资源：E:\Dropbox\TimeSeries\literature\（文献清单、文献索引.md、KNOWLEDGE-*.md）
  ```
- **方案 B · 启动参数**：`codex --instructions "读取 <SKILL.md路径> 并按其执行"`；
- **方案 C · 对话内**：第一句"读取 <SKILL.md路径> 并严格遵循"。

## ③ Cline / Cursor / 其他 CLI agent（含 cowork 类工具）

通用三步（不依赖工具专有格式）：
1. 把 `SKILL.md` 复制到项目目录 `skills/<name>/SKILL.md`（或直接引用原路径）；
2. 在工具的指令文件（`CLAUDE.md` / `AGENTS.md` / `.cursorrules` / rules 文件）中写入与 Codex 方案 A 相同的引用段落；
3. 对话中显式要求："读取 skills/ts-research-*.md 并严格遵循"。

## ④ 通用兜底（任何 agent，什么都不配也能用）

对话第一句直接给路径：

> 读取 E:\Dropbox\TimeSeries\literature\README.md 与 C:\Users\jshmx\AppData\Roaming\reasonix\skills\ts-research-application\SKILL.md，按 skill 流程开始（参数：root=...、focus=...）。

## 参数（两个 skill 通用）

| 参数 | 默认 | 说明 |
|---|---|---|
| `root` | `<工作区>/research/应用或方法-<日期>` | 研究项目根目录（progress.md 所在） |
| `literature_dir` | `<工作区>/literature` | 文献区（清单/索引/先验） |
| `knowledge_dir` | `<root>/knowledge` | 知识沉淀（按条） |
| `focus` | 无 | 应用：领域；方法：12 热点之一 |

## 注意事项

1. **配套资源必须可访问**：skill 依赖 `literature/`（文献清单、文献索引.md、KNOWLEDGE-*.md），agent 需要有该路径的读写权限；
2. **同步更新**：skill 每次升级后，需重新复制到各工具目录（Reasonix 的 `install_skill` 只更新 Reasonix 目录）；
3. **路径写法**：Windows 下不同工具对 `C:\` 与 `C:/`、中文路径的兼容性不同，若引用失败改用相对路径或正斜杠。
