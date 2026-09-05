n = int(input('digite um numero: '))
##print(f'a tabuada deste numero é {n*1} {n*2} {n*3} {n*4} {n*5} {n*6} {n*7} {n*8} {n*9} {n*10}')

contador = 0
while contador < 101:
    if contador == 0:
        print("A tabuada deste número é 0", end=" ")
        contador += 1
    else:
        print(n * contador, end=" ")
        contador += 1