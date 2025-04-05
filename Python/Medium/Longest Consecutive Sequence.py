def consecutive_seq(nums):
  ans=0
  set_nums =set(nums)
  
  for num in nums:
    if num-1 not in set_nums:
      size=0
      curr= num
      while curr in set_nums:
        size +=1
        curr +=1
      ans= max(ans,size)
  return ans