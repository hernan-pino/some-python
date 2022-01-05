def es_divisible(n,d):
    if n % d == 0:
        return True
    else:
        return False


def es_primo(num):
    num_divisores=0
    for i in range(1,num+1):
        es_divisible(num,i)
        if es_divisible(num,i)==True:
            num_divisores+=1
    if num_divisores==2:
         return True
    else:
         return False


def i_esimo_primo(i):
    inicial=2
    cant_primos=0
    while True:
       if es_primo(inicial)==True:
           cant_primos+=1
       if cant_primos==i:
           print(inicial)
           break
       else:
           inicial+=1





