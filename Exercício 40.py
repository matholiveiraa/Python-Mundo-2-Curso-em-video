#crie um programa que leia duas nota
#média baixo de 5 reprova
#entre 5 e 6.9 recuperação
#maior aprovado

import time

print("Iremos fazer um programa que calcule a média e dirá se você passou")
time.sleep(2)
nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))
calculo = (nota1+nota2)/2

if calculo>=7:
    print("Aprovado")
elif calculo < 5:
    print("Reprovado")
else:
    calculo <= 6.9
    print("Recuperação")