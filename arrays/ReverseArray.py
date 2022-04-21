"""1. Given the array ,reverse the array. 


Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}



Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}"""


from inspect import stack

# by using stack


def revArray(a):
    revArr = stack()
    while len(a):
        revArr.append(a.pop())
    return revArr

# with no extra space and swapping  technique


def revarray(arr):
    start, end = 0, len(arr)-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start] #swapping
        start += 1
        end -= 1
    return arr


print(revArray([1, 2, 3]))
print(revArray([4, 5, 1, 2]))

print(revarray([1, 2, 3]))
print(revarray([4, 5, 1, 2]))
