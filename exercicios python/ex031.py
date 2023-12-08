km = float(input('quantos km tera sua viagem?  '))
valor = km * 0.50
if km >= 200:
    print('a valor da viagem sera R${:.2f}'.format(km * 0.45))
else :
    print('o valor da viagem sera R${:.2f}'.format(valor))