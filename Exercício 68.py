#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. 
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
import time

print("Iremos jogo você joga um número e o computador outro, você deve advinhar se a soma dos dois é par ou impar!")
time.sleep(2)
print("Preparado!?")
time.sleep(2)
escolhapc = [0,1,2,3,4,5,6,7,8,9,10]
acertos = 0

while True:
    p = 0
    i = 0

    n = int(input("Jogue um número:"))
    escolhapc1 = random.choice(escolhapc)
    soma = n + escolhapc1

    if soma % 2 == 0:
        p += 1
    elif soma % 2 != 0:
        i += 1

    pergunta = str(input("É par ou impar!? [P/I]")).lower()

    if pergunta == "p":
        if p == 1:
            acertos += 1
            print(f"Sua escolha: {pergunta}")
            print(f"Escolha PC: {escolhapc1}")
            print(f"Parabéns você acertou!")
            
        else:
            p != 1
            print(f"Você errou, Total de acertos: {acertos}, Escolha PC: {escolhapc1}")
            break

    if pergunta == "i":
        if i == 1:
            acertos += 1
            print(f"Sua escolha: {pergunta}")
            print(f"Escolha PC: {escolhapc1}")
            print(f"Parabéns você acertou!")

        else:
            i != 1
            print(f"Você errou, Total de acertos: {acertos}, Escolha PC: {escolhapc1}")
            break
    


    
