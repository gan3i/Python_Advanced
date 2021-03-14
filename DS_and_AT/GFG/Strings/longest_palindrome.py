class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        
        if A == None or len(A) == 0:
            return

        r = len(A)
        
        pal= A[0]
        
        i = 1
        while i < r:

            left = self.getPalLength(A,i,i)
            right = self.getPalLength(A,i-1,i)
            
            if left > right and left > len(pal):
                pal = A[i-left//2:i+left//2]
            elif right > len(pal):
                pal = A[i-right//2:i+(right)//2]
            
            i += 1

            
        return pal
            
    def getPalLength(self, A, left, right):
        
        while left >=0 and right<len(A):
            if A[left].lower() != A[right].lower():
                break

            left -=1
            right +=1
        
        return right - left - 1
        
        
s = Solution()
print(s.longestPalindrome("abb"))