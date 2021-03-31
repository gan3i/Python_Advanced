from collections import Counter, defaultdict
               
def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ''
    
    t_counter = Counter(t)
    required = len(t_counter)
    s_counter = defaultdict(int)
    left = 0
    right = 0
    ans = (float('inf'), None, None)
    equal_counts = 0
    
    while right < len(s):
        if s[right] not in t_counter:
            right +=1
            continue
        
        s_counter[s[right]] +=1
        if s_counter[s[right]] == t_counter[s[right]]:
            equal_counts +=1
            
        while equal_counts == required:
            if s[left] not in t_counter:
                left +=1
                continue
            window_width = right - left
            if window_width < ans[0]:
                ans = (window_width, left, right+1) 
                
            s_counter[s[left]] -=1
            
            if s_counter[s[left]] < t_counter[s[left]]:
                equal_counts -=1
            left +=1
            
        right +=1
    
    if ans[0] == float('inf'):
        return ''
    return s[ans[1]:ans[2]]

s = "aa"
t = "aa"    
print(minWindow(s, t))