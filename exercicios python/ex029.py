v = int(input('em qual velocidade vc esta dirigindo? '))
mul = v*7
if v >= 80:
    print('vc sera multado em R${} por alta velocidade!!!'.format(mul))
else:
    print('voce esta dentro da velocidade, pode continuar a viagem')