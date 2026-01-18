#Faça um programa que calcule a soma entre todos os números
#que são múltiplos de três e que se encontram no intervalo de 1 até 500.

import time

print("Iremos montar um programa que conta de 1 até 500, todos os multiplos de 3")

time.sleep(2)

print("Vamos lá??")

time.sleep(2)

A = 0

for C in range (1,500):
    if C % 3 == 0:
        print(C)
        A += C
print(f"Este é o total!: {A}")
        