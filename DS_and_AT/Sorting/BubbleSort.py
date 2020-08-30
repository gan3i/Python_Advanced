nums = [4,1,5,2,3,6,6,6]
nums = [1,2,3,4,5]


def bubble_sort(nums):
    ln = len(nums)
    swap = True
    for _ in range(ln):
        if not swap:
            return
        swap = False
        print("hello")
        for j in range(ln-1):

            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                swap = True



bubble_sort(nums)
print(nums)