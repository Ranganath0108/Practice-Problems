"""maximum product subarray"""


def maxProductSubarry(arr):
    mx = arr[0]
    for i in range(len(arr)+1):
        for j in range(i, len(arr)):
            mx = max(mx, product(arr[i:j+1]))
    return mx


def product(arr):
    pro = 1
    for i in arr:
        pro = pro*i
    return pro


print(maxProductSubarry([6, -3, -10, 0, 2]))
print(maxProductSubarry([2, 3, 4, 5, -1, 0]))
