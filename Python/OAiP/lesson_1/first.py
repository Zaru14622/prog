num = input("Введите чило ")
sumch = 0
sumnch = 0
if len(num) == 5:
	for i in range(0,len(num)):
		if int(num[i])%2 == 0:
			sumch += int(num[i])
		else:
			sumnch += int(num[i])
	if sumch > sumnch:
		print("Сумма чётных чисел больше")
	else:
		print("Сумма нечётных чисел больше")
else:
	print("неверное число")