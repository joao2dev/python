casa = float(input('qual o valor da casa? '))
salario = float(input('e quanto vc ganha? '))
anos = int(input('e em enquantos anos vc quer pagar? '))
pres = casa / (anos * 12)
min = salario * 30 / 100
print('a prestação ficara R$',pres)
if pres <= min:
    print(input('Seu emprestimo foi autorizado'))
elif pres >= min:
    print(input('seu emprestimo nao esta autorizado'))
