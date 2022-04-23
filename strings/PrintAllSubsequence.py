"""Print all Subsequence in a Given String"""


def subsequence(s):
    n=len(s)
    for i in range(n):
        for j in range(i,n):
            print(s[i:j+1],end =" ")

subsequence("abcdeff")
