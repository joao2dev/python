nmr = int(input('digite um numero: '))
for p in range(1,nmr + 1):
    if nmr % 2 == 0 or nmr % 3 == 0 or nmr % 5 == 0:
        print(p)
    elif nmr % 2 >= 1 or nmr % 3 >= 1 or nmr % 5 >= 1:
        print(p)
if nmr % 2 == 0 or nmr % 3 == 0 or nmr % 5 == 0:
    print('o numero {} e nao e Primo'.format(nmr))
elif nmr % 2 >= 1 or nmr % 3 >= 1 or nmr % 5 >= 1:
    print('o numero e Primo')
