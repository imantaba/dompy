import os
import pathlib
from pathlib import Path

PIPE = "│"
directory = pathlib.Path('/home/ubuntu/test')        # create a path from string path
# print(directory)

# print(os.sep)           # show folder separator in all operating systems ex : windows "\" and linux "/"
# for x in directory.iterdir():     # show all files and directories in specified directory with absolute path
#     print(x)


# entries = directory.iterdir()
# # print(entry.is_file())
# entries = sorted(entries, key=lambda entry: entry.is_file())
# print(entries)

class _TreeGenerator:
    def __init__(self, directory):
        self._directory = directory
        self._tree = []
        
    def build_tree(self):
        self._tree_head()
        self._tree_body(self._directory)    
    def _tree_head(self):
        print(self._directory)
        self._tree.append(f"{self._directory}{os.sep}")
        self._tree.append(PIPE)
    
    def _tree_body(self, directory, prefix=""):
        entries = directory.iterdir()
        entries = sorted(entries, key=lambda entry: entry.is_file())
        for index, entity in enumerate(entries):
            print(index,entity)

a = _TreeGenerator(directory)
b = a.build_tree()
