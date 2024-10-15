n = int(input(":::"))
a = n
res = ""
i  = 2

while i < a+1:
    if a % i == 0:
        sum = 0
        b = 1
        while 1 <= b <= i:
            if i % b == 0:
                sum += 1
            b += 1
        if sum > 1:
            a = a // i
            res += f"{i} * "
    i += 1

print(res[:-2])