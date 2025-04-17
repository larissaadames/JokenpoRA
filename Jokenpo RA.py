
# IDEIAS:
#   Os jogadores poderão escolher quantas rodadas querem jogar. 
#       Implementar isso de modo que seja: "Melhor de [numero de rodadas]", ou "Primeiro a [numero de vitorias]"
#       Se alguém digitar um número IMENSO de quantidade de rodadas, o programa realmente confirma se a pessoa quer prosseguir
#
#   Fazer animaçãozinha de JO \n - KEN \n - PO \n e mostrar o resultado da rodada 
#   COM TEXTO ASCII A LINHA DE CIMA
#
#   Mostrar pontuação dos jogadores no menu
#
# ANOTAÇÕES
#
#   Gostaria que alguem conseguisse dar um jeito de descobrir como limpa o terminal pra botar em varias partes do codigo e ficar super clean 
#   Se a
#   
# ERROS:    
# 
#   Nos dialogos, nao tem nada com pronome feminino, entao fica esquisito se alguma jogadora aparece
#   Quando o usuário for optar pela quantidade de rodadas, ele pode digitar uma string e quebrar o código. Não sei oq fazer, pq a prof limitou nossos recursos pra usar outras coisas q counterariam isso
#

import time # tempo
import random # random
import os # clear no terminal

nome1 = "default1" # essas variaveis nome1 e nome2 são usadas posteriormente para atribuir nomes aos jogadores.
nome2 = "default2" # também sao usadas para verificar se o jogador trocou o nome ou não, mudando alguns diálogos.

melhorDeQuantasRodadas = 3
rodadasPraGanhar = int((melhorDeQuantasRodadas + 1 )/2)

vitoriasJogador1 = 0
vitoriasJogador2 = 0

