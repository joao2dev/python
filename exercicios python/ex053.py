frase = str(input('escreva um frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('o inverso de {} e {}'.format(junto,inverso))
if inverso == junto:
    print('isso e um palidromo')
else:
    print('nao e um palidromo')