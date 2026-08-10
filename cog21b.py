def subsets(nums):
    result=[]
    n=len(nums)

    for mask in range(2 ** n):
        current=[]
        for i in range(n):
            if mask & (1<<i):
                current.append(nums[i])

        result.append(current)

    return result

print(subsets([1,2,3]))
