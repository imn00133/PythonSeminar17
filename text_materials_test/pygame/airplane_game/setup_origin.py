import sys
import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Users\KJH\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\KJH\AppData\Local\Programs\Python\Python36\tcl\tk8.6'

build_exe_options = {
    "packages": ["pygame", "sys", "random", "time"],
    "excludes": ["numpy"],
    "include_files": ["images/"]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Test",
    version="1.0",
    description="test",
    author="Kim Jaehyeong",
    options={"build_exe": build_exe_options},
    executables=[Executable("8_rule_add.py", base=base)]
)