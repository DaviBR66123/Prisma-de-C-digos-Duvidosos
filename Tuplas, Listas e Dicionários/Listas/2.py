import time

n = int(input("Insira um número: "))
n1 = int(input("Insira outro número: "))
n2 = int(input("Insira mais outro número: "))
n3 = int(input("Insira mais algum número: "))

lista = [n, n1, n2, n3]
print(lista)

print("Você tem ", len(lista), "valores em 'lista'")
time.sleep(1.5)

print("Gostaria de remover algum número? Qual?")
vl = int(input())
time.sleep(1.5)

vlr = lista.index(vl)
lista.pop(vlr)  #Aqui tem um erro que não sei corrigir
print(lista)

print("Verificando se ele foi removido")
time.sleep(1.5)

print(vl, "está presente na lista?")
time.sleep(1)
if vl in lista:
    print("Sim!")

else:
    print("Não")