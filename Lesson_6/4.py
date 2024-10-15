from random import randint

def RanMas():
    mas = []
    for i in range(1,11):
        mas.append(randint(0,9))
    return mas

mas = RanMas()
DopMas = RanMas()

i = 0
while i < len(mas):
    DopMas[i] = mas[i+1]
    DopMas[i+1] = mas[i]
    i += 2
print(f"Изначальный список: {mas}")
print(f"Изменённый список: {DopMas}")
