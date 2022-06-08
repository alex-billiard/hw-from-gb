a = 15
b = 9
c = 3
p = 1
for i in range(c):
    p = b / a * p
    a = a - 1
    b = b - 1
p = round(p * 100, 2)
print(f"Ответ на 3-ю задачу:{p} процента(ов)")
