def subsets(nums):
    result =[]
    def generate(index,current):
        if (index==len(nums)):
            result.append(current.copy())
            return 

        generate(index+1,current)

        current.append(nums[index])
        generate(index+1,current)

        current.pop()

    generate(0,[])
    return result

print(subsets([1,2,3]))