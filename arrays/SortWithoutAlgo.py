"""4. Given an array which consists of only 0,1,2 sort them without using sorting algo"""

def sortWithoutAlgo(arr):
    n=len(arr)
    count0=0
    count1=0
    count2=0
    for i in arr:
        if(i==0):
            count0+=1
        elif (i==1):
            count1+=1
        elif (i==2):
            count2+=1
    j=0
    for j in range(n):
        if(count0!=0):
            arr[j]=0
            count0-=1
        elif (count1!=0):
            arr[j]=1
            count1-=1
        elif (count2!=0):
            arr[j]=2
            count2-=1
    return arr


print(sortWithoutAlgo([0,2,1,2,0]))