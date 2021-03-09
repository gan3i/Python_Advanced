class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def get_hash(s):
            r_hash = 0
            for i in range(len(s)):
                r_hash = (r_hash + ord(s[i]) * PRIME ** i) % mod
            return r_hash
        
        def get_rolling_hash(r_hash,start, end):
            return ((r_hash - ord(start))/PRIME) + (ord(end) * (PRIME ** (len(needle)-1))) % mod
                
            
        PRIME = 3
        needle_len = len(needle)
        hs_len = len(haystack)
        mod = 2 ** 31
        
        
        if not needle_len:
            return 0
        
        if needle_len > hs_len:
            return -1
        
        needle_hash = get_hash(needle)
        r_hash = get_hash(haystack[:len(needle)])
        start = 0
        end = len(needle)
        if needle_hash == r_hash and needle == haystack[start:end] :
            return start
        
        
        while end < len(haystack):
            r_hash = get_rolling_hash(r_hash, haystack[start], haystack[end])
            start +=1
            end +=1
            if needle_hash == r_hash and needle == haystack[start:end]:
                return start
            
        return -1
                
        
                
        
obj = Solution()

obj.strStr("ababcaababcaabc","ababcaabc")