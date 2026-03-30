notas = []
ws = True

print("Digite um numero negativo para terminar")

while ws == True:
    n = float(input("Insira uma nota"))

    if n >= 0:
        notas.append(n)
    
    elif n < 0:
        break

    else:
        print("Erro")

media = sum(notas)
media /= len(notas)

if media >= 7:
    sit = "Aprovado"

elif media < 7:
    sit = "Reprovado"

else:
    print("Erro1")

media = f'{media:.2f}'

print(f"Notas: {notas}")
print(f"Média: {media}")
print(f"Situação: {sit}")