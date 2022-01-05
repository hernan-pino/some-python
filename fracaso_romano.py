
def romano(n):
   numeros={"M": 1000, "D": 500,
           "C": 100, "L": 50,
           "X": 10, "V": 5,
           "I": 1}
   mayusc=n.upper()
   acumulado=0

   if len(mayusc)>1:
      pico=mayusc[0]
      val_anterior=numeros[pico]

   for letra in mayusc:
       if letra in numeros:
           val_actual=numeros[letra]
       else:
           raise ValueError

       if val_actual<=val_anterior:
           acumulado+=val_actual
       else:
           acumulado-=val_actual-(2*val_anterior)#(acum-anterio) + (actual-anterior)

       val_anterior=val_actual

   print(acumulado)


romano('DLIV')#554


