"""Median Of  array:
"""


def medianOfArray(arr):
    arr.sort()
    n = len(arr)
    if(n % 2 != 0):
        return arr[(n//2)]
    return (arr[(n//2)-1]+arr[n//2])//2


print(medianOfArray([90, 100, 78, 89, 67]))
print(medianOfArray([56, 67, 30, 79]))
