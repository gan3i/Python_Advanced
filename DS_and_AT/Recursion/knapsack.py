def knapSack(W, wt, val, n):
    def helper(cap, curr_pos):
        if curr_pos < 0 or cap <= 0:
            return 0
            
        if memo[curr_pos][cap] > -1:
            return memo[curr_pos][cap]
        
        result = 0
        if wt[curr_pos] > cap:
            result = helper(cap, curr_pos-1)
        else:   
            result=  max(helper(cap, curr_pos-1)
                        , val[curr_pos] + helper(cap - wt[curr_pos], curr_pos-1))
                            
        memo[curr_pos][cap] = result
        return memo[curr_pos][cap]
        
    memo = [[-1] * (W+1) for _ in range(n)]
    
    return helper(W, n-1)
'''
           0  1  2  3
      0 0 [0, 0, 0, 0]
      2 2 [0, 0, 2, 2]
      6 5 [0, 0, 2, 2]
      3 3 [0, 0, 2, 3]
      2 1 [0, 2, 2, 4]


           0  1  2  3  4
      0 0 [0, 0, 0, 0, 0]
      1 4 [0, 0, 0, 0, 1]
      2 5 [0, 0, 0, 0, 0]
      3 1 [0, 0, 0, 0, 0]
'''

    

def knapSack_dp(W, wt, val, n):
    if n == 0 or  W == 0:
        return 0
    
    values_dp = [[0] * (W+1) for _ in range(n+1)]
            
    for row in range(1,n+1):#1
        for col in range(1, W+1):#1
            curr_wt = wt[row-1]  # 4
            curr_val = val[row-1] # 1
            if curr_wt > col:
                values_dp[row][col] = values_dp[row-1][col]
            else:
                values_dp[row][col] = max(values_dp[row-1][col], curr_val + values_dp[row-1][col - curr_wt]) 
        
    return values_dp[n][W]

N = 3
W = 4
values = [1,2,3]
weight = [4,5,1]
print(knapSack_dp(W, weight, values, N))