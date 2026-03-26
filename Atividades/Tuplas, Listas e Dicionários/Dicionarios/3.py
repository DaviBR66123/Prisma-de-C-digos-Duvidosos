

produto = {"nome": "Batatas", "preco": 9.99}

if "desconto" in produto:
    produto.pop("desconto")
    print(produto)

else:
    desc = float(input("Insira o desconto: "))

    print("Antes: ", produto)

    produto["desconto"] = desc
    print("Depois: ", produto)