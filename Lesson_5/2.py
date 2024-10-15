n = int(input(":::"))
sum = 0

for i in range(1,n+1):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    sum += fact/2**i
print(sum)