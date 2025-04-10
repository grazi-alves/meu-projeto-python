# faça um programa que leia o comprimento do co e ca e calcule a hipotenusa
import math
Co = int(input('Qual é o comprimento do cateto oposto do triângulo retângulo?  '))
Ca = int(input('Qual é o comprimento do cateto adjascente do triângulo retângulo?  '))
hipotenusa = math.hypot(Co, Ca)

print('Com os valores do cateto oposto {} e do cateto adjascente {} o valor da hipotenusa é {:.0f}'.format(Co,Ca, hipotenusa))
