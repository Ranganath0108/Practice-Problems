"""Find if there is any subarray with sum equal to 0"""


def Is_subarraySumZero(arr):
    for i in range(len(arr)+1):
        for j in range(i, len(arr)):
            if(sum(arr[i:j+1]) == 0):
                return True
    return False


print(Is_subarraySumZero([4, 4, -2, -2]))
