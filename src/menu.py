'''
Programa: Menu de Senhas
Autor: Lucas Santos Morais
Data: 26/11/2026

'''

import time
import os


while True:
    print(" == Menu de Senhas ==\n")

    print("""
    1 - Gerar senha
    2 - Ver senhas salvas
    0 - Sair
    """)

    try:
     escolha = int(input("\nEscolha uma opção:"))

    except ValueError:
        print("Erro: Digite apenas números inteiros.")
        time.sleep(2)
        os.system('cls')
        continue

