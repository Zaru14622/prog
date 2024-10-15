a = int(input(":::"))
i = 1

while 0 < i < n+1:
    sum = 0
    b = 1
    while 1 <= b <= i:
        if i % b == 0:
            sum += 1
        b += 1
    if sum > 1:
        a = a // i
        print(i)
    i += 1