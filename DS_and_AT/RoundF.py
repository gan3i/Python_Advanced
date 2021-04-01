from heapq import heapify, heappop

t  = int(input())

for case in range(t):
    n , x = list(map(int,input().split()))
    nums = list(map(int,input().split()))

    result = []
    heap = []
    
    for i in range(n):
        div = nums[i] // x
        mod = nums[i] % x
        if div == 0 or (div == 1 and mod == 0):
            result.append(str(i+1))
        else:
            div = div -1 if mod==0 else div
            heap.append([div,i+1])
        
    heapify(heap)   
    while heap:
        _,index = heappop(heap)
        result.append(str(index))
     
    print("Case #{}: {}".format(case+1,' '.join(result)))


