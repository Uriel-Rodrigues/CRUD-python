#FUNÇÕES DE ESTILIZAÇÃO DO MENU
def linha():
    return '-*' * 24
def cabecalho(mensagem):
    print(linha())
    print(mensagem.center(48))
    print(linha())
#FUNÇÃO PARA LER A RESPOSTA
def leiaint():
    while True:
        resposta = input('digite sua resposta: ')
        try:
            n = int(resposta)
        except (ValueError, TypeError):
            print('- ERROR :( - Digite um numero inteiro valido')
        except(KeyboardInterrupt):
            print('- ERROR :( - Usuario preferiu não responder')
            return 0
        else:
            return n
#FUNÇÃO REFERENTE AO MENU
def menu ():
    cabecalho('MENU PRINCIPAL')
    opcoes = ['Cadatrar novo Usuario','Deletar Cadastro', 'Verificar Cadastros', 'Sair da Aplicação']

    C = 1
    for i in opcoes:
        print(f'{C} - {i}')
        C+= 1
    print(linha())
    print('digite abaixo uma das opções numericas referentes a sua escolha')
    resposta = leiaint()

    return resposta