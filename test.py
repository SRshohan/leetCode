def jumpgame(nums):
    max_reachable = 0  # The farthest index that can be reached
    n = len(nums)

    for i in range(n):
        # If the current index is greater than the maximum reachable index, it's not possible to proceed
        if i > max_reachable:
            return False
        print(f"i : {i}")
        # Update the maximum reachable index
        max_reachable = max(max_reachable, i + nums[i])

        # Print the current index and the maximum reachable index
        print(f"Index: {i}, Max Reachable: {max_reachable}")

        # Check if the last index is reachable
        if max_reachable >= n - 1:
            return True

    return False  # The last index is not reachable


# Example usage:
nums = [3,2,1,0,4]
print(jumpgame(nums))  # Expected output: True, as the last index is reachable

