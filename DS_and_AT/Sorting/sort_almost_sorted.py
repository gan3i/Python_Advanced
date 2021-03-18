from heapq import heapify, heappop, heappush

def sort_array(nums, n, k):
	if not nums or not n or not k:
		return nums
	
	target_index , current_index, heap= 0, 0 , [ ]
	while current_index <= k:
		heap.append(nums[current_index])
		current_index +=1
	
	heapify(heap)
	
	while current_index < n:
		nums[target_index] = heappop(heap)
		heappush(heap, nums[current_index])
		current_index +=1
		target_index +=1

	while heap:
		nums[target_index] = heappop(heap)
		target_index +=1

	return nums

print(sort_array(None,0,0))