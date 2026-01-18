#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, 
#mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, 
#peça a digitação novamente até ter um valor correto.

import time


print("Iremos fazer um programa que lerá o sexo de uma pessoa caso errado peça novamente")

time.sleep(2)



while True:
    sexo = str(input("Digite o sexo: ")).upper()
    if sexo == "M" or sexo == "F":
      print("Obrigado!")
      break # Sai do loop
    else:
       print("tente novamente")