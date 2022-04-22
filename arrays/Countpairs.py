"""Count all pairs on integer sub array whose sum is equal to given number"""


def CountPairs(arr, k):
    count = 0
    for i in range(len(arr)+1):
        for j in range(i, len(arr)):
            if(i != j):
                if(arr[i]+arr[j] == k):
                    count += 1
    return count


print(CountPairs([1, 1, 1, 1], 2))
print(CountPairs([4, 1, 3, 4], 7))
