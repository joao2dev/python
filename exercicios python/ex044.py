prod = int(input('qual foi o valor da compra? '))
print('[1] para dinheiro')
print('[2] para cartão')
print('[3] para parcelar em 2x')
print('[4] para parcelar em 3x ou mais')
opção = input()
dinheiro = (10 / 100) * prod - prod
cartão = (5 / 100) * prod - prod
duasx = prod / 2

if opção == 1:
    print('sua compra ficara com o valor de {}'.format(dinheiro))
elif opção == 2:
    print('sua compra ficara com o valor de {}'.format(cartão))
elif opção == 3:
    print('sua compra ficara com o valor de {}'.format(duasx))
elif opção == '4':
    parcelas = int(input('em quantas pacelas desejas? '))
    juros = prod + (prod * 20 / 100)
    tres = juros / parcelas

    print('sua compra ficara com o valor total de {} e as parcelas com juros ficara {}'.format(juros,tres))