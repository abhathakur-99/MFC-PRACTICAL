import numpy as np

def row_echelon(A):
    A = A.astype(float)
    r, c = A.shape
    row = 0
    for col in range(c):
        if row >= r:
            break
        max_r = np.argmax(abs(A[row:, col])) + row
        if A[max_r, col] == 0:
            continue
        if max_r != row:
            A[[row, max_r]] = A[[max_r, row]]
        A[row] = A[row] / A[row, col]
        for rr in range(row+1, r):
            A[rr] -= A[rr, col]*A[row]
        row += 1
    return A

def get_matrix_input():
    while True:
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            if rows <= 0 or cols <= 0:
                print("Rows and columns must be positive integers.")
                continue
            print(f"Enter {rows*cols} matrix elements separated by spaces:")
            entries = list(map(float, input().strip().split()))
            if len(entries) != rows*cols:
                print(f"Please enter exactly {rows*cols} elements.")
                continue
            matrix = np.array(entries).reshape(rows, cols)
            return matrix
        except ValueError:
            print("Invalid input. Please enter numeric values only.")

matrix = get_matrix_input()
echelon = row_echelon(matrix.copy())
rank = np.linalg.matrix_rank(matrix)

print("\nRow Echelon Form:")
print(echelon)
print("\nRank of the matrix:", rank)
