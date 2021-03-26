

def get_unique_ss_count(word):
    if not word:
        return 0
    ss_set = set()
    return ss_count_helper(word, [], 0, ss_set, dict())
    #return ss_set

def ss_count_helper(word, partial_ss, curr_pos, ss_set, memo):
    if curr_pos == len(word):
        curr_ss = ''.join(partial_ss)
        if curr_ss in ss_set:
            return 0
        else:
            ss_set.add(''.join(curr_ss))
            return 1
    if (''.join(partial_ss),curr_pos) in memo:
        return memo[(''.join(partial_ss),curr_pos)]
    partial_ss.append(word[curr_pos])
    taken = ss_count_helper(word, partial_ss, curr_pos+1, ss_set, memo)
    partial_ss.pop()
    not_taken = ss_count_helper(word, partial_ss, curr_pos+1, ss_set, memo)
    memo[(''.join(partial_ss),curr_pos)] = taken + not_taken
    return memo[(''.join(partial_ss),curr_pos)]

print(get_unique_ss_count("gfgffhhghfhfgfhghggg"))