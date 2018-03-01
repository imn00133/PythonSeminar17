import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "excludes": ["numpy"],
    "include_files": ["images/"]
}
"""
build_exe_options = dict(
    excludes=["numpy"],
    include_files=["images/"]
)
"""
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Test",
    version="1.0",
    description="test",
    author="Kim Jaehyeong",
    options={"build_exe": build_exe_options},
    executables=[Executable("8_add_rule.py", base=base)]
)