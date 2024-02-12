def plusOne(digits):
    n = len(digits)

    # Start from the last digit and work backwards
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            # If the current digit is less than 9, just add one and return
            digits[i] += 1
            return digits
        else:
            # If the current digit is 9, it becomes 0 and we carry over to the next digit
            digits[i] = 0

    # If all digits were 9, we need to add a new digit at the beginning
    return [1] + digits


# Example usage:
digits = [4, 3, 2, 1]
print(plusOne(digits))  # Output: [4,3,2,2]

# Another example with carries:
digits = [9, 9, 9]
print(plusOne(digits))  # Output: [1,0,0,0]

