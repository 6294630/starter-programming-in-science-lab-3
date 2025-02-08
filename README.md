# Programming in Science - Lab 3
This template repository is the starter project for Programming in Science Lab 3. Written in Python, and tested with Pytest.

1. Converting from polar coordinates (r,θ) to Cartesian coordinates (x,y) :

![image](https://github.com/user-attachments/assets/ec53c19a-6f58-4766-a2d6-0d6e745a7056)

![image](https://github.com/user-attachments/assets/8795d139-912b-4129-9ffa-ff85b8cea833)

where angle θ is in radian.

2. Converting from Cartesian coordinates (x,y) to polar coordinates (r,θ):

![image](https://github.com/user-attachments/assets/9f7bb532-77fc-4bca-9ef4-dc182f83a913)

![image](https://github.com/user-attachments/assets/a2dde9f1-b6b6-43a8-9080-8d16eab196d7)



3. Oscillatory motion is periodic motion that repeats itself over time, like a pendulum, a vibrating string, or a mass on a spring. In physics, it is often described using the equation: 

![image](https://github.com/user-attachments/assets/a0683e32-04c9-4fb0-b2ac-934b8c2dbf16)

   or 
   
![image](https://github.com/user-attachments/assets/2ad4c530-1651-419a-803b-1e736330e994)



Where:

x is the displacement at time t.

A is the amplitude (maximum displacement).

𝜔 is the angular frequency ( 𝜔 = 2𝜋𝑓), 

where 

f is the frequency.

t is the time in seconds.

ϕ is the phase shift.


### Question(s)

1. Convert polar coordinates (r,θ) to Cartesian coordinates (x,y) - write a Python function polar_to_cartesian(r,θ).

2. Convert Cartesian coordinates (x,y) to polar coordinates (r,θ) - write a Python function cartesian_to_polar(x,y).

3. Calculate the position of pendulum :  x=calculate_position(A, f, ϕ, t)
  
   ![image](https://github.com/user-attachments/assets/2ad4c530-1651-419a-803b-1e736330e994)

Example 1: polar_to_cartesian(5, math.pi/3)=(2.5, 4.33)     

Example 2: cartesian_to_polar(1, 1)=(1.41, 0.79)  

Example 3: calculate_position(10,1,1/4,0)=10


Hint: 
1. just programm the functions, do nothing extra.
2. Use math.pi instead of pi=3.14 and use math.sin() for sin function.  
