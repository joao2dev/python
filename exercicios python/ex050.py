cont = 0
soma = 0
for n in range(1,7):
    num = int(input('digite o {} numero: '.format(n)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('a soma desses numeros sera {}, e a quantidades de pares sera {} '.format(soma, cont))