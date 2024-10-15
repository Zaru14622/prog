from random import randint

def RanMas():
    mas = []
    for i in range(1,11):
        mas.append(randint(0,9))
    return mas

mas = RanMas()
MaxInd = 0
MinInd = 0
max = mas[0]
min = mas[0]

i = 0
while i < len(mas):
    if mas[i] > max:
        max = mas[i]
        MaxInd = i
    if mas[i] < min:
        min = mas[i]
        MinInd = i
    i += 1
print(f"Изначальный список: {mas}")
mas[MaxInd] = min
mas[MinInd] = max
print(f"Изменённый список: {mas}")
