#Refaça o exercício 35
#Acrescente o recurso de mostrar 
#Que tipo de triangulo será mostrado

#TOdos os lados iguais Equilatéro
#Isósceles Dois lados iguais
#Escaleno: Todos os lados Diferentes

import time

print("Começa agora!")
time.sleep(2)
lado1 = int(input("Digite o primeiro lado: "))
time.sleep(1)
lado2 = int(input("Digite o segundo lado: "))
time.sleep(1)
lado3 = int(input("Digite o terceiro lado: "))

lados=[lado1, lado2, lado3]

teste = 0

if lado1 < lado2 + lado3:
    teste += 1
if lado2 < lado1 + lado3:
    teste += 1
if lado3 < lado1 + lado2:
    teste += 1

if teste == 3:
    print("\33[1;32mPode ser um triângulo!")
else:
    teste < 3
    print("\33[1;31mNão pode ser um triângulo")

if len(set(lados)) == 1 and lados: #aqui ele vai tirar todos os elementos iguais e vai deixar apenas 1, caso tiver apenas um 1 elemento na lista é um equilátero
    print("É um triângulo equiláterio")

elif (lado1 == lado2) or (lado2 == lado3) or (lado1 == lado3):
    print("Triangulo Isósceles")

elif (lado1!=lado2) and (lado2!=lado3) and(lado1!=lado3):
    print("Triangulo Escaleno")



