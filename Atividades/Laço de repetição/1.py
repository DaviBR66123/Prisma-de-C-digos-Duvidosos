def media(l):
    n = len(l)
    l = sum(l)
    l /= n
    l = f"{l:.2}"
    return l

import sys

print("Registrando valor compras")

lista = []

while True:
    try:
        vl = float(input())
    
    except TypeError:
        print("Valor inválido")
    
    if vl != 0.00:
        lista.append(vl)
    
    else:

        print(f"Preço total: {sum(lista):.2f}")
        print(f"Compras realizadas: {len(lista)}")
        print(f"Média dos valores das compras: {media(lista)}")
        sys.exit()