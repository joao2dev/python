import time
nome = str(input('seu nome completo; '))
time.sleep(0.1)
print('aguarde um momento')
time.sleep(1)
nmr = nome[0:]
print('seu nome em minusculo; {}'.format(nome.lower()))
print('em maiusculo: {}'.format(nome.upper()))
print('tem {} letras'.format(len(nome)))
print('e seu primeiro nome tem {} letras'.format(len(nome[0:].split())))