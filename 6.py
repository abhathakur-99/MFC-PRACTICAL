import numpy as np
from scipy.linalg import lu, svd
from scipy.linalg import null_space

def basis_column_space(A):
    # Pivot columns of original matrix from LU or QR factorization can form basis
    # Using singular value decomposition to find rank and basis via left singular vectors
    U, S, Vh = svd(A)
    rank = np.sum(S > 1e-12)
    return U[:, :rank]

def basis_row_space(A):
    # Row space is column space of A transpose
    return basis_column_space(A.T)

def basis_null_space(A):
    # scipy.linalg.null_space returns orthonormal basis for null space
    return null_space(A)

def basis_left_null_space(A):
    # Left null space = null space of A transpose
    return null_space(A.T)

def pretty_print_basis(basis, name):
    print(f"\nBasis of {name} (each column is a basis vector):")
    if basis.size == 0:
        print("Zero subspace (only zero vector).")
    else:
        # Convert to integer vectors if possible for nicer display
        if np.allclose(basis, basis.astype(int)):
            print(basis.astype(int))
        else:
            print(np.round(basis, decimals=4))

def main():
    rows = int(input("Number of rows of the matrix: "))
    cols = int(input("Number of columns of the matrix: "))
    print(f"Enter {rows*cols} matrix elements row-wise separated by spaces:")
    entries = list(map(float, input().split()))
    if len(entries) != rows * cols:
        print("Incorrect number of elements.")
        return
    A = np.array(entries).reshape(rows, cols)

    col_basis = basis_column_space(A)
    row_basis = basis_row_space(A)
    null_basis = basis_null_space(A)
    left_null_basis = basis_left_null_space(A)

    pretty_print_basis(col_basis, "Column Space")
    pretty_print_basis(row_basis, "Row Space")
    pretty_print_basis(null_basis, "Null Space")
    pretty_print_basis(left_null_basis, "Left Null Space")

main()
