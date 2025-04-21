
# IDEIAS:
#
#   
#
#   Fazer animaçãozinha de JO \n - KEN \n - PO \n e mostrar o resultado da rodada 
#   COM TEXTO ASCII A LINHA DE CIMA
#
#   Mostrar pontuação dos jogadores no menu
#
#   Se o usuário já jogou o modo pvp, o programa lembra disso e pergunta se os jogadores querem trocar de nome.
#
# ANOTAÇÕES
#   
#   Professora, enquanto fazia isso aqui fiquei em dúvida sobre qual é mais importante: É melhor que o código seja mais eficiente mas mais díficil de entender, ou
#   menos eficiente mas mais fácil de entender?? 
#   Tem coisas que eu poderia repetir mais vezes, ou mudar um pouco a estrutura, mas daí acho que acabaria criando muitas variáveis, ou só repetindo desnecessariamente mesmo
#
#   - dar clear direito quando jogarem 
#   - polir diálogos, timings e testar varias possibilidades de sacanagem do usuario, ou caminhos naturais aleatorios
#
# ERROS:    
# 
#   Quando o usuário for optar pela quantidade de rodadas, ele pode digitar uma string e quebrar o código. Não sei oq fazer, pq a prof limitou nossos recursos pra usar outras coisas q counterariam isso
#

import time # tempo
import random # random
import os # clear no terminal

nome1 = "default1" # essas variaveis nome1 e nome2 são usadas posteriormente para atribuir nomes aos jogadores.
nome2 = "default2" # também sao usadas para verificar se o jogador trocou o nome ou não, mudando alguns diálogos.
acabouDeNomear = False # feita pra perguntar se querem mudar de nome. fica positiva quando acabam de trocar, pra evitar ficar perguntando repetidas vezes em pouco tempo.

modo = "abc"

melhorDeQuantasRodadas = 3
rodadasPraGanhar = int((melhorDeQuantasRodadas + 1 )/2)

vitoriasJogador1 = 0
vitoriasJogador2 = 0

partidasJogadas = 0 # contabiliza quantas partidas o usuário jogou no total
pvpJogados = 0  # contabiliza jogador x jogador (player vs player)
pveJogados = 0 # contabiliza jogador x máquina (player vs environment)
eveJogados = 0 # contabiliza máquina x máquina (environment vs environment)
permaVitoriasJogador1 = 0
permaVitoriasJogador2 = 0

escolhaDeNome = "0" # essa parte do codigo ta completamente uma bosta eu fiz numa confusao maluca tem que dar um revamp nessa joça

terminar = False # nos fins dos jogos o usuario pode escolher pra sair do programa, aí isso aqui é definido como True, e no começo do loop principal é checado e da break pra acabar o programa
voltarMenu = False # Alguns lugares o usuário quer voltar pro menu e fica mais organizado definir uma variavel só pra isso e ir mandando ele por if: {break}
while True:

    # definir algumas variaveis no inicio do menuloop:
    vitoriasJogador1 = 0
    vitoriasJogador2 = 0

    prosseguir = "1" # jeito que achei de fazer a pessoa digitar pra continuar em alguns diálogos, ele é definido aqui pois algumas lógicas quebrariam se ele nao fosse setado como 1 no começo do loop.
    voltarMenu = False

    if modo == "5": # sair do programa, deixei ele aqui pq quando alguem termina um modo e quer fechar o programa, a pessoa é jogada pro menu e cai aqui com o modo definido como "5"; tem que estar antes de tudo no código.
        print("=-=-=-=-=-=-=Você escolheu SAIR=-=-=-=-=-=-=\n\n")

        print(f"{pvpJogados} partidas JxJ jogadas!\n {pveJogados}partidas JxIA jogadas!\n {eveJogados} partidas IAxIA assistidas!")
        

        if nome1 == "default1" and nome2 == "default2": # se os nomes dos dois jogadores nao foram modificados
            print(f"Você nem jogou direito e vai sair já?? Tá bom né, até mais!!!! :))\n\n")

        elif nome2 == "default2": # se o nome do segundo jogador nao foi modificado
            
            print(f"\n\n| {nome1} ganhou {permaVitoriasJogador1} partidas em geral!")
            print(f"Muito obrigado {nome1} por usar nosso programa de Jokenpô!!! Até mais!!!! :))\n\n")

        else: # se os dois nomes foram modificados
            
            print(f"| {nome1} ganhou {permaVitoriasJogador1} partidas em geral!")
            print(f"\n| {nome2} ganhou {permaVitoriasJogador2} partidas em geral!")
            print(f"Muito obrigado {nome1} e {nome2} por usarem nosso programa de Jokenpô!!! Até mais!!!! :))\nFeito por Luis Felipe Quintiliano, Larissa Adames, Davi Cagnato\n\n")

        
        

        break


    print(f"\n=-=-=-=-=-=-=Eai! Bem-vindo ao MELHOR JOKENPÔ DO PLANETA!!!!!=-=-=-=-=-=-=\n")
    print(f"-------> HUMANO X HUMANO - Quero batalhar com meu amiguinho >:) [1]\n")
    print(f"-------> HUMANO X MÁQUINA - Quero acabar com TODAS as máquinas!!! [2]\n")
    print(f"-------> MÁQUINA X MÁQUINA - Quero ver os robôs se detonando [3]\n")
    print(f"-------> TUTORIAL - Como que joga isso? Me ajuda pelo amor de Deus! [4]\n") # <- perguntar pra prof se pode botar um botão a mais de tutorial, ou se só mete o tutorial antes do jogo msm
    print(f"-------> SAIR - Eu quero sair, tô bem de boa, Valeu! ^^ [5]\n") 
    print(f"=-=-=-=-=-=-=-==--===-====-=====-========-=====-====-===--==-=-=-=-=-=-=-=\n")

    modo = input(f"Digite o número da sua opção: ") # isso propositalmente é uma string, pra caso a pessoa digite algo errado o codigo nao quebrar

    if modo == "1": # modo player x player

        while True: # loop do modo 1 

            vitoriasJogador1 = 0
            vitoriasJogador2 = 0
        
            prosseguir = "1"
            escolhaDeNome = "0" # 
            print(f"\n\n=-=-=-=-=-=-=Você escolheu o modo HUMANO X HUMANO=-=-=-=-=-=-=\n\n")

            if voltarMenu == True: # setado no fim da rodada se o usuário optou por voltar ao menu
                break

            while pvpJogados == 0: # se já jogaram uma partida pvp, o usuario vai cair no else, que vai perguntar se querem trocar de nome ou nao.

                if acabouDeNomear == False: # pra evitar repetidas vezes de ficar perguntando o nome, caso algo faça o usuario voltar antes de começar o jogo
                    nome1 = input(f"-------> Jogador 1, por favor digita o seu nome: ")
                    nome2 = input(f"-------> Agora, Jogador 2, digita o seu nome aí também: ")
                    acabouDeNomear = True
                    break
                else:
                    break

            else:

                if acabouDeNomear == False: # pra evitar repetidas vezes de ficar perguntando o nome, caso algo faça o usuario voltar antes de começar o jogo

                    if escolhaDeNome == "0": # só entrará aqui se estiver como "0", q é definido no começo do loop acima

                        print(f"Eu lembro de vocês {nome1} e {nome2}, vocês querem continuar jogando com esses nomes ou vão trocar?")
                        print(f"-------> Queremos continuar com nossos nomes! [1]")
                        print(f"-------> Vamos trocar de nome, por favor! [2]")
                        acabouDeNomear = True
                        escolhaDeNome = input("da a escolha")

                        if escolhaDeNome == "2":
                            nome1 = input(f"-------> Então tá, Jogador 1, por favor digita o seu novo nome: ")
                            nome2 = input(f"-------> E você Jogador 2, o seu novo nome é: ")

            
            print(f"\nPor último, {nome1} e {nome2}, vocês querem que o jogo acabe com quantas rodadas? \nExemplo: Melhor de [3] rodadas, Melhor de [5] rodadas... Pode escolher qualquer número inteiro ímpar positivo!") # <- Melhorar diálogo?
            melhorDeQuantasRodadas = int(input(f"\n\n-------> Digite um número para a quantidade de Melhor de [___] rodadas: ")) # <- Melhorar diálogo? I
            # aqui infelizmente nao tem o que fazer, o usuário pode digitar uma string e cagar o código. com as opçoes que a prof nos deu, nao tem um jeito muito pratico de counterar isso :/

            # O que acontece é o seguinte: 
            # Esse código calcula quantas rodadas são necessárias para o usuário ganhar, isso deixa o programa mais intuitivo e esclarecido.
            # Se a opção de "Melhor de Quantas Rodadas" for ímpar, ele soma esse número com 1, e divide por 2. Ex: O usuario escolhe 5, então (5 + 1)/2 = 3.
            # 3 é a quantidade de rodadas necessárias para ganhar nesse caso.
            #
            # Caso a opção de "Melhor de Quantas Rodadas for par", o programa deve atuar diferentemente:
            # Ele soma esse número com 2, e divide por 2. Ex: O usuario escolhe 6, então (6 + 2)/2 = 4
            # Um pouco à frente no código, o programa define o "Melhor de Quantas Rodadas como += 1", então, no fim das contas, se o usuário optar por
            # um número par, o programa pegará o próximo ímpar, pra que tudo fique certinho.
            # Eu não defino o "Melhor de Quantas Rodadas += 1" nessa parte anterior, pq eu queria colocar um diálogo especial, q precisa modificar a variavel depois daí.

            if melhorDeQuantasRodadas %2 != 0:

                rodadasPraGanhar = int((melhorDeQuantasRodadas + 1 )/2) # se for impar, calcula a quantidade de rodadas que alguém precisa ganhar para acabar
            else:
                rodadasPraGanhar = int((melhorDeQuantasRodadas + 2)/2) # se for par, calcula a quantidade de rodadas que alguém precisa ganhar para acabar

            if melhorDeQuantasRodadas >= 10:
                print(f"\nCalma lá gente, vocês têm certeza que querem jogar tantas rodadas assim? Pode acabar demorando demais!")
                time.sleep(1.5)
                print("\nA gente quer continuar assim mesmo! [1]")
                print("\nÉ verdade, acho melhor voltar! [2]")
                
                prosseguir = input("\n-------> Digite a sua opção: ")

            if prosseguir == "1":

                print("\n" * 100)

                if melhorDeQuantasRodadas % 2 != 0 and melhorDeQuantasRodadas > 1 : # se o número for IMPAR e MAIOR QUE 1 entao roda o codigo normal

                    print(f"Beleza, vocês então vão jogar um Melhor de {melhorDeQuantasRodadas}, ou seja, quem fizer {rodadasPraGanhar} primeiro vence!\n")
                    time.sleep(4)
                    print(f"Boa Sorte {nome1} e {nome2}!")
                    time.sleep(1.5)
                    pass
                
                elif melhorDeQuantasRodadas % 2 == 0 and melhorDeQuantasRodadas > 1: # se o numero for PAR e MAIOR QUE 1, ele soma 1 no numero
                    melhorDeQuantasRodadas += 1
                    print(f"Beleza, eu dei uma ajustada porque o número tinha que ser ímpar, mas então vocês vão jogar um Melhor de {melhorDeQuantasRodadas}, ou seja, quem fizer {rodadasPraGanhar} primeiro vence!\n")
                    time.sleep(4)
                    print(f"Boa Sorte {nome1} e {nome2}!")
                    time.sleep(1.5)
                    pass

                elif melhorDeQuantasRodadas == 1 : # se o numero for IGUAL A 1, tem esse diálogo especial
                    print(f"Então vocês vão jogar só uma rodada? Interessante! Que vença o melhor!!\n")
                    time.sleep(3)
                    print(f"Boa Sorte {nome1} e {nome2}!")
                    time.sleep(1)
                    pass # pass passa adiante


                elif melhorDeQuantasRodadas < 1: # se o numero for MENOR QUE UM, ele manda o pessoal de volta pro menu
                    print(f"\nVocês tão de sacanagem né? Esse número nem faz sentido! Que feio, {nome1} e {nome2}! Vou mandar vocês de volta para o menu >:(\n")
                    input("Digita alguma coisa pra voltar pro menu >:(")
                    voltarMenu = True
                    continue
                
                print("\nJO")
                time.sleep(0.5)
                print("\nKEN")
                time.sleep(0.5)
                print("\nPÔ!")
                time.sleep(0.5)

                while (vitoriasJogador1 < rodadasPraGanhar) and (vitoriasJogador2 < rodadasPraGanhar): # roda esse código enquanto a quantidade vitorias de um dos jogadores for menor que a variavel rodadasPraGanhar
                    
                    while True: # loop jogador1

                        print(f"\n=-=-=Vamo lá!! {nome1}, não deixa o/a coleguinha {nome2} olhar a sua escolha hein!!=-=-=")
                        print("\n- [Pedra] ou [1]\n- [Papel] ou [2]\n- [Tesoura] ou [3]\n")
                        
                        escolha1 = str(input(f"-------> {nome1}, digite qual você quer! ")).lower().strip()

                        if escolha1 == "pedra" or escolha1 == "1":
                            escolha1 = "pedra"
                            break
                        elif escolha1 == "papel" or escolha1 == "2":
                            escolha1 = "papel"
                            break
                        elif escolha1 == "tesoura" or escolha1 == "3":
                            escolha1 = "tesoura"
                            break
                        else:
                            print(f"Calma lá né! {nome1}, você digitou errado sem querer ou tá brincando comigo? Vai de novo...")
                            time.sleep(1.5)
                            continue

                    while True: # loop jogador2
                        print(f"\n=-=-=Agora é a vez de {nome2}!! Não deixa {nome1} dar uma espiadinha, olha lá!!¬¬=-=-=")
                        print("\n- [Pedra] ou [1]\n- [Papel] ou [2]\n- [Tesoura] ou [3]\n")
                        
                        escolha2 = str(input(f"-------> {nome2}, digite qual você quer! ")).lower().strip()

                        if escolha2 == "pedra" or escolha2 == "1":
                            escolha2 = "pedra"
                            break
                        elif escolha2 == "papel" or escolha2 == "2":
                            escolha2 = "papel"
                            break
                        elif escolha2 == "tesoura" or escolha2 == "3":
                            escolha2 = "tesoura"
                            break
                        else:
                            print(f"Calma lá né! {nome2}, você digitou errado sem querer ou tá brincando comigo? Vai de novo...")
                            continue
                        
                    print(f"=-=-=Agora é a hora da verdade!=-=-=")

                    print("\nJO")
                    time.sleep(0.5)
                    print("\nKEN")
                    time.sleep(0.5)
                    print("\nPÔ!")
                    time.sleep(0.5)

                    if escolha1 == "pedra" and escolha2 == "tesoura":
                        print(f"\n{nome2} joga tesoura, mas {nome1} de maneira muito sagaz a destrói com uma pedrada!")
                        time.sleep(2.5)
                        print(f"{nome1} ganhou a rodada!")
                        time.sleep(0.5)
                        vitoriasJogador1 += 1

                    elif escolha1 == "papel" and escolha2 == "pedra":
                        
                        print(f"\n{nome1} joga papel e amassa totalmente a pedra de {nome2}!")
                        time.sleep(2.5)
                        print(f"{nome1} ganhou a rodada!")
                        time.sleep(0.5)
                        vitoriasJogador1 += 1

                    elif escolha1 == "tesoura" and escolha2 == "papel":
                        print(f"\n{nome2} arremessa o papel com muita força na direção de {nome1}, entretanto, {nome1} faz picadinhos do papel com sua tesoura.")
                        time.sleep(2.5)
                        print(f"\n{nome1} ganhou a rodada!")
                        time.sleep(0.5)
                        vitoriasJogador1 += 1

                    elif escolha1 == escolha2:
                        print(f"\nUm empate! Vocês dois jogaram {escolha1}!")
                        time.sleep(2.5)

                    elif escolha2 == "pedra" and escolha1 == "tesoura":
                        print(f"\n{nome2} joga pedra e arrebenta com a tesoura de {nome1}!!")
                        time.sleep(2.5)
                        print(f"\n{nome2} ganhou a rodada!")
                        time.sleep(0.5)
                        vitoriasJogador2 += 1

                    elif escolha2 == "papel" and escolha1 == "pedra":
                        print(f"{nome1} joga uma pedra com o intuito de acertar {nome2}. {nome2} envolve a pedra com um papel muito bem posicionado e vence a rodada.")
                        time.sleep(3.0)
                        print(f"\n{nome2} ganhou a rodada!")
                        time.sleep(0.5)
                        vitoriasJogador2 += 1

                    elif escolha2 == "tesoura" and "papel":
                        print(f"com sua tesoura afiadíssima, {nome2} tritura o papel de {nome1}")
                        time.sleep(2.5)
                        print(f"\n{nome2} ganhou a rodada!")
                        time.sleep(0.5)
                        vitoriasJogador2 += 1
                        
                    print(f"\n=-=-=PLACAR=-=-=") # placar
                    print(f"\n| {nome1}: {vitoriasJogador1}")
                    print(f"\n| {nome2}: {vitoriasJogador2}")
                    print(f"\nMeta: {rodadasPraGanhar}")
                    print(f"\n=-=-=--=--=-=-=\n")

                    if vitoriasJogador1 == rodadasPraGanhar: # Textinho embaixo do placar que diz a situação comparando as vitórias dos jogadores
                        print(f"\n{nome1} ganhou!!! Parabéns!!! Você destruiu {nome2} completamente!!!!!!")
                    elif vitoriasJogador2 == rodadasPraGanhar:
                        print(f"\n{nome2} ganhou!!! Parabéns!!! Você destruiu {nome1} completamente!!!!!!")
                    elif vitoriasJogador1 > vitoriasJogador2: 
                        print(f"{nome1} está na frente!")
                    elif vitoriasJogador2 > vitoriasJogador1:
                        print(f"{nome2} está na frente!")
                    else:
                        print(f"Está empatado!")

                    input("\nDigite algo para continuar: ")
                    # fazer input pra revelar a resposta

                prosseguir = "000"
                partidasJogadas += 1
                pvpJogados += 1
                acabouDeNomear = False

                if vitoriasJogador1 > vitoriasJogador2: # dá vitórias "permanentes" aos jogadores, pra mostrar depois quando decidirem quitar no jogo, ou no menu mesmo
                    permaVitoriasJogador1 += 1
                elif vitoriasJogador2 > vitoriasJogador1:
                    permaVitoriasJogador2 += 1
                


                print(f"\n=-=-=Eai, vocês vão querer continuar jogando??=-=-=")
                print(f"\n---> Sim, bora de novo! [1]")
                print(f"\n---> A gente quer voltar pro menu! [2]") # lembrar de adicionar valor pra mudar easter egg de fechar sem jogar
                print(f"\n---> Já deu né, queremos sair do jogo! [3]")
                prosseguir = input("\n-------> Por favor, escolha sua opção: ")

                if prosseguir == "1":
                    continue
                elif prosseguir == "2":
                    break                  
                elif prosseguir == "3":
                    modo = "5" # modo 5 é checado no começo do menu pra acabar com o programa
                    break
                else:
                    break
        else:
            continue # isso aqui volta la no primeiro while, vai pro menu.


    elif modo == "2":
        # modo 2, player x ia 
        # pôr um while com um timerzinho "pensando..." pra maquina responder
        pass

    elif modo == "3":
        # modo 3, ia x ia
        pass

    elif modo == "4": # modo 4, tutorial
        print("\n\n=-=-=-=-=-=-=Você escolheu o TUTORIAL=-=-=-=-=-=-=\n\n")
        print(f"Jokenpô ou Pedra Papel e Tesoura, é um jogo de dois jogadores no qual, durante as rodadas, ambos devem escolher entre uma das opções: Pedra, Papel, ou Tesoura.\n")
        print(f"Quando os dois escolherem, o jogo vai dizer quem ganhou, com base nas seguintes regras:\n\n")
        print(f"- Pedra VENCE Tesoura\n- Tesoura VENCE Papel\n- Papel VENCE Pedra\n\n")
        print(f"=-=-=-=-=-=-=-==--===-====-=====-========-=====-====-===--==-=-=-=-=-=-=-=\n")

        prosseguir = input(f"Entendeu? Digite qualquer coisa para voltar ao menu! \n")
        continue # <- sera que a prof deixa usar isso aqui também? eu nao sei como voltar ao inicio do while sem ser assim

    else:
        print("\n\nDigita alguma coisa válida né!! Tá achando que eu tenho cara de palhaço?\n")
        input("Escreva alguma coisa para continuar: \n")
