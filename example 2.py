nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
mean = (nota_1 + nota_2) / 2
print(f'Sua média é de {mean:.2f}')
if mean >= 6:
    print('Sua nota foi boa, parabéns!')
else:
    print('Sua nota foi ruim, estude mais!')
