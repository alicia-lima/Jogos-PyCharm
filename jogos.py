import advinhacao
import forca

print ("****************************************")
print("*********** Escolha seu jogo! ***********")
print ("****************************************")

print("(1) Forca (2) Advinhação ")
escolha_usuario = int(input("Escolha o seu jogo: "))

if (escolha_usuario == 1 ):
    forca.jogar ()
elif (escolha_usuario == 2):
    advinhacao.jogar ()