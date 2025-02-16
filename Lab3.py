# Function 1 (30): Convert the given polar coordinates (r,θ) to Cartesian coordinates (x,y). 
# This function should take the polar coordinates (r,θ) and return Cartesian coordinates (x,y), where θ=theta.
import math 
def polar_to_cartesian(r,θ):
    x = r * math.cos(math.radians(theta))
    y = r * math.sin(math.radians(theta))
    
    return (round(x, 5), round(y, 5))

# Function 2(30): Convert Cartesian coordinates (x,y) to polar coordinates (r,θ) , where θ=theta.
# This function should take the Cartesian coordinates (x,y) as input and return the polar coordinates (r,θ).
def cartesian_to_polar(x,y):
    # TODO: Implement this function
    pass  # Replace with your code

# Function 3 (40): Calculate the position of pendulum for (A, f, Φ, t), where Φ=phi.
# This function should take (A, f, Φ, t) as input and return the position value x=A*sin(2*π*f*t+Φ) .
def calculate_position(A, f, Φ, t):
    # TODO: Implement this function
    pass  # Replace with your code
