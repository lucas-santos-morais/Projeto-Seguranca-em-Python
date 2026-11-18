'''
Programa: Gerador de Senhas
Autor: Lucas Santos Morais
Data: 05/09/2026
'''

import secrets
import string
import os
import time

def gerar_senha(tamanho, maiusculas=True, minusculas=True, numeros=True, simbolos=True):

    caracteres = ''

    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Escolha pelo menos um tipo de caracter para gerar a senha.")
    
    return ''.join(secrets.choice(caracteres) for i in range(tamanho)) 

def ler_entrada():

    while True:
        try:
            tamanho = int(input('Digite o tamanho da senha: '))

        except ValueError:
            print('Erro: digite apenas números inteiros.')
            os.system('cls')
            continue

        if tamanho <= 0:
            print('Erro: o tamanho da senha deve ser um número inteiro positivo.')
            os.system('cls')
            continue

        return tamanho

def validar_resposta(pergunta):
    
    while True:
        try:
            resposta = input(pergunta).strip().upper()

            if resposta not in ('S', 'N'):
                raise ValueError("Digite apenas S ou N.")

            return resposta == 'S'
    
        except ValueError as erro:
            print(f'Erro: {erro}')
            os.system('cls')

def main():

    print("\n== Iniciando o Gerador de Senhas ==\n")

    tamanho = ler_entrada()

    incluir_maiusculas = validar_resposta('Incluir letras maiúsculas? (S/N): ')
    incluir_minusculas = validar_resposta('Incluir letras minúsculas? (S/N): ')
    incluir_numeros = validar_resposta('Incluir números? (S/N): ')
    incluir_simbolos = validar_resposta('Incluir símbolos? (S/N): ')

    senha = gerar_senha(tamanho, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)

    print('\nConfigurando sua senha...\n')

    time.sleep(2)

    print(f'Senha gerada: {senha}')

if __name__ == '__main__':
    main()