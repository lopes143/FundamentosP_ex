#Recursão com operações adiadas
def numero_digitos(n):
    if n==0:
        return 0
    return 1+numero_digitos(n//10)

#Recursão de cauda
def numero_digitos_cau(n):
    def numero_digitos_cau_aux(n, acc):
        if n==0:
            return acc
        return numero_digitos_cau_aux(n//10, acc+1)
    return numero_digitos_cau_aux(n,0)

#Processo iterativo
def numero_digitos_it(n):
    if n==0:
        return 0
    acc=0
    while n>0:
        acc+=1
        n//=10
    return acc



print(numero_digitos(9))
print(numero_digitos(1012))

print(numero_digitos_cau(9))
print(numero_digitos_cau(1012))

print(numero_digitos_it(9))
print(numero_digitos_it(1012))