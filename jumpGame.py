def jumpgame(nums):
    # First jump it would take the first value from index
    # a take the value and use it as index
    # Check if the value reach to the last index
    n = len(nums)
    max_reachable = 0

    for i in range(n):
        if i > max_reachable:
            return False

        max_reachable = max(max_reachable, i + nums)

        if max_reachable >= n-1:
            return True

    return False










