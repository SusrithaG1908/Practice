def equilibrium_index(nums):
    left = 0
    total = sum(nums)

    for i in range(len(nums)):
        right = total - left - nums[i]
        if left==right:
            return i
        left+=nums[i]

    return -1

print(equilibrium_index([1, 3, 5, 2, 2]))