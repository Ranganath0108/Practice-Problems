"""Trapping Rainwater Problem
"""


def maxWater(arr):
    res = 0
    for i in range(1, len(arr)-1):
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])
        right = arr[i]
        for j in range(i+1, len(arr)):
            right = max(right, arr[j])
        res = res+min(left, right)-arr[i]
    return res


print(maxWater([3, 0, 3]))
print(maxWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
