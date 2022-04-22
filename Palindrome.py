"""Check whether the string is palindome or not"""

from sympy import re


def is_palindrome(s):
    if (len(s)==0 or len(s)==1):
        return True
    if(s[0]==s[len(s)-1]):
        return is_palindrome(s[1:len(s)-1])
    return False

print(is_palindrome("aabbaa"))
print(is_palindrome("abc"))