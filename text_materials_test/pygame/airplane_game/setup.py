import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "excludes": ["numpy"],
    "include_files": ["images/",
                      "sounds/"]
}
"""
build_exe_options = dict(
    excludes=["numpy"],
    include_files=["images/",
                   "sounds/"]
)
"""
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="airplane_game",
    version="1.0",
    description="airplane_game distribute",
    author="Kim Jaehyeong",
    options={"build_exe": build_exe_options},
    executables=[Executable("9_add_sound.py", base=base)]
)
