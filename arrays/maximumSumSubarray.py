"""8. Find the largest sum of contagious subarray"""

def MaxSumSubarray(arr):
    mx=arr[0]
    for i in range(len(arr)+1):
        for j in range(i,len(arr)):
            mx=max(mx,sum(arr[i:j+1]))
    return mx

def KadensAlgo(arr):
    c=arr[0]
    mx=arr[0]
    for i in arr[1:]:
        c+=i
        mx=max(c,mx)
        if(c<0):
            c=0
    return mx
    
print(MaxSumSubarray([1, 2, 3, -2, 5]))
print(KadensAlgo([1, 2, 3, -2, 5]))
