t = 1

for case in range(1,t+1):
    n,k =(3,1)
    ses = [100 ,200 ,230]
 added = 0
    while added < k:
        maxd = 1
        maxi = -1
        l = len(ses)
        for i in range(l-1):
            if (ses[i+1]-ses[i])> maxd:
                maxd = ses[i+1]-ses[i]
                maxi = i
        
        if maxi == -1:
            break
        add = [(ses[maxi]+ses[maxi+1])//2]
        ses[:] = ses[:maxi+1] + add + ses[maxi+1:]
        added +=1
    
    
    if added<k:    
        print('Case #{}: {}'.format(case,1))
    else:
        maxdif = 0
        l = len(ses)
        
        for i in range(l-1):
            if (ses[i+1]-ses[i])>maxdif:
                    maxdif = ses[i+1]-ses[i]
        print('Case #{}: {}'.format(case,maxdif))