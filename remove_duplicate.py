def remove_duplicates(seq):
    result=[]
    for i in range(len(seq)):
        if i==0:
            result.append(seq[i])
        else:
            for j in range(len(result)):
                if seq[i]==result[j]:
                    break
            else:
                result.append(seq[i])
    return result