# Que leia um frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A'
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a ultima vez

frase = str(input('Digite uma frase: ')).upper().strip()
print(f'Quantas vezes aparece a letra (A): {frase.count("A")}')
print(f'A posição em que a letra (A) aparece pela primeira vez é: {frase.find('A')+1}°')
print(f'posição em que a letra (A) aparece pela ultima vez é: {frase.rfind('A')+1}')