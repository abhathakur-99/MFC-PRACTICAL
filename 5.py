import numpy as np

def gauss_jordan_homogeneous(A):
    n = A.shape[0]
    # Augment with zero vector
    aug = np.hstack((A.astype(float), np.zeros((n,1))))
    
    row = 0
    for col in range(n):
        # Find pivot row
        pivot = None
        for r in range(row, n):
            if not np.isclose(aug[r, col], 0):
                pivot = r
                break
        if pivot is None:
            continue
        
        # Swap to top
        aug[[row, pivot]] = aug[[pivot, row]]
        
        # Normalize pivot row
        aug[row] = aug[row] / aug[row, col]
        
        # Eliminate other rows
        for r in range(n):
            if r != row and not np.isclose(aug[r, col], 0):
                aug[r] -= aug[r, col]*aug[row]
        row += 1
        if row == n:
            break
    
    # Identify free variables (columns without pivots)
    pivots = []
    for i in range(n):
        for j in range(n):
            if np.isclose(aug[i,j], 1):
                pivots.append(j)
                break
    free_vars = [j for j in range(n) if j not in pivots]
    
    print("Reduced Row Echelon Form (Augmented Matrix):")
    print(np.round(aug, decimals=4))
    
    if not free_vars:
        print("Only trivial solution (all zero vector).")
    else:
        print("Free variables:", free_vars)
        print("General solution:")
        for free_var in free_vars:
            sol = np.zeros(n)
            sol[free_var] = 1
            for i, pivot in enumerate(pivots):
                sol[pivot] = -aug[i, free_var]
            print(sol)

def main():
    n = int(input("Enter number of variables: "))
    print(f"Enter the {n*n} coefficients row-wise (space-separated):")
    elements = list(map(float, input().split()))
    if len(elements) != n*n:
        print("Incorrect number of coefficients.")
        return
    A = np.array(elements).reshape(n, n)
    gauss_jordan_homogeneous(A)

main()
