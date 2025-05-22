def mensagem(msg):
    print(f'''\033[1;32m{'-' * 60}\033[m
\033[1;33m{msg:^60}\033[m
\033[1;32m{'-' * 60}\033[m''')

def soma(a, b):
    print(f'A = {a} e B={b}')
    s = a + b
    print(f'A soma A + B = {s}')


mensagem('Teste de Parâmetros')
soma(4, 5)