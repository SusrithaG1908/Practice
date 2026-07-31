def union(n, m, arr1, arr2):
    res = []
    i = 0
    j = 0

    while i < n and j < m:

        if arr1[i] < arr2[j]:
            if len(res) == 0 or res[-1] != arr1[i]:
                res.append(arr1[i])
            i += 1

        elif arr1[i] > arr2[j]:
            if len(res) == 0 or res[-1] != arr2[j]:
                res.append(arr2[j])
            j += 1

        else:
            if len(res) == 0 or res[-1] != arr1[i]:
                res.append(arr1[i])
            i += 1
            j += 1

    while i < n:
        if len(res) == 0 or res[-1] != arr1[i]:
            res.append(arr1[i])
        i += 1

    while j < m:
        if len(res) == 0 or res[-1] != arr2[j]:
            res.append(arr2[j])
        j += 1

    return res

n = 5
m = 5 
arr1 = [1,2,3,4,5]  
arr2 = [2,3,4,4,5]
print(union(n,m,arr1,arr2))