#Refaça o DESAFIO 9 mostrando a tabuada de um número que o usuário escolher só que agora utilizando um laço for

import time

print("Iremos fazer uma tabuada para você!")

time.sleep(2)

n = int(input("Digite o valor da tabuada que deseja: "))

contador = 0

for C in range(n,(n*10)+1,n):
    contador += 1 
    print(f"{n} x {contador} = {C}")