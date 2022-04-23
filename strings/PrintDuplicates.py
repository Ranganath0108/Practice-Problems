"""Print All the Duplicates in the Given string"""


def allDuplicates(s):
    dup = {}
    for i in s:
        if i not in dup:
            dup[i] = 1
        else:
            dup[i] += 1
    res = [k for k, v in dup.items() if v > 1]
    return res


print(allDuplicates("abaacdase"))
print(allDuplicates("aanfdrhddd"))
