# ````
#     tacocats -> True
#     racercar -> True
#     adbc -> False
# ````

def isPalindromeWithOneCharRemove(string):
    if not string:
        return True
    if len(string) <= 3:
        return True
    pal_char_count = int(len(string)/2-1)
    pchc_end = pal_char_count + 1
    print(pchc_end)
    for char in string:
        new_str = string.replace(char, '')
        print(new_str[pchc_end:])
        if new_str[:pal_char_count] == new_str[pchc_end::-1]:
            print("palindrom")

isPalindromeWithOneCharRemove('tacocats')