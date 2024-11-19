from random import randint
s = [randint(0,9) for n in range(0,10)]
print(s)
print("*"*30)
m = set()
for i in range(0,len(s)):
    if i%2!=0:
        m.add(s[i]**2)
    else:
        m.add(s[i]*2)
print(m)