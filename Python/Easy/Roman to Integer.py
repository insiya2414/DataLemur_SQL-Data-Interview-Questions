def romanToInt(s: str) -> int:
    # Mapping of Roman numerals to their integer values
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0

    for i in range(len(s)):
        current_value = roman_map[s[i]]

        if i + 1 < len(s) and current_value < roman_map[s[i + 1]]:
            total -= current_value
        else:
            total += current_value

    return total

    