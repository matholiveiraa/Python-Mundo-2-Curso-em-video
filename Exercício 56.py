#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

import time
from datetime import datetime

print("Iremos ver nome, idade e sexo de 4 pessoas")
time.sleep(2)
print("No final mostraremos a média de idade do grupo, nome do homem mais velho e quantas mulheres tem menos de 20 anos")
time.sleep(2)



nomesm = []
idadem = []
nomef = []
idadef = []
contadormulheresmenor = 0

for C in range (4):
    sexo = str(input("Digite o sexo, F para feminino e M para masculino: ")).upper()
    if sexo == "F":
        nf = str(input("Digite o nome: "))
        nomef.append(nf)

        idadf = int(input("Digite a idade: "))
        idadef.append(idadf)

        if idadf < 20:
            contadormulheresmenor += 1

    if sexo == "M":
        nm = str(input("Digite o nome: "))
        nomesm.append(nm)

        idadm = int(input("Digite a idade: "))
        idadem.append(idadm)
    


print(f"A media de idade do grupo é {(sum(idadem) + sum(idadef)) / 4}")
print(f"Total de mulheres menor de idade: {contadormulheresmenor}")
if len(idadem) > 0:
    maior_idade = max(idadem) #Achou o maior valor
    indice = idadem.index(maior_idade) #E agora vai setar ele
    homem_mais_velho = nomesm[indice]
else:
    homem_mais_velho = "Não há homens no grupo"
print(f"O homem mais velho é: {homem_mais_velho}")




