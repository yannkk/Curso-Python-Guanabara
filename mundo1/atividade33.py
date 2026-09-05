n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite outro numero ai: '))
if n1 > n2 and n1 > n3:
    print(f'O maior numero é o {n1}')
if n2 > n1 and n2 > n3:
    print(f'O maior numero é o {n2}')
if n3 > n1 and n3 > n2:
    print(f'O maior numero é o {n3}')
if n1 < n2 and n1 < n3:
    print(f'O menor numero é o {n1}')
if n2 < n1 and n2 < n3:
    print(f'O menor numero é o {n2}')
if n3 < n1 and n3 < n2:
    print(f'O menor numero é o {n3}')