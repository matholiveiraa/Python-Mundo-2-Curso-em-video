#Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.

import time

print("Iremos fazer um programa que lera o peso de cinco pessoas")
time.sleep(2)
print("E iremos mostrar o maior e menor peso")

pesos = []

for C in range(5):
    n = float(input("Digite o peso: "))
    pesos.append(n)
print(f"O maior peso foi {max(pesos)}, e o menor foi: {min(pesos)}")