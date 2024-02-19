def powerOfTwo(n):
    while n != 0:
        if n == 1:
            return True
        if n % 2 == 0:
            n /= 2
        else:
            return False
    return True

n = 16

print(powerOfTwo(n))