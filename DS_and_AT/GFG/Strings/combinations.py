



def combinations(nums, i ,results, path):

    if i ==len(nums):
        results.append(path)
        return
    
    curr_path = []
    for j in range(len(path)):
        curr_path.append(path[j])
    curr_path.append(nums[i])

    combinations(nums,i+1,results,path)
    combinations(nums, i+1, results, curr_path)

s = 'ABC'

results = []
path = []

combinations(s, 0,results,path)

print(results)