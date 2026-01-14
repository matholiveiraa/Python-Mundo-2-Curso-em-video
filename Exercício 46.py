#Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva 
#para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import random
import time
print("Iremos fazer uma contagem pros fogos de artifício!")

time.sleep(2)

print("Preparado?!!")

time.sleep(2)


for C in range (1,11,1):
    print(f"{C}...")
    time.sleep(1)
print("Bem vindo ao ano novo!!✨✨")
