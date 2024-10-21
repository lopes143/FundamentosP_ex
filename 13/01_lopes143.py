def apenas_digitos_impares(n):  
    dig = n%10
    if n<=0:
        return 0
    elif dig%2!=0:
        return dig+10*apenas_digitos_impares(n//10)
    else:
        return apenas_digitos_impares(n//10)
    
print(apenas_digitos_impares(468))
print(apenas_digitos_impares(12426374856))