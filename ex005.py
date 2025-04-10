
# Crie um algoritmo que peça um numero e depois dê o seu antecessor e sucessor

# old
n1 = int(input('Digite um número: '))
n2 = n1-1
n3 = n1+1
print('O seu antecessor é {} e o seu sucessor é {}'.format (n2,n3))


#nova versão
n1 = int(input('Digite um número: '))

print(f'Seu antecessor é {n1-1} e seu sucessor é {n1+1}!')