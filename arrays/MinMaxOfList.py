"""2. Find the max and min element of a list
input =[1,2,2,3] output =(1,3)
input =[6,5,32,2], output=(2,32)

"""
def MinMax1(arr):
    return min(arr),max(arr)

def MinMax2(arr):
    min,max=arr[0],arr[0]
    for i in arr[1:]:
        if(i>max):
            max=i
        if(i<min):
            min=i
    return min,max

print(MinMax1([1,2,2,3]))
print(MinMax1([6,5,32,2]))

#check by second fuction
print(MinMax2([1,2,2,3]))
print(MinMax2([6,5,32,2]))