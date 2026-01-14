#Faça um programa que leia dois números inteiros
#compare os e diga as mensagem da tela
#O primeiro valor é maior
#O segundo valor é maior
#Os dois são iguais

import time

print("Iremos fazer um programa que calcula qual é o maior entre dois números")
time.sleep(2)

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1>n2:
    print(f"{n1} é maior que {n2}")
elif n2>n1:
    print(f"{n2} é maior que {n1}")
else:
    n1==n2
    print("Os dois números são iguais")
    print(n1)
    print(n2)