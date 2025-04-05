def triangular_sum(nums):
    while len(nums)>1:
        next_nums = []
        for i in range(1,len(nums)):
            next_nums.append((nums[i-1]+nums[i])%10)
        nums = next_nums
    return nums[0]