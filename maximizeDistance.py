def maxDistToClosest(seats):
    n = len(seats)
    print(f'n (total seats): {n}')

    prev = -1  # Position of the last occupied seat
    print(f'Initial prev: {prev}')

    maxDist = 0  # Maximum distance
    print(f'Initial maxDist: {maxDist}')

    for i in range(n):
        print(f'\nChecking seat {i}, Value: {seats[i]}')
        if seats[i] == 1:
            if prev == -1:
                maxDist = i
                print(f'First occupied seat at {i}, maxDist updated to: {maxDist}')
            else:
                maxDist = max(maxDist, (i - prev) // 2)
                print(f'Occupied seat found at {i}, Distance to prev occupied ({prev}): {(i - prev) // 2}, maxDist updated to: {maxDist}')
            prev = i
            print(f'Prev updated to: {prev}')

    if seats[n-1] == 0:
        maxDist = max(maxDist, n - 1 - prev)
        print(f'\nLast seat empty, Distance to last occupied from end: {n - 1 - prev}, maxDist updated to: {maxDist}')

    print(f'\nFinal maxDist: {maxDist}')
    return maxDist

# Example usage
seats = [1, 0, 0, 0, 1, 0, 1]
maxDistToClosest(seats)




