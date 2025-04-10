# Crie um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos digitos separados
# em classes matemáticas

#number = int(input("Digite um número de 0 a 9999:  "))
#print(f'O numerador é: {number[3:4]}')
#print(f'O número de classe da dezena é: {number[2:3]}')
#print(f'O número de classe da centena é: {number[1:2]}')
#print(f'O número de classe de milhar é: {number[0:1]}')


# o modo que fiz não deu certo, pois so funciona com os 4 digítos.
# modo do Guanabara

num = int(input("Digite um número de 0 a 9999:  "))

#Divisão: 1234 / 10 = 123,4
#Divisão inteira: 1234 //10 = 123
#Módulo: 1234 % 10 = 4
#Pra ele descobrir a centena ele faz isso:
#Faz a divisão inteira por 100: 1234 // 100 = 12
#Depois pega o resultado e dividi por 10, mas pega só o resto dessa divisão (que é o módulo): 12 % 10 = 2
#Ou seja, a centena é 2.


un = num // 1 % 10
dz = num // 10 % 10
cn = num // 100 % 10
mi = num // 1000 % 10
print(f'O numerador é: {un}')
print(f'O número de classe da dezena é: {dz}')
print(f'O número de classe da centena é: {cn}')
print(f'O número de classe de milhar é: {mi}')