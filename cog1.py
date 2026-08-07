def maxProfit_stocks(arr):
    maxProfit=0
    n=len(arr)
    l=0
    r=1
    while r<n:
        if arr[l]<arr[r]:
            profit=arr[r]-arr[l]
            maxProfit=max(maxProfit,profit)
        else:
            l=r
        r+=1
    return maxProfit


arr=[7,1,5,3,6,4]
print(maxProfit_stocks(arr))
