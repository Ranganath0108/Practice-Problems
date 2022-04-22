"""3. Minimum characters to be added at front to make string palindrome"""


def is_palindrome(s):
    return s == s[::-1]


def minTomakePalindrome(s):
    count = 0
    while len(s) > 0:
        if(is_palindrome(s)):
            break
        else:
            count += 1
            s = s[:-1]
    return count


print(minTomakePalindrome("abc"))
print(minTomakePalindrome("AABCBAAA"))
