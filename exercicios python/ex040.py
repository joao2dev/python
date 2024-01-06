nota1 = float(input('sua primeira nota: '))
nota2 = float(input('sua segunda nota: '))
media = (nota1 + nota2) / 2

if 7 > media >= 5:
    print('voce esta em recuperação!!!')
elif media < 6:
    print('voce esta em recuperação!!!')
if media > 7 :
    print('voce esta aprovado')