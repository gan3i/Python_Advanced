
def longestCommonPrifix(s1,s2):

    lps = []
    if s1 == None or s2 == None:
        return ''.join(lps) 

    if len(s1)> len(s2):
        longestCommonPrifix(s2,s1)
    s1 = s1.lower()
    s2 = s2.lower()
    ns1 = len(s1)

    for i in range(ns1):

        if s1[i] == s2[i]:
            lps.append(s[i])
        else:
            return ''.join(lps)

    return ''.join(lps)

def buildSuffixes(s):

    suffixes = []

    if s == None:
        return suffixes

    for i in range(len(s)):
        suffixes.append(s[i:])
    suffixes.sort() 
    return suffixes


def longestRepeatingString(s):
    
    lrs = ''
    if s == None:
        return lrs

    suffixes = buildSuffixes(s) # O(n**2)

    # for suffix in suffixes:
    #     print(suffix)

    for i in range(len(s)-1): # O(n**2)

        temp_lrs = longestCommonPrifix(suffixes[i],suffixes[i+1])

        if len(temp_lrs) > len(lrs):
            lrs = temp_lrs

    return lrs


s = 'AABACAABA'

print(longestRepeatingString(s))




    