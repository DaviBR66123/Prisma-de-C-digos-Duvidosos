def é_par (n1):
    n1 %= 2

    if n1 == 1:
        r = "ímpar"
    
    else:
        r = "par"
    
    return r

n1 = float(input("Digite um número: "))

print(f"O número é {é_par(n1)}")