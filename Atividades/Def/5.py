def contar_letras(l):
    r = list(l)
    r = len(l)
    return r

r = input("Digite uma palavra: ")

print(f"A palavra {r} possui {contar_letras(r)} letras")