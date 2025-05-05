galera = []
dados = []
while True:
    dados.append(str(input('Nome: ')).title().strip())
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if stop == 'N':
        break
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é o maior de idade!')
    else:
        print(f'{p[0]} é o menor de idade!')
