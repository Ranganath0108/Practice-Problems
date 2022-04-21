"""##### 13. Next Permutation


A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Input: nums = [1,2,3]
Output: [1,3,2]

Input: nums = [3,2,1]
Output: [1,2,3]

Input: nums = [1,1,5]
Output: [1,5,1]


<img src="https://leetcode.com/media/original_images/31_Next_Permutation.gif"/>
"""


def nextPermutation(arr):
    if(arr == None or len(arr) == 1):
        return
    n = len(arr)-1
    i = n-1
    while(i > 0 and arr[i] > arr[i+1]):
        i = i-1
    j = n
    if(i > 0):
        while(arr[j] <= arr[i]):
            j = j-1
        arr[i], arr[j] = arr[j], arr[i]
        arr[i+1:] = reversed(arr[i+1:])
    else:
        arr = arr[::-1]
    return arr


print(nextPermutation([1, 5, 8, 4, 7, 6, 5, 3, 1]))
print(nextPermutation([1, 1, 5]))
print(nextPermutation([3, 2, 1]))
print(nextPermutation([1, 2, 3]))
