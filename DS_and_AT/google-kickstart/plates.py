t = int(input())

for _ in range(t):
    n,k,p = map(int,input().split())
    stacks = []
    for _ in range(n):
        stacks.append(list(map(int,input().split())))
    
    stack_sum = {x:None for x in range(1,k+1)}
    i=1
    while i <=p and i <= k:
        max = 0
        for j in range(n):
            if max < sum(stacks[n][:i]):
                max = sum(stacks[n][:i])
                
        stack_sum[i]= max
    plates = 0    
    for i in range(p):
        if (p-i):
            pass
    
            
        
        
        i +=1
    #print('Case #{}: {}'.format())
        
    
    