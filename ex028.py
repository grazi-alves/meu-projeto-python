# Leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente

nome = input('Digite seu nome completo: ').upper().strip()
n2 = nome.split()
print(f'O primeiro nome é: {n2[0]}')
print(f'O ultimo nome é: {n2[-1]}') 