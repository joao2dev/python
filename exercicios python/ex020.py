import random

n1 = input('um nome: ')
n2 = input('outro nome: ')
n3 = input('mais um nome: ')
n4 = input('mais outro nome: ')
n = [n1, n2, n3, n4]
random.shuffle(n)
print(n)
