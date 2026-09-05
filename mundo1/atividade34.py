salario = int(input('Digite o salario de seu funcionario: '))
aumens = salario * 10/100 + salario
af = salario * 15/100 + salario
if salario < 1.250:
    print(f'O novo salario dele será: {af}')
else:
    print(f'O novo salario dele será: {aumens}')    