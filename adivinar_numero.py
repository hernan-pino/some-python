import random
print(f"<:menor, >:mayor \n")
intento=1
menor=1
mayor=101
guess=random.randrange(menor,mayor)
print(f"intento {intento}: {guess}")
result=""

while result!="=":
     result = input("tu numero es mayor o menor:")
     if result=="<":
         mayor=guess
         intento+=1
     elif result==">":
         menor=guess+1
         intento+=1
     guess = random.randrange(menor, mayor)
     print(f"intento {intento}: {guess}")
else:
    print(f"lo adivino en {intento} intentos")

