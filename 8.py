import numpy as np

# Step 1: Take user input
n = int(input("Enter dimension of vectors (n): "))
m = int(input("Enter number of vectors: "))

vectors = []
for i in range(m):
    v = list(map(float, input(f"Enter vector {i+1} (space-separated {n} values): ").split()))
    vectors.append(v)

A = np.array(vectors, dtype=float).T  # columns represent vectors

print("\nMatrix of vectors A:")
print(A)

# Step 2: Gram-Schmidt Orthogonalization
def gram_schmidt(A):
    n, m = A.shape
    Q = np.zeros((n, m))
    for j in range(m):
        v = A[:, j]
        for i in range(j):
            proj = np.dot(Q[:, i], A[:, j]) * Q[:, i]
            v = v - proj
        norm = np.linalg.norm(v)
        if norm == 0:
            print(f"\nVector {j+1} is linearly dependent on previous ones.")
            Q[:, j] = np.zeros(n)
        else:
            Q[:, j] = v / norm
    return Q

Q = gram_schmidt(A)

# Step 3: Display orthonormal basis
print("\nOrthonormal basis vectors (columns of Q):")
print(Q)

# Optional: Verify orthonormality
print("\nCheck QᵀQ (should be identity):")
print(np.round(Q.T @ Q, 3))
