# def max_two_sum(nums, k):
# 	return -1

# def max_two_sum(nums, k):
#   maxSum=0
#   for i in range(len(nums)):
#     if j in range(len(nums)+1):
#       maxSum= nums[i] + nums[j]
#       maxSum < k
      
#       return maxSum
#   return -1
      
def max_two_sum(nums, k):
  nums.sort()
  # initialize pointers
  left = 0
  right = len(nums)-1

  max_sum = -1
  
  while left < right:
    cur_sum = nums[left] + nums[right]
    if cur_sum >= k:
      right = right-1
    else:
      max_sum = max(cur_sum, max_sum)
      left = left+1
    
  return max_sum