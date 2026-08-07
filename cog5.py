def maxSubarraySum(arr):
    maxSum=float('-inf')
    sum=0
    for num in nums:
        sum+=num
        maxSum=max(maxSum,sum)
        if sum<0:
            sum=0

    return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubarraySum(nums))