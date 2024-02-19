def removeElement(val, nums):
    # loop through the nums
    # when val and elements match, it would swap the elemnt
    # After

    n = 4
    count = 0


    for i in range(n):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1

        return count
