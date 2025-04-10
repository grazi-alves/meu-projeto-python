#Leia a velocidade do carro.
# Se ele ultrapassar 80km/h mostre uma mensagem que ele foi multado.
# A MULTA VAI custar 7,00 por cada km acima do limite

v1 = float(input(" Qual a velocidade atual do carro?  "))
if v1 > 80: # Usa somente condição simples
    multa = (v1 - 80) * 7
    print(f'Você ultrapassou o limite permitido de 80km/hr e foi multado! \n Deve pagar,portanto, {multa}')
print(" Tenha um Bom dia \n Dirija em segurança!")





