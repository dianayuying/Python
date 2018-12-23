def anti_vowel(text):
    l=len(text)
    newStr=""
    for i in range(l):
        if text[i].lower() in ['a','e','i','o','u']:
            newStr=newStr
        else:
            newStr=newStr+text[i]
    return newStr

anti_vowel("Hello World!")