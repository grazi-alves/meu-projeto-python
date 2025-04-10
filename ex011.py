#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

pl = float(input('Qual a largura da parede do seu quarto? '))

pa = float(input('Qual a altura da parede do seu quarto? '))

print('A área dessa parede é {:.2f} m² e a quantidade de tinta necessária para pinta-la é {:.2f} litros'.format(pl*pa,(pl*pa)/2))
