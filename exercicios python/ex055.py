lista = []
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('peso da {} pessoa: '.format(p)))
    lista.append(peso)
print('o maior peso sera {}'.format(max(lista)))
print('o maior peso sera {}'.format(min(lista)))
