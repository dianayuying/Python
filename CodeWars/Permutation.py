"""
Permutaion
"""
def permutations(string):
    if len(string)==1:
        return string

    recursive_perms=[]
    
    for x in string:
        for perm in permutations(string.replace(x,'',1)):
            recursive_perms.append(x+perm)
    # remove duplicate by making the list as a set
    return set(recursive_perms)
#--------------
# Test cases
Test.assert_equals(sorted(permutations('a')), ['a']);
Test.assert_equals(sorted(permutations('ab')), ['ab', 'ba'])
Test.assert_equals(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])