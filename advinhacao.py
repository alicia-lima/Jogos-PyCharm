import random
def jogar ():
    numero_pontos = 1000
    numero_aleatorio = sorteio()
    tela_inicio()
    numero_total_de_chances = escolha_nivel()

    for numero_chances in range (1, numero_total_de_chances + 1):
        numero_escolhido = palpite(numero_chances, numero_total_de_chances)

        if numero_escolhido < 1 or numero_escolhido > 100:
            print("\nVocê digitou um número invalido tente novamente")
            continue

        elif numero_aleatorio == numero_escolhido:
            print("\nParabéns! Você acertou e fez {} ponto e sendo o número sorteado {}".format(numero_pontos, numero_aleatorio))
            break

        elif numero_chances == numero_total_de_chances:
            print("\nVocê perdeu! o numero era ", numero_aleatorio)

        else:
           numero_pontos = palpite_errado(numero_aleatorio, numero_escolhido, numero_pontos)

    print ("\nFim de Jogo")
def tela_inicio():
    print ("****************************************")
    print("Olá, vamos jogar o jogo de adivinhação!")
    print ("****************************************")

def sorteio():
    numero_aleatorio = random.randint(1, 100)
    return numero_aleatorio

def escolha_nivel():
    print ("Escolha o nível de dificuldade:")
    print ("(1) fácil (2) Médio (3)Díficil")
    nivel = int(input("Defina seu nível: "))
    if nivel == 1:
        numero_total_de_chances = 20
    elif nivel == 2:
        numero_total_de_chances = 10
    else:
        numero_total_de_chances = 5
    return numero_total_de_chances

def palpite (numero_chances, numero_total_de_chances):
    print("Tentativa {} de {}.".format(numero_chances, numero_total_de_chances))
    # {}.format pode ser delimitado em {:f} ou {:d} e {:3.2f} ou {:2d}
    numero_escolhido = int(input("Escolha um número entre 1 e 100: \n"))
    return numero_escolhido

def palpite_errado (numero_aleatorio, numero_escolhido, numero_pontos):
    if numero_aleatorio < numero_escolhido:
        print("\nO número é menor que ", numero_escolhido)

    elif numero_aleatorio > numero_escolhido:
        print("\nO número é maior que ", numero_escolhido)

    numero_pontos = numero_pontos - abs(numero_escolhido - numero_aleatorio)
    return numero_pontos

if (__name__ == "__main__"):
    jogar()