#Escreva um programa que leia um número N inteiro qualquer e 
#mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

#0 – 1 – 1 – 2 – 3 – 5 – 8

import time
print("Iremos fazer um programa que lhe mostrará a sequência fibonacci")
time.sleep(2)
print("Vamos lá?")
time.sleep(2)

#Fn é a soma dos dois anteriores Fn-1 e Fn-2

qtd = int(input("Deseja ver quantos números da sequência fibonacci: "))
n1 = 0
n2 = 1

contador = 3

print(f"{n1} -> {n2} -> ", end="")

while contador <= qtd:
    fn = n1 + n2
    print(f"{fn} -> ", end ="")
    n1 = n2
    n2 = fn
    contador+=1