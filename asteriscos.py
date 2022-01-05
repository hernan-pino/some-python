lados=int(input("num: "))
maxasteriscos= (3 * lados) - 2

for i in range(lados, maxasteriscos, 2):
    x="*"*i
    print(x.center(maxasteriscos, " "))

for j in range(maxasteriscos, lados - 2, -2):
    y = "*" * j
    print(y.center(maxasteriscos, " "))
