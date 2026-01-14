#Escreva um programa que leia um numero inteiro
#Na saida será escolhido 
#1 para binário
#2 para octal
#3 para hexadecimal

print("1 para binário")
print("2 para octal")
print("3 para hexadecimal")

n1 = int(input("Digite o valor: "))
escolha = int(input("Digite o a escolha: "))

if escolha == 1:
    print(bin(n1).replace('0b', ''))
elif escolha == 2:
    print(oct(n1).replace('0o', ''))
else:
    escolha == 3
    print(hex(n1).replace('0x', '').upper())