"""11. find the duplicate in an array of n+1 integers 
"""


def findDuplicate(arr):
    dup = {}
    for i in arr:
        if i not in dup:
            dup[i] = 1
        else:
            return i
    return "No Duplicates"


print(findDuplicate([1, 2, 3, 3, 4]))
print(findDuplicate([1, 2, 3]))
