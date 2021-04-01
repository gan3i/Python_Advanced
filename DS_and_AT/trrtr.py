t = int(input())

for case in range(t):
    
    n, k = list(map(int,input().split()))
    times = [0] * 201
    for i in range(n):
        s,e = list(map(int,input().split()))
        times[s] = 1
        times[e] = 2
        
    temp_k = 0
    dep = False
    harv = False
    count = 0
    
    for i in times:
        
        if not harv:
            if i == 0:
                if temp_k > 0:
                    temp_k -=1
                    if temp_k == 0:
                        count +=1
            else: # start harvesting
                if temp_k > 0:
                    temp_k -=1
                    if temp_k == 0:
                        count +=1
                        temp_k = k
                else:
                    temp_k = k
                harv = True
        else:
            if i == 2:
                temp_k -=1
                if temp_k == 0:
                    count +=1
                harv = False
            else:
                temp_k -=1
                if temp_k == 0:
                    count +=1
                    temp_k = k
             
    
    print("Case #{}: {}".format(case+1, count))
                          
        

  