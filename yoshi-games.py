def cadastrar_jogador():
    print("Jogador Cadastrado com sucesso!")




jogadores = [

    {"nome":"Carlos","pontos": 0}, 
    {"nome":"Yoshi","pontos": 0}, 
    {"nome":"Mario","pontos": 0} ]

while True:
    print("=" * 30)

    print("         YOSHI-GAMES")

    print("=" * 30)


    print("""

    [1]- Cadastrar Jogadores.
    [2]- Ver jogadores.
    [3]- Adicionar Pontos.
    [4]- Ver ranking.
    [5]- Buscar Jogadore
    [0]- Sair

    """)


    opcao = input("Digite o número que deseja:")

    if opcao == "1":

        print("=" * 30)

        print("       Tela de Cadastro")

        print("=" * 30)


        cadastro = input("Digite um usuario: ").capitalize()
        senha = int(input("Digite uma senha: "))

        nv_jogador = {"nome": cadastro, "pontos":0 }

        jogadores.append(nv_jogador)

        cadastrar_jogador()

    elif opcao == "2":
        print("=" * 30)

        print("      Tabela de Jogadores")

        print("=" * 30)

        for i in range(len(jogadores)):
            print(i + 1,"-", jogadores[i]["nome"],"-", jogadores[i]["pontos"], "pontos")


    elif opcao == "3":
        try:
            for i in range(len(jogadores)):
                        print(i + 1,"-", jogadores[i]["nome"],"-", jogadores[i]["pontos"], "pontos")

            jogador_pontos = input("Qual dos jogadores acima você quer colocar os pontos: ").capitalize()

            for i in range(len(jogadores)):
                if jogadores[i]["nome"] == jogador_pontos:
                    add_pontos = int (input("Quantidade de pontos: "))

                    jogadores[i]["pontos"] += add_pontos


        except ValueError:
             print("Essse nome não está dentro da listagem!!")

    elif opcao == "4":

        print("=" * 30)

        print("      Tabela de Ranking")

        print("=" * 30)


        #vou testar o sorted para deixar em ordem
        jogadores_ordem = sorted(jogadores, key = lambda jogador:jogador["pontos"],reverse=True)

        for i in range(len(jogadores_ordem)):
             print(i+1,"-", jogadores_ordem[i]["nome"],"-", jogadores_ordem[i]["pontos"],"pontos")
             

    elif opcao == "5":
        print("=" * 30)

        print("      Busca por Jogador")
        
        print("=" * 30)


        busca = input("Digite o nome do Jogador que deseja: ").capitalize()

        encontrado = False

        for i in range(len(jogadores)):
            
            if jogadores[i]["nome"] == busca:

               print("Usuario encontrado:")

               print(i+1,"-",jogadores[i]["nome"])

               encontrado = True

        if encontrado == False:
                 print("Jogador Não encontrado!!")

    elif opcao == "0":
         print("Obrigado por participar")
         print("finalizando Sistema...")

         break