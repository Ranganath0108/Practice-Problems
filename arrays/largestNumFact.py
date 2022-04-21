"""Find the Factorial Of a Larger number
"""
from math import factorial


def LargestNumFactorial(arr):
    return factorial(max(arr))


def LargestNumFact2(arr):
    mx = arr[0]
    for i in arr:
        mx = max(mx, i)
    return fact(mx)


def fact(n):
    if(n == 0 or n == 1):
        return n
    return n * fact(n-1)


print(LargestNumFactorial([4, 2, 6, 7]))
print(LargestNumFact2([4, 6, 7, 1]))
