from pprint import pprint
#esta wea deja controlar lo que imprimimos


sentence="this is a common interview question"

letras={}

for letra in sentence:
    if letra in letras:
        letras[letra]+=1
    else:
        letras[letra]=1

frecuensi_letra = sorted(letras.items(), key=lambda kv:kv[1], reverse=True)
print(frecuensi_letra[0])

