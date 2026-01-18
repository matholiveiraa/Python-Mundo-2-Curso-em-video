#Faça um programa que leia um número qualquer e mostre o seu fatorial. 
#Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

import math
import time

print("Iremos fazer um programa que calculará o fatorial para você")
time.sleep(2)
print("Preparado?")

n = int(input("Digite o valor que deseja: "))
fatorialn = math.factorial(n)
contador = 0
lista = []


while contador != n:
    lista.append(contador)
    contador += 1
if contador == n:
    lista.append(n)
    novalist = lista[::-1]
    print(f"{n}! = {' x '.join(map(str, novalist))} = {fatorialn}") # join junta a lista usando " x ", map(str, ...) converte números para string
    

        
