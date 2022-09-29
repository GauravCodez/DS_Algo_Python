# Given an image represented by N X N matrix, write a method to rotate the image by 90 degrees
# Asked in interviews by companies such as Google, Facebook, Apple and Microsoft
"""
1 2 3                     7 4 1
4 5 6         ======>     8 5 2
7 8 9                     9 6 3

"""

import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Matrix : ")
print(arr1)


def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            # Saving the top element
            top = matrix[layer][i]
            # Move the left element to top
            matrix[layer][i] = matrix[-i-1][layer]
            # Move bottom element to the left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            # Move right to bottom
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            # Move to the right
            matrix[i][-layer-1] = top

    return matrix


print("90 degree rotated matrix : ")
print(rotate_matrix(arr1))
