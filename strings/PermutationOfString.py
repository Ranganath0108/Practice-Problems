"""Print all permutation of given string"""


def permuatation(s):
    if(len(s) == 1):
        return s
    perms = permuatation(s[1:])
    char = s[0]
    res = []
    for perm in perms:
        for i in range(len(perm)+1):
            res.append(perm[:i]+char+perm[i:])
    return res


print(permuatation("ABCD"))
