# n x n matrix which is sqaure matrix
# Transpose the matrix
# Then reverse the row

# Big O(n^2) and space is 0(1)
def rotateImage(matrix):
    n = len(matrix)

    # Transpose, row becomes column and column becomes rows

    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # For reverse
    for i in range(n):
        matrix[i].reverse()
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotateImage(matrix))

