# Next Permutation
# For example, for arr = [1,2,3], the following are all the permutations of arr:
# [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]
# Input: nums = [1,2,3]
# Output: [1,3,2]
def nextPermu(nums):
    # Finding the last index 'k'
    k = -1
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            k = i

    if k == -1:
        nums.reverse()
        return nums

    # Find the largest Index 'l' Greater Than 'k'
    for j in range(len(nums) - 1, k, -1):
        if nums[j] > nums[k]:
            l = j
            break

    nums[k], nums[l] = nums[l], nums[k]

    nums[k+1:] = reversed(nums[k+1:])

    return nums

nums = [1, 2, 3]
print(nextPermu(nums))



