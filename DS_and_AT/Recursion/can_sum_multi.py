
def can_sum(arr, target):
    if not arr or not target:
        return False
    else:
        memo = dict()
        return can_sum_helper(arr, target, memo) 

def can_sum_helper(arr, target, memo):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False   
    for num in arr:
        if can_sum_helper(arr, target - num, memo):
            memo[target] = True
            return True
    memo[target] = False
    return False

print(can_sum([4, 3, 2, 7, 13, 15], 400))


