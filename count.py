def count(sequence, item):
    result=0
    for i in range(len(sequence)):
        if str(sequence[i])==str(item):
            result=result+1
    return result

print count([4,'foo',5,'foo'],5)