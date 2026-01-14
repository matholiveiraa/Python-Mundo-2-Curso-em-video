#faça um programa
#leia o ano de nascimento de um jovem
#Informe se ele ainda vai se alistar no exercito
#Se é hora de se alistar
#Se passou do tempo de se alistar

import time
import datetime

print("Processo de alistarmento por favor você irá colocar seu ano de nascimento")
time.sleep(2)
data_atual = datetime.date.today()
ano = int(input("Digite o ano de seu nascimento: "))
calculo = data_atual.year - ano

if calculo > 18:
    print("Já passou ja hora de se alistar, caso já se alistou ignore, caso não compareça imediatamente")
elif calculo == 18:
    print("Seu tempo de alistamento é agora")
else:
    calculo < 18
    print("Ainda não é sua hora de se alistar")
