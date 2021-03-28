def best_sub_seq(arr, target):\
    return best_ss_helper(arr, target, 0, [],dict())
    
def best_ss_helper(arr, target, curr_pos, sub_seq, memo):
    if target == 0:
        return sub_seq
        
    if target < 0 or curr_pos == len(arr):
        return []

    if (target, curr_pos) in memo:
        print("Hi")
        return memo[(target, curr_pos)]   

    incl_curr_pos = best_ss_helper(arr, target - arr[curr_pos]
                            , curr_pos + 1, sub_seq[:] + [arr[curr_pos]], memo)
    
    not_incl_curr_pos =  best_ss_helper(arr, target, curr_pos + 1, sub_seq[:], memo )
    
    if incl_curr_pos and not_incl_curr_pos:
        memo[(target, curr_pos)] = min(incl_curr_pos, not_incl_curr_pos, key= lambda x : len(x))
    else:
        memo[(target, curr_pos)] = incl_curr_pos if incl_curr_pos else not_incl_curr_pos

    return memo[(target, curr_pos)]

