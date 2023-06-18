
from collections import deque
import queue


words = ["word","world","row","woy","y"]
order = "worldabcefghijkmnpqstuvxyz"




class sortWithAlienDic:
    def __init__(self, words, order):
        self.words = words
        self.order = order

    def _create_dic_from_words(self):
        words = self.words
        order = self.order
        words_lookup = {}
        lookup = {c:index for index,c in enumerate(order)}
        for word in words:
            l = []
            for c in word:
                l.append(lookup[c])
            words_lookup[word] = l
        return words_lookup
    
    def sort_words(self):
        words_lookup = self._create_dic_from_words()
        q = deque()

        lst = []
        for word in words_lookup:
            lst.append(words_lookup[word])

        sorted_list = sorted(lst)
        for item in sorted_list:
            for word in words_lookup:
                if words_lookup[word] == item:
                    q.append(word)

        return list(q)

a = sortWithAlienDic(words, order)
print(a.sort_words())