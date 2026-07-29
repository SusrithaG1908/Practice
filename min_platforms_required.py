def min_platforms_required(arr,dep):
    arr.sort()
    dep.sort()
    n=len(arr)

    platforms =1
    result =1
    i=1
    j=0
    while i<n and j<n:
        if arr[i]<dep[j]:
            platforms+=1
            i+=1
        else:
            platforms-=1
            j+=1
        result = max(result,platforms)
    return result




arr = [900, 945, 955, 1100, 1500, 1800]
dep = [920, 1200, 1130, 1150, 1900, 2000]
print(min_platforms_required(arr,dep))