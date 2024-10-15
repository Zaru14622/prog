num_1 = int(input(":::"))
num_2 = int(input(":::"))

nOD = 0
nOK = 0

i = 1
while nOD == 0 or nOK == 0:
    if num_1 % i == 0 and num_2 % i ==0:
        nOD = i
    if i % num_1 == 0 and i % num_2 ==0:
        nOK = i
    i += 1

print(f"nOD: {nOD}, nOK: {nOK}")