# Function 1 (30): Convert the given polar coordinates (r,θ) to Cartesian coordinates (x,y). 
# This function should take the polar coordinates (r,θ) and return Cartesian coordinates (x,y), where θ=theta.
import math
def polar_to_cartesian(r, θ):
    x = r * math.cos(math.radians(θ))
    y = r * math.sin(math.radians(θ))
    return (round(x, 5), round(y, 5))

# Function 2(30): Convert Cartesian coordinates (x,y) to polar coordinates (r,θ) , where θ=theta.
# This function should take the Cartesian coordinates (x,y) as input and return the polar coordinates (r,θ).
import math
def cartesian_to_polar(x, y):
    r = math.sqrt(x**2 + y**2)  
    θ = math.degrees(math.atan2(y, x)) 
    return (round(r, 5), round(θ, 5))

# Function 3 (40): Calculate the position of pendulum for (A, f, Φ, t), where Φ=phi.
# This function should take (A, f, Φ, t) as input and return the position value x=A*sin(2*π*f*t+Φ) .
import math
def calculate_position(A, f, Φ, t):
  Φ=math.radians(Φ)
  omega = 2 * math.pi * f  
  return A * math.sin(omega * t +Φ)
