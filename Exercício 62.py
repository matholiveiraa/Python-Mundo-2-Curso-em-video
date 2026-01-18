#Exercício Python 61: Refaça o DESAFIO 51, 
# lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

#a10 = a1 + 9r

#An= a1 + (n - 1) * r

import time

print("Vamos fazer os 10 primeiros termos de uma p.a para você")

n = int(input("Digite o primeiro termo: "))

razao = int(input("Digite a razão: "))


a10 = n + 9*razao

contador = 0
contador1 = 0
escolha = 1

while contador < 10:
    contador += 1
    contador1 += 1
    print(f"a{contador} = {n + contador1*razao}")


while True:
    escolha = int(input("Quantos termos você quer mostrar mais?"))
    teste = 0
    if escolha != 0:
        while teste < escolha:
            contador += 1
            contador1 += 1
            print(f"a{contador} = {n + contador1*razao}")
            teste += 1

    else:
        escolha == 0
        print("Acabou")
        break












    