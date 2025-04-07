# this problem is based on the well-known "Rabbits in the Forest" problem from LeetCode

import math

def min_attendees(answers):
    frequency = {}
    attendance = 0
    
    # Count how many times each answer appears
    for ans in answers:
        if ans in frequency:
            frequency[ans] += 1
        else:
            frequency[ans] = 1
    
    for ans in frequency:
        # Calculate the number of full groups for this answer
        batches = math.ceil(frequency[ans] / (ans + 1))
        # Each group has ans + 1 people
        attendance += batches * (ans + 1)
    
    return attendance
    