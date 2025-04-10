#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n1 = float(input('Digite uma distância em metros:'))
n2 = n1*100
n3 = n1*1000

print('Essa distância em centímetros é {} e em milimetros {}.'.format(n2,n3))