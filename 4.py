import numpy as np

def gauss_elimination(A, b):
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)

    # Forward elimination
    for i in range(n):
        # Partial pivoting
        max_row = np.argmax(abs(A[i:, i])) + i
        if A[max_row, i] == 0:
            continue
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
        # Eliminate below
        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    # Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        if A[i, i] == 0:
            if np.isclose(b[i], 0):
                x[i] = 0  # Free variable; here chosen as zero
            else:
                raise ValueError("No solution")
        else:
            x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x

def main():
    n = int(input("Enter number of variables: "))
    print(f"Enter the {n*n} coefficients row-wise (space-separated):")
    elements = list(map(float, input().split()))
    if len(elements) != n*n:
        print("Incorrect number of coefficients.")
        return
    A = np.array(elements).reshape(n, n)

    print("Is the system homogeneous? (y/n): ")
    hom_flag = input().lower()

    if hom_flag == 'y':
        b = np.zeros(n)
    else:
        print(f"Enter {n} constants (space-separated):")
        b_elements = list(map(float, input().split()))
        if len(b_elements) != n:
            print("Incorrect number of constants.")
            return
        b = np.array(b_elements)

    try:
        solution = gauss_elimination(A.copy(), b.copy())
        print("Solution (one possible if free variables present):")
        print(solution.astype(int) if np.allclose(solution, solution.astype(int)) else solution)
    except ValueError as e:
        print(e)

main()
