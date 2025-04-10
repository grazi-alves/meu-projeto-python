#DEsenvolva um programa que pergunte a distãncia de uma viagem em km.
#Calcule o preço da passagem cobrando 0,50 por km para viagens de até 200 km e 0,45 para viagens mais longas

distancia = float(input("Qual a distancia da viagem desejada, em km?  "))
if distancia <= 200:
    p1 = distancia * 0.5
    print(f'O preço da passagem será {p1:.2f}')
else:
    p2 = distancia * 0.45
    print(f'O preço da passagem será {p2:.2f}')


       #ou


# distancia = float(input("Qual a distancia da viagem desejada, em km?  "))
# if distancia <= 200:
     #preço = distancia * 0.5
# else:
   #preço = distancia * 0.45

#print(f"O preço da passagem será {preço:.2f}")