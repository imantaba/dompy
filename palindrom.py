# ````
#     tacocats -> True
#     racercar -> True
#     adbc -> False
# ````


class IsPalindrome:
    def __init__(self, string):
        self._generate = _Calculate(string)
    def showResult(self):
        result = self._generate.isPalindromeWithOneCharRemove()
        print(result)
        
class _Calculate:
    def __init__(self, string):
        self._str = string
    def isPalindromeWithOneCharRemove(self):
        string = self._str
        if not string:
            return True
        if len(string) <= 3:
            return True
        pal_char_count = int(len(string)/2-1)
        pchc_end = pal_char_count + 1
        for char in string:
            new_str = string.replace(char, '')
            if new_str[:pal_char_count] == new_str[:pal_char_count:-1]:
                return True
            else:
                return False

s = "adbc"
a = IsPalindrome(s)
a.showResult()
