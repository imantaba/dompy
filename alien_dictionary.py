from typing import List


words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"

class Solution:
    def __init__(self, words: List[str], order: str):
        self.words = words
        self.order = order
    def isAlienStored(self):
        words = self.words
        order = self.order
        lookup = {c:index for index,c in enumerate(order)}

        words2 = []
        for w in words:
            tmp = []
            for c in w:
                tmp.append(lookup[c])
            words2.append(tmp)

        for i in range(1, len(words2)):
            if words2[i-1]>words2[i]:
                return False
        return True

a = Solution(words,order)
print(a.isAlienStored())