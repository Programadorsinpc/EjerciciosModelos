def sumadigitos(n):
    if n==0:
        return 0
    else:
        return n%10+sumadigitos(n/10)

print(sumadigitos(123))

def potencia(base,exponente):
    if exponente==0:
        return 1
    elif exponente%2==0:
        return potencia(base*base,exponente/2)
    else:
        return base*potencia(base,exponente-1)

print(potencia(2,2))

def multiplicacion(a,b):
    if b==0:
        return 0
    else:
        return a+multiplicacion(a,b-1)

print(multiplicacion(5.2,3))

def mayor(n,c):
    if int(n)!=0:
        if c<int((abs(n) - abs(int(n)))*10):
            return mayor(n/10,int((abs(n) - abs(int(n)))*10))
        else:
            return mayor(n/10,c)
    elif int((abs(n) - abs(int(n)))*10)!=0:
        if c<int((abs(n) - abs(int(n)))*10):
            return mayor(n/10,int((abs(n) - abs(int(n)))*10))
        else:
            return mayor(n/10,c)
    else:
        return c
        
print(mayor(34343254365,0))

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(10))