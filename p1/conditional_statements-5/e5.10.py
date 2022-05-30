#E-5.9: Solving a quadratic equation

#Problem: Please write a program for solving a quadratic equation of the form ax²+bx+c.
#The program asks for values a, b and c.
#It should then use the quadratic formula to solve the equation.
#The quadratic formula expressed with the Python sqrt function is as follows:

#x = (-b ± sqrt(b²-4ac))/(2a).

#You can assume the equation will always have two real roots,
#so the above formula will always work.

#An example of expected behaviour:

#Value of a: 1
#Value of b: 2
#Value of c: -8

#The roots are 2.0 and -4.0

#Solution:

from math import sqrt
import cmath


v1 = int(input("Value of a:"))
v2 = int(input("Value of b:"))
v3 = int(input("Value of c:"))
a = v1
b = v2
c = v3
d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("The roots are", sol1, "and", sol2)
