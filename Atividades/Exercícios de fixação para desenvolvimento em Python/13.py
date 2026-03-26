salario = float(1500)

aumento = float(input("Digite um aumento em (%): "))

aumento /= 100
aumento *= salario
salario += aumento

print("Novo salario: ", salario)