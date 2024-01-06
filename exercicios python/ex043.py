peso = float(input('seu peso: '))
altura = float(input('altura: '))
imc = peso / (altura * altura)
if imc <= 18:
    print('magreza')
elif imc <= 24:
    print('normal')
elif imc <= 29:
    print('sobrepeso')