def min_amplitude(arr):
    if len(arr) < 5:
        return 0
    arr.sort()
    
    # Four cases to minimize amplitude
    # Change the three smallest numbers
    case_1 = arr[-1] - arr[3]
    # Change the two smallest and the largest number
    case_2 = arr[-2] - arr[2]  
    # Change the smallest and two largest numbers
    case_3 = arr[-3] - arr[1]  
    # Change the three largest numbers
    case_4 = arr[-4] - arr[0]  

    # Return the smallest amplitude from the four cases
    return min(case_1, case_2, case_3, case_4)
    