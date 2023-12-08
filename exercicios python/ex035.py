a = int(input('o valor do segmento a? '))
b = int(input('o valor do segmento b? '))
c = int(input('o valor do segmento c? '))
if a < b + c and b < a + c and c < a + b:
    print('os valores formam um triangulo')
else:
    print('os valores nao formam um triangulo')