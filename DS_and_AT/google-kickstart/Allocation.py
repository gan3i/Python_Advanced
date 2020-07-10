t = int(input())

for i in range(t):
    n,b = map(int,input().split())
    price= list(map(int,input().split()))
    
    
    price.sort()

    c= 0 
    j = 0
    while c<= b and j<n:
        c +=price[j]
        if c<=b:
            j +=1
        
    print(f'Case #{i+1}: {j}')