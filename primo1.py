# cantidad_primos = int(input("cuantos primos quieres?.. "))
# num_divisores = 0
# num_impreso = 0
# num=2


# while num_impreso!=cantidad_primos:
#    for i in range(1,num+1):
#         if num%i==0:
#             num_divisores+=1

#    if num_divisores==2:
#         print(num)
#         num_impreso+=1
#    num += 1
#    num_divisores=0

# otra forma de hacerlo

numero=int(input("ingrese numero... "))

primo=True
base=2

while numero>base and primo==True:
    if numero%base==0:
        primo=False
    base+=1

if primo:
    print("es primo")
else:
    print("no es primo")













