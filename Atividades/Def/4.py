def qual_maior(lista):
    lens = len(lista)
    cont = int(0)
    r = int(0)

    for cont in range(lens):
        if lista[cont] >= r:
            r = lista[cont]

    return r

lista = [int(0)]
r = 0

print("Acrescente números a lista. Digite uma letra para sair")

while True:
    r = input()

    if r.lower() == "sair":
        lista.append(r)
        break

    try:
        r = int(r)
        lista.append(r)
        print(type(lista[-1]))
    
    except ValueError:
        print("Invalido")

r = qual_maior(lista)
print(f"O maior número é {r}")