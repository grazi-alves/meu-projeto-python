# faça um programa que leia o ângulo e mostre o sen, coss e tg desse Ângulo
import math
ang = float(input('Qual o ângulo deseja analisar? '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.atan(math.radians(ang))
print(' A partir do ângulo informado {} infere-se o seno {:.2f} o cos {:.2f} e a tangente {:.2f}'.format(ang,sen,cos,tg))