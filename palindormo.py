palabra = input("ingrese una palabra.. ")
invert =[]
normal=[]

for letra in palabra[::-1]:
    if letra == " ":
        invert.append(letra)
        invert.pop()
    else:
        invert.append(letra)

for letra in palabra:
    if letra == " ":
        normal.append(letra)
        normal.pop()
    else:
        normal.append(letra)

normal_str="".join(normal)
inv_str="".join(invert)

if inv_str == normal_str:
    print("es palindromo")
else:
    print("no es palindromo")
