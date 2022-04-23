"""Check Wheather the given Strings are isomorphic each other"""


def is_Isomorphic(s1, s2):
    iso_map = dict()

    if(len(s1) != len(s2)):
        return False
    else:
        for i, j in zip(s1, s2):
            if i not in iso_map:
                iso_map[i] = j
            else:
                if(iso_map[i] != j):
                    return False
    return True


print(is_Isomorphic("aab", "xxy"))
print(is_Isomorphic("foo", "bar"))
print(is_Isomorphic("paper", 'title'))
