#Faça um programa que mostre a tabuada de vários números, 
# um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

import time

print("Iremos montar um programa que fará tabuadas a vontade para ti, caso queira terminar digite um número negativo!")
time.sleep(2)

multiplicador = 0

while True:
        n = int(input("Digite qual tabuada você deseja: "))
        if n < 0:
             break
        while multiplicador < 10:
            multiplicador += 1
            print(f"{n} x {multiplicador} = {n * multiplicador}")
        if multiplicador == 10:
            multiplicador = 0
print("Muito Obrigado!")
    


