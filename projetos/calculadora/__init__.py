from funcoes import *;

menu = {'adição': soma, '+': soma, 'subtração': menos, '-': menos, 'multiplicação': vezes, '*': vezes, 'divisão': dividir, '/': dividir}

def calcule():
    while True:
        print(f"Opções: {','.join(list(menu.keys()))}")
        print("Ou aperte S para sair")
        escolha = input()
        if escolha == "S":
            break
        else:
            try:
                menu[escolha(input('Digite um número a:'),input('Digite um número b:'))]
            except KeyError:
                print("Opção inválida")
