from itertools import permutations

s = 'Asdf'


# returns tuple of characters for 
# all the permutaions of the string
perm = permutations(s)
for i in perm:
    print (''.join(i))


# permutation with given length
perm = permutations(s,2)
for i in perm:
    print (''.join(i))