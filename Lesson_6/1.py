from random import randint

def RanMas():
    mas = []
    for i in range(1,11):
        mas.append(randint(0,9))
    return mas

sumCh = 0
sumNCH = 0
mas = RanMas()

for i in mas:
    if i%2 == 0:
        sumCh += i
    else:
        sumNCH += i
print(f"Изначальный список: {mas}")
print(f"Сумма чётных чисел:{sumCh}")
print(f"Сумма нечётных чисел{sumNCH}")
