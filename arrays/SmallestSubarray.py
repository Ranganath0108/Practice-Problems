"""smallest-subarray-with-sum-greater-than-Value"""


def SmallestSubarrayGreaterThanGivenValue(arr, k):
    if(sum(arr) <= k):
        return "Not Possible"
    Small_Array = []
    for i in range(len(arr)+1):
        for j in range(i, len(arr)):
            if(sum(arr[i:j+1]) > k):
                Small_Array.append(arr[i:j+1])
    return min(Small_Array, key=len), len(Small_Array)


print(SmallestSubarrayGreaterThanGivenValue([1, 2, 3], 3))
print(SmallestSubarrayGreaterThanGivenValue([1, 4, 45, 6, 0, 19], 51))
print(SmallestSubarrayGreaterThanGivenValue([1, 10, 5, 2, 7], 9))
print(SmallestSubarrayGreaterThanGivenValue(
    [1, 11, 100, 1, 0, 200, 3, 2, 1, 250], 280))
print(SmallestSubarrayGreaterThanGivenValue([1, 2, 4], 8))
