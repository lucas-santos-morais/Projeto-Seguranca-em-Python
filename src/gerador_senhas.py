'''

Programa: Gerador de Senhas
Autor: Lucas Santos Morais
Data: 05/09/2026

'''

import secrets
import string

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
            continue

        if tamanho <= 0:
            print('Erro: o tamanho da senha deve ser um número inteiro positivo.')
            continue

        return tamanho


    
def main():

    tamanho = ler_entrada()
    
    incluir_maiusculas = input('Incluir letras maiúsculas? (S/N): ').upper() == 'S'
    incluir_minusculas = input('Incluir letras minúsculas? (S/N): ').upper() == 'S'
    incluir_numeros = input('Incluir números? (S/N): ').upper() == 'S'
    incluir_simbolos = input('Incluir símbolos? (S/N): ').upper() == 'S'
    
    senha = gerar_senha(tamanho, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)

    print(f'Senha gerada: {senha}')


if __name__ == '__main__':
    main()