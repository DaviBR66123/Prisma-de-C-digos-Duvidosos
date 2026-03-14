print("Melancias de 30$ com 10% de desconto")
print("Quantas você compra?")
compras = int(input())

melancia = 30
melancia /= 100
melancia *= 90

compras *= melancia

print("Valor a ser pago: ", compras)