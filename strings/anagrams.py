"""4. Given a seq of words, print all anagrams together"""


def Anagrams(words):
    grp = dict()
    for i in words:
        if "".join(sorted(i)) not in grp:
            grp["".join(sorted(i))] = [i]
        else:
            grp["".join(sorted(i))].append(i)
    res = [v for k, v in grp.items()]
    return res


print(Anagrams(['no', 'on', 'is']))
print(Anagrams(['act', 'god', 'cat', 'dog', 'tac']))
