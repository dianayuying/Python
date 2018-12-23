def median(seq):
    nseq=sorted(seq)
    print nseq
    if len(nseq)%2==1:
        return(nseq[(len(nseq)-1)/2])
    else:
        print nseq[len(nseq)/2-1]
        print nseq[len(nseq)/2]
        return (nseq[len(nseq)/2-1]+nseq[len(nseq)/2])/2.0
print median([4,5,4,5])