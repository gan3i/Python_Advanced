

def merge_sort(nums):
    if len(nums)>1:
        m = len(nums)//2
        lnums = nums[:m]  #left sub array
        rnums = nums[m:]  #right sub array

        merge_sort(lnums) 
        merge_sort(rnums)
        
        i = j = k = 0
        # copy arrays to temp arrays lnums[] and rnums[]
        while i < len(lnums) and j <  len(rnums):
            if lnums[i] < rnums[j] :
                nums[k] = lnums[i]
                i +=1
            else :
                nums[k] = rnums[j]
                j += 1
            k +=1
        while i < len(lnums):
            nums[k] = lnums[i]
            i +=1
            k  +=1
        while j < len(rnums):
            nums[k] = rnums[j]
            j +=1
            k  +=1


nums  = [35,10,4,5,40,2,1,3,3]
print(nums)
merge_sort(nums)
print(nums)



