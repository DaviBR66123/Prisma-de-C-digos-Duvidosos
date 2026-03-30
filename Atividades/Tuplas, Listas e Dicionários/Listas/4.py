n = float(input("Insira uma nota: "))
n1 = float(input("Insira outra nota: "))
n2 = float(input("Insira mais outra nota: "))

lista = [n, n1, n2]

md = n + n1 + n2
md /= 3

print(md)

n = float(input("Insira nota de recuperação: "))

lista.sort
lista.pop(0)
lista.insert(0, n)
lista.sort

n = lista[0]
n += lista[1]
n += lista[2]
n /= 3

print(lista)
print("Nova media: ", n)