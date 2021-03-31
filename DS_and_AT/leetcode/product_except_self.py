class Solution:
    def productExceptSelf(self, nums) :
        
        if not nums or len(nums) < 2:
            return nums
            
        n = len(nums)
        result = [0] * n
        result[0] = nums[0]
        
        for i in range(1, n):
            result[i] = result[i-1] * nums[i]
            
        right_prod = 1 
        
        for i in range(n-1, -1, -1):
            if i == 0:
                result[i] = right_prod
            else:
                result[i] = result[i-1] * right_prod
                right_prod = right_prod * nums[i]
            
        return result
        
        