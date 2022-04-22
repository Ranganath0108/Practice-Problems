"""Given an array of size n and a number k, find all elements that appear more than n/k times


Given an array of size n, find all elements in array that appear more than n/k times. For example, if the input arrays 
is {3, 1, 2, 2, 1, 2, 3, 3} and k is 4, 
then the output should be [2, 3]. 
Note that size of array is 8 (or n = 8), so we need to find all elements"""


def moreThan_NbyK(arr, k):
    n = len(arr)
    x = n//k
    freq = dict()
    for i in arr:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    return [k for k, v in freq.items() if v > x]


print(moreThan_NbyK([3, 1, 2, 2, 1, 2, 3, 3], 4))
