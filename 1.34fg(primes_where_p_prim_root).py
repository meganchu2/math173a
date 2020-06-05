# Megan Chu
# MATH 173A
# Exercise 1.34fg
# primes where p is primitive root
# 7/11/18

# change pr variable to test different primitive roots
pr = 4
p = list()
r = list()

# test for primeness of integers less than 100
for i in range(2,100):
    prime = 0
    for j in range(2,i):
        if i%j == 0:
            prime = 1
            break
    # if this number is a prime then test for primitive root
    if prime == 0:
        p.append(i)
        primitive = 0
        a = pr%i
        if a == 1 or pr >= i:
                primitive = 1
        else:
            for k in range(2,i-1):
                a = (a*pr)%i
                if a == 1:
                    primitive = 1
                    break
        if primitive == 0:
            r.append(i)

print("primes < 100: ")
for i in range(0,len(p)-1):
     print(p[i], end=", ")
print(str(p[len(p)-1]) + "}")
print("primes where " + str(pr) + " is a primitive root: {", end="")
if len(r) > 0:
    for i in range(0,len(r)-1):
         print(r[i], end=", ")
    print(str(r[len(r)-1]) + "}")
else:
    print("}")
