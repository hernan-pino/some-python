numero=int(input("ingrese el numero de fibonachi que desea... "))
primero=0
segundo=1

for i in range(numero+1):
    if i > 1:
        final=primero+segundo
        primero=segundo
        segundo=final

if numero==0 or numero==1:
    print(f"el {numero} numero de fibonacci es {numero}")
else:
    print(f"el {numero} numero de fibonacci es {final}") 