from random import randint
def RandomMas(a,b):
    mas = []
    for i in range(0,a):
        mas.append([])
        for j in range(0,b):
            mas[i].append(randint(0,9))

    return mas

mas = RandomMas(10,10)
sum = 0

for i in mas:
    sum += max(i)

print(f"Сумма максимальных чисел в каждой строке : {sum}")

