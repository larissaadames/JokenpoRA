# . O programa deve respeitar as regras do Jokenpô (Pedra ganha da tesoura / Tesoura ganha do papel
# / Papel ganha da pedra)
# 2. O jogo possui três modalidades: humano x humano, humano x computador ou computador x
# computador. A escolha da modalidade deve ser definida no início do programa, e não pode ser
# modificada ao longo da execução.
# 3. Após a escolha da modalidade, o jogo pode ter inúmeras partidas, ao final de cada partidas o
# programa deve perguntar se o jogador quer CONTINUAR ou SAIR.
# 4. Em cada partida o programa deve, solicitar a jogada (PEDRA, PAPEL OU TESOURA) se o jogador for
# humano ou gerar a jogada de forma randômica se o jogador for computador. Após coletar as
# jogadas, o programa deve indicar quem foi o vencedor e mostrar o placar geral.
# 5. Caso o jogador deseje CONTINUAR, o programa deve começar mais uma partida. Caso o jogador
# deseje SAIR, o programa deve exibir o placar geral e apresentar uma mensagem de agradecimento
# com os nomes dos estudantes.
# 6. O código do programa deve estar documentado e pode ser implementado em grupos de 2 ou 3
# pessoas.
# 7. Os estudantes devem ter domínio sobre todo o código, será realizado um teste de autoria nas
# entregas para avaliar o domínio de cada estudante. Em caso de cópia ou plágio, a nota atribuída
# a atividade será zero.
# 8. Data de Entrega: 23/04/2025 no CANVAS.
# Atividade somativa



import time
import random

print ("---- Bem-vindo ao nosso Jokenpô! ----")
print ("\n ---> HUMANO 👨 x HUMANO 👨 [1] \n ---> HUMANO 👨 x MÁQUINA 🤖 [2] \n ---> MÁQUINA 🤖 x MÁQUINA 🤖 [3]")

modo = int(input("Por favor, escolha um modo de jogo: "))

vitoriasP1 = 0
vitoriasP2 = 0
empates = 0

if modo == 1:
    
    print("\n---- Você escolheu o modo HUMANO x HUMANO ----")

    nomeP1 = ("🔵 Jogador 1, por favor digite o seu nome: ")

    nomeP2 = ("🔴 Jogador 2, digite seu nome por favor: ")

    vezP1 = True # Define a vez do jogador 1

    while vezP1 == True: 

        print("\n---- Jogador 1, Qual desses você quer jogar? ----")
        print("\n---> 🗿 [Pedra] ou [1],\n ---> 🧻 [Papel] ou [2] \n--->✂️ [Tesoura] ou [3] ")
        
        escolhaP1 = input("Escolha: ").lower().strip()

        if escolhaP1 == "1" or escolhaP1 == "pedra": # Permite que o usuário escreva a escolha pelo numeral ou pelo nome do objeto, padronizando-os
            escolhaP1 == "pedra"

        elif escolhaP1 == "2" or escolhaP1 == "papel":
            escolhaP1 == "papel"

        elif escolhaP1 == "3" or escolhaP1 == "tesoura":
            escolhaP1 == "tesoura"

        else:
            escolhaP1 = input("Por favor, escolha uma opção válida: ")
            
        vezP1 = False

    vezP2 = True
    
    while vezP2 == True:
        print("\n---- Jogador 2, Qual desses você quer jogar? ----")
        print("\n---> 🗿 [Pedra] ou [1],\n ---> 🧻 [Papel] ou [2] \n--->✂️ [Tesoura] ou [3] ")
        
        escolhaP2 = input("Escolha: ").lower().strip()
        if escolhaP2 == "1" or escolhaP2 == "pedra": # Permite que o usuário escreva a escolha pelo numeral ou pelo nome do objeto, padronizando-os
            escolhaP2 == "pedra"

        elif escolhaP2 == "2" or escolhaP2 == "papel":
            escolhaP2 == "papel"

        elif escolhaP2 == "3" or escolhaP2 == "tesoura":
            escolhaP2 == "tesoura"

        else:
            escolhaP2 = input("Por favor, escolha uma opção válida: ")
        
        vezP2 = False

    ## vitorias p1
    if escolhaP1 == "pedra" and escolhaP2 == "tesoura":
        print(f"\n{nomeP1} manda PEDRA e destrói completamente a tesoura de {nomeP2}!")
        time.sleep(2.5)
        print(f"{nomeP1} ganhou a rodada!")
        time.sleep(0.5)
        vitoriasP1 += 1

    elif escolhaP1 == "papel" and escolhaP2 == "pedra":
        print(f"\n{nomeP1} joga PAPEL e amassa totalmente a PEDRA de {nomeP2}!")
        time.sleep(2.5)
        print(f"{nomeP1} ganhou a rodada!")
        time.sleep(0.5)
        vitoriasP1 += 1

    elif escolhaP1 == "tesoura" and escolhaP2 == "papel":
        #print historinha
        print(f"\n {nomeP1} ganhou a rodada!")
        time.sleep(1.5)
        #print vitoria
        print(f"\n {nomeP1} ganhou!")

        ## empates
    elif escolhaP1 == escolhaP2: # empate
        print(f"\nOs dois escolheram {escolhaP1}")
        time.sleep(1.0)
        print(f"\nFoi um empate")
        empates += 1
    
    ## vitorias p2
    elif escolhaP2 == "pedra" and escolhaP1 == "tesoura":
        print(f"\n{nomeP2} manda PEDRA e destrói completamente a tesoura de {nomeP1}!")
        time.sleep(2.5)
        print(f"{nomeP2} ganhou a rodada!")
        time.sleep(0.5)
        vitoriasP2 += 1

    elif escolhaP2 == "papel" and escolhaP1 == "pedra":
        print(f"\n{nomeP2} joga PAPEL e amassa totalmente a PEDRA de {nomeP1}!")
        time.sleep(2.5)
        print(f"{nomeP2} ganhou a rodada!")
        time.sleep(0.5)
        vitoriasP2 += 1

    elif escolhaP2 == "tesoura" and escolhaP1 == "papel":
        #print historinha
        print(f"\n {nomeP2} ganhou a rodada!")
        time.sleep(1.5)
        #print vitoria
        print(f"\n {nomeP2} ganhou!")

elif modo == 2:
    print("\n ---- Você escolheu o modo HUMANO x MÁQUINA ----")
    print("")

elif modo == 3:
    pass

if modo == 4:
    print("Obrigado por jogar nosso jokenpô!! Volte sempre! 😉 Feito por: Larissa Adames, Luis Felipe Quintiliano, Davi Cagnato")