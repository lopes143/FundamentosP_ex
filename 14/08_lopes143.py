def maior_inteiro(l):
    def maior_intiero_aux(l, n, acc):
        if acc>l:
            return n-1
        return maior_intiero_aux(l, n+1, acc+n+1)
    return maior_intiero_aux(l, 0, 0)

print(maior_inteiro(6))
print(maior_inteiro(20))