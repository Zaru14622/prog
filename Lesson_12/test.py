from random import randint

m = [[[randint(0, 9) for j in range(0, 10)] for j in range(0, 10)] for j in range(0, 10)]
for i in m:
    print(i)