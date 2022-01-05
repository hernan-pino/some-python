def binary(num):
    bin = []
    while num/2 != 0:
        residuo = num%2
        bin.insert(0,residuo)
        num = int(num/2)
    x = "".join(map(str,bin))
    return x


def decimal(num):
    #suma total
    sumatoria=0

    #2 elevado a potencia
    potencia=0

    #pasamos el num a str y lo agregamos a la lista invertido
    num=str(num)
    d=[]
    for i in num:
        d.insert(0,i)

    #lo pasamos a str otra vez
    x="".join(d)

    #multiplicamos cada elemento por (2 elvado a potencia) y le sumas 1 a potencia
    for j in x:
        sumatoria=sumatoria+(int(j)*(2**potencia))
        potencia+=1
    return sumatoria

print(decimal(10111))