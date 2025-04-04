# Sets are fast to check for membership (if n in seen)
# Perfect for detecting loops or repeated values

def is_looping_number(n):
    seen = set()

    while n != 1:
        if n in seen:
            return True  # Loop detected
        seen.add(n)

        # Replace n with the sum of the squares of its digits
        n = sum(int(digit)**2 for digit in str(n))

    return False  # Reached 1, so it's NOT a looping number