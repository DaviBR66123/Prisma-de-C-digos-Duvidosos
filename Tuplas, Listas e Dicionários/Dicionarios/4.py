produto = {"nome": "Batatas", "preco": 1.49, "quantidade": 0}

ind = float(input("Insira aumento percentual de preço: "))
ind /= 100
ind += 1

produto["preco"] *= ind

produto["quantidade"] += int(input("Adicionar mais: "))

ind = produto["quantidade"] * produto["preco"]
print(f"Total a ser pago: {ind:.2f}")