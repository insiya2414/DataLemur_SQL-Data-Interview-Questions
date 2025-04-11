def most_popular(nums, n):
    # Get the frequency of each number
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Initialize a list of empty lists, one for each possible frequency
    arr = [[] for _ in range(len(nums) + 1)]  

    # Append each number to the list at the index equal to its frequency
    for num in freq:
        arr[freq[num]].append(num)

    '''
    Start from the last index and collect numbers while ensuring 
    the limit is not exceeded
    '''
    ans = []
    for i in range(len(arr) - 1, -1, -1):
        for num in arr[i]:
            ans.append(num)
        if len(ans) == n:
        	break
    ans.sort()
    return ans