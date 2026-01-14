#Até 9 anos mirim
#até 14 anos infantil
#até 19 anos junior
#até 20 anos senior
#acima master

import time

print("Vamos te mostrar a categoria de um atleta de acordo com sua idade")

time.sleep(2)

idade = int(input("Digite sua idade: "))

if idade <= 9:
    print("Mirim")
elif idade <= 14:
    print("infantil")
elif idade <= 19:
    print('Junior')
else:
    idade >= 20
    print("Master")