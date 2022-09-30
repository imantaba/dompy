import os
import pathlib
from pathlib import Path

directory = Path('/home/ubuntu/aws')

# print(os.sep)
# for x in directory.iterdir():
#     print(x)


entries = directory.iterdir()
# print(entry.is_file())
entries = sorted(entries, key=lambda entry: entry.is_file())
print(entries)