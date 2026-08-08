def missingNum(nums):
    n=len(nums)
    freq={}
    for num in nums:
        freq[num]= freq.get(num,0)+1
        if freq[num]==2:
            repeating_num = num
    print(freq)
    missing_num = -1
    for i in range(1,n+1):
        if i not in freq:
            missingNum = i
    return repeating_num, missingNum

nums=[1,2,3,4,5,6,8,8]
print(missingNum(nums))
