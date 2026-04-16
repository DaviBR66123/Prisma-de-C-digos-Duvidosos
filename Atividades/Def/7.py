def verificar_polidromo(l):
    r = list(l)
    
    if r == r[::-1]:
        r = "é"
    
    else:
        r = "não é"

    return r

r = str(input("Digite uma palavra: "))

print(f"A palavra {verificar_polidromo(r)} um políndromo")