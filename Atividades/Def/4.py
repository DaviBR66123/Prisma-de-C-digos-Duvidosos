def qual_maior(lista):
    lens = len(lista)
    cont = int(0)
    r = int(0)

    for cont in range(lens):
        if lista[cont] > r:
            r = lista[cont]

    return r

lista = []
r = 0

print("Acrescente números a lista. Digite uma letra para sair")

while r != "sair" and r != "Sair":
    r = input()
    if r != "sair" and r != "Sair":
        lista.append(r)

r = qual_maior(lista)
print(f"O maior número é {r}")