
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

print(can_sum([4, 3, 2, 7, 10, 15], 23))