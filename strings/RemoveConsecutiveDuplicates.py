"""Remove Consecutive Duplicates in a given String"""

from os import remove


def removeConsecutiveDuplicates(s):
    c = s[0]
    ans = c
    for i in s[1:]:
        if(c != i):
            ans += i
        c = i
    return ans


print(removeConsecutiveDuplicates("aabbccc"))
print(removeConsecutiveDuplicates("ababcccd"))
