a = input('segmento A: ')
b = input('segmento b: ')
c = input('segmento C: ')


if a == b and a == c and b == a and b == c :
    print('o triangulo e equilatero')

elif a != b and a != c and b != a and b != c:
    print('triangulo escaleno')
else:
    print('e um triangulo isoceles')