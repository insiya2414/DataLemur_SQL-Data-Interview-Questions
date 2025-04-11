def sorted_two_sum(nums, target):
  left = 0
  right = len(nums)-1

  # Start at opposite ends
  # When the pointers meet, you have considered all options
  while right > left:
    cur_sum = nums[left] + nums[right]
    '''
    cur_sum is the greatest possible sum including left
    and the smallest possible sum including right
    '''
    if cur_sum == target:
      return [left, right]

    elif cur_sum < target:
      '''
      Highest possible sum including left is still less than target. 
      Therefore, eliminate left from consideration
      '''
      left = left+1
    elif cur_sum > target:
      '''
      Lowest possible sum including right is still greater than target. 
      therefore, eliminate nums[right] from consideration
      '''
      right = right-1

  return [-1,-1]