import sympy as sp

# Step 1: Define the variables
x, y, z = sp.symbols('x y z')

# Step 2: Take user input for scalar field
expr_input = input("Enter a scalar field f(x, y, z): ")
f = sp.sympify(expr_input)

# Step 3: Compute gradient
grad_f = [sp.diff(f, var) for var in (x, y, z)]

# Step 4: Display result
print("\nScalar field f(x, y, z):")
sp.pprint(f)

print("\nGradient of f:")
sp.pprint(grad_f)

# Optional: Substitute a point to evaluate the gradient numerically
choice = input("\nDo you want to evaluate at a specific point? (y/n): ")
if choice.lower() == 'y':
    x0 = float(input("Enter x = "))
    y0 = float(input("Enter y = "))
    z0 = float(input("Enter z = "))
    grad_value = [g.subs({x: x0, y: y0, z: z0}) for g in grad_f]
    print(f"\nGradient at ({x0}, {y0}, {z0}): {grad_value}")
