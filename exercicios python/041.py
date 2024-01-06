ano = int(input('seu nascimento: '))
categoria = 2023 - ano
if categoria <= 9:
    print(categoria)
    print('atleta mirim')
elif categoria <= 14:
    print('atleta infantil')
elif categoria <= 19:
    print('junior')
elif categoria <= 25:
    print('senior')
elif categoria > 25:
    print('master')