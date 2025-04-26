import time
import random

print ("\n---- Bem-vindo ao nosso Jokenpô! ----")
print ("\n ---> HUMANO 👨 x HUMANO 👨 [1] \n ---> HUMANO 👨 x MÁQUINA 🤖 [2] \n ---> MÁQUINA 🤖 x MÁQUINA 🤖 [3]\n")

modo = int(input("Por favor, escolha um modo de jogo: "))

vitoriasP1 = 0
vitoriasP2 = 0
empates = 0
prosseguir = "continuar"
continuar = 0
sair = 0

if modo == 1:
    
    print("\n---- Você escolheu o modo HUMANO 👨 x HUMANO 👨 ----")

    nomeP1 = input("\n🔵 Jogador 1, por favor digite o seu nome: ")

    nomeP2 = input("\n🔴 Jogador 2, digite seu nome por favor: ")
    
    while prosseguir == "continuar":

        vezP1 = True # Define a vez do jogador 1

        while vezP1 == True: 

            print(f"\n---- {nomeP1}, Qual desses você quer jogar? ----")
            print("\n---> 🗿 [Pedra] ou [1],\n---> 🧻 [Papel] ou [2] \n---> ✂️ [Tesoura] ou [3] ")
            
            escolhaP1 = input("Escolha: ").lower().strip()

            if escolhaP1 == "1" or escolhaP1 == "pedra": # Permite que o usuário escreva a escolha pelo numeral ou pelo nome do objeto, padronizando-os
                escolhaP1 = "pedra"


            elif escolhaP1 == "2" or escolhaP1 == "papel":
                escolhaP1 = "papel"


            elif escolhaP1 == "3" or escolhaP1 == "tesoura":
                escolhaP1 = "tesoura"


            else:
                escolhaP1 = input("Por favor, escolha uma opção válida: ")
                
            vezP1 = False # fim do loop do jogador 1

        print("\n"* 30) # empurra o terminal pra cima

        vezP2 = True # inicia o loop do jogador 2 
        
        while vezP2 == True:
            
            print(f"\n---- {nomeP2}, Qual desses você quer jogar? ----")
            print("\n---> 🗿 [Pedra] ou [1],\n---> 🧻 [Papel] ou [2] \n---> ✂️ [Tesoura] ou [3] ")
            
            escolhaP2 = input("Escolha: ").lower().strip()
            if escolhaP2 == "1" or escolhaP2 == "pedra": # Permite que o usuário escreva a escolha pelo numeral ou pelo nome do objeto, padronizando-os
                escolhaP2 = "pedra"

            elif escolhaP2 == "2" or escolhaP2 == "papel":
                escolhaP2 = "papel"

            elif escolhaP2 == "3" or escolhaP2 == "tesoura":
                escolhaP2 = "tesoura"

            else:
                escolhaP2 = input("Por favor, escolha uma opção válida: ")
            
            vezP2 = False

        print("""
            JO
                _______
            ---'   ____)
                    (_____)
                    (_____) 
                    (____)
        -   --._____(___)
        """)
        time.sleep(0.8)

        print("""
            KEN
            _______
        ---'   ____)__
                ______)
                _______)
                _______)
        ---.__________)
        """)
        time.sleep(0.8)

        print("""
            PÔ
            _______
        ---'   ____)____
                    ______)
                    ________)
                (____)
            ---.(___)                        
        """)
        time.sleep(0.8)

        ## vitorias p1
        if escolhaP1 == "pedra" and escolhaP2 == "tesoura":
            print(f"\n{nomeP1} manda PEDRA 🗿 e destrói completamente a TESOURA ✂️ de {nomeP2}!")
            time.sleep(1.5)
            print(f"🔵 {nomeP1} ganhou a rodada!")
            time.sleep(1)
            vitoriasP1 += 1

        elif escolhaP1 == "papel" and escolhaP2 == "pedra":
            print(f"\n{nomeP1} joga PAPEL 🧻 e amassa totalmente a PEDRA 🗿 de {nomeP2}!")
            time.sleep(1.5)
            print(f"🔵 {nomeP1} ganhou a rodada!")
            time.sleep(1)
            vitoriasP1 += 1

        elif escolhaP1 == "tesoura" and escolhaP2 == "papel":
            print(f"\n {nomeP1} jogou TESOURA ✂️  e fez picadinhos do PAPEL 🧻 de {nomeP2}")
            print(f"\n🔵 {nomeP1} ganhou a rodada!")
            time.sleep(1.5)
            print(f"\n {nomeP1} ganhou!")
            vitoriasP1 += 1

            ## empates
        elif escolhaP1 == escolhaP2: # empate
            print(f"\nOs dois escolheram {escolhaP1}")
            time.sleep(1.0)
            print(f"\nFoi um empate")
            time.sleep(1.0)
            empates += 1
        
        ## vitorias p2
        elif escolhaP2 == "pedra" and escolhaP1 == "tesoura":
            print(f"\n{nomeP2} joga PEDRA 🗿 e arrebenta com a TESOURA ✂️ de {nomeP1}!")
            time.sleep(1.5)
            print(f"🔴 {nomeP2} ganhou a rodada!")
            time.sleep(1)
            vitoriasP2 += 1

        elif escolhaP2 == "papel" and escolhaP1 == "pedra":
            print(f"\n{nomeP2} joga PAPEL 🧻 e amassa totalmente a PEDRA 🗿 de {nomeP1}!")
            time.sleep(1.5)
            print(f"🔴 {nomeP2} ganhou a rodada!")
            time.sleep(1)
            vitoriasP2 += 1

        elif escolhaP2 == "tesoura" and escolhaP1 == "papel":
            print(f"\n {nomeP2} joga TESOURA ✂️ e faz destroços do PAPEL 🧻 de {nomeP1}")
            time.sleep(1.5)
            print(f"\n🔴 {nomeP2} ganhou a rodada!")
            time.sleep(1)
            vitoriasP2 += 1

        print(f"\n=-=-=PLACAR=-=-=") # placar
        print(f"\n| {nomeP1}: {vitoriasP1}")
        print(f"\n| {nomeP2}: {vitoriasP2}")
        print(f"\n| Empates: {empates}")
        print(f"\n=-=-=-=-=-=-=-=-=\n")

        time.sleep(1.5)

        while prosseguir == "continuar":
            print("Vocês querem continuar jogando?")
            print("\n---> [Continuar] ou [1]")
            print("\n---> [Sair] ou [2]\n")
            prosseguir = input("Escolha : ").lower().strip()

            
            if prosseguir == "1" or prosseguir == "continuar":
                prosseguir = "continuar"
                break
            
            elif prosseguir == "2" or prosseguir == "sair":
                prosseguir == "sair"
                print("Obrigado por jogar nosso jokenpô!! Volte sempre! 😉 \nFeito por: Larissa Adames, Luis Felipe Quintiliano, Davi Cagnato\n")
            else:
                print("Digite algo válido, por favor!")
                prosseguir = "continuar"
                time.sleep(0.5)




elif modo == 2:

    robo = "Robonilson"
    vitoriasP1 = 0
    empates = 0
    vitoriasRobo = 0

    print("\n ---- Você escolheu o modo HUMANO 👨 x MÁQUINA 🤖 ----")

    nomeP1 = input("\n🔵 Jogador 1, por favor digite o seu nome: ")
        
    while prosseguir == "continuar":

        escolhaRobo = random.randint(1,3)

        if escolhaRobo == 1: # define como pedra, papel, ou tesoura pra facilitar a leitura do código

            escolhaRobo = "pedra"

        elif escolhaRobo == 2:

            escolhaRobo = "papel"

        else:
            
            escolhaRobo = "tesoura"
        
        vezP1 = True # Define a vez do jogador 1


        print("""
            JO
                _______
            ---'   ____)
                    (_____)
                    (_____) 
                    (____)
        -   --._____(___)
        """)
        time.sleep(0.5)

        print("""
            KEN
            _______
        ---'   ____)__
                ______)
                _______)
                _______)
        ---.__________)
        """)
        time.sleep(0.5)

        print("""
            PÔ
            _______
        ---'   ____)____
                    ______)
                    ________)
                (____)
            ---.(___)                        
        """)
        time.sleep(0.5)

        
        while vezP1 == True:
            print(f"\n---- {nomeP1}, Qual desses você quer jogar? ----")
            print("\n---> 🗿 [Pedra] ou [1],\n---> 🧻 [Papel] ou [2] \n---> ✂️  [Tesoura] ou [3] ")
            
            escolhaP1 = input("Escolha: ").lower().strip()
            if escolhaP1 == "1" or escolhaP1 == "pedra": # Permite que o usuário escreva a escolha pelo numeral ou pelo nome do objeto, padronizando-os
                escolhaP1 = "pedra"
            elif escolhaP1 == "2" or escolhaP1 == "papel":
                escolhaP1 = "papel"
            elif escolhaP1 == "3" or escolhaP1 == "tesoura":
                escolhaP1 = "tesoura"
            else:
                escolhaP1 = input("Por favor, escolha uma opção válida: ")
            vezP1 = False # fim do loop do jogador 1

    #vitoriasP1
        if escolhaP1 == "pedra" and escolhaRobo == "tesoura":
            print(f"\n{nomeP1} manda PEDRA 🗿 e destrói completamente a TESOURA ✂️  de {robo}!")
            time.sleep(1.5)
            print(f"🔵 {nomeP1} ganhou a rodada!")
            time.sleep(1)
            vitoriasP1 += 1

        elif escolhaP1 == "papel" and escolhaRobo == "pedra":
            print(f"\n{nomeP1} joga PAPEL 🧻 e amassa totalmente a PEDRA 🗿 de {robo}!")
            time.sleep(1.5)
            print(f"🔵 {nomeP1} ganhou a rodada!")
            time.sleep(1)
            vitoriasP1 += 1

        elif escolhaP1 == "tesoura" and escolhaRobo == "papel":
            print(f"\n {nomeP1} jogou TESOURA ✂️  e fez picadinhos do PAPEL 🧻 de {robo}")
            time.sleep(1.5)
            print(f"\n {nomeP1} ganhou!")
            time.sleep(1)
            vitoriasP1 += 1

    ## empates
        elif escolhaP1 == escolhaRobo:
            print(f"\n Os dois escolheram {escolhaP1}")
            time.sleep(1.0)
            print(f"\n Foi um empate")
            time.sleep(1.0)
            empates += 1
        
    ## vitorias robo
        elif escolhaRobo == "pedra" and escolhaP1 == "tesoura":
            print(f"\n{robo} joga PEDRA 🗿 e arrebenta com a TESOURA ✂️  de {nomeP1}!")
            time.sleep(1.5)
            print(f"🔴 {robo} ganhou a rodada!")
            time.sleep(1)
            vitoriasRobo += 1

        elif escolhaRobo == "papel" and escolhaP1 == "pedra":
            print(f"\n{robo} joga PAPEL 🧻 e amassa totalmente a PEDRA 🗿 de {nomeP1}!")
            time.sleep(1.5)
            print(f"🔴 {robo} ganhou a rodada!")
            time.sleep(1)
            vitoriasRobo += 1

        elif escolhaRobo == "tesoura" and escolhaP1 == "papel":
            #print historinha
            print(f"\n {robo} joga TESOURA ✂️  e faz destroços do PAPEL 🧻 de {nomeP1}")
            time.sleep(1.5)
            #print vitoria
            print(f"\n🔴 {robo} ganhou a rodada!")
            time.sleep(1)
            vitoriasRobo += 1


        print(f"\n=-=-=PLACAR=-=-=") # placar
        print(f"\n| {nomeP1}: {vitoriasP1}")
        print(f"\n| {robo}: {vitoriasRobo}")
        print(f"\n| Empates: {empates}")
        print(f"\n=-=-=-=-=-=-=-=-=\n")

        time.sleep(1.5)

        while prosseguir == "continuar":
            print("Você quer continuar jogando?")
            print("\n---> [Continuar] ou [1]")
            print("\n---> [Sair] ou [2]\n")
            prosseguir = input("Escolha : ").lower().strip()

            if prosseguir == "1" or prosseguir == "continuar":
                prosseguir = "continuar"
                break

            elif prosseguir == "2" or prosseguir == "sair":
                prosseguir == "sair"
                print("Obrigado por jogar nosso jokenpô!! Volte sempre! 😉 \nFeito por: Larissa Adames, Luis Felipe Quintiliano, Davi Cagnato")
            else:
                print("Digite algo válido, por favor!")
                prosseguir = "continuar"
                time.sleep(0.5)

elif modo == 3:
    
    robo1 = "Robonilson"
    robo2 = "Bananilson"
    vitoriasRobo1 = 0
    vitoriasRobo2 = 0
    
    print("\n ---- Você escolheu o modo MÁQUINA 🤖 x MÁQUINA 🤖 ----")
    time.sleep(1)
    print("""
        JO
            _______
        ---'   ____)
                (_____)
                (_____) 
                (____)
    -   --._____(___)
    """)
    time.sleep(0.8)

    print("""
        KEN
        _______
    ---'   ____)__
            ______)
            _______)
            _______)
    ---.__________)
    """)
    time.sleep(0.8)

    print("""
        PÔ
        _______
    ---'   ____)____
                ______)
                ________)
            (____)
        ---.(___)                        
    """)
    time.sleep(0.8)


    while prosseguir == "continuar":

        escolhaRobo1 = random.randint(1,3)
        if escolhaRobo1 == 1: # define como pedra, papel, ou tesoura pra facilitar a leitura do codigo
            escolhaRobo1 = "pedra"
            
        elif escolhaRobo1 == 2:
            escolhaRobo1 = "papel"

        else:
            escolhaRobo1 = "tesoura"  

        escolhaRobo2 = random.randint(1,3)
        if escolhaRobo2 == 1:
                escolhaRobo2 = "pedra"

        elif escolhaRobo2 == 2:
            escolhaRobo2 = "papel"

        else:
            escolhaRobo2 = "tesoura"  
        
        # vitorias robo1
        if escolhaRobo1 == "pedra" and escolhaRobo2 == "tesoura":
            print(f"\n{robo1} manda PEDRA 🗿 e destrói completamente a TESOURA ✂️  de {robo2}!")
            time.sleep(1.5)
            print(f"🔵 {robo1} ganhou a rodada!")
            time.sleep(1)
            vitoriasRobo1 += 1
        
        elif escolhaRobo1 == "papel" and escolhaRobo2 == "pedra":
            print(f"\n{robo1} joga PAPEL 🧻 e amassa totalmente a PEDRA 🗿 de {robo2}!")
            time.sleep(1.5)
            print(f"🔵 {robo1} ganhou a rodada!")
            time.sleep(1)
            vitoriasRobo1 += 1

        elif escolhaRobo1 == "tesoura" and escolhaRobo2 == "papel":
            print(f"\n {robo1} jogou TESOURA ✂️  e fez picadinhos do PAPEL 🧻 de {robo2}")
            time.sleep(1.5)
            print(f"\n {robo1} ganhou!")
            vitoriasRobo1 += 1

        # empate
        elif escolhaRobo1 == escolhaRobo2:
            print(f"\n Os dois escolheram {escolhaRobo1}")
            time.sleep(1.0)
            print(f"\n Foi um empate")
            empates += 1

        # vitorias robo2
        elif escolhaRobo2 == "pedra" and escolhaRobo1 == "tesoura":
            print(f"\n{robo2} joga PEDRA 🗿 e arrebenta com a TESOURA ✂️  de {robo1}!")
            time.sleep(1.5)
            print(f"🔴 {robo2} ganhou a rodada!")
            time.sleep(1)
            vitoriasRobo2 += 1


        elif escolhaRobo2 == "papel" and escolhaRobo1 == "pedra":
            print(f"\n{robo2} joga PAPEL 🧻 e amassa totalmente a PEDRA 🗿 de {robo1}!")
            time.sleep(1.5)
            print(f"🔵 {robo2} ganhou a rodada!")
            time.sleep(1)
            vitoriasRobo2 += 1

        elif escolhaRobo2 == "tesoura" and escolhaRobo1 == "papel":
            print(f"\n {robo2} joga TESOURA ✂️  e faz destroços do PAPEL 🧻 de {robo1}")
            time.sleep(1.5)
            print(f"\n🔴 {robo2} ganhou a rodada!")
            time.sleep(1)
            vitoriasRobo2 += 1

        print(f"\n=-=-=PLACAR=-=-=") # placar
        print(f"\n|🔵 {robo1}: {vitoriasRobo1}")
        print(f"\n|🔴 {robo2}: {vitoriasRobo2}")
        print(f"\n| Empates: {empates}")
        print(f"\n=-=-=-=-=-=-=-=-=\n")

        time.sleep(1.5)

        while prosseguir == "continuar":
                    print("Você quer continuar assistindo?")
                    print("\n---> [Continuar] ou [1]")
                    print("\n---> [Sair] ou [2]\n")
                    prosseguir = input("Escolha : ").lower().strip()

                    if prosseguir == "1" or prosseguir == "continuar":
                        prosseguir = "continuar"
                        break

                    elif prosseguir == "2" or prosseguir == "sair":
                        prosseguir == "sair"
                        print("Obrigado por jogar nosso jokenpô!! Volte sempre! 😉 \nFeito por: Larissa Adames, Luis Felipe Quintiliano, Davi Cagnato")
                    else:
                        print("Digite algo válido, por favor!")
                        prosseguir = "continuar"
                        time.sleep(0.5)






