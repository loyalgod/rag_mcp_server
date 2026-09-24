"""pytest 根配置：把 src/ 注入 sys.path，使测试可直接 import 五个顶层包。

这是全项目唯一的手动路径注入点（A1 的 main.py 除外）——
conftest.py 位于 rootdir 时，pytest 会在收集测试前自动执行本文件，
因此所有 unit/integration/e2e 测试无需重复处理导入路径。
"""

import sys
from pathlib import Path

SRC_DIR = Path(__file__).parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))
