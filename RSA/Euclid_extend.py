import math
import random as rd

e = 6 + 2 * 10

p = q = 0
T = 0
while(T == 0):
    rd.seed(1234)
    t = rd.randint(10E20, 10E30)
    if(math.gcd(e,t) == 1):
        T = t

print(T)
