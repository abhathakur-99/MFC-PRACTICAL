import sympy as sp

# Step 1: Define the variables
x, y, z = sp.symbols('x y z')

# Step 2: Take user input for vector field components
print("Enter the components of the vector field F = (P, Q, R):")
P = sp.sympify(input("Enter P(x, y, z): "))
Q = sp.sympify(input("Enter Q(x, y, z): "))
R = sp.sympify(input("Enter R(x, y, z): "))

# Step 3: Compute Curl (∇ × F)
curl_x = sp.diff(R, y) - sp.diff(Q, z)
curl_y = sp.diff(P, z) - sp.diff(R, x)
curl_z = sp.diff(Q, x) - sp.diff(P, y)
curl_F = (curl_x, curl_y, curl_z)

# Step 4: Display result
print("\nVector field F = (P, Q, R):")
sp.pprint([P, Q, R])

print("\nCurl of F (∇ × F):")
sp.pprint(curl_F)

# Optional: Evaluate at a point
choice = input("\nDo you want to evaluate the curl at a specific point? (y/n): ")
if choice.lower() == 'y':
    x0 = float(input("Enter x = "))
    y0 = float(input("Enter y = "))
    z0 = float(input("Enter z = "))
    curl_value = [c.subs({x: x0, y: y0, z: z0}) for c in curl_F]
    print(f"\nCurl at ({x0}, {y0}, {z0}) = {curl_value}")
