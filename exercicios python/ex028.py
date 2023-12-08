import random
import time
nmr = int(input('estou pensando em um sumero entre 0 e 5, qual e ele? '))
print('aguarde...')
time.sleep(2)
r = random.randint(0,5)
if nmr == r:
    print('vc acertou!!!')
else:
    print('vc errou!! o numero era {}'.format(r))