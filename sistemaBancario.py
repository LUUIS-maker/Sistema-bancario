saldo = 0
senha = 1108
tentativas = 3
cont = operacaodepo = operacaosaque = soma = somasaque = saque = deposito = 0
while tentativas > cont:
    acesso = int(input('Para acessar o sistema, digite a senha: '))
    cont += 1
    if acesso != senha:
        print('Senha incorreta. Restam {} tentativas...'.format(3-cont))
    if acesso == senha:
        print('Acesso liberado!')
        break
    if cont == tentativas:
        print('Acesso bloqueado!')
        break

while acesso == senha:
    print('===== BANCO =====')
    print('''
[ 1 ] Consultar saldo
[ 2 ] Depositar
[ 3 ] Sacar
[ 4 ] Sair
''')
    opc = int(input('Escolha uma opcao: '))
    if opc == 1:
        print('Seu saldo atual é R${}'.format(saldo))
    if opc == 2:
        deposito = float(input('Qual valor sera depositado: '))
        if deposito > 0:
            saldo = saldo+deposito
            print('Saldo atualizado com sucesso!')
            print('Seu saldo disponivel agora é R${}'.format(saldo))
            operacaodepo += 1
            soma = soma+deposito
        else:
            print('Valor invalido!')
    if opc == 3:
        saque = float(input('Qual o valor desejado: '))
        if saque <= 0:
            print('Valor invalido!')
        elif saque > saldo:
            print('Saldo insuficiente!')
        else:
            saldo = saldo-saque
            print('Saldo atualizado com sucesso!')
            print('Seu saldo disponivel agora é R${}'.format(saldo))
            operacaosaque += 1
            saque = saque
            somasaque = somasaque+saque
    if opc == 4:
        print('====== EXTRATO FINAL ======')
        print('Saldo final:R${}'.format(saldo))
        print('Total depositado:R${}'.format(soma))
        print('Total sacado:R${}'.format(somasaque))
        print('Quantidade de depositos: {}'.format(operacaodepo))
        print('Quantidade de saques: {}'.format(operacaosaque))
        print('Obrigado por utilizar nosso banco!')
        break
