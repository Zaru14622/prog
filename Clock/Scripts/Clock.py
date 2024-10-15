hours = int(input("hours: "))
if hours == 12:
    hours = 0
min = int(input("min: "))
if min == 60:
    min = 0
del_hours = hours
itteration = 1
while True:
    itteration += 1
    min += 1
    if min == 60:
        min = 0
        del_hours += 1
    if del_hours == 12:
        del_hours = 0
    if del_hours * 5 + min//12 == min:
        break



print(itteration)