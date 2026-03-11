# Leia um contador (int) e um passo (int). Faça contador += passo duas vezes. Mostre o resultado.

contador = int(input("Contador: "))
passo = int(input("Passos: "))

contador += passo

passo = int(input("Passos: "))
contador += passo

print("Contador: ", contador)