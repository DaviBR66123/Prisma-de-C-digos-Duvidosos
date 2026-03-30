fila = ["Ana", "Bruno"]

n = str(input("Insira um nome: "))
fila1 = [n]

n = str(input("Insira outro nome com privilegio: "))
fila1.append(n)

print(fila1)

print("Cliente priotitario: ", n)
print(fila)

fila.extend(fila1)
fila.pop(-1)
fila.insert(1, n)
fila.pop(0)

print(fila)