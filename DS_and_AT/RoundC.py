t  = int(input())

for case in range(t):
    
    n, k = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    
    result = 0
    count = 0
    
    for i in range(n-1):
        
        if nums[i] - 1 == nums[i+1]:
            count +=1
        else:
            count = 0
            
        if count == k:
            result +=1
            count = 0
            
            
    print("Case #{}: {}".format(case+1, result))
        
        
    