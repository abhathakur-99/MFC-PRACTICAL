import sympy as sp

# Step 1: Define the variables
x, y, z = sp.symbols('x y z')

# Step 2: Take user input for vector field components
print("Enter the components of the vector field F = (P, Q, R):")
P = sp.sympify(input("Enter P(x, y, z): "))
Q = sp.sympify(input("Enter Q(x, y, z): "))
R = sp.sympify(input("Enter R(x, y, z): "))

# Step 3: Compute divergence
div_F = sp.diff(P, x) + sp.diff(Q, y) + sp.diff(R, z)

# Step 4: Display results
print("\nVector field F = (P, Q, R):")
sp.pprint([P, Q, R])

print("\nDivergence of F (∇·F):")
sp.pprint(div_F)

# Optional: Evaluate at a point
choice = input("\nDo you want to evaluate divergence at a specific point? (y/n): ")
if choice.lower() == 'y':
    x0 = float(input("Enter x = "))
    y0 = float(input("Enter y = "))
    z0 = float(input("Enter z = "))
    div_value = div_F.subs({x: x0, y: y0, z: z0})
    print(f"\nDivergence at ({x0}, {y0}, {z0}) = {div_value}")
