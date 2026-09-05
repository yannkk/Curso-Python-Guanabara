km = int(input('Quantos km tem a sua viagem? '))
menor = km*0.5
maior = km*0.45
if km <= 200:
    print(f'O preço da passagem será {menor}')
else: 
    print(f'O preço da passagem será {maior}')