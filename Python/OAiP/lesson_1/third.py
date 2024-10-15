from math import sqrt
a = int(input("Введите коофицент: a "))
b = int(input("Введите коофицент: b "))
c = int(input("Введите коофицент: c "))

D = b**2 - 4*a*c 
if D > 0:
	x = (-b + sqrt(D))/(2*a)
	print(f"первый X:{x}")
	X = (-b - sqrt(D))/(2*a)
	print(f"второй X:{X}")
elif D == 0:
	X = -b/(2*a) 
	print(f"X:{X}")
else:
	print("Отрицательный дискриминант")