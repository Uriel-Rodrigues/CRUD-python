# FUNÇÃO REFERENTE A INTERAÇÃO COM ARQUIVO
from ex115_sozinho.funcionalidades.sistema import *
def escrever_arquivo():
    dicionario = {
        'nome': str(input('Nome completo do usuario: ')),
        'endereco': str(input('endereço do usuario: ')),
        'nascimento': str(input('data de nascimento do usuario: '))
    }

    with open('cadastro_usuarios.txt', 'a') as arq:
        arq.write(f'{dicionario}\n')

def ler_arquivo():
    with open("cadastro_usuarios.txt", 'r') as arq:
        linhas = arq.readlines()
        if len(linhas) == 0:
            print("INFO: Você ainda não tem usuarios cadastrados")
            print("INFO: Digite a opção 1 no menu principal para iniciar seus cadastros")
        else:
            cont = 1
            for dicionario in linhas:
                cabecalho(f'USUARIO {cont}')
                cont += 1
                for chave, valor in eval(dicionario).items():
                    print(f'{chave}:{valor}')

def deletar_cadastro():
    nome = input('digite o nome completo do usuario a ser deletado: ')

    with open("cadastro_usuarios.txt", 'r') as arq:
        linhas = arq.readlines()

    linhas_atualizadas = [linha for linha in linhas if nome not in linha]

    with open("cadastro_usuarios.txt", 'w') as arq:
        arq.writelines(linhas_atualizadas)

    print(f'INFO: Usuario de nome {nome} deletado com sucesso')