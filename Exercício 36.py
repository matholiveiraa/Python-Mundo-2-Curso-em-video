#Escreva um programa 
#3 entradas: Valor da casa, Salario, Quantas anos quer pagar
#Calcule a prestação mensal não pode exceder o valor de 30% do salário

import time

print("Veremos se o usuário consegue comprar uma casa, e ser aprovado ou negado")
time.sleep(1)

vcasa = int(input("Digite o valor da casa: "))
time.sleep(1)
salario = int(input("Digite o valor do salário: "))
time.sleep(1)
anos = int(input("Quer pagar em quantos anos: "))

prestacaomensal = (salario * (anos * 12))/vcasa
prestacaomensal = prestacaomensal*100
novotempo = 0
teste=float
teste1=float

if prestacaomensal * (anos*12) > vcasa:
    print(f"prestacaomensal ela já ultrapassa o valor da casa!")
    print(prestacaomensal * (anos*12))
    reajuste = prestacaomensal * (anos*12)
    teste=(vcasa / prestacaomensal)
    teste1=(teste/ 12)

if prestacaomensal > 0.30 * salario:
    print("Compra negada")

else:
    prestacaomensal < 0.30 * salario
    print("Compra permitida")
    print(f"{vcasa}, VALOR DA CASA")
    print(f"{salario}, SEU SALÁRIO")
    print(f"{anos}, ANOS QUE VOCÊ DESEJA")
    print(f"{teste1:.2f}, FIZEMOS A CORREÇÃO VOCÊ IRÁ PAGAR EM ISSO DE ANOS")
    print(f"{prestacaomensal}, PRESTAÇÃO MENSAL")

