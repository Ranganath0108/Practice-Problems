"""9. Minimize the maximum difference heights



Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each tower either by increasing or decreasing them by K only once. After modifying, height should be a non-negative integer. 
Find out the minimum possible difference of the height of shortest and longest towers after you have modified each tower.


Input:
K = 2, N = 4
Arr[] = {1, 5, 8, 10}
Output:
5
Explanation:
The array can be modified as 
{3, 3, 6, 8}. The difference between 
the largest and the smallest is 8-3 = 5.



Input:
K = 3, N = 5
Arr[] = {3, 9, 12, 16, 20}
Output:
11
Explanation:
The array can be modified as
{6, 12, 9, 13, 17}. The difference between 
the largest and the smallest is 17-6 = 11.






"""


def minMaxDiff(arr,k):
    arr.sort()
    res=arr[len(arr)-1]-arr[0]
    smallest=arr[0]+k
    longest=arr[len(arr)-1]-k
    for i in range(len(arr)):
        mn=min(smallest,arr[i]-k)
        mx=max(longest,arr[i]+k)
        if(mn<0):
            continue
        res=min(res,mx-mn)

    return res


print(minMaxDiff([7,12,3],8))
print(minMaxDiff([3, 9, 12, 16, 20],3))
print(minMaxDiff([1, 5, 8, 10],2))