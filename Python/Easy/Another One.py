
def plus_one(digits):
    num = int("".join(map(str, digits)))  # Convert digits to an integer
    num += 1  # Add 1
    return list(map(int, str(num)))  # Convert back to a list of digits