#Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.

#n1 = int(input('Digite um número: '))

#print('A tabuada de 1 ao 10 do número {} é\n {}\n {}\n {}\n {}\n '.format((n1),(n1*1),(n1*2),(n1*3),(n1*4)))
#print(' {}\n {}\n {}\n {}\n {}\n {}\n'.format((n1*5),(n1*6),(n1*7),(n1*8),(n1*9),(n1*10)))

#não consegui terminar desse jeito, mas vi um aluno que fez

#n = int(input('Digite um número para descobrir sua tabuada: '))
#print('Tabuada do {}:\n{}x{}:{}\n{}x{}:{}\n{}x{}:{}\n{}x{}:{}\n{}x{}:{}\n{}x{}:{}\n{}x{}:{}\n{}x{}:{}\n{}x{}:{}\n{}x{}:{}\n{}x{}:{}'.format(n, n, 0, n*0, n, 1, n*1, n, 2, n*2, n, 3, n*3, n, 4, n*4, n, 5, n*5, n, 6, n*6, n, 7, n*7, n, 8, n*8, n, 9, n*9, n, 10, n*10))

 #Jeito que o professor fez:
n1 = int(input('Digite um número para ver sua tabuada: '))

# '-'*12 vai repetir esse tracinho 12 vezes
print('-'*12)
print('{} x {:2} = {}'.format(n1,1,n1*1))
print('{} x {:2} = {}'.format(n1,2,n1*2))
print('{} x {:2} = {}'.format(n1,3,n1*3))
print('{} x {:2} = {}'.format(n1,4,n1*4))
print('{} x {:2} = {}'.format(n1,5,n1*5))
print('{} x {:2} = {}'.format(n1,6,n1*6))
print('{} x {:2} = {}'.format(n1,7,n1*7))
print('{} x {:2} = {}'.format(n1,8,n1*8))
print('{} x {:2} = {}'.format(n1,9,n1*9))
print('{} x {} = {}'.format(n1,10,n1*10))
print('-'*12)

