def search(matrix, x):
    # Write your code here.
    # print(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if x == matrix[i][j]:
                return [i,j]
    return [-1,-1]