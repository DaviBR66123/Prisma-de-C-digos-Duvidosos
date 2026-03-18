n = int(input("Insira um número: "))
n1 = int(input("Insira outro número: "))
n2 = int(input("Insira mais outro número: "))
n3 = int(input("Insira mais algum número: "))

lista = [n, n1, n2, n3]
print(lista)

print("Você tem ", len(lista), "valores em 'lista'")
print("Gostaria de remover algum número? Qual?")
vl = int(input())

vl = lista.index(vl)
#lista.remove(lista.index(vl))  #Aqui tem um erro que não sei corrigir
print(lista)

print("Verificando se ele foi removido")
print(vl, "está presente na lista?")
print(vl in lista)