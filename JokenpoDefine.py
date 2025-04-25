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

print ("---- Bem-vindo ao nosso Jokenpo! ----")
print ("\n ---> HUMANO 👨 x HUMANO 👨 [1] \n ---> HUMANO 👨 x MÁQUINA 🤖 [2] \n ---> MÁQUINA 🤖 x MÁQUINA 🤖 [3]")

modo = int(input("Por favor, escolha um modo de jogo: "))

if modo == 1:
    
    print("\n---- Você escolheu o modo HUMANO x HUMANO ----")

    vezJogador1 = True # Define a vez do jogador 1

    while vezJogador1 == True: 

        print("\n---- Jogador 1, Qual desses você quer jogar? ----")
        print("\n---> 🗿 [Pedra] ou [1],\n ---> 🧻 [Papel] ou [2] \n--->✂️ [Tesoura] ou [3] ")
        
        escolha1 = input("Escolha: ").lower().strip()

        if escolha1 == "1" or escolha1 == "pedra": # Permite que o usuário escreva a escolha pelo numeral ou pelo nome do objeto, padronizando-os
            escolha1 == "pedra"

        elif escolha1 == "2" or escolha1 == "papel":
            escolha1 == "papel"

        elif escolha1 == "3" or escolha1 == "tesoura":
            escolha1 == "tesoura"

        else:
            escolha1 = input("Por favor, escolha uma opção válida: ")
            
        
        
        
        vezJogador1 = False

    vezJogador2 = True
    
    while vezJogador2 == True:
        print("\n---- Jogador 2, Qual desses você quer jogar? ----")
        print("\n---> 🗿 [Pedra] ou [1],\n ---> 🧻 [Papel] ou [2] \n--->✂️ [Tesoura] ou [3] ")
        
        escolha1 = input("Escolha: ").lower().strip()

        if escolha1 == "1" or escolha1 == "pedra": # Permite que o usuário escreva a escolha pelo numeral ou pelo nome do objeto, padronizando-os
            escolha1 == "pedra"

        elif escolha1 == "2" or escolha1 == "papel":
            escolha1 == "papel"

        elif escolha1 == "3" or escolha1 == "tesoura":
            escolha1 == "tesoura"

        else:
            escolha1 = input("Por favor, escolha uma opção válida: ")

        

    
elif modo == 2:
    print("\n ---- Você escolheu o modo HUMANO x MÁQUINA ----")
    print("")

elif modo == 3:
    
if modo == 4:
    print("Obrigado por jogar nosso jokenpô!! Volte sempre! 😉 Feito por: Larissa Adames, Luis Felipe Quintiliano, Davi Cagnato")