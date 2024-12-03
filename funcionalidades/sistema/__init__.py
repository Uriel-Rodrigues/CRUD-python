from ex115_sozinho.funcionalidades.interface import *
from ex115_sozinho.funcionalidades.arquivo import *
def crud():
    while True:
        resposta = menu()
        if resposta == 1:
            cabecalho('Cadastrar novo Usuario')
            escrever_arquivo()
            while True:
                novo = input('gostaria de cadastrar um novo usuario? sim/nao: ')
                if novo in "simSIM":
                    escrever_arquivo()
                else:
                    break
        elif resposta == 2:
            cabecalho('Deletar cadastro')
            deletar_cadastro()
            while True:
                novo = input('gostaria de deletar outro usuario? sim/nao: ')
                if novo in "simSIM":
                    deletar_cadastro()
                else:
                    break
        elif resposta == 3:
            cabecalho('Cadastros')
            ler_arquivo()
