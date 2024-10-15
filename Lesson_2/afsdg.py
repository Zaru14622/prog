a = int(input(":::"))

while True:
    if a % 2 == 0:
        print(2)
        a = a / 2
    elif a % 3 == 0:
        print(3)
        a = a / 3
    elif a % 5 == 0:
        print(5)
        a = a /5
    elif a % 7 == 0:
        print(7)
        a = a /7
    else:
        if a != 1:
            print(a)
        break