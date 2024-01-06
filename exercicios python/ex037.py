nmr = int(input('digite um numero: '))
print(' [1] para binario;'
      ' [2] para octal;'
      ' [3] para hexa.')
escolha = int(input('escolha a maneira de converter: '))
binario = bin(nmr)
octal = oct(nmr)
hexa = hex(nmr)
if escolha == 1 :
    print(nmr, 'convertido para binario fica {}',format(binario))
elif escolha == 2:
    print(nmr, 'convertido para octal fica {}', format(octal))
elif escolha == 3:
    print(nmr, 'convertido para hexa fica {}', format(hexa))
