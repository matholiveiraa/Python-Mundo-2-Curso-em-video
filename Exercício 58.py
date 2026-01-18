#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
import time
escolha = [0,1,2,3,4,5,6,7,8,9,10]

print("Iremos fazer um jogo da adviganhação com você tente acertar de 0 a 10, iremos contar seues erros!")
time.sleep(2)
print("Vamos lá?")
escolhajogador = 12
escolhapc = 0
contagem = 0

while escolhajogador != escolhapc:
    escolhapc = random.choice(escolha)
    escolhajogador=(int(input("Digite o valor, contaremos o erro: ")))
    if escolhajogador != escolhapc:
        contagem += 1
if escolhajogador == escolhapc:
    print("Parabens você acertou!!")
    print(f"Número de erros {contagem}")
