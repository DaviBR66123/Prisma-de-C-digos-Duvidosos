# Leia saldo (float) e depósito (float). Use saldo += deposito e mostre o novo saldo.

saldo = float(1500.00)

print("Saldo atual: ", saldo)

action = input("Depositar, Extratar ou Sair?")

if action == "Depositar" or "depositar":
    deposito = float(input("Quanto gostaria de positar? "))

    saldo = saldo + deposito

    print("Saldo atual: ", saldo)

elif action == "Extratar" or "extratar":
    extrato = float(input("Quanto gostaria de extratar? "))

    saldo = saldo - extrato

    print("Saldo atual: ", saldo)

else:
    print("Saindo")