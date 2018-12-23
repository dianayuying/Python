"""
Distribute Candies evenly
m candies
n kids
"""

def distribute(m, n):
    if n<=0:
        return []
    else:
        res=[0 for i in range(n)]
        if m<=0:
            return res
        else:
            for i in range(m):
                res[i%n]+=1
            return res
#
# Test Case
test.assert_equals(distribute(-5,  0) , [] )
test.assert_equals(distribute( 0,  0) , [] )
test.assert_equals(distribute( 5,  0) , [] )
test.assert_equals(distribute(10,  0) , [] )
test.assert_equals(distribute(15,  0) , [] )
test.assert_equals(distribute(-5, -5) , [] )
test.assert_equals(distribute( 0, -5) , [] )
test.assert_equals(distribute( 5, -5) , [] )
test.assert_equals(distribute(10, -5) , [] )
test.assert_equals(distribute(15, -5) , [] )
test.assert_equals(distribute(-5, 10) , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] )
test.assert_equals(distribute( 0, 10) , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] )
test.assert_equals(distribute( 5, 10) , [1, 1, 1, 1, 1, 0, 0, 0, 0, 0] )
test.assert_equals(distribute(10, 10) , [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] )
test.assert_equals(distribute(15, 10) , [2, 2, 2, 2, 2, 1, 1, 1, 1, 1] )