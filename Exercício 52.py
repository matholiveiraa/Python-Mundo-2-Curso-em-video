#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

import time

print("Iremos fazer um programa que terá se o número é primo ou não!")


time.sleep(2)

print("Vamos lá?")

time.sleep(2)

for C in range(1):
    n1 = int(input("Digite o número: "))
    if n1 == 2:
        print("É um número primo")
    elif n1 % 1 == 0 and n1 % n1 == 0 and n1 % 2 != 0:
        print("É um número primo")
    else:
        print("Não é um número primo")