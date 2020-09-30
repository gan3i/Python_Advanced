



def combinations(nums, i ,results, path):

    if i ==2:
        results.append(path)
        return
    
    curr_path = []
    for j in range(len(path)):
        curr_path.append(path[j])
    curr_path.append(nums[i])

    combinations(nums,i+1,results,path) # path without current elememt
    combinations(nums, i+1, results, curr_path) # with Current element

s = 'ABC'

results = []
path = []

combinations(s, 0,results,path)

print(results)