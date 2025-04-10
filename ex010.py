#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
n1 = float(input('Digite quantos reais você tem:R$'))
print('Com R${:.2f}, você pode comprar US${:.2f}.'.format(n1,n1/5))