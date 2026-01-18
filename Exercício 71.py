#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, 
# pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

import time


print("Iremos fazer um sistema de saque, você irá digitar quantos que você deseja sacar")
time.sleep(2)
print("Informaremos a quantidade de célula")
time.sleep(2)


while True:
    sacar = int(input("Digite o valor que deseja sacar: "))
    if sacar == 0:
        print("Obrigado por usar nossos serviços!!")
        break
    
    sacar50 = sacar / 50
    if sacar50 < 0:
        sacar50 = 0
    print(f"Cédulas de 50: {int(sacar50)}")

    sacar20= (int(sacar50)*50)
    sacar201 = (int(sacar50*50) - sacar20)/20
    if sacar20 < 0:
        sacar20 = 0
    print(f"Cédulas de 20: {int(sacar201)}") 

    sacar10= (int(sacar201)*20)
    sacar101 = (int(sacar201*20) - sacar10)/10
    if sacar10 < 0:
        sacar10 = 0
    print(f"Cédulas de 10: {int(sacar101)}") 

    sacar1 = str(sacar)[-1] #Este é um conversor
    print(f"Cédulas de 1: {sacar1}")

    