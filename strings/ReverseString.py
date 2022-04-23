"""Reverse a given String"""


def reverseS(s):
    if(len(s) == 0 or len(s) == 1):
        return s
    res = s[len(s)-1]+reverseS(s[:len(s)-1])
    return res


print(reverseS("github"))
print(reverseS("Ranganath0108"))
