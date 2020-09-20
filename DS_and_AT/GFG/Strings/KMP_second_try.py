
def fillLps(lps, pat)->None:

    i = 0
    j = 1
    
    while j < len(pat):

        if pat[j] == pat[i]:
            lps[j] = lps[j-1] + 1
            i +=1
            j +=1
        else:
            if i==0:
                lps[j] = 0
                j +=1
            else:
                i -=1


def getMatchIndex(text, pat)->int:
    if text == None or pat == None:
        return -1

    lt,lp = len(text),len(pat)

    if lp > lt:
        return -1

    lps = [0] * lp
    fillLps(lps,pat)
          
    i = j = 0

    while j < lp and i < lt:

        if text[i] == pat[j]:
            i +=1
            j +=1
        else:
            if j==0:
                i +=1
            else:
                j = lps[j-1]

    if j == lp:
        return i-j
    else:
        return -1


txt ="AAABCC" #"ABABDABACDABABCABAB"
pat = "AABC"#"ABABCABAB"
print(getMatchIndex(txt, pat))



