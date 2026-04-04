def soma(r):

    r = sum(r)
    
    return r

n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
r = [n1, n2]
r = soma(r)
print(f"A soma dos números é {r}")