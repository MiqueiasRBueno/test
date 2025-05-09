from random import randint
from time import sleep

jogadores = dict()
for j in range(0, 4):
    jogadores[f'jogador {j + 1}'] = randint(1, 6)
for k, v in jogadores.items():
    sleep(0.8)
    print(f'{f'{k}'.title()} tirou {v}')
