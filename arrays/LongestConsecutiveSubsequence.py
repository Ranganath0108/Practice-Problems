"""Longest consecutive subsequence"""

from turtle import rt


def longestConsecutiveSeq(arr):
    count = 0
    arr.sort()
    mx = 0
    if(len(arr) == 1):
        return 1
    for i in range(len(arr)-1):
        if(arr[i+1]-arr[i] == 1):
            count += 1
        elif(arr[i+1]-arr[i] == 0):
            continue
        else:
            mx = max(count, mx)
            count = 0
    return count


print(longestConsecutiveSeq([1, 2, 3, 4, 4, 5, 7, 44]))
