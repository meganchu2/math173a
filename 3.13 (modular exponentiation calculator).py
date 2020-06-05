# Megan Chu
# MATH 173A
# Exercise 3.13
# modular exponentiation calculator
# 7/31/18

import math

# a is the base
a = 732959706

# b is the exponent
b = 496549570#1393020501

# N is the modular value
N = 1889570071

ans = 1

highexp = -1
while b >= math.pow(2,highexp+1):
    highexp += 1

exp = list()
exp.append(a)
for i in range(1,highexp+1):
    exp.append((math.pow(exp[len(exp)-1],2))%N)
    
temp = b
while highexp >= 0:
    if temp - math.pow(2,highexp) >= 0:
        ans = (ans*exp[highexp])%N
        temp -= math.pow(2,highexp)
    highexp -= 1

print(str(a)+"^"+str(b)+" congruent to "+str(ans)+" (mod "+str(N)+")")
print(65934508*740914441-1889570071*25853409)
