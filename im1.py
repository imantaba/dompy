f = [
    "/webapp/assets/html/a.html",
    "/webapp/assets/html/b.html",
    "/webapp/assets/js/c.js",
    "/webapp/index.html",
    "/.gitignore"
]


def build_trie(files):
    trie = FilesystemNode(name='/')
    for file in files:
        current_trie_node = trie
        for file_path_element in file.split('/'):
            new_child = current_trie_node.add_child_if_not_exists(file_path_element)
            if new_child is not None:
                current_trie_node = new_child
                

build_trie(f)