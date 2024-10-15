i = 10

while 9 < int(i) < 100:
    i = str(i)
    if int(i[0]) % 2 !=0:
        if int(i[1]) % 2 !=0:
            print(i)
    i = int(i) + 1