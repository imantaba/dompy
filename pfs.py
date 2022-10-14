files = [
    "/webapp/assets/html/a.html",
    "/webapp/assets/html/b.html",
    "/webapp/assets/js/c.js",
    "/webapp/index.html",
    "/.gitignore"
]

# -- webapp
#   -- assets
#     -- html
#       -- a.html
#       -- b.html
#     -- js
#       -- c.js
#   -- index.html

DUBLE_SPACE = "  "
DUBLE_DASH = "-- "

class FileStructure:
    def __init__(self, files):
        self._generate = _StructureGenerator(files)
    def generate(self):
        tree = self._generate.build_tree()
        for entry in tree:
            print(entry)


class _StructureGenerator:
    def __init__(self, files):
        self._files = files
        self._tree = []
    
    def build_tree(self):
        dic = {}
        paths = self._files
        for path in paths:
            list_count = len(path.split('/'))
            prefix = ""
            for index, entry in enumerate(path.split('/')):
                if index != 0:
                    prefix += DUBLE_SPACE
                    if (index, entry) in dic.items():
                        continue
                    if index != list_count - 1:
                        dic[index] = entry
                    if index == 1:
                        prefix=""
                    self._tree.append(f"{prefix}{DUBLE_DASH}{entry}")
        return self._tree
    

a = FileStructure(files)
a.generate()