def maxSum_matrix(matrix):
    maxSum = float('-inf')
    rows=len(matrix)
    cols=len(matrix[0])
    for r in range(rows):
        sum=0
        for j in range(cols):
            sum+=matrix[r][j]
        maxSum=max(sum,maxSum)

    for c in range(cols):
        ans=0
        for j in range(rows):
            ans+=matrix[j][c]
        maxSum=max(ans,maxSum)
    return maxSum

matrix = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
print(maxSum_matrix(matrix))