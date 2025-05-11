from operator import itemgetter
from random import randint
from time import sleep

print(f'''\033[1;31m{'=' * 55}\033[m
{'Jogo de Dados':-^55}
\033[1;31m{'=' * 55}\033[m''')
jogadores = {'Jogador 01': randint(1, 6), 'Jogador 02': randint(1,6),
             'Jogador 03': randint(1, 6), 'Jogador 04': randint(1,6)}
ranking = list()
sleep(1)
print(f'''{'Valores Sorteados':-^55}
\033[1;31m{'=' * 55}\033[m''')
for k, v in jogadores.items():
    sleep(1)
    print(f'{f'{k} tirou {v}':-^55}')
sleep(1)
print(f'''\033[1;31m{'=' * 55}\033[m
{sleep(1)}
{'RANKING DE JOGADORES':_^55}''')
sleep(1)
ranking = (sorted(jogadores.items(), key=itemgetter(1), reverse=True))
for i, v in enumerate(ranking):
    sleep(1)
    print(f'{f'{i + 1}º Lugar:':<2} {f'{v[0]} com':-^40}{f'{v[1]}':->5}')
sleep(1)
print(f'\033[1;31m{'=' * 55}\033[m')
