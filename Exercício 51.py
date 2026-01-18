#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
#No final, mostre os 10 primeiros termos dessa progressão.

#a10 = a1 + 9r

#An= a1 + (n - 1) * r

import time

print('''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.''')

time.sleep(2)

pt = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
contador = 0 

for C in range(pt, ((pt)+9*razao)+1, razao):
    contador += 1
    print(f"a{contador} = {C}")


