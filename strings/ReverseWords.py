"""Reverse a words in a given Sentence"""


def reverseWords(s):
    words = s.split(" ")
    n = len(words)-1
    ans = ""
    for i in range(n, -1, -1):
        ans += " "+words[i]

    return ans


print(reverseWords("Hi I am Ranganath"))
