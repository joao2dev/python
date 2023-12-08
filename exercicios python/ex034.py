sal = float(input('qual o seu salario? '))
aumento = (sal * 10) / 100 + sal
if sal <= 1250.00:
    print('o aumento sera de {:.2f}'.format((sal * 15) / 100 + sal))
else:
    print('o aumento sera de {:.2f}'.format(aumento))
