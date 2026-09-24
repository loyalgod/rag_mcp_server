"""A2 冒烟测试：断言工程目录骨架（包结构契约）完好.

只验证"顶层包 + 关键子包"可导入——不追求全文件覆盖：
空壳模块 import 必然成功没有信息量，而未来模块的健康度由其各自的单元测试负责。
本测试的语义是：5.2 目录树定义的架构边界仍然存在且可导入。
"""

import importlib

import pytest

# 结构契约：DEV_SPEC 5.2 定义的顶层包与关键子包
STRUCTURAL_MODULES = [
    "mcp_server",
    "mcp_server.tools",
    "core",
    "core.query_engine",
    "core.response",
    "core.trace",
    "ingestion",
    "ingestion.chunking",
    "ingestion.transform",
    "ingestion.embedding",
    "ingestion.storage",
    "libs",
    "libs.loader",
    "libs.llm",
    "libs.embedding",
    "libs.splitter",
    "libs.vector_store",
    "libs.reranker",
    "libs.evaluator",
    "observability",
    "observability.dashboard",
    "observability.evaluation",
]


@pytest.mark.unit
@pytest.mark.parametrize("module_name", STRUCTURAL_MODULES)
def test_structural_package_importable(module_name: str) -> None:
    """五层架构的每个包都必须可导入（骨架被破坏时第一时间报警）。"""
    module = importlib.import_module(module_name)
    assert module is not None, f"package {module_name} failed to import"


@pytest.mark.unit
def test_main_entry_runs() -> None:
    """最小入口 main.py 可执行且不抛异常。"""
    import subprocess
    import sys
    from pathlib import Path

    root = Path(__file__).resolve().parents[2]
    result = subprocess.run(
        [sys.executable, str(root / "main.py")],
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode == 0
    assert "skeleton entry OK" in result.stdout
