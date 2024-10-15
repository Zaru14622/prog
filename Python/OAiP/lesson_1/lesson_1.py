num = str(input("Ввод числа"))
if len(num) == 5:
	a = 0
	b = 0
	for i in range(0,len(num)):
		if int(num[i])%2 == 0:
			a += 1
		else:
			b += 1

	if a > b:
		print("Больше чётных")
	else:
		print("Больше нечётных")
else:
	print("Число не пятизначное")
	