#Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

import time

print("Iremos fazer uma lista que mostre todos os número pares de 1 até 50!")

time.sleep(2)

print("Vamos lá!")

time.sleep(2)

for C in range(1,51):
    if C % 2 == 0:
        print(C)
    