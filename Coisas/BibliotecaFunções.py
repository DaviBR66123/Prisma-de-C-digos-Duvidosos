def format_telefone(cont):
    import sys

    cont = str(cont)
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
    
    return cont