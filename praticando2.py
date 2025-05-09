from random import randint
from time import sleep

print(f'''\033[1;31m{'=' * 55}\033[m
{'Jogo de Dados':^55}
\033[1;31m{'=' * 55}\033[m''')
jogadores = dict()
for j in range(0, 4):
    jogadores[f'jogador {j + 1}'] = randint(1, 6)
print(f'''{'Valores Sorteados':^55}
\033[1;33m{'-' * 55}\033[m''')
for k, v in jogadores.items():
    sleep(1)
    print(f'{f'{k}'.title()} tirou {v}')
print(f'''\033[1;33m{'-' * 55}\033[m
{'RANKING DE JOGADORES':^55}
\033[1;33m{'-' * 55}\033[m''')
