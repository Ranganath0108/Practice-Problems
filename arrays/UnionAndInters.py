"""4. Find the union and intersection of two sorted array"""
def UnionInter(arr1,arr2):
    set=dict()
    union=[]
    Intersection=[]


    for i in arr1:
        if(i not in set):
            set[i]=1
        else:
            set[i]+=1
    for j in arr2:
        if(j not in set):
            set[j]=1
        else:
            set[j]+=1
    for k,v in set.items():
        if(v>1):
            Intersection.append(k)
        union.append(k)


    return f"{union=},{Intersection=}"

    



print(UnionInter([1,2,3,4],[6,1,4]))