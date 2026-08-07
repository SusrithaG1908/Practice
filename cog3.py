def rotateArray(arr,k):
    k=k%len(arr)
    arr1=arr[-k:]
    arr2=arr[:-k]
    print(arr1)
    print(arr2)
    arr[:]=arr1+arr2
    return arr

print(rotateArray([1,2,3,4,5,6,7],3))