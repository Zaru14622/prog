from random import randint
s1 = [randint(0,9) for n in range(0,10)]
s2 = [randint(0,9) for n in range(0,10)]
print(s1)
print(s2)
print("*"*30)
m = set(s1)
for i in s2:
    m.add(i)
print(m)