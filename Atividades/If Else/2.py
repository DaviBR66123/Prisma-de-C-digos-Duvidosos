n = float(input("Insira a Nota: "))
n = f'{n:.1f}'
n = float(n)
print(n)

if n < 5:
    print("Reprovado")

elif n > 4.9 and n < 7:
    print("Recuperação")

elif n > 6.9 and n < 9:
    print("Aprovado")

elif n > 8.9 and n < 10.1:
    print("Aprovado com excelência")

else:
    print("Erro")