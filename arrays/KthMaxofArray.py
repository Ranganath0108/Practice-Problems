
"""3.Find the kth max element in the array
input=[1,0,4,55,8],2   output=8
"""

def kthMax(arr,k):
    arr=sorted(arr,reverse=True)
    return arr[k-1]


print(kthMax([1,0,4,55,8],2 ))