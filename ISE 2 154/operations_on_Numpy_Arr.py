
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("Addition:")
print(np.add(A,B))

print("Subtraction:")
print(A - B)

print("Element-wise Multiplication:")
print(A * B)

print("Matrix Multiplication:")
print(A @ B)
