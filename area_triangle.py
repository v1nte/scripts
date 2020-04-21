from math import sqrt
from sys import argv 

a, b, c = argv[1], argv[2], argv[3]
float(a), float(b), float(c)

s = float(a+b+c)*0.5
area = (s*(s-a)*(s-b)*(s-c))

print("Area: ",sqrt(area))