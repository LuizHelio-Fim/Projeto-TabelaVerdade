
continuar = "SIM"
while (continuar == "SIM"):
    print("SELECIONE A TABELA VERDADE QUE DESEJA VER:")
    print("1 - Conjunção")
    print("2 - Disjunção Inclusiva")
    print("3 - Disjunção Exclusiva")
    print("4 - Condicional")
    print("5 - Bicondicional")
    resp = int(input("> "))
    match resp:
        case 1:
            print("\n")
            print("p | q | p ^ q")
            print("v | v |   V  ")
            print("v | f |   F  ")
            print("f | v |   F  ")
            print("f | f |   F  ")
        case 2:
            print("\n")
            print("p | q | p v q")
            print("v | v |   V  ")
            print("v | f |   V  ")
            print("f | v |   V  ")
            print("f | f |   F  ")
        case 3:
            print("\n")
            print("p | q | p # q")
            print("v | v |   F  ")
            print("v | f |   V  ")
            print("f | v |   V  ")
            print("f | f |   F  ")
        case 4:
            print("\n")
            print("p | q | p → q")
            print("v | v |   V  ")
            print("v | f |   F  ")
            print("f | v |   V  ")
            print("f | f |   V  ")
        case 5:
            print("\n")
            print("p | q | p ↔ q")
            print("v | v |   V  ")
            print("v | f |   F  ")
            print("f | v |   F  ")
            print("f | f |   V  ")
        case _:
            print("Valor",resp,"inválido")

    continuar = input("Deseja continuar? ").upper()
