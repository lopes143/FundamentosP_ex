# Recursão com operações adiadas
def squared(n):
    if n==0:
        return 0
    
    return (n+n-1)+squared(n-1)

print(squared(8))

# Recursão de cauda
def squared_cau(n):
    def squared_aux(n, acc):
        if n==0:
            return acc
        return squared_aux(n-1, acc+n+n-1)
    return squared_aux(n,0)

print(squared_cau(8))

#Processo iterativo
def squared_it(n):
    acc=0
    if n==0:
        return acc
    while n>0:
        acc+=n+n-1
        n-=1
    return acc

print(squared_it(8))