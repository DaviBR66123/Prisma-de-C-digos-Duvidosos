def é_par (n1):
    n1 %= 2

    if n1 == 1:
        r = "não"
    
    else:
        r = "sim"
    
    return r

n1 = float(input("Digite um número: "))
r = é_par(n1)

print("O número é par?")
print(r)