import time
time.sleep(1)

inv = []

print("Digite 'sair' para sair do inventario")
time.sleep(1)

print("Guardar... ")

while True:
    n = str(input())
    if n == "sair" or n == "Sair":
        break

    else:
        inv.append(n)

inv.sort()

time.sleep(1)
print(f"Inventario: {inv}")

time.sleep(1)
print(f"Você coletou {len(inv)} itens")