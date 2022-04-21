"""7. Write a program to cyclically rotate array one by one"""


def rotate(arr):
    first = arr[len(arr)-1]
    for i in range(len(arr))[::-1]:
        arr[i] = arr[i-1]
    arr[0] = first
    return arr


def rotate2(arr):
    a = arr.pop()
    arr.insert(0, a)
    return arr


print(rotate([2, 7, 8, 9]))
print(rotate2([1, 2, 3]))
