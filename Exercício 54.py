#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import time
from datetime import datetime

ano_atual_datetime = datetime.now().year

print("Iremos fazer um programa que lê o ano de nascimento de 7 pessoas")
time.sleep(2)
print("E iremos dizer se já são maiores ou não")
time.sleep(2)

nmaior = 0
maior = 0

for C in range(7):
    n = int(input("Digite o ano de nascimento: "))
    if ano_atual_datetime - n >= 18:
        maior += 1
    else:
        ano_atual_datetime - n < 18
        nmaior += 1
print(f"São de maior: {maior}, são de menores {nmaior}")
        