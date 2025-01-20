import sys
import os

if sys.version_info < (3, 8):
    raise ImportError("nanobind does not support Python < 3.8.")

def include_dir() -> str:
    "Return the path to the nanobind include directory"
    return "/usr/share/nanobind/include"

def cmake_dir() -> str:
    "Return the path to the nanobind CMake module directory."
    return "/usr/share/nanobind/cmake"

__version__ = "2.4.0"

__all__ = (
    "__version__",
    "include_dir",
    "cmake_dir",
)
