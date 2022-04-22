"""Remove Duplicates in an array"""


def removeDuplicates(arr):
    d = {}
    for i in range(len(arr)-1):
        if arr[i] not in d:
            d[arr[i]] = 1
        else:
            arr.pop(i)
    return arr


print(removeDuplicates([1, 2, 3, 44, 34, 44, 67, 48]))
