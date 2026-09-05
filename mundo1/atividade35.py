n1 = int(input('Digite o comprimento de uma reta deste triangulo: '))
n2 = int(input('Digite outro comprimento do mesmo triangulo: '))
n3 = int(input('Digite outro comprimento do mesmo triangulo: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Essas retas podem formar um triangulo')
else:
    print('Essas retas nao podem formar um triangulo')