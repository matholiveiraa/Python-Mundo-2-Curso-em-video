#Desenvolva um programa que leia seis números inteiros.
#E mostre a soma apenas daqueles que forem pares. 
#Se o valor digitado for ímpar, desconsidere-o.

print("Iremos fazer um programa que lerá 6 números e fará a soma apenas dos pares")

conta = 0
valores = []

for C in range(6):
    n = int(input("Digite um valor: "))
    valores.append(n)
    if n % 2 == 0:
        conta += n

print(f"Todos os valores aqui: {valores}")
print(f"A soma de todos os valores pares é: {conta}")

