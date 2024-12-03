
nome  = str(input('digite o bnome completo do usuario a ser deletado '))
with open("funcionalidades\cadastro_usuarios.txt",'r') as arq
    linhas = arq.readlines()

with


''''arq = open("funcionalidades\cadastro_usuarios.txt",'r')
nome = input('nome: ')
lista = []
cont = 0
for linha in arq:
    linha_limpa = linha.strip()
    lista.append(linha_limpa)
for dicionario in lista:
    if nome in dicionario:
        del lista[cont]

    cont += 1

arq = open("funcionalidades\cadastro_usuarios.txt",'w')
for i in lista:
    arq.write(i)
    arq.write('\n')'''

'''deletar = input("nome: ")
for dicionario in arq:
    temp.append(dicionario.replace('',''))
print(temp)
for usuario in temp:
    if deletar in usuario:
        temp.remove(usuario)
        arq = open("funcionalidades\cadastro_usuarios.txt",'w')
        arq.write(temp)
print(temp)'''




'''cont = 1
for dicionario in arq:
    print('-'*24)
    print(f'USUARIO {cont}'.center(24))
    print('-' * 24)
    cont += 1
    for chave, valor in eval(dicionario).items():
        print(f'{chave}:{valor}')'''


#eval() valida o que esta sendo passado como string
