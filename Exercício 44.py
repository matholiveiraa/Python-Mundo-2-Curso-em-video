#Elabora um programa que calcule
#Um valor a ser pago por um produto
#Considerando o seu proeço normla e condição de pagamento

#A vista dinheiro ou cheque 10% de desconto

#A vista no cartão 5% desconto

#em até 2x no cartão preço normal

#3x ou mais no cartão 20% de juros

import time

print("Iremos fazer um programa que calcula seu preço e condição de pagamento")

time.sleep(2)

print("Você vai digitar se quer fazer a vista ou quantas vezes no cartao")
print("Quantas vezes no cartão")

n = ""
n=str(input("Digite você quer fazer a vista ou cheque S ou N: ")) .upper()
escolha = str(input("Você quer fazer no cartão? S ou N: "))
vezes = int(input("Digite quantas vezes você quer fazer no cartão, digite o número ou 0: "))

if n == "S":
    print("Você receberá 10% de desconto")
if n == "S" and escolha == "S":
    print("Você ganhou 5% de desconto")
if escolha  == "S" and vezes == 2:
    print("Você não ganhou desconto, preço normal")
if escolha == "S" and vezes >= 3:
    print("Você recebeu 20% juros")