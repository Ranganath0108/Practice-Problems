def smallestWindow(s):
    dist_count = len(set(s))
    size = len(s)
    for i in range(len(s)):
        count = 0
        substr = ""
        visited = {k: 0 for k in set(s)}
        for j in range(i, len(s)):
            if visited[s[j]] == 0:
                count += 1
                visited[s[j]] = 1
            substr += s[j]
            if(count == dist_count):
                break
        if(len(substr) < size and count == dist_count):
            res = substr
            size = len(res)
    return res, size


print(smallestWindow("AABBBCBBAC"))
print(smallestWindow("aaab"))
print(smallestWindow("aabcbcdbca"))
print(smallestWindow("GEEKSGEEKSFOR"))
