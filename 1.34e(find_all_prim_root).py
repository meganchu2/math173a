# Megan Chu
# MATH 173A
# Exercise 1.34e
# primitive root finding code
# 7/11/18


p = 229
r = list()

#run for 2 through p-1, all possible primitive roots
for i in range(2,p):
    primitive = 0
    
    # run for 1 through p-1, all possible powers of primitive
    # root not congruent to 1 mod p
    a = i
    for j in range(2,p-1):
        a = (a*i)%p
        if a == 1:
            primitive = 1
            break
    if primitive == 0:
        r.append(i)

print("number primitive roots mod " + str(p) + ": " + str(len(r)))
print("primitive roots: {", end="")
for i in range(0,len(r)-1):
     print(r[i], end=", ")
print(str(r[len(r)-1]) + "}")
