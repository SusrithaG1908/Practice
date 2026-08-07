def replaceElements(arr):
    n=len(arr)
    max_right=arr[-1]
    arr[-1]=-1
    for i in range(n-2,-1,-1):
        temp=arr[i]
        arr[i]=max_right
        max_right=max(temp,max_right)
    return arr

print(replaceElements([17,18,5,4,6,1]))