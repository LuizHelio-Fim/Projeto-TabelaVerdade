p1 = ["V","V","F","F"]
q1 = ["V","F","V","F"]

p2 = ["V","V","V","V","F","F","F","F"]
q2 = ["V","V","F","F","V","V","F","F"]
r  = ["V","F","V","F","V","F","V","F"]

n = int(input("Quantas sentenças serão utilizadas?(2 ou 3): "))

if n == 2:
    continuar = "SIM"
    if (continuar == "SIM"):
        
        print("DIGITE A SENTENÇA (p, a, x...): ")
        sentenca_p = str(input("> ")).lower()
        print("\n")

        print("ESCOLHA UM CONECTIVO:")
        print("1 = ^")
        print("2 = v")
        print("3 = #")
        print("4 = →")
        print("5 = ↔")
        conec_1 = int(input("> "))
        print("\n")

        print("DIGITE A PRÓXIMA SENTENÇA (q, b, y):")
        sentenca_q = str(input("> ")).lower()
        print("\n")

        print("DESEJA CONTINUAR A EQUAÇÃO?")
        continuar = (input("> ")).upper()

        print("ESCOLHA UM CONECTIVO:")
        print("1 = ^")
        print("2 = v")
        print("3 = #")
        print("4 = →")
        print("5 = ↔")
        conec_2 = int(input("> "))
        print("\n")

        print("DIGITE A SENTENÇA (p, a, x...): ")
        sentenca_p2 = str(input("> ")).lower()
        print("\n")

        print("ESCOLHA UM CONECTIVO:")
        print("1 = ^")
        print("2 = v")
        print("3 = #")
        print("4 = →")
        print("5 = ↔")
        conec_3 = int(input("> "))
        print("\n")
        
        print("DIGITE A PRÓXIMA SENTENÇA (q, b, y):")
        sentenca_q2 = str(input("> ")).lower()
        print("\n")

        print("DESEJA CONTINUAR A EQUAÇÃO?")
        continuar = (input("> ")).upper()
    


elif n == 3:
    print("")

else:
    print("Valor invalido")