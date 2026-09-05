from math import sqrt
a = int(input('digite o numero do cateto adjacente: '))
o = int(input('digite o numero do cateto oposto: '))
h = sqrt(a**2 + o**2)
print(f'o valor da hipotenusa é {h}')