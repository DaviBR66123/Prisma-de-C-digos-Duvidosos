import time
import sys


agenda = {"contato1": {"nome": "Ana", "telefone": "1111-1111"},
          "contato2": {"nome": "Bruno", "telefone": "2222-2222"}}

print("Adicionar, Atualizar, Remover ou Lista Ordenada")
print("Oque fazer?")
r = str(input())

if r == "adicionar" or r == "Adicionar":
    nome = input("Insira seu nome: ")
    cont = input("Insira seu número: ")

    cont = str(cont)
    cont = list(cont)
    print(cont)

    if cont[-5] != "-":            # Adiciona "-" xxxxxx-xxxx
        cont.insert(-4, "-")
    
    if cont[2] != " ":             # Adiciona " " xx xxxx-xxxx
        cont.insert(2, " ")
    
    if cont[3] != "9":               # Adiciona "9" xx 9xxxx-xxxx
        cont.insert(3, "9")

    nc = len(cont)    
    if nc == 13:                   # Para formato xx 9xxxx-xxxx '13 caracteres'

        cont.insert(2, ")")        # Para formato (xx) 9xxxx-xxxx
        cont.insert(0, "(")

    else:                
        print("O número está errado")
        sys.exit()
    
    cont = "".join(cont)
    agenda["contato2"] = {"nome": nome, "telefone": cont}
    print("Contato adicionado", agenda["contato2"])

elif r == "atualizar" or r == "Atualizar":
    print("Qual contato atualizar? (Ex: contato1)")
    r1 = str(input())

    print(agenda[r1])

    print("Oque editar? (nome ou telefone)")
    r = str(input())

    if r == "nome" or r == "Nome":
        r = input("Insira o novo nome: ")
        agenda[r1, ["nome", r]]
        print(agenda)

    elif r == "telefone" or r == "Telefone":
        r = input("Insira o novo telefone: ")

        cont = str(r)
        cont = list(cont)

        if cont[-5] != "-":            # Adiciona "-" xxxxxx-xxxx
            cont.insert(-4, "-")
    
        if cont[2] != " ":             # Adiciona " " xx xxxx-xxxx
            cont.insert(2, " ")
    
        if cont[3] != "9":               # Adiciona "9" xx 9xxxx-xxxx
            cont.insert(3, "9")

        nc = len(cont)    
        if nc == 13:                   # Para formato xx 9xxxx-xxxx '13 caracteres'

            cont.insert(2, ")")        # Para formato (xx) 9xxxx-xxxx
            cont.insert(0, "(")

        else:
            print("O número está errado")
            sys.exit()
    
        cont = "".join(cont)

        agenda[r1, {"telefone": cont}]
        print(agenda)