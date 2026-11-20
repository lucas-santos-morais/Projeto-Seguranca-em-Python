'''
Programa: Validador de Senhas
Autor: Lucas Santos Morais
Data: 19/11/2026

'''

import string
import os

"""Váriavel que define o tamanho mínimo da senha."""
TAMANHO_MINIMO = 8


def validar_senha(senha):
    """Retorna um dicionário com cada critério e se foi atendido."""
    return {
        f'Pelo menos {TAMANHO_MINIMO} caracteres': len(senha) >= TAMANHO_MINIMO,
        'Letra maiúscula': any(c.isupper() for c in senha),
        'Letra minúscula': any(c.islower() for c in senha),
        'Número': any(c.isdigit() for c in senha),
        'Símbolo': any(c in string.punctuation for c in senha),
    }

def classificar_senha(criterios):
    """Classifica a senha de acordo com a quantidade de critérios atendidos."""
    atendidos = sum(criterios.values())

    if atendidos == len(criterios):
        return 'Forte'
    if atendidos >= 3:
        return 'Média'
    return 'Fraca'

def main():

    while True:
        print('\n== Validador de Senhas ==\n')

        senha = input('Digite a senha para validação: ')
            
        if senha.strip() == '':
            print("Erro: a senha não pode ser vazia.")
            os.system('cls')
            continue

        criterios = validar_senha(senha)

        print()
        for descricao, atendido in criterios.items():
            marca = '✔' if atendido else '✘'
            print(f'[{marca}] {descricao}')

        print(f'\nForça da senha: {classificar_senha(criterios)}')
        break

if __name__ == '__main__':
    main()

