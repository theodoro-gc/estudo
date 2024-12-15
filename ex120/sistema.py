from ex120.lib.interface import *
from ex120.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas',  'Cadastrar nova pessoa',  'Sair do Sistema'])
    if resposta == 1:
        # opção de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome:  '))
        idade = int(leiaInt('Idade:  '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do programa... até logo!')
        break
    else:
        print('\033[31mERRO.. Digite uma opção valida!\033[m')
    sleep(2)

