
def selection_sort(nums):
    ln = len(nums)

    for i in range(ln):
        min_index = i
        for j in range(i+1,ln):
            if nums[min_index] > nums[j]:
                min_index = j
        if min_index == i:
            continue
        nums[i],nums[min_index] =nums[min_index],nums[i]

nums = [6,4,5,1,3,2,2]
selection_sort(nums)
print(nums)
