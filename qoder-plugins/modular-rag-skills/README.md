# Modular RAG 项目工作流技能包 (modular-rag-skills)

Qoder 原生插件，打包了 **MODULAR-RAG-MCP-SERVER** 项目的 9 个 Agent Skill，覆盖从开发、测试、配置、打包到简历与面试准备的完整生命周期。

## 包含的 Skills

| Skill               | 触发方式                                    | 作用                                                                                                    |
| ------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **auto-coder**      | `auto code` / `自动开发` / `autopilot`      | Spec 驱动自动编码：读 DEV_SPEC → 定位下一个待办任务 → 写代码 → 跑测试（最多 3 轮自动修复）→ 原子 commit |
| **qa-tester**       | `跑测试` / `QA test` / `test and fix`       | 全自动 QA：CLI / Dashboard（Streamlit AppTest）/ MCP 协议 JSON-RPC 测试，自动诊断修复并记录进度         |
| **setup**           | `setup` / `环境配置` / `初始化`             | 交互式配置向导：选 Provider → 配 API Key → 装依赖 → 生成配置 → 启动 Dashboard，失败自动修 3 轮          |
| **package**         | `package` / `打包` / `清理项目`             | 清理缓存、虚拟环境、密钥等，产出最小可分发的干净代码包                                                  |
| **resume-writer**   | `写简历` / `resume`                         | 按"写作原则 + 项目亮点 + 用户画像"三角模型生成定制化简历项目经历                                        |
| **interview-prep**  | `模拟面试` / `考我`                         | 模拟技术面试官：最多 3 轮深度追问，生成含参考答案与评分的面试报告                                       |
| **project-learner** | `学习项目` / `检验项目` / `knowledge check` | 面试教练式问答学习：10 大知识域 × 45 个知识点，动态出题、评分、持久化进度                               |
| **project-review**  | `复习项目` / `复盘`                         | 老师式章节复习：逐题互动问答 + 参考答案，记录并回顾掌握进度                                             |
| **skill-creator**   | `create skill` / `new skill`                | 创建 / 更新新 Skill 的指南工具                                                                          |

## 使用说明

- 这些 Skill 是为 **MODULAR-RAG-MCP-SERVER** 项目量身定制的，`auto-coder`、`qa-tester`、`setup` 等依赖项目根目录下的 `DEV_SPEC.md`、`config/settings.yaml` 等文件，**需在该项目工作区内使用**。
- `qa-tester` 会读写 `skills/qa-tester/QA_TEST_PLAN.md`、`QA_TEST_PROGRESS.md`；`project-review` 会读写 `review_progress.md` 作为进度持久化文件（已随包附带初始进度）。
- `resume-writer` / `interview-prep` / `project-learner` 等求职类 Skill 可脱离项目独立使用。

## 来源（Provenance）

- **源目录**：`f:\AAAkwh\MODULAR-RAG-MCP-SERVER\.github\skills`（项目本地 SKILL.md，非联网下载）
- **保留内容**：9 个 skill 的全部 `SKILL.md` 及其 `references/`、`scripts/` 支持文件，完整复制未改动
- **Omitted**：无
- **Logo**：`assets/avatar.svg` 为本插件生成的占位图标，非第三方素材

## 校验（Validation）

见对话中的 `validate_qoder_plugin.py` 离线校验结果。
