
 #Função
def config_exit (parametro):
    if parametro == 'exit':
        return 'parar'
    if parametro == 'back':
        return 'voltar'
    return '...'

 #Loop
while True:
#Menu Juros
    print('|--------------------|')
    print('| 1 - Juros Simples  |')
    print('|--------------------|')
    print('| 2 - Juros Composto |')
    print('|--------------------|')
    print('Digite Exit para Sair do Programa ou Back para voltar para o inicio')
    print('\n')

 #Escolha do Tipo de Juros
    escolha = (input('Escolha sua opção para calculo de Juros: ')).lower()

 #Config do exit/back 
    if escolha == 'exit':
            print('\n')
            break
    
    #Controle de erro-------------------------------------------------- 
    if escolha == '1' or escolha == '2':                             #|
         pass                                                        #|
    else:                                                            #|
        print('ERROR: Escolha o número dentro das opções (1 ou 2)')  #|
        print('\n')                                                  #|
        break                                                        #|
    #------------------------------------------------------------------

 #Escolha do Capital
    Capital = (input('Digite o Capital: ')).lower()
    print('\n')


 #Config do exit/back
    status = config_exit(Capital)
    if status == 'parar':
        break
    if status == 'voltar':
        continue

    #Controle de erro----------------------------------------------
    try:                                                         #|
                                                                 #|
        Capital = float(Capital)                                 #|
                                                                 #|
    except ValueError:                                           #|
        print('ERROR: O capital deve ser um numero!')            #|
        break                                                    #|
    #--------------------------------------------------------------


 #Menu de unidade de Taxa
    print('|-----------------|')
    print('| 1 - Taxa ao Mes |')
    print('|-----------------|')
    print('| 2 - Taxa ao Ano |')
    print('|-----------------|')
    print('| 3 - Taxa ao Dia |')
    print('|-----------------|')
    print('\n')

 #Escolha da unidade de Taxa
    unidade_taxa = input('Escolha de acordo com a unidade de tempo de sua Taxa: ').lower()

 #Config do exit/back
    if unidade_taxa == 'exit':
        print('\n')
        break
    if unidade_taxa == 'back':
        print('\n')
        continue

    #controle de error----------------------------------------------------------        
    if unidade_taxa == '1' or unidade_taxa == '2' or unidade_taxa == '3':     #|
         pass                                                                 #|
    else:                                                                     #|
        print('ERROR: Escolha o número dentro das opções (1, 2 e 3)')         #|
        print('\n')                                                           #|
        break                                                                 #|
    #---------------------------------------------------------------------------

 #Escolha da Taxa
    Taxa = (input('Digite a Taxa (sem o uso da %): ')).lower()

 #Config do exit/back
    status = config_exit(Taxa)
    if status == 'parar':
        break
    if status == 'voltar':
        continue

    #Controle de erro----------------------------------------------
    try:                                                         #|
                                                                 #|
        Taxa = float(Taxa) / 100                                 #|
                                                                 #|
    except ValueError:                                           #|
        print('ERROR: A taxa deve ser um numero!')               #|
        break                                                    #|
    #--------------------------------------------------------------
    print('\n')



 #menu de unidade de Tempo
    print('|------------------|')
    print('| 1 - Tempo ao Mes |')
    print('|------------------|')
    print('| 2 - Tempo ao Ano |')
    print('|------------------|')
    print('| 3 - Tempo ao Dia |')
    print('|------------------|')
    print('\n')

 #Escolha da unidade de Tempo
    unidade_tempo = (input('Escolha de acordo com a unidade de tempo do seu Tempo: ')).lower()

 #Config do exit/back
    if unidade_tempo == 'exit':
        print('\n')
        break
    if unidade_tempo == 'back':
        print('\n')
        continue

    #controle de error----------------------------------------------------------        
    if unidade_tempo == '1' or unidade_tempo == '2' or unidade_tempo == '3':  #|
         pass                                                                 #|
    else:                                                                     #|
        print('ERROR: Escolha o número dentro das opções (1, 2 e 3)')         #|
        print('\n')                                                           #|
        break                                                                 #|
    #---------------------------------------------------------------------------
    

 #Escolha do Tempo
    Tempo = (input('Digite o tempo: ')).lower()

 #Config do exit/back
    status = config_exit(Tempo)
    if status == 'parar':
        break
    if status == 'voltar':
        continue

    #Controle de erro----------------------------------------------
    try:                                                         #|
                                                                 #|
        Tempo = float(Tempo)                                     #|
                                                                 #|
    except ValueError:                                           #|
        print('ERROR: O tempo deve ser um numero!')              #|
        print('\n')                                              #|
        break                                                    #|
    #--------------------------------------------------------------
    print('\n')


 #Conversão da unidade de Tempo para a Taxa
    if unidade_taxa == '1':
        if unidade_tempo == '1': Tempo = Tempo
        if unidade_tempo == '2': Tempo = Tempo * 12
        if unidade_tempo == '3': Tempo = Tempo / 30
    elif unidade_taxa == '2':
        if unidade_tempo == '1': Tempo = Tempo / 12
        if unidade_tempo == '2': Tempo = Tempo
        if unidade_tempo == '3': Tempo = Tempo / 365
    elif unidade_taxa == '3':
        if unidade_tempo == '1': Tempo = Tempo * 30
        if unidade_tempo == '2': Tempo = Tempo * 365
        if unidade_tempo == '3': Tempo = Tempo


 #Formula de juros Simples/Composto
    if escolha == '1':
        JurosSimples = Capital * Taxa * Tempo
        print('='*30)
        print(f'Juros Simples: {JurosSimples:.2f}')
        montante = JurosSimples + Capital
        print(f'Montante: {montante:2f}')
        print('='*30)
        break

    if escolha == '2':
        JurosComposto = Capital * (1 + Taxa) ** Tempo - Capital
        print('='*30)
        print(f'Juros Composto: {JurosComposto:.2f}')
        montante = JurosComposto + Capital
        print(f'Montante: {montante:.2f}')
        print('='*30)
        break
