def alternate(nums):
    arr=[0]*len(nums)
    postive_index=0
    negative_index=1
    for num in nums:
        if num >=0:
            arr[postive_index]=num
            postive_index+=2
        else:
            arr[negative_index]=num
            negative_index+=2
    return arr

nums=[-2,-4,-5,3,24,5,-6,2]
print(alternate(nums))