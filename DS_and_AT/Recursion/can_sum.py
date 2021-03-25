
def can_sum(arr, target):
    if not arr:
        return False
    memo = [[None] * (target + 1) for _ in range(len(arr))]
    return can_sum_helper(arr, target, 0, memo)

def can_sum_helper(arr, target, curr_pos, memo):
    if target == 0:
        return True
    if curr_pos == len(arr):
        return False
    if target < 0:
        return False
    if memo[curr_pos][target] != None:
        return memo[curr_pos][target]
    result =  (can_sum_helper(arr, target - arr[curr_pos], curr_pos + 1, memo)
            or  can_sum_helper(arr, target , curr_pos + 1,memo))
    memo[curr_pos][target] = result
    return memo[curr_pos][target]

def can_sum_dp(arr, target):
    if not arr:
        return False
    n = len(arr)
    dp = [[False] * (target + 1) for _ in range(n)]

    for row in range(n):
        for col in range(1, target+1):
            if row == 0:
                dp[row][col] =  arr[row] == col
            else:
                if arr[row] == col:
                    dp[row][col] = True
                if arr[row] > col:
                    dp[row][col] = dp[row-1][col]
                else:
                    dp[row][col] = dp[row - 1][col] or dp[row-1][col - arr[row]]

    return dp[n-1][target]

'''
    0     1       2    3       4       5
1[False, False, False, False, False, False]0
3[False, False, False, False, False, False]1
4[False, False, False, False, False, False]2
2[False, False, False, False, False, False]3

'''
print(can_sum_dp([4, 3, 2, 7, 8, 15], 4 ))