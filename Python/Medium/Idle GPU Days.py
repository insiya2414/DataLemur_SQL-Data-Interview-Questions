def gpu_idle_days(days, training_sessions):
    # Step 1: Sort the intervals
    training_sessions.sort()
    
    # Step 2: Merge overlapping intervals
    merged_sessions = []
    start, end = training_sessions[0]
    
    for s, e in training_sessions:
        if start <= s <= end:  # Overlap detected
            end = max(end, e)  # Merge by extending the interval
        else:
            merged_sessions.append([start, end])
            start, end = s, e
    
    # Don't forget to add the last interval
    merged_sessions.append([start, end])
    
    # Step 3: Calculate total days the GPUs are in use
    total_used_days = 0
    for s, e in merged_sessions:
        total_used_days += (e - s + 1)
    
    # Step 4: Subtract total used days from total available days
    return days - total_used_days
    