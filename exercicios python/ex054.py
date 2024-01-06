from datetime import date
atual = date.today().year
maior = 0
menor = 0
for p in range(1,8):
    nasc = int(input('nascimento da {} pessoa? '.format(p)))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas maiores de idade'.format(maior))
print('{} pessoas menores de idade'.format(menor))