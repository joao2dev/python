nome = input('digite uma frase: ').strip()
print('essa frase possui {} letras A'.format(nome.count('a')+1))
print('ela aparece na {} posiçao'.format(nome.find('a')+1))
print('e a ultima letra A aparece na {} posiçao'.format(nome.rfind('a')))