def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[i]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))