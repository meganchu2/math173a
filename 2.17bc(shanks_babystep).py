# Megan Chu
# MATH 173A
# Exercise 2.17bc
# shank's babystep giant step method
# 7/19/18

import math

# change variable values depending on problem
p = 3571
g = 650
h = 2213

# calculate list 1
list1 = list()
n = math.ceil(math.sqrt(p))
toAdd = 1
for i in range(0,n+1):
    list1.append(toAdd)
    toAdd = (toAdd*g)%p

# find g^(-n) for easy list 2 calculation
gnInv = g
for i in range(2, p-1-n+1):
    gnInv = (gnInv*g)%p

# calculate list2 and stop when find a match with list1
list2 = list()
toAdd = h
for i in range(0,n+1):
    list2.append(toAdd)
    if toAdd in list1:
        print("x = "+str(list1.index(toAdd)+i*n)+" is a solution to ", end="")
        print(str(g)+"^x conguent to "+str(h)+" in F"+str(p))
        break
    else:
        toAdd = (toAdd*gnInv)%p
