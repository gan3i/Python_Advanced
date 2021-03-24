'''
    [40, 20, 30, 10]

     
    [1, 2, 3, 4, 5]

'''

def get_matrix_chain_cost(matrix):
    if not matrix:
        return 0
    n = len(matrix)
    cost_memo = [[0] * n for _ in range(n)]
    return chain_order_cost(matrix, 1, n-1, cost_memo)

def chain_order_cost(matrix, start , end, memo):
    if start == end:
        return  0

    if memo[start][end] > 0 :
        return memo[start][end]

    memo[start][end] = float('+inf')
    for bracket in range(start, end):
        cost = (chain_order_cost(matrix, start , bracket, memo) 
                + chain_order_cost(matrix, bracket + 1 , end, memo)
                + (matrix[ start- 1] * matrix[bracket] * matrix[end]))

        memo[start][end] = min(memo[start][end], cost)

    return memo[start][end]

def get_matrix_chain_cost_dp(matrix, n):
    if not matrix:
        return 0

    cost_matrix = [[0] * n for _ in range(n)]
    # n  = 5
    for cl in range(2, n): # 4
        for i in range(1, n-cl+1): # 1
            j = i + cl -1 # 4
            cost_matrix[i][j] = float('+inf')
            for k  in range(i, j): # 3
                cost_matrix[i][j] =min(cost_matrix[i][j], cost_matrix[i][k] + cost_matrix[k+1][j] + matrix[i-1] * matrix[k] * matrix[j])

    return cost_matrix[1][n-1]
    

'''
        start = 1
        end = 4
        bracket = 1
       0  1  2  3  4
       4, 2, 3, 1,  5
  0 4 [0, 0, 0, 0, 0]  
  1 2 [0, 0,24,14, 34] 14 + 0 + 4 * 1 * 5
  2 3 [0, 0, 0, 6, 55]  
  3 1 [0, 0, 0, 0, 15] 
  4 5 [0, 0, 0, 0, 0] 
'''

print(get_matrix_chain_cost_dp([4, 2, 3, 1 , 5],5))

