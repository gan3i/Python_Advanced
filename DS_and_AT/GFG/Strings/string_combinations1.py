from itertools import combinations

s = [1,2,3]


# returns tuple of characters for 
# all the combinations of the string
perm = combinations(s,len(s))
for i in perm:
    print (''.join(str(i)))

perm = combinations(s,2)
for i in perm:
    print (''.join(str(i)))