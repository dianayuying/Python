def matrix_mult(a, b):
    #import numpy as np
    #return np.matmul(a,b).tolist()
    cxy=[]
    for i in range(len(a)):
        cx=[]
        for j in range(len(b[0])):
            c=0
            for k in range(len(b)):
                c += a[i][k]*b[k][j]
            cx.append(c)
        cxy.append(cx)
    return cxy