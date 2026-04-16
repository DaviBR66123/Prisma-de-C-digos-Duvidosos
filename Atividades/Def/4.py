def qual_maior(l):
    l = max(l)
    return l

lista = [int(0)]
r = 0

print("Acrescente números a lista. Digite 'sair' para sair")

while True:
    r = input()

    if r.lower() == "sair":
        break

    try:
        r = int(r)
        lista.append(r)
        print(type(lista[-1]))
    
    except ValueError:
        print("Invalido")

print(f"O maior numero é {qual_maior(lista)}")