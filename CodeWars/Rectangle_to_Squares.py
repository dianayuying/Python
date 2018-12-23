"""
Rectangle Into Squares
 translate this drawing into an algorithm?

You will be given two dimensions

a positive integer length (parameter named lng)
a positive integer width (parameter named wdth)
"""
def sqInRect(lng, wdth):
    if lng==wdth:
        return None
    else:
        xmax=max(lng, wdth)
        xmin=min(lng, wdth)
        res=[]
        while xmax!=xmin:
            res.append(xmin)
            newx=xmax-xmin
            newy=xmin
            xmax = max(newx, newy)
            xmin = min(newx, newy)
        else:
            res.append(xmax)
        return res


#------------
# Test
test.assert_equals(sqInRect(5, 5), None)
test.assert_equals(sqInRect(5, 3), [3, 2, 1, 1])