t = int(input())

for i in range(1, t+1):
    n, k = map(int, input().split())
    s = input()
    result = 0
    
    count = 0
    
    for i in range(n//2):
        first = s[i]
        last = s[n-1-i]
        
        if first != last:
            count +=1
        
    if count != k:
        result = abs(k - count)
        
    
    print(f'Case #{i}: {result}')


'''
1
3 0
CAB


4 2
ABAA

'''
