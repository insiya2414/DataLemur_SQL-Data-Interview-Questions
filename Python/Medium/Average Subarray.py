# A contiguous subarray is a sequence of elements that are next to each other in the array — meaning they appear without any gaps or skips.
# Think of it like taking a slice or chunk from the array where you don't rearrange or jump over elements.

def max_avg_subarray(nums, k):
    n = len(nums)
    
    # Step 1: Calculate the sum of the first 'k' elements
    window_sum = sum(nums[:k])
    max_sum = window_sum  # Initialize max_sum with this first sum
    
    # Step 2: Slide the window from left to right across the array
    for i in range(k, n):
        # Remove the element that goes out of the window
        # Add the new element that comes into the window
        window_sum += nums[i] - nums[i - k]
        
        # Update max_sum if this new window has a larger sum
        max_sum = max(max_sum, window_sum)
    
    # Step 3: Calculate average and round to 2 decimal places
    return round(max_sum / k, 2)
