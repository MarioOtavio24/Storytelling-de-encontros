import os
os.system ('cls')

print('Bem vindo ao melhor programa de relacionamentos do mundo!')
Nome=input('digite o seu nome: ')
idade=int(input('digite a sua idade: '))
if idade < 18:
    print('Proibidos menores de 18 anos criarem conta aqui!')
else:
    genero=input("digite a seu gênero: ")
    preferencia=input('digite a sua preferência: ')

    listahetero1=[['Ian emanuel', 'Raphael Prendes', 'José Junior', 'Mario Otavio']]
    if preferencia =='homem':
        print('Esses são os perfis recomendados para essa categoria')
        print(listahetero1)

    listahetero2=[['Amanda Silva','Jennifer Cristine','Rayane Krostyvikya','Sabrina Povskylia']]  #lista que tem perfis mulheres!
    if preferencia =='mulher':
        print('Essas são os perfis recomendados para essa categoria')
    print(listahetero2)
    print('Amanda Silva, gostou de você, ela é loira, olhos azul, gosta de dias nublados, para ficar lendo Shakespeare, principalmente Hamlet! E tomar chá')
    encontro=input('Digite sim, para gostar dela de volta ')
   
    if encontro =='sim':                                    
        print('vocês tem sentimentos mutuos um pelo outro!')            # esse bloco sinaliza se o usuário  aceita ou não a proposta
    elif encontro =='não':                                                      
            print('infelizmente vocês não tiveram sentimentos mutuos.')
        
    print('Você tem alguma ideia de date?')       
    encontro=input('Que tal esses lugares: aperte enter')
    lugaresparadate=[['Restaurante chinês','Restaurante Japonês','Shopping Center','Uma viagem misteriosa']]   # este bloco sinaliza os lugares da onde vai ser o encontro!
    print(lugaresparadate)
    lugaresparadate=input('digite um numero de 1 a 4: ')
    if lugaresparadate =='1':                                                                                  # este bloco sinaliza as opções dos restaurantes para o encontro.
        print('Você escolheu Restaurante chinês')
    elif lugaresparadate =='2':
        print('Você escolheu o Restaurante Japonês')
    elif lugaresparadate =='3':
        print('Você escolheceu o Shopping center')
    elif lugaresparadate =='4':
        print('você escolheu Uma viagem misteriosa') 
    if lugaresparadate =='1':
        print(' Amanda, adorou a ideia de restaurante chinês, ela está ansiosa para te encontar, mas falta perguntar que horas é o date né?')
    
    horas=input('Qual horas você quer se encontar com ela? digite um numero de 1 a 4: 13h, 16h, 19h, 21h ')  
    if horas =='1':
        print('você escolheu sair com ela a tarde as 13h')                              # este é o bloco que sinaliza as horas que você vai sair com a Amanda Silva!
    elif horas =='2':
        print('Você escolheu sair com ela a tarde as 16h')
    elif horas =='3':
        print('Você escolheu sair com ela a tarde as 19h')
    elif horas =='4':
        print('você escolheu sair com ela a tarde as 21h')
    print('==============================================================================================================')
    print('vocês se encontraram num sabado as 13h no restaurante chinês, ela está com um sorriso prateado na sua direção,')
    print('===============================================================================================================')
    reação=input('qual será a sua reação? digite um numero de 1 a 4: sorrir de volta, contar piada, beijar, ignorar, escolha com cuidado ein!')#esse bloco indicara as reações aos eventos.
    if reação =='1':
        print('==================================================')                                                                                                                            
        print('Você sorriu de volta, ela adorou a reciproca')
        print('=============================================')
    elif reação =='2':
        print('você quis contar uma piada,ela achou engraçado mas esquisito também')
    elif reação=='3':                                                                                                                                 #Aqui desenrola já no restaurante
        print('você quis beijar, ela te deu um celinho, porque evidentemente ela ainda não lhe conhece.Ela te achou audacioso demais cuidado!')        
    elif reação =='4':
        print('você quis ignorar, isso não te ajudou, ela não está com tantas boas impressões de você agora!')
    
    print('Vocês sentaram na mesa o garçom chegou, perguntando o que vão comer e beber? Você como um belo cavalheiro pergunta para madame o que ela gostaria de comer?')
    print ('e se ela tem alguma alergia?')
    
    garçon=input('O que você gostaria de pedir ao garçon para você comer? digite um numero de 1 a 4: Mapo Tofu, Frango kung pao, pato a pequim, Porco agridoce ') #Esse bloco diz respeito ao garçon, para pedir a comida para você.
    if garçon =='1':
        print('você escolheu Mapo tofu')
    elif garçon =='2':
        print('você escolheu Frango kung pao')
    elif garçon =='3':
        print('você escolheu pato a pequim')
    elif garçon =='4':
        print('Você escolheu o porco agridoce')
    print('===============================================================================================')
    print('agora você irá perguntar delicadamente o que a Amanda Silva ou melhor dizendo, a cremosa quer?')
    print('Amanda Silva "Eu gostaria de pato a pequim, parece ser uma delicia!".')
    print('===============================================================================================')
    print('Vocês acabaram de comer, agora obviamente você vai puxar um papinho né')
    print('===============================================================================================')
    conversa=input('Sobre o que você quer conversar com a Amanda Silva? digite um numero de 1 a 4: sobre literatura, sobre cinema, sobre música,sobre o clima ')
    if conversa =='1': #cada uma dessas opções de dialogo vão acarretar em histórias diferentes!
        print('você decidiu conversar sobre literatura com a Amanda silva')
        print('Amanda adora hamlet e outras obras de Shakespeare, ela também adora Tolkien e idade média no geral.')
        print('ela está te perguntando o que você adora ler em seu acervo no seu quarto?')
    elif conversa =='2':
        print('você decidiu conversar sobre cinema com a Amanda silva')
    elif conversa =='3':
        print('você decidiu conversar sobre musica com a Amanda silva')
    elif conversa =='4':
        print('você decidiu conversar sobre o clima com a Amanda silva.')
    leitura=input('O que você ama ler digite uma opção de 1 a 4: Hamlet,Hobbit,Retrato de Dorian Gray, Frankenstein ')
    if leitura =='1':
        print('Amo ler hamlet também')
    elif leitura =='2':
        print('Eu amo Hobbit e todos os livros incriveis do majestoso Tolkien')     #Bloco escrevendo sobre literatura!
    elif leitura =='3':                                                             
        print('Eu amo Retrato de Dorian Gray')                                                          
    elif leitura =='4':
        print('Eu adoro Frankenstein, da Maravilhosa Mary Shelley')
    print('===============================================================================')
    print('Eu não acredito que você ama ler hamlet também, Mas você também gosta de outras obras de William Shakespeare') #
    print('qual sua obra favorita dele?')
    print('===============================================================================')
    Shakespeare=input('Qual obra do Shakespeare você gosta? digite de 1 a 4: Macbeth, Otelo, Hamlet,Sonhos de uma noite de verão ')
    if Shakespeare =='1':
        print('O meu livro favorito de William Shakespeare é Macbeth, a mensagem de excesso de ambição e traição é impactante demais pra mim!')
    elif Shakespeare =='2':
        print('O meu livro favorito de William Shakespeare é Otelo, a mensagem de ciume,amor,inveja e relacionamento interracial é magnifico.Acho uma obra perfeita!')
        print('É uma obra perfeita uma das melhores já feitas pelo ser humano!')
    elif Shakespeare =='3':
        print('Hamlet é inexplicavel, a primeira vez que eu o li, eu chorei muito')
    elif Shakespeare =='4':
        print('é um livro extremamente bem humorado, eu sinto que eu estou numa floresta mágica, cujo o narrador me compeliu! Cheio de fadas, mitologia grega, com inglesa.')