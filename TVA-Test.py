import itertools

p1 = ["V","V","F","F"]
q1 = ["V","F","V","F"]

p2 = ["V","V","V","V","F","F","F","F"]
q2 = ["V","V","F","F","V","V","F","F"]
r  = ["V","F","V","F","V","F","V","F"]

def obter_sentenca(numero):
    sentenca = input(f"Digite a sentença {numero} (p, a, x...): ").lower()
    return sentenca

def obter_conectivo(numero):
    print(f"Escolha o conectivo para a sentença {numero}:")
    print("1 = ^")
    print("2 = v")
    print("3 = #")
    print("4 = →")
    print("5 = ↔")
    conectivo = int(input("> "))
    return conectivo

def continuar_equacao():
    resposta = input("Deseja continuar a equação? (SIM/NÃO): ").upper()
    return resposta == "SIM"

n = int(input("Quantas sentenças serão utilizadas? (2 ou 3): "))

if n == 2:
    continuar = True
    while continuar:
        sentenca_p = obter_sentenca("p")
        conectivo_1 = obter_conectivo("1")
        sentenca_q = obter_sentenca("q")

        continuar = continuar_equacao()

        if not continuar:
            break

        conectivo_2 = obter_conectivo("2")
        sentenca_p2 = obter_sentenca("p2")
        conectivo_3 = obter_conectivo("3")
        sentenca_q2 = obter_sentenca("q2")

        continuar = continuar_equacao()



elif n == 3:
    print("")

else:
    print("Valor invalido")