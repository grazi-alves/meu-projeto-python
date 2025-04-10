#Faça o pc pensar em um numéro int entre 0 a 5 e peça para o usuario descobrir qual o foi o numero pensado pelo pc.
# o programa devera dizer se o usuario perdeu ou ganhou

from random import randint
from time import sleep
computador = randint(0,5) #faz o computador pensar
print('-'*30)
print('Vou pensar em um número entre 0 e 5, tente advinhar...')
print('-'*30)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS, Você acertou!')
else:
    print(f'Ganhei! Eu pensei no número {computador} e não no {jogador}')






