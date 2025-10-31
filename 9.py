import numpy as np

# Step 1: Take user input
n = int(input("Enter the size of the square matrix (n x n): "))

print("Enter the matrix row by row:")
A = []
for i in range(n):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    A.append(row)

A = np.array(A)
print("\nMatrix A:")
print(A)

# Step 2: Eigenvalues and Eigenvectors
eigvals, eigvecs = np.linalg.eig(A)
print("\nEigenvalues:")
print(eigvals)
print("\nEigenvectors (columns):")
print(eigvecs)

# Step 3: Check if matrix is diagonalizable
# A is diagonalizable if there are n linearly independent eigenvectors
rank_eigvecs = np.linalg.matrix_rank(eigvecs)
if rank_eigvecs == n:
    print("\n✅ The matrix is diagonalizable.")
else:
    print("\n❌ The matrix is NOT diagonalizable.")

# Step 4: Verify Cayley–Hamilton Theorem
# Compute the characteristic polynomial and substitute A
char_poly = np.poly(A)  # returns coefficients of det(λI - A)
print("\nCharacteristic polynomial coefficients (λ^n ... constant):")
print(char_poly)

# Verify P(A) = 0
P_A = np.zeros_like(A, dtype=float)
for i in range(len(char_poly)):
    P_A += char_poly[i] * np.linalg.matrix_power(A, n - i)

print("\nP(A) (should be close to zero matrix):")
print(np.round(P_A, 5))

if np.allclose(P_A, np.zeros_like(A)):
    print("\n✅ Cayley–Hamilton theorem is verified: P(A) = 0")
else:
    print("\n❌ Cayley–Hamilton theorem is NOT satisfied (numerical error possible).")
