def missingNumber(nums):
    n = len(nums)
    nums.sort()
    if n == 1 and nums[n-1] != 0:
        return 0

    for i in range(n):
        if nums[i] != i:
            return i

nums = [0,1]

print(missingNumber(nums))