from random import randint

def RanMas():
    mas = []
    for i in range(1,11):
        mas.append(randint(0,9))
    return mas

mas = RanMas()
RevertMas = []
i = 0
while i < len(mas):
    RevertMas.append(mas[len(mas) - 1 - i])
    i += 1

print(f"Изначальный список: {mas}")
print(f"Изменённый список: {RevertMas}")
