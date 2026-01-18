#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

#APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO

import time

print("programa que leia uma frase qualquer e diga se ela é um palíndromo!")

time.sleep(2)

print("Preparado?")

time.sleep(2)

for C in range(1):
    palavra = str(input("Digite a palavra: ")).lower().replace(" ","")
    if palavra == palavra[::-1]:
        print("É um palindromo")
    else:
        print("Não é um palindromo")
    