"""Modular RAG MCP Server - 主入口（A1 最小可运行版）.

职责：把 src 加入 sys.path 后做启动自检。
MCP Server 真正的启动逻辑在阶段 E（server.py）实现后接入。
"""

import sys
from pathlib import Path

SRC_DIR = Path(__file__).parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


def main() -> None:
    print("Modular RAG MCP Server: skeleton entry OK")


if __name__ == "__main__":
    main()
