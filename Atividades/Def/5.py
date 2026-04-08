def contar_letras(strlista):
    frag = list(strlista)
    r = len(strlista)
    return r

strlista = []
strlista.append(input("Digite uma palavra: "))

r = contar_letras(strlista)
print(f"A palavra possui {r} letras")