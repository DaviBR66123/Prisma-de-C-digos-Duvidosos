def media_lista(l):
    n = len(l)
    l = sum(l)
    l /= n
    l = f"{l:.2f}"
    return l

n = float(input("Insira um número: "))
n1 = float(input("Insira outro número: "))
n2 = float(input("Insira mais outro número: "))
n3 = float(input("Insira mais algum número: "))

lista = [n, n1, n2, n3]

print(f"A média dos valores é {media_lista(lista)}")