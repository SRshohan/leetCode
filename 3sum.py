def threeSum(nums):
    # Input: nums = [-1, 0, 1, 2, -1, -4]
    # Output: [[-1, -1, 2], [-1, 0, 1]]
    nums.sort()
    # [-4, -1, -1, 0, 1, 2]
    tripletArr = []



    for i in range(len(nums) - 2): # It needs to stop here because we need 3 numbers
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, len(nums) -1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                tripletArr.append([nums[i], nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left+1] and left < right:
                    left += 1
    return tripletArr



nums = [-1,0,1,2,-1,-4]

print(threeSum(nums))
