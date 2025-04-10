#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

p = float(input('Quantidade de km percorridos pelo carro alugado:'))
d = float(input('Quantidades de dias de aluguel:'))
total = (60*d) + (0.15*p)

print('Se o carro percorrer {:.1f}km durante {:.1f} dias, o total a se pagar é R${:.1f}'.format(p,d,total))