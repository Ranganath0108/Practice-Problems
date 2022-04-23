"""Longest palindromic Subsequence"""


def is_palindrome(s):
    if(len(s) == 1 or len(s) == 0):
        return True
    if(s[0] == s[len(s)-1]):
        return is_palindrome(s[1:len(s)-1])
    return False


def longestPalindromicSubsequence(s):
    palindromes = []
    for i in range(len(s)+1):
        for j in range(i, len(s)):
            if(is_palindrome(s[i:j+1])):
                palindromes.append(s[i:j+1])
    return max(palindromes, key=len)


print(longestPalindromicSubsequence("aaaabbaa"))