while True:
    print(f"\n\n=-=-=-=-=-=-=Eai! Bem vindo ao MELHOR JOKENPÔ DO PLANETA!!!!!=-=-=-=-=-=-=\n\n")
    print(f"-------> HUMANO X HUMANO - Quero batalhar com meu amiguinho >:) [1]\n")
    print(f"-------> HUMANO X MÁQUINA - Quero acabar com TODAS as máquinas!!! [2]\n")
    print(f"-------> MÁQUINA X MÁQUINA - Quero ver os robôs se detonando [3]\n")
    print(f"-------> TUTORIAL - Como que joga isso? Me ajuda pelo amor de Deus! [4]\n") # <- perguntar pra prof se pode botar um botão a mais de tutorial, ou se só mete o tutorial antes do jogo msm
    print(f"-------> SAIR - Eu quero sair, tô bem de boa, Valeu! ^^ [5]\n\n") 
    modo = input(f"Digite o número da sua escolha: ") # isso propositalmente é uma string, pra caso a pessoa digite algo errado o codigo nao quebrar

    if modo == "1": # modo player x player
        print(f"\n\n=-=-=-=-=-=-=Você escolheu o modo HUMANO X HUMANO=-=-=-=-=-=-=\n\n")
        nome1 = input(f"-------> Jogador 1, por favor digita o seu nome: ")
        nome2 = input(f"-------> Agora, Jogador 2, digita o seu nome aí também: ")
        print(f"\nPor último, {nome1} e {nome2}, vocês querem que o jogo acabe com quantas rodadas? Exemplo: Melhor de [3] rodadas, Melhor de [5] rodadas...") # <- Melhorar diálogo?

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

        if melhorDeQuantasRodadas % 2 != 0 and melhorDeQuantasRodadas > 1 : # se o número for IMPAR e MAIOR QUE 1 entao roda o codigo normal
            print(f"Beleza, vocês então vão jogar um Melhor de {melhorDeQuantasRodadas}, ou seja, quem fizer {rodadasPraGanhar} primeiro vence!\n")
            print(f"Boa Sorte {nome1} e {nome2}!")
            time.sleep(3)
            pass
        
        elif melhorDeQuantasRodadas % 2 == 0 and melhorDeQuantasRodadas > 1: # se o numero for PAR e MAIOR QUE 1, ele soma 1 no numero
            melhorDeQuantasRodadas += 1
            print(f"Beleza, eu dei uma ajustada pq o número tinha que ser ímpar, mas então vocês vão jogar um Melhor de {melhorDeQuantasRodadas}, ou seja, quem fizer {rodadasPraGanhar} primeiro vence!\n")
            print(f"Boa Sorte {nome1} e {nome2}!")
            time.sleep(3)
            pass

        elif melhorDeQuantasRodadas == 1 : # se o numero for IGUAL A 1, tem esse diálogo especial
            print(f"Então vocês vão jogar só uma rodada? Interessante! Que vença o melhor!!\n")
            print(f"Boa Sorte {nome1} e {nome2}!")
            time.sleep(3)
            pass # pass passa adiante

        elif melhorDeQuantasRodadas < 1: # se o numero for MENOR QUE UM, ele manda o pessoal de volta pro menu
            print(f"\nVocês tão de sacanagem né? Esse número nem faz sentido! Que feio, {nome1} e {nome2}! Vou mandar vocês de volta para o menu >:(\nAguarde...")
            time.sleep(3)
            continue # continue reseta o loop
        
        print("\nJO")
        time.sleep(0.5)
        print("\nKEN")
        time.sleep(0.5)
        print("\nPÔ!")
        time.sleep(0.5)

        while vitoriasJogador1 or vitoriasJogador2 < rodadasPraGanhar: # roda esse código enquanto a quantidade vitorias de um dos jogadores for menor que a variavel rodadasPraGanhar

            print(f"\n=-=-=Vamo lá!! {nome1}, não deixa o/a coleguinha {nome2} olhar a sua escolha hein!!=-=-=")
            print("\n- [Pedra] ou [1]\n- [Papel] ou [2]\n- [Tesoura] ou [3]\n")
            
            escolha1 = str(input(f"-------> {nome1}, digite qual você quer! ")).lower().strip()


            if escolha1 == "pedra" or escolha1 == "1":
                escolha1 = "pedra"
            elif escolha1 == "papel" or escolha1 == "2":
                escolha1 = "papel"
            elif escolha1 == "tesoura" or escolha1 == "3":
                escolha1 = "tesoura"
            else:
                print(f"Calma lá né! {nome1}, você digitou errado sem querer ou tá brincando comigo? Vai de novo...")
                time.sleep(1.5)
                continue
            print(f"\n=-=-=Agora é a vez de {nome2}!! Não deixa {nome1} dar uma espiadinha hein ¬¬=-=-=")
            print("\n- [Pedra] ou [1]\n- [Papel] ou [2]\n- [Tesoura] ou [3]\n")
            
            escolha2 = str(input(f"-------> {nome2}, digite qual você quer! ")).lower().strip()

            if escolha2 == "pedra" or escolha2 == "1":
                escolha2 = "pedra"
            elif escolha2 == "papel" or escolha2 == "2":
                escolha2 = "papel"
            elif escolha2 == "tesoura" or escolha2 == "3":
                escolha2 = "tesoura"
            else:
                print(f"Calma lá né! {nome1}, você digitou errado sem querer ou tá brincando comigo? Vai de novo...")
            
            print(f"=-=-=Agora é a hora da verdade!=-=-=")

            print("\nJO")
            time.sleep(0.5)
            print("\nKEN")
            time.sleep(0.5)
            print("\nPÔ!")
            time.sleep(0.5)

            if escolha1 == "pedra" and escolha2 == "tesoura":
                vitoriasJogador1 += 1
            elif escolha1 == "papel" and escolha2 == "pedra":
                vitoriasJogador1 += 1
            elif escolha1 == "tesoura" and escolha2 == "papel":
                vitoriasJogador1 += 1
            elif escolha1 == escolha2:
                print(f"Um empate! Vocês dois jogaram {escolha1}!")
            else:
                vitoriasJogador2 += 1
            print("ta funcionando")
            print(f"vitorias jogador1 {vitoriasJogador1}") # diálogos a modificar ainda
            print(f"vitorias jogador2 {vitoriasJogador2}")
            print(f"Lembrando que quem fizer {rodadasPraGanhar} vence hein!!")

            # fazer input pra revelar a resposta


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
        prosseguir = input(f"Entendeu? Digite qualquer coisa para voltar ao menu! \n")
        continue # <- sera que a prof deixa usar isso aqui também? eu nao sei como voltar ao inicio do while sem ser assim

    elif modo == "5": # sair do programa
        print("=-=-=-=-=-=-=Você escolheu SAIR=-=-=-=-=-=-=\n\n")
        if nome1 == "default1" and nome2 == "default2": # se os nomes dos dois jogadores nao foram modificados
            print(f"Você nem jogou direito e vai sair já?? Tá bom né, até mais!!!! :))\n\n")

        elif nome2 == "default2": # se o nome do segundo jogador nao foi modificado
            print(f"Muito obrigado {nome1} por usar nosso programa de Jokenpô!!! Até mais!!!! :))\n\n")

        else: # se os dois nomes foram modificados
            print(f"Muito obrigado {nome1} e {nome2} por usarem nosso programa de Jokenpô!!! Até mais!!!! :))\n\n")
        break
    else:
        print("\n\nDigita alguma coisa válida né!! Tá achando que eu tenho cara de palhaço?\n")
        prosseguir = input("Escreva alguma coisa para continuar: \n")
        continue
