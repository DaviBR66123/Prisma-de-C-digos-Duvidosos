n = int(input("Insira um número: "))
n1 = int(input("Insira outro número: "))
n2 = int(input("Insira mais outro número: "))

lista = [n, n1, n2]
print(lista)

r = n + n1

lista.pop(-1)
lista.insert(2, r)
print(lista)