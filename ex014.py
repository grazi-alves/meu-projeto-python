#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Digite um valor para temperatura em Celsius: '))

print('{}° Celsius convertido em Fahrenheit é {:.1f}'.format(c,1.8*c+32))