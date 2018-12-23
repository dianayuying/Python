def censor(text, word):
    wd=text.split(" ")
    result=""
    l=len(wd)
    for i in range(l):
        if wd[i].lower()==word.lower():
            for j in range(len(word)):
                result=result+"*"
            result=result+" "
        else:
            result=result+wd[i]+" "
    result=result[0:len(result)]
    return result

print censor("hey hey hey", "hey")