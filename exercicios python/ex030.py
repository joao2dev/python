import math
nmr = int(input('digite qualquer numero: '))
r = nmr % 2
if r == 0:
    print('o numero {} e par'.format(nmr))
else:
    print('o numero {} e impar'.format(nmr))
