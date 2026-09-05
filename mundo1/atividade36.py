valor = int(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do salario: '))
anos = int(input('Digite a quantidade de anos: '))
meses = 12 * anos 
prestação = valor / meses 
if prestação > (salario * (30/100)):
    print('O empresitmo foi negado')
else:
    print(f'O emprestimo foi validado e o valor da prestação é {prestação}')
