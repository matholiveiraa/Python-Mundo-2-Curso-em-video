#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

#A) quantas pessoas tem mais de 18 anos.

#B) quantos homens foram cadastrados.

#C) quantas mulheres tem menos de 20 anos.

import time

print("Iremos analisar quantas pessoas, quantos homens, e quantas mulheres < que 20 anos")
time.sleep(2)

mulheresidade = []
homensidade = []
valor = 18

while True:
    idade = 0
    sexo = ""
    abaixo_18 = len([x for x in mulheresidade if x < 18])
    abaixo_181 = len([a for a in homensidade if a < 18])
    abaixos = abaixo_18 + abaixo_181
    abaixomulheres = len([b for b in mulheresidade if b < 20]) #aqui criei uma lista para contar quantas pessoas tem na lista mulheres idades, abaixo de 20 anos, len serve para contar elementos
    #nova_lista = []
    #for x in mulheresidade:
    #if x < 20:
    #nova_lista.append(x)

    #abaixomulheres = len(nova_lista)
    #fiz examente isso
    print("Vamos cadastrar!")
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo [F/M]: ")).lower()

    if sexo == 'f': 
        mulheresidade.append(idade)
    else:
        sexo == "m"
        homensidade.append(idade)

    escolha = str(input("Deseja continuar!? [S/N]: ")).lower()

    if escolha == "n":
        print(f"Total homens cadastrados: {len(homensidade)}")
        print(f"Total de pessoas abaixo de 18 anos: {abaixos}")
        print(f"Total de mulheres abaixo de 20 anos: {abaixomulheres}")
        break



