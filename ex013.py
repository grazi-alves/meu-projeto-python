#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Qual é o seu salário? R$'))
a = s*1.15

print('O seu salário de {:.2f}, com 15% de aumento fica {:.2f}'.format(s,a))