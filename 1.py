import numpy as np

# Example complex matrix
matrix = np.array([[1.+0.j, 2.+0.j], [2.+0.j, 2.+0.j]])

# Remove imaginary part, convert to integers
matrix_int = matrix.real.astype(int)

print("Original matrix:\n", matrix_int)
print("Transpose:\n", matrix_int.T)
print("Conjugate Transpose:\n", matrix_int.T)  # Same as transpose for real numbers
