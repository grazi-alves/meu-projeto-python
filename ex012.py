#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = int(input('Qual o preço do produto que deseja comprar?:R$'))
d = p - (p*5)/100
print('O produto com 5% de desconto fica R${:.2f}'.format(d))