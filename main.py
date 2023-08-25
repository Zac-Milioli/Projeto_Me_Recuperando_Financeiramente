import time

print('\n'*150)
while True:
    valor = open('devendo.txt', 'r').readlines()[0]
    renda = open('renda.txt', 'r').readlines()[0]
    usuario = open('usuario.txt', 'r').readlines()[0]
    print('/ '*45)
    opt = input(f'\nBem vindo(a) {usuario}\n\nAtualmente devendo: R$ {valor}\n\nO que você deseja fazer?\n\n[0]Alterar dados do cadastro\n[1]Mostrar situação\n\n[ENTER]Encerrar o programa\n\n{"/ "*45}\n\n--> ')
    if opt == '0':
        config = True
        while config:
            print('\n'*150)
            renda = open('renda.txt', 'r').readlines()[0]
            valor = open('devendo.txt', 'r').readlines()[0]
            usuario = open('usuario.txt', 'r').readlines()[0]
            print('/ '*45)
            opc = input(f'\nDados de {usuario}\n\nDevendo R$ {valor}\nRenda mensal R$ {renda}\n\nO que você deseja alterar?\n\n[0]Alterar valor que deve\n[1]Alterar renda mensal\n[2]Alterar nome de usuário\n\n[ENTER]voltar\n\n{"/ "*45}\n\n--> ')
            print('/ '*45)
            if opc == '':
                config = False
                print('\n'*150)
            elif opc == '0':
                print('\n'*150)
                print('/ '*45)
                novo_valor = input(f'\n\nAtualmente devendo: R$ {valor}\n\nPara qual valor você deseja alterar?\n\n[ENTER]Cancelar\n\n{"/ "*45}\n\n--> ')
                if novo_valor != '':
                    open('devendo.txt', 'w').write(novo_valor)
                print('\n'*150)
            elif opc == '1':
                print('\n'*150)
                print('/ '*45)
                novo_valor = input(f'\n\nRenda mensal atual: R$ {renda}\n\nPara qual valor você deseja alterar?\n\n[ENTER]Cancelar\n\n{"/ "*45}\n\n--> ')
                if novo_valor != '':
                    open('renda.txt', 'w').write(novo_valor)
                print('\n'*150)
            elif opc == '2':
                print('\n'*150)
                print('/ '*45)
                novo_valor = input(f'\n\nNome de usuário: {usuario}\n\nPara qual nome você deseja alterar?\n\n[ENTER]Cancelar\n\n{"/ "*45}\n\n--> ')
                if novo_valor != '':
                    open('usuario.txt', 'w').write(novo_valor)
                print('\n'*150)
    elif opt == '1':
        print('\n'*150)
        print('/ '*45)
        print('\n\nSua situação\n\n')
        quitar = float(valor)/float(renda)
        if quitar > round(quitar-0.5, 0):
            quitar_round = round(quitar-0.5, 0)+1
        else:
            quitar_round = quitar
        resto = (float(renda)*quitar_round)-float(valor)
        print(f'{usuario},\nConsiderando sua renda mensal de {renda} e sua dívida de {valor}...\n\nVocê vai levar {quitar_round:.0f} meses para pagar sua dívida ({round(quitar, 2)} meses).\n\nAo pagar a última parcela sobrará R$ {resto} da sua renda.\n\n')
        print('/ '*45)
        input('\n\nPressione qualquer tecla para continuar\n')
        print('\n'*150)
    elif opt == '':
        break

print('\n'*150)
print('Programa encerrado\n')