a = str(input(":::"))
l = 0
r = 0
sum = 0
i = 0

while i < len(a):
    if a[i] == '(' and r == 0:
        l += 1
        sum += 1
    elif a[i] == ')':
        r += 1
        sum += 1
    i += 1
    if l == r:
        l = 0
        r = 0
if l == r:
    print("можно")
else:
    print("нельзя")