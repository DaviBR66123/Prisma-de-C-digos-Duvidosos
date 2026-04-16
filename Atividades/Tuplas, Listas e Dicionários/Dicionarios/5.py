from Coisas.BibliotecaFunções import format_telefone
import sys


agenda = {"contato1": {"nome": "Ana", "telefone": "(22) 91111-1111"},
          "contato2": {"nome": "Bruno", "telefone": "(33) 92222-2222"}}

print("Adicionar, Atualizar, Remover ou Lista Ordenada")
print("Oque fazer?")
r = str(input())

if r == "adicionar" or r == "Adicionar":
    nome = input("Insira seu nome: ")
    cont = input("Insira seu número: ")

    cont = format_telefone(cont)
    
    agenda[r] = {"nome": nome, "telefone": cont}
    print("Contato adicionado", agenda[r])

elif r == "atualizar" or r == "Atualizar":
    print("Qual contato atualizar? (Ex: contato1)")
    edit = str(input())

    print(agenda[edit])

    print("Oque editar? (nome ou telefone)")
    r = str(input())

    if r == "nome" or r == "Nome":
        r = input("Insira o novo nome: ")
        
        agenda["contato1"]["nome"] = r

        print(f"Contato atualizado: {agenda[edit]}")

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

        agenda[edit]["telefone"] = cont
        print(f"Contato atualizado: {agenda[edit]}")

    else:
        print("Erro")

elif r  == "remover" or r == "Remover":
    print("Qual contato remover?")
    r = str(input())

    del agenda[r]
    print(f"agenda: {agenda}")

elif r == "listar" or r == "Listar":
    print(f"Agenda: {agenda}")

else:
    print("Erro")