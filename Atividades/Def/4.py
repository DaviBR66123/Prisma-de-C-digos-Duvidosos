def qual_maior(lista):
    print(f"O maior numero é {max(lista)}")

lista = [int(0)]
r = 0

print("Acrescente números a lista. Digite 'sair' para sair")

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

qual_maior(lista)