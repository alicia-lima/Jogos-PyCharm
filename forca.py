import random

def jogar ():

    tela_inicio ()

    palavra_secreta = escolha_palavra_secreta()
    letras_acertadas = exibi_palavra_sorteada (palavra_secreta)

    enforcou = False
    acertou = False

    palavra_escolhida = " "
    erros = 0

    while (not enforcou and not acertou):

        letra_escolhida = letra_do_usuario()

        if(letra_escolhida in palavra_secreta):
            palavra_escolhida = marca_letra_correta (palavra_secreta, letra_escolhida, letras_acertadas)

        else:
            erros += 1
            desenha_forca(erros)

        if  (palavra_escolhida == palavra_secreta):
            acertou = True
            imprime_mensagem_vencedor()

        elif (erros == 7):
            enforcou = True
            imprime_mensagem_perdedor(palavra_secreta)
def tela_inicio():
        print("****************************************")
        print("** Olá, vamos jogar o jogo de forca!  **")
        print("****************************************")
def escolha_palavra_secreta():
    arquivo = open('palavras.txt', "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    palavra_secreta = random.choice(palavras)
    palavra_secreta = palavra_secreta.upper()
    return palavra_secreta
def exibi_palavra_sorteada (palavra_secreta):
    letras_acertadas = ["_" for letras in palavra_secreta]
    quantidade_de_letras = len(palavra_secreta)  # quantidade
    print("\n** Palavra sorteada **")
    print("  ", "_" * quantidade_de_letras, "  \n")
    return letras_acertadas
def letra_do_usuario ():
    letra_escolhida = input("Escolha uma letra: ")
    letra_escolhida = letra_escolhida.strip().upper()
    return letra_escolhida
def desenha_forca(erros):
    print(r"  _______     ")
    print(r" |/      |    ")

    if(erros == 1):
        print(r" |      (_)   ")
        print(r" |            ")
        print(r" |            ")
        print(r" |            ")

    if(erros == 2):
        print(r" |      (_)   ")
        print(r" |      \     ")
        print(r" |            ")
        print(r" |            ")

    if(erros == 3):
        print(r" |      (_)   ")
        print(r" |      \|    ")
        print(r" |            ")
        print(r" |            ")

    if(erros == 4):
        print(r" |      (_)   ")
        print(r" |      \|/   ")
        print(r" |            ")
        print(r" |            ")

    if(erros == 5):
        print(r" |      (_)   ")
        print(r" |      \|/   ")
        print(r" |       |    ")
        print(r" |            ")

    if(erros == 6):
        print(r" |      (_)   ")
        print(r" |      \|/   ")
        print(r" |       |    ")
        print(r" |      /     ")

    if (erros == 7):
        print(r" |      (_)   ")
        print(r" |      \|/   ")
        print(r" |       |    ")
        print(r" |      / \   ")

    print(r" |            ")
    print(r"_|___         ")
    print()
def marca_letra_correta(palavra_secreta, letra_escolhida, letras_acertadas):
    index = 0
    meu_separador = ""
    for letra in palavra_secreta:
        if (letra_escolhida == letra):
            letras_acertadas[index] = letra
        index += 1
        palavra_escolhida = meu_separador.join(letras_acertadas)
    print("\n** Palavra sorteada **")
    print("   ", palavra_escolhida, "   \n")
    return  palavra_escolhida
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print(r"    _______________         ")
    print(r"   /               \       ")
    print(r"  /                 \      ")
    print(r"//                   \/\  ")
    print(r"\|   XXXX     XXXX   | /   ")
    print(r" |   XXXX     XXXX   |/     ")
    print(r" |   XXX       XXX   |      ")
    print(r" |                   |      ")
    print(r" \__      XXX      __/     ")
    print(r"   |\     XXX     /|       ")
    print(r"   | |           | |        ")
    print(r"   | I I I I I I I |        ")
    print(r"   |  I I I I I I  |        ")
    print(r"   \_             _/       ")
    print(r"     \_         _/         ")
    print(r"       \_______/           ")
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print(r"       ___________      ")
    print(r"      '._==_==_=_.'     ")
    print(r"      .-\:      /-.    ")
    print(r"     | (|:.     |) |    ")
    print(r"      '-|:.     |-'     ")
    print(r"        \::.    /      ")
    print(r"         '::. .'        ")
    print(r"           ) (          ")
    print(r"         _.' '._        ")
    print(r"        '-------'       ")
if (__name__ == "__main__"):
    jogar()

