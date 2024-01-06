idade = []
name = []
somaIDD = 0
i = 0
for r in range(1,5):
    nome = input('o seu nome: ')
    sexo = input('seu sexo [M/F]: ')
    idd = int(input("Informe a idade: "))
    somaIDD = somaIDD + idd
    i += 1
    mediaIDD = int(somaIDD / r)

    if sexo == 'M':
        idade.append(idd)
if sexo == 'F' and idd <= 20 :
    print('nao ha mulheres maiores que 20 anos')



print("A média das idades da turma é de: ", mediaIDD)
print('o homem mais velho tem  sua idade de {} '.format(max(idade)))
