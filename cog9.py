def twoSum_pairs(nums,target):
    ans=[]
    seen=set()
    for num in nums:
        complement=target-num
        if complement in seen:
            ans.append((complement,num))
        seen.add(num)
    return ans


nums = [2, 7, 11, 15, 3, 6]
target = 9
print(twoSum_pairs(nums,target))