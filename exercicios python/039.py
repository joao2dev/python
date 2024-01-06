ano = int(input('sua data de nascimento: '))
aprovado = 2023 - ano
faltam = aprovado - 18
perdeu = 2023 - faltam
espera = 18 - aprovado
if aprovado < 18:
    print('ainda faltam {} anos para se alistar.'.format(espera))
    print('aguardamos voce em {}'.format(espera + ano))
elif aprovado == 18:
    print('alistesse imediatamente esse ano!!!')
if aprovado > 18:
    print('voce devia esta alistado ha {}'.format(faltam))
    print('voce deveria esta alistado desde {}'.format(perdeu))