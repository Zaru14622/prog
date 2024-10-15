i = 100
while 99 < int(i) < 1000:
    i = str(i)
    if int(i[0]) * int(i[1]) == int(i[2]):
        print(i)
    elif int(i[1]) * int(i[2]) == int(i[0]):
        print(i)
    elif int(i[0]) * int(i[2]) == int(i[1]):
        print(i)
    i = int(i) +1