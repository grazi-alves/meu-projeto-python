# Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome

nome = input('Digite o seu nome: ').strip()
print("SILVA" in nome.upper())

#ou

nome = input('Digite seu nome completo: ').strip()
print(f'O seu nome tem Silva? {'SILVA' in nome.upper()}')

#ou esse do chat gpt

def verificar_silva(nome):
    """Verifica se o nome contém 'Silva'."""
    return 'SILVA' in nome.upper()

def obter_nome():
    """Obtém o nome completo do usuário, tratando espaços extras."""
    return input('Digite seu nome completo: ').strip()

def main():
    """Função principal para execução do script."""
    nome = obter_nome()
    tem_silva = verificar_silva(nome)
    print(f'O seu nome tem Silva? {tem_silva}')

if __name__ == "__main__":
    main()