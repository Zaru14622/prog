num = int(input(":::"))
i = 0

while i < len(str(num)):
    print(num// 10**i % 10, end="")

    i += 1