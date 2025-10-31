import numpy as np

# Step 1: Take user input
n = int(input("Enter dimension of vectors (n): "))
m = int(input("Enter number of vectors: "))

vectors = []
for i in range(m):
    v = list(map(float, input(f"Enter vector {i+1} (space-separated {n} values): ").split()))
    vectors.append(v)

A = np.column_stack(vectors)

print("\nMatrix of vectors A:")
print(A)

# Step 2: Check linear dependence
rank = np.linalg.matrix_rank(A)
print("\nRank of A:", rank)
if rank < m:
    print("→ The vectors are linearly dependent.")
else:
    print("→ The vectors are linearly independent.")

# Step 3: Create a linear combination
coeffs = list(map(float, input(f"\nEnter {m} coefficients for linear combination: ").split()))
coeffs = np.array(coeffs)

combination = A @ coeffs
print("\nLinear combination =", combination)
