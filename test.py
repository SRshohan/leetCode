def threeSum(nums):
    nums.sort()  # Sorting the array
    print(f"Sorted nums: {nums}")
    tripletArr = []

    for i in range(len(nums) - 2):
        # Skip duplicate values for the current element
        if i > 0 and nums[i] == nums[i - 1]:
            print(f"Skipping duplicate for i={i}, nums[i]={nums[i]}")
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            print(f"Checking triplet: {nums[i]}, {nums[left]}, {nums[right]}, total: {total}")

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                tripletArr.append([nums[i], nums[left], nums[right]])
                print(f"Found triplet: {nums[i]}, {nums[left]}, {nums[right]}")
                left += 1
                right -= 1

                # Skip duplicate values to avoid duplicate triplets in the result
                while left < right and nums[left] == nums[left - 1]:
                    print(f"Skipping duplicate left= {left}, nums[left]={nums[left]}")
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    print(f"Skipping duplicate right= {right}, nums[right]={nums[right]}")
                    right -= 1

    return tripletArr

nums = [-1, 0, 1, -1, 2]
print(threeSum(nums))


