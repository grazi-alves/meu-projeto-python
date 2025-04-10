# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

#  NÃO CONSEGUI FAZER

cid = str(input('Digite o nome de uma cidade: ')).strip()
print(cid[:5].upper() == "SANTO ")

# ou

cidade = str (input ('Digite o nome da cidade: ')).strip()
c = cidade.title()
print (f'Começa com a palavra Santo? {'Santo' in c}')
