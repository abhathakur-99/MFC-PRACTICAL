import numpy as np

def minor(mat, i, j):
    return np.delete(np.delete(mat, i, axis=0), j, axis=1)

def cofactor_matrix(mat):
    n = mat.shape[0]
    cof = np.zeros_like(mat, dtype=float)
    for i in range(n):
        for j in range(n):
            minor_det = np.linalg.det(minor(mat, i, j))
            cof[i, j] = ((-1) ** (i + j)) * minor_det
    return cof

def pretty_print(mat):
    if np.allclose(mat, mat.astype(int)):
        print(mat.astype(int))
    else:
        print(mat)

def main():
    n = int(input("Enter the size of the square matrix: "))
    print(f"Enter {n * n} elements separated by space:")
    elements = list(map(float, input().split()))
    if len(elements) != n * n:
        print("Incorrect number of elements entered.")
        return
    mat = np.array(elements).reshape(n, n)

    det = np.linalg.det(mat)
    print("Matrix:")
    pretty_print(mat)
    print("Determinant:", int(det) if np.isclose(det, int(det)) else det)

    cof = cofactor_matrix(mat)
    print("Cofactor matrix:")
    pretty_print(cof)

    adjoint = cof.T
    print("Adjoint matrix:")
    pretty_print(adjoint)

    if abs(det) > 1e-12:
        inv = np.linalg.inv(mat)
        print("Inverse matrix:")
        pretty_print(inv)
    else:
        print("Matrix is singular; inverse does not exist.")

main()
