def busqueda_binaria(lista,num):
    lista.sort()
    inicio=0
    final=len(lista)-1
    while inicio<=final:
        marca=(inicio+final)//2
        if lista[marca]==num:
            return f"esta en la posicion {marca}"
        elif lista[marca]>num:
            final=marca-1
        else:
            inicio=marca+1
    return "no esta la shit"
