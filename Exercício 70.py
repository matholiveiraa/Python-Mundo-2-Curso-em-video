#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.

import time

print("Iremos fazer uma nota fiscal para ti!")
time.sleep(2)
print("Total gasto, quantos produtos acima de 1000, nome produto mais barato")
time.sleep(2)
print("         NOTA FISCAL")
time.sleep(2)

gasto = 0
acima1000= 0
nomes = []


valorzinho = []
menorvalor = 0

while True:
    nome = str(input("Digite o nome do produto: "))
    nomes.append(nome)


    valorproduto = int(input("Digite o valor do produto: "))
    valorzinho.append(valorproduto)
    gasto += valorproduto # Somador de valores

    if valorproduto == min(valorzinho):
        novonome = nome
        menorvalor = valorproduto


    if valorproduto > 1000: # B
        acima1000 += 1
    continua = str(input("Deseja continuar?! [S/N]")).lower()

    if continua == "n":
        print(f"O total gasto é: {gasto}") #A
        print(f"Produtos acima de R$1000: {acima1000}") #B
        print(f"O produto mais barato foi {novonome}")

        break

    


