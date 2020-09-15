from typing  import List

def searchPattern( text : str, pat: str) -> List:
    
    result = []

    if text==None or pat == None:
        return result

    lt = len(text)
    lp = len(pat)

    if lt == 0 or lp == 0:
        return result

    lps =[0] * lp

    fillLPS(lps,lp,pat)
    i = 0
    j = 0

    while i< lt:

        if text[i] == pat[j]:
            i += 1
            j +=1
        
        if j == lp:
            result.append((i-j,i))
            j = lps[j-1]

        elif i < lt and text[i] != pat[j]:

            if j !=0:
                j = lps[j-1]
            else:
                i +=1

    return result


def fillLPS(lps,lp,pat):

    i = 1
    l = 0

    while i < lp:

        if pat[i] == pat[l]:
            l+=1
            lps[i] = l
            i +=1
        else:

            if l!=0:
                l = lps[l-1]
            else:
                lps[i] = 0
                i +=1

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
print(searchPattern(txt, pat))






