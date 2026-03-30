n = int(input("Primeiro número: "))
n1 = int(input("Segundo número: "))
n2 = int(input("Terceiro número: "))
n3 = int(input("Quarto número: "))

print("Contar qual número?")
r= int(input())

nl = (n, n1, n2, n3)

print("A quantidade de", r, "na tuple é: ", nl.count(r))