def plusOne(digits):
    n = len(digits)


    sum = digits[n-1] + 1
    if sum < 10:
        digits[n-1] = sum
    else:
        for i in range(n-1, -1, -1):
            sum = digits[i] + 1
            carry = sum // 10
            digits[i] = sum % 10

            if carry == 0:
                break

        if carry:
            digits.insert(0, carry)

    print(digits)







digits = [9,9,9]
plusOne(digits)



