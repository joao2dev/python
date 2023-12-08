v1 = int(input('primeiro valor: '))
v2 = int(input('segundo: '))
v3 = int(input('terceiro: '))
maior = v1
if v1 > maior:
  maior = v1

if v2 > maior:
    maior = v2
if v3 > maior:
    maior = v3
print('Maior: ',maior)

menor = v1
if v1 < menor:
    menor = v1
if v2 < menor:
    menor = v2
if v3 < menor:
    menor = v3
    print('Menor: ', menor)