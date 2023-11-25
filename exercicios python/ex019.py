import random

n1 = input('um nome: ')
n2 = input('outro nome: ')
n3 = input('mais um nome: ')
n4 = input('mais outro nome: ')
n5 = input('um ultimo nome: ')
names = [n1,n2,n3,n4,n5]
print('o nome sorteado foi: {}.'.format(random.choice(names)))
