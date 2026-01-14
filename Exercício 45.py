#Faça um programa para computador jogar Jokenpô com você

import random
import time

print("Iremos fazer um programa que joga jokenpô com você!")
time.sleep(2)
print("Preparado(a)?")
time.sleep(2)

escolhacomputador = ['pedra', 'papel', 'tesoura']
escolhajogador = str(input("Escolha entre pedra, papel, tesoura: "))



while escolhajogador == escolhajogador:
    escolhajogador = str(input("Escolha entre pedra, papel, tesoura: "))

    escolhacomputador1=random.choice(escolhacomputador)


    if escolhajogador != 'pedra' or 'papel' or 'tesoura':
        print("Por favor, tente novamente e digite a palavra corretamente!")

    if escolhacomputador1 == 'pedra' and escolhajogador =='papel':
        print("Você ganhou!")
        print(f"Essa foi a escolha nossa: {escolhacomputador1}")

    elif escolhacomputador1 == 'pedra' and escolhajogador =='tesoura':
        print("Você perdeu!")
        print(f"Essa foi a escolha nossa: {escolhacomputador1}")

    elif escolhacomputador1 == 'pedra' and escolhajogador =='pedra':
        print("Empate!")
        print(f"Essa foi a escolha nossa: {escolhacomputador1}")

    elif escolhacomputador1 == 'papel' and escolhajogador =='tesoura':
        print("Você ganhou!")
        print(f"Essa foi a escolha nossa: {escolhacomputador1}")

    elif escolhacomputador1 == 'papel' and escolhajogador =='pedra':
        print("Você perdeu!")
        print(f"Essa foi a escolha nossa: {escolhacomputador1}")

    elif escolhacomputador1 == 'papel' and escolhajogador =='papel':
        print("Empate!")
        print(f"Essa foi a escolha nossa: {escolhacomputador1}")

    elif escolhacomputador1 == 'tesoura' and escolhajogador =='pedra':
        print("Você ganhou!")
        print(f"Essa foi a escolha nossa: {escolhacomputador1}")

    elif escolhacomputador1 == 'tesoura' and escolhajogador =='papel':
        print("Você perdeu!")
        print(f"Essa foi a escolha nossa: {escolhacomputador1}")

    else:
        escolhacomputador1 == 'tesoura' and escolhajogador =='tesoura'
        print("Empatou")
        print(f"Essa foi a escolha nossa: {escolhacomputador1}")




