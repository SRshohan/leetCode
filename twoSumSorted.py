def hasTwoSumZero(a):
    n = len(a)
    j = 0

    if n == 1:
        return False

    for i in range(n):
        if (a[i] + a[j]) == 0:
            return True
        j += 1
    return False

a = [-3, 1, 3, 4]

print(hasTwoSumZero(a))