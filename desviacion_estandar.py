def desviacion_estandar(valores):
    prom=sum(valores)/len(valores)
    valores2=[]
    for i in valores:
        x=(i-prom)**2
        valores2.append(x)
    x=sum(valores2)/(len(valores2)-1)
    o=x**0.5
    return o
