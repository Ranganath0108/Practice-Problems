"""Check Wheather the given Strings are isomorphic each other"""


def is_Isomorphic(s1, s2):
    map1 = dict()
    map2=dict()

    if(len(s1) != len(s2)):
        return False
    for i, j in zip(s1, s2):
        if i not in map1 and j not in map2:
            map1[i] = j
            map2[j]=i
        elif (map1.get(i)!=j or map2.get(j)!=i):
            return False
    return True


print(is_Isomorphic("aab", "xxy"))
print(is_Isomorphic("foo", "bar"))
print(is_Isomorphic("paper", 'title'))
print(is_Isomorphic("pijthbsfy","fvladzpbf"))
