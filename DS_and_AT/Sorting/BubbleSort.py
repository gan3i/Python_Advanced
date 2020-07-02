nums = [4,1,5,2,3,6,6,6]


def bubble_sort(nums):
    ln = len(nums)
    for _ in range(ln):
        for j in range(ln-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
bubble_sort(nums)
print(nums)