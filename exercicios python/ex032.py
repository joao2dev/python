import datetime
import die
ano = int(input('digite um ano e se quiser ver o ano atual digite 0: '))

v = ano % 4
if ano == 0 :

    print('o ano atual e {}'.format(datetime.date.today().year))

if v == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} e bissexto'.format(ano))


else:
    print('esse ano nao e bissexto!!!')

