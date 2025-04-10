#Crie um programa que leia o nome completo de uma pessoa e mostre:


# O nome com todas as letras maíscúlas

nome = str(input('Digite seu nome completo:  '))
print(f'Seu nome completo em maiúsculo é: {nome.upper()}.')



# O nome com todas as minúsculas

nome = str(input('Digite seu nome completo:  '))
print(f'Seu nome completo em minúsculo é {nome.lower()}.')



# Quantas letras ao todo sem considerar espaços

nome = str(input('Digite seu nome completo:  ')).strip()
print(f'seu nome sem espaços tem {len(nome)-nome.count(' ')} letras.')

#ou

nome_completo = input("Digite seu nome completo: ")
quantidade_letras = len(nome_completo.replace(" ", ""))
print(f"Seu nome tem ao todo {quantidade_letras} letras (sem considerar os espaços).")



#Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo:  ')).strip()
print(f"A quantidade de letras do seu primeiro nome é {nome.find(' ')}")