#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3= (n1+n2)/2
print('A média das notas é {:.2f}.'.format(n3))

#{:.2f}  significa depois do ponto flutuante coloque dois números.