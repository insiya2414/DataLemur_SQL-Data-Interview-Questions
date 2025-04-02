def to_base_13(num):
    if num == 0:
        return "0"

    digits = "0123456789ABC"
    result = ""
    is_negative = num < 0  # Check if the number is negative
    num = abs(num)  # Work with the absolute value

    while num > 0:
        remainder = num % 13
        result = digits[remainder] + result
        num //= 13

    return "-" + result if is_negative else result  # Add '-' if the number was negative

