import math
c1 = float(input('qual o valor do cateto oposto?'))
c2 = float(input('qual o valor do cateto adjacente?' ))
print('o valor da hipotenusa sera: {:.2f} '.format(math.hypot(c1,c2)))
