def singleNum(nums):
    return (3 * sum(set(nums)) - sum(nums)) // 2


nums = [2,2,3,2]

print(singleNum(nums))