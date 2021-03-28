def how_sum(arr, target):
    if not arr or not target:
        return None
    result = []
    if check_sum(arr, result, 0, target):
        return result
    return None

r_count = [0]
def check_sum(arr, result, curr_pos, target):
    global r_count
    r_count[0] +=1
    if target == 0:
        return True
    if target < 0 or curr_pos == len(arr):
        return False
    result.append(arr[curr_pos])
    if check_sum(arr, result, curr_pos + 1, target - arr[curr_pos]):
        return True
    result.pop()
    if check_sum(arr, result, curr_pos + 1, target):
        return True
    return False


def how_sum2(arr, target, memo):
    global r_count
    r_count[0] +=1
    if not target:
        return []
    if target < 0:
        return None
    # if target in memo:
    #     # print(target)
    #     # print("hi")
    #     return memo[target]
    for num in arr:
        result = how_sum2(arr, target-num, memo)
        if result !=None:
            result.append(num)
            memo[target] = result[:]
            return result
    memo[target] = None
    return None


memo = dict()
print(how_sum2([7, 14], 300, memo))
print(r_count)
