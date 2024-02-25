def singleNumber(nums):
    return 2*sum(set(nums)) - sum(nums)

nums = [1,0,1]

print(singleNumber(nums))

