import platform
import sys
from pathlib import Path

PYTHON_VERSION = sys.version.split()[0]

IS_LINUX = platform.system() == "Linux"
IS_MACOS = platform.system() == "Darwin"
IS_WINDOWS = platform.system() == "Windows"

IS_FROZEN = getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS")

PYINSTALLER_LIB_ROOT = Path(sys._MEIPASS) if IS_FROZEN else Path.cwd()
