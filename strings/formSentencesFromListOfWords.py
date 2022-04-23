def formSentences(words,result='',n=0):

    if not words:
        return

    if(n==len(words)):
        print(result)
        return

    for word in words[n]:
        out=result+" "+word
        formSentences(words,out,n+1)


print(formSentences([["you", "we"],
                ["have", "are"],
                ["sleep", "eat","drink"]]))
