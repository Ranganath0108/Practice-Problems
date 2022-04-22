"""Find the array is Subset of Another array"""


def is_subset(arr1, arr2):
    if(len(arr1) < len(arr2)):
        arr1, arr2 = arr2, arr1

    for i in arr2:
        if i not in arr1:
            return False
    return True


print(is_subset([11, 1, 13, 21, 3, 7], [11, 3, 7]))
