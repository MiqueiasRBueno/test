name = str(input('Digite seu nome: ')).title().strip()
if name == 'Miquéias':
    print('Nossa, como seu nome é lindo, Miquéias!')
elif name == 'Ana' or name == 'Renato' or name == 'Letícia' or name == 'Leticia':
    print('Seu nome é bem popular no Brasil!')
else:
    print('Seu nome é bastante comum!')
print(f'Tenha um boa tarde {name}!')
