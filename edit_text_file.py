def replace_word(filename, old_word, new_word):
    with open(filename, 'rt') as f:
        s = f.read()
        print(s)
        if old_word not in s:
            print('"{old_word}" not found in {filename}.'.format(**locals()))
            return
        
        
    with open(filename, 'wt') as f:
        print('Changing "{old_word}" to "{new_word}" in {filename}'.format(**locals()))
        s = s.replace(old_word, new_word)
        f.write(s)
        
        
replace_word('test.txt', 'neo4j', 'iman')