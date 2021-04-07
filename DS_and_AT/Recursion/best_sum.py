def best_sub_seq(arr, target):
    n = len(arr)
    return best_ss_helper(arr, target, n-1,dict())
    
def best_ss_helper(arr, target, curr_pos, memo):
    if target == 0:
        return list()
        
    if target < 0 or curr_pos < 0:
        return None

    if (target, curr_pos) in memo:
        return memo[(target, curr_pos)]   
    
    incl_curr_pos = best_ss_helper(arr, target - arr[curr_pos], curr_pos - 1, memo)
    
    not_incl_curr_pos =  best_ss_helper(arr, target, curr_pos - 1, memo )
    
    if incl_curr_pos != None and not_incl_curr_pos != None:
        memo[(target, curr_pos)] = min(incl_curr_pos, not_incl_curr_pos, key= lambda x : len(x))
        memo[(target, curr_pos)].append(arr[curr_pos])
    elif incl_curr_pos != None:
        incl_curr_pos.append(arr[curr_pos])
        memo[(target, curr_pos)] = incl_curr_pos
    elif not_incl_curr_pos !=None:
        memo[(target, curr_pos)] = not_incl_curr_pos
    else:
        memo[(target, curr_pos)] = None

    return memo[(target, curr_pos)]




print(best_sub_seq([4, 3, 2, 7, 8, 15], 15 ))

