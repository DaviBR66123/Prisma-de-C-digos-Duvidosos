nome = str(input("Insira o Nome: "))
peso = float(input("Insira seu Peso(Kg): "))
altura = float(input("Insira sua Altura(M): "))

imc = peso / (altura ** 2)

print(imc)

print(f"IMC de {nome}: {imc: .2f}")

if imc < 18.5:
    print("Abaixo do Peso")

elif imc >= 18.5 and imc < 25:
    print("Normal")

elif imc >= 25 and imc < 30:
    print("Sobrepeso")

else:
    print("Obesidade")