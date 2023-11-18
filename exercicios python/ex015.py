Dias = float(input('dias rodados: '))
Km = float(input('kilometros percorridos: '))
var1 = Dias * 60
var2 = Km * 0.15
final = var1 + var2
print('o valor do aluguel foi: R${:.2f} '.format(final))