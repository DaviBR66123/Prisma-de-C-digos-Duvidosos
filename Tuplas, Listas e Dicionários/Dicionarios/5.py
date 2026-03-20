# Alterar o nome depois para "Calculadora que Calcula o Mundo"

agenda = {"contato": {"nome": "Ana", "telefone": "1111-1111"},
          "contato1": {"nome": "Bruno", "telefone": "2222-2222"}}

print("Adicionar, Atualizar, Remover ou Lista Ordenada")
print("Oque fazer?")
r = str(input())

if r == "adicionar" or "Adicionar":
    nome = input("Insira seu nome: ")
    cont = input("Insira seu número: ")