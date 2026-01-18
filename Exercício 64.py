#Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, 
# mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

import time

print("Iremos fazer um jogo contigo temos de 0 a 1000 tente acertar o número")
time.sleep(2)
print("Iremos contar os erros, e a soma de todos os erros!")
time.sleep(2)

erros = 0
somaerros = 0
listaerros = []


while True:
    acerto = int(input("Tente acertar o número: "))
    if acerto != 999:
        erros += 1
        somaerros += acerto
        listaerros.append(acerto)

    else:
        acerto == 999
        print("Você acertou!!")
        print(f"Tua lista dos números tentados: {listaerros}")
        print(f"Total de erros: {erros}, total de soma dos números contidos nos erros: {somaerros}")
        break
