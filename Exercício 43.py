#calcule imc
#abaixo 18.5 abaixo do peso
#entre 18.5 e 25 peso ideal
#25 até 30 sobrepeso
#30 até 40 obesidade
#acima de 40 obesidade mórbida

import math

import time

print("Faremos um programa que calculará seu imc!")
time.sleep(2)

peso = int(input("Digite seu peso: "))
altura = float(input("Digite sua altera: "))

altura = math.pow(altura, 2)
print(altura)
conta = peso / altura
print(conta)

if conta <= 18.5:
    print("Abaixo do peso")
elif conta >= 18.5 and conta <=25:
    print("Peso ideal")
elif conta > 25.0 and conta <=30:
    print("Sobrepeso")
elif conta > 30 and conta < 40:
    print("Obesidade")
else:
    conta >=40
    print("Obesidade mórbida")