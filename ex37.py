senha = str(input('Digite uma senha de 8 a 16 caracteres: '))
tamanhoDaSenha = len(senha)
temEspacoEmBranco = " " in senha
if temEspacoEmBranco:
    print('\033[0;31m Erro: A senha não pode conter espaços em branco.')
    str(input(senha))
else:
    if tamanhoDaSenha >= 8 and tamanhoDaSenha <= 16:
       confirmacaoDeSenha = str(input('Escreva novamente a sua senha: '))
       if senha == confirmacaoDeSenha:
           print('\033[0;32m Senha criada com sucesso!')
       else:
           print('\033[0;31m Erro: As senhas não conhecidem.')
    else:
        if tamanhoDaSenha < 8:
            print('\033[0;31m Erro: Sua senha tem que ter no mínimo 8 caracteres.')

        else:
            print('\033[0;31m Erro: Sua senha tem que ter no máximo 16 caraceres.')
