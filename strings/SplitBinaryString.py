"""Split the binary string into substrings with equal number of 0s and 1s

Given a binary string str of length N, the task is to find the maximum 
count of consecutive substrings str 
can be divided into such that all the substrings are balanced i.e.
they have equal number of 0s and 1s. If it is not possible to split str satisfying the conditions then print -1.
"""


def Max_count(s):
    cnt, cnt0, cnt1 = 0, 0, 0
    for i in s:
        if(i == '0'):
            cnt0 += 1
        else:
            cnt1 += 1
        if(cnt0 == cnt1):
            cnt += 1
    if(cnt0 != cnt1):
        return -1
    return cnt


print(Max_count("010100111100"))
