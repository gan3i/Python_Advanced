

def best_sum_ss(arr, target, memo = dict()):
    if target == 0:
        return []
    if target < 0 :
        return None
        
    if target in memo:
        print("Hi")
        return memo[target] 
    sub_seq = None
    for num in arr:
        remainder = target - num
        remainder_sub_seq = best_sum_ss(arr, remainder)
        if remainder_sub_seq != None:
            remainder_sub_seq.append(num)
            if sub_seq !=None :
                sub_seq = min(sub_seq, remainder_sub_seq, key = lambda seq : len(seq))
            else:
                sub_seq = remainder_sub_seq
    memo[target] = sub_seq
    return memo[target]

print(best_sum_ss([4, 3, 2, 7, 8, 15], 128 ))



