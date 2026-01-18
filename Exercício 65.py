#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
#mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

import time

print("Iremos fazer um programa que mostra e média e o maior e menor valor lido, dos números que você digitar")
time.sleep(2)
print("Vamos lá!?")
time.sleep(2)

listanumeros = []


while True:
    
    n = int(input("Jogue um número!: "))
    listanumeros.append(n)
    tentativa = str(input("Você parar?? S para sim, caso não digite qualquer outro valor!: ")).lower()
    if tentativa == "s":
        maxlistanumeros = max(listanumeros)
        medianumeros = sum(listanumeros) / len(listanumeros)
        minlistanumeros = min(listanumeros)
    
        print(f"Max: {maxlistanumeros}, Min: {minlistanumeros}, Média: {medianumeros}")
        break