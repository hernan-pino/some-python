productos={"A":270, "B":340, "C":390}
print(productos)
eleccion=input("ingrese producto: ").upper()
monedas=[10,50,100]

#variable que lleve la cuenta de del total demonedas ingresadas
monto=0
# while la wea sea menor al precio del producto
print("ingrese monedas:")
while monto<productos[eleccion]:
    try:
        moneda=int(input())
        monto+=moneda
    #solo acepta 10,50,100

        if moneda not in monedas:
            raise ValueError

        #si lo ingresado es mayor al precio damos vuelto si es igual termina el codigo
        if monto>productos[eleccion]:
            print("vuelto:")
            vuelto=monto-productos[eleccion]

            #mientras el vuelto sea distinto de cero seguira dando monedas
            #empieza de la moneda mas grande a la mas pequeña
            while vuelto!=0:
                if vuelto>=100:
                    print("100")
                    vuelto-=100
                elif vuelto>=50:
                    print("50")
                    vuelto-=50
                elif vuelto>=10:
                    print("10")
                    vuelto-=10
            print("gracias por su compra")

        elif monto==productos[eleccion]:
            print("gracias por su compra")
    except ValueError:
        print("no eceptamos esa moneda")

