cont = 0
soma = 0
for m in range(1,500, 2):
    if m%3 == 0:
        soma += m
        cont += 1
        print(soma)