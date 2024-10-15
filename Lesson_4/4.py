# a = int(input(":::"))
# res = ""
# while True:
#     if a % 2 == 0:
#         res += " 2 *"
#         a = a / 2
#     elif a % 3 == 0:
#         res += " 3 *"
#         a = a / 3
#     elif a % 5 == 0:
#         res += " 5 *"
#         a = a /5
#     elif a % 7 == 0:
#         res += " 7 *"
#         a = a /7
#     else:
#         if a != 1:
#             res += f" {int(a)} *"
#         break
# print(res[:-1])
n = int(input(":::"))
a = n
res = ""
i  = 1

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
