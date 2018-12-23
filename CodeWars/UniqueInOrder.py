"""
Unique in Order
    Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same 
    value next to each other and preserving the original order of elements.
"""
def unique_in_order(iterable):
    res=[]
    for i in iterable:
        if len(res)==0:
            res.append(i)
        elif len(res)>0 and i!=res[-1]:
            res.append(i)
    return res

#--------
# Test Case
test.assert_equals(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])
