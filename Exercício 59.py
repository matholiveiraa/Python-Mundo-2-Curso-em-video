#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

#[ 1 ] somar

#[ 2 ] multiplicar

#[ 3 ] maior

#[ 4 ] novos números

#[ 5 ] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.

import time

print("Iremos fazer um programa calculadora pra você")
time.sleep(2)
print ('''#[ 1 ] somar #[ 2 ] multiplicar #[ 3 ] maior #[ 4 ] novos números #[ 5 ] sair do programa''')


escolha = 0

while escolha != 5:
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    escolha = int(input("Digite sua escolha: "))
    if escolha == 1:
        print(f"Está é a soma {n1} + {n2} = {n1+n2}")
    elif escolha == 2:
        print(f"A multiplicação de {n1} * {n2} = {n1*n2}")
    elif escolha == 3:
        if n1 > n2:
            print(n1)
        else:
            n2 > n1 
            print(n2)
    else:
        escolha == 4
        n1 = int(input("Digite novo valor primeiro número: "))
        n2 = int(input("Digite novo valor segundo número: "))
    

