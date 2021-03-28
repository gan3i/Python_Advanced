

def get_unique_ss_count(word):
    if not word:
        return 0
    ss_set = set()
    return ss_count_helper(word, [], 0, ss_set)
    return ss_set

def ss_count_helper(word, partial_ss, curr_pos, ss_set):
    if curr_pos == len(word):
        curr_ss = ''.join(partial_ss)
        if curr_ss in ss_set:
            return 0
        else:
            ss_set.add(''.join(curr_ss))
            return 1
    partial_ss.append(word[curr_pos])
    taken = ss_count_helper(word, partial_ss, curr_pos+1, ss_set)
    partial_ss.pop()
    not_taken = ss_count_helper(word, partial_ss, curr_pos+1, ss_set)
    return taken + not_taken

def get_unique_ss_count_dp(word):
    if not word:
        return 0
    n  = len(word)
    char_count = dict()
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n+1):
        char = word[i-1]
        dp[i] = 2 * dp[i-1]
        if char in char_count:
            dp[i] -= dp[char_count[char]]
        char_count[char] = i - 1
    return dp[n]

print(get_unique_ss_count_dp("gfgffdfgfggbdf"))
print(get_unique_ss_count("gfgffdfgfggbdf"))