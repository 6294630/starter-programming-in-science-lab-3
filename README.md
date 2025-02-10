# Programming in Science - Lab 3

This template repository is the starter project for Programming in Science Lab 3. Written in Python, and tested with Pytest.

### Question(s)

1. Write a function that converts polar coordinates (r,θ) to Cartesian coordinates (x,y) using the following formulas. Return the coordinates in a tuple and round the result with 5 decimal points:

![image](https://github.com/user-attachments/assets/ec53c19a-6f58-4766-a2d6-0d6e745a7056)

![image](https://github.com/user-attachments/assets/8795d139-912b-4129-9ffa-ff85b8cea833)

where angle θ (theta) is in radian.

2. Write a function that converts Cartesian coordinates (x,y) to polar coordinates (r,θ) using the following formulas. Return the coordinates in a tuple and round the result with 5 decimal points:

![image](https://github.com/user-attachments/assets/9f7bb532-77fc-4bca-9ef4-dc182f83a913)

![image](https://github.com/user-attachments/assets/a2dde9f1-b6b6-43a8-9080-8d16eab196d7)



3. Oscillatory motion is periodic motion that repeats itself over time, like a pendulum, a vibrating string, or a mass on a spring. In physics, it is often described using the equation: 

![image](https://github.com/user-attachments/assets/a0683e32-04c9-4fb0-b2ac-934b8c2dbf16)

   or 
   
![image](https://github.com/user-attachments/assets/2ad4c530-1651-419a-803b-1e736330e994)



Where, 

- `x` is the displacement at time `t`.  
- `A` is the amplitude (maximum displacement).  
- `𝜔` is the angular frequency (`𝜔 = 2𝜋𝑓`).  

And where,  

- `f` is the frequency.  
- `t` is the time in seconds.  
- `ϕ` is the phase shift.  


### Run Command

`pytest`


Hint: 
      Use math.pi instead of pi=3.14 and use math.sin() for sin function.  
