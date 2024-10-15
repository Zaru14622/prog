hours = int(input("Введите часы "))
min = int(input("Введите минуты"))
if hours == 12:
    hours = 0

hours_to_min = hours * 5

itteration = 0

while hours_to_min != min:
    itteration += 1
    min += 1
    if min == 60:
        min = 0
print(itteration)