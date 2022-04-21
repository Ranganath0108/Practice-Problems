"""5. Move all the negative numbers to beginning and positive to end with extra spaces"""


def moveNum(arr):
    n = len(arr)
    j = 0
    for i in range(0, n):
        if (arr[i] < 0):
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr


print(moveNum([-12, 11, -13, -5, 6, -7, 5, -3, -6]))
