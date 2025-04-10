# leia um numero inteiro na tela e mostre se ele é par ou impar

n1 = int(input("Digite um número qualquer: ")) #Pede ao usuário para inserir um número
if n1%2==0: #O resto da divisao por 2
    print(f'O número digitado é par ')
else:
    print(f" O número {n1} é impar")

