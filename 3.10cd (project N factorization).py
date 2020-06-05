# Megan Chu
# MATH 173A
# Exercise 3.10cd
# N factorization trial and error
# 7/19/18

import math

# change variable values depending on problem
gcd = 129112350
N = 1291233941

a = 1
b = 0
c = N
ration = 0
boolean = 1
i = math.floor(N/gcd)+1# account for decrement at start of while loop

# try increasing i until we find integer p and q
while boolean == 1 and i > 0:
    i -= 1
    b = N+1-gcd*i
    ration = math.pow(b,2)-4*a*c
    
    # check if 4b-ac is a perfect square
    if math.sqrt(ration) == math.floor(math.sqrt(ration)) or \
       math.sqrt(ration) == math.ceil(math.sqrt(ration)):

        # check if quadratic formula gives integer p and q
        if (b+math.sqrt(ration))/2 == math.floor((b+math.sqrt(ration))/2) or \
           (b+math.sqrt(ration))/2 == math.ceil((b+math.sqrt(ration))/2):
            boolean = 0

if i == 0:
    print("Error p and q not found!")
    exit()

print("gcd = "+str(gcd))
print("N = "+str(N))
print()
print("i = "+str(i))
print("p+q = "+str(b))
print("b-4ac = "+str(int(ration)))
print("p and q are "+str(int((b-math.sqrt(ration))/2))+", "\
      +str(int((b+math.sqrt(ration))/2)))
print("Check: "+str(int((b-math.sqrt(ration))/2))+"*"\
      +str(int((b+math.sqrt(ration))/2))+" = "\
      +str(int((b-math.sqrt(ration))/2)*int((b+math.sqrt(ration))/2)))
