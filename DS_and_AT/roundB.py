t = int(input())

for i in range(t):
    
    n = int(input())
    nums= list(map(int,input().split()))
    
    peak_count = 0
    
    for i in range(1,n-1):
        if  nums[i-1] < nums[i] > nums[i+1]:
            peak_count +=1
            
    print("Case #{}: {}".format(i+1,peak_count))