#!/usr/bin/env python3
""" Author: Szymon Feliński """

import os
import fnmatch
import pylint

def find_all_python_files(path):
    """Finds all python files in current directory and below, without excluded directories"""
    result = []
    exclude_dirs = [".venv"]
    for root, dirs, files in os.walk(path, topdown=True):
        dirs[:] = [dir for dir in dirs if dir not in exclude_dirs]
        for name in files:
            if fnmatch.fnmatch(name, "*.py"):
                result.append(os.path.join(root, name))
    return result

print("Now running pylint on myself, cool!")

python_files = find_all_python_files(os.curdir)
pylint.run_pylint(python_files)
