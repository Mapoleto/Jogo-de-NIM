#Inicia o jogo chamando campeonato ou partida.
def inicio():
    
    
    
    modo = int(input(" Bem vindo ao jogo de NIM! Escolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato 2 " ))
 
    if modo == 2 :
        print("\nVocê escolheu um campeonato!")
        campeonato()
    else:
        partida()
                 
#define campeonato        
def campeonato():
    #repete a função partida 3 vezes
    cont = 1
    while cont<= 3:
        
        print("\n****Rodada",cont,"****")
        partida()
        if cont >= 3:
            print("\n**** Final do campeonato ****")
            print("\nPlacar: Você 0 X 3 Computador")
        cont+=1
        
#define a jogado do computador de acordo com a estrategia vencedora.
def computador_escolhe_jogada(n,m):
    
    i = 1
    escolha = True
    
    while i <= m:
        
        if  (n-i)!= 0 and (n-i)%(m+1) == 0:
            
            escolha = True
            m = i
            return m
                
        else:
            escolha = False
            
        i+=1
        
    if escolha == False:
        i = m
        while not escolha:
            
            m = i
            
            if n-m >= 0:
                
                escolha = True
         
                return m
            else:
                i-=1
            
#Função que define a jogada do usuario            
def usuario_escolhe_jogada(n,m):
    cont =1
    jogada = 0
    while cont != jogada:
    
        jogada = int(input("\nQuantas peças você vai tirar? "))
        
        if jogada <= m and jogada > 0:
            
            cont = jogada
            m = jogada
            return m
            
        else :
            print("oops! jogada invalida! tente denovo")
#funçao que inicia a partida define a vez de cada jogador alternando as funçoes "computador_joga()" e "usuario_joga()".          
def partida():
    numero_peças = int(input("Quantas peças? "))
    limite_jogada = int(input("Limite de peças por jogada"))
    computador_joga = True
    usuario_joga = False
    primeira_partida = True
    i = 0
    
    while i <= numero_peças:
        
        if numero_peças == 0:
            if computador_joga == False :
                print("\nFim de jogo! O computador ganhou.")
                break;
            elif usuario_joga == False:
                print("\nFim de jogo! O usuario ganhou")
                break;
                
        if primeira_partida == True:
            cont = 1
            while cont <= limite_jogada:
            
                if (numero_peças-cont)%(limite_jogada+1) == 0:
                    print("\nComputador começa")
                
                    escolha=computador_escolhe_jogada(numero_peças,limite_jogada)
                    numero_peças-=escolha 
                    usuario_joga = True
                    computador_joga = False
                    primeira_partida = False
                    if escolha > 1:
                        print("O computador tirou %s peças" %escolha)
                        if numero_peças != 0:
                            print("Agora resta %s peças no tabuleiro" %numero_peças)
                    elif escolha == 1:
                        print("O computador tirou %s peça" %escolha)
                        if numero_peças != 0:
                            print("Agora resta %s peça no tabuleiro" %numero_peças)
                else:
                    cont+=1
                    
                    
            if primeira_partida == True and usuario_joga == False: 
                print("\nUsuario começa!")
                escolha=usuario_escolhe_jogada(numero_peças,limite_jogada)
                numero_peças-=escolha
                usuario_joga = False
                computador_joga = True
                primeira_partida = False
                if escolha > 1:
                    print("\nO usuario tirou %s peças" %escolha)
                    if numero_peças != 0:
                        print("Agora resta %s peças no tabuleiro" %numero_peças)
                elif escolha == 1:
                    print("\nO usuario tirou %s peça" %escolha)
                    if numero_peças != 0:
                        print("Agora resta %s peça no tabuleiro" %numero_peças)
        elif computador_joga == True:
            escolha= computador_escolhe_jogada(numero_peças,limite_jogada)
            numero_peças-=escolha
            usuario_joga = True
            computador_joga = False
            if escolha > 1:
                print("\nO computador tirou %s peças" %escolha)
                if numero_peças != 0:
                    print("Agora resta %s peças no tabuleiro" %numero_peças)
            elif escolha == 1:
                print("\nO computador tirou %s peça" %escolha)
                if numero_peças != 0:
                    print("Agora resta %s peça no tabuleiro" %numero_peças)
        elif usuario_joga == True:
            escolha=usuario_escolhe_jogada(numero_peças,limite_jogada)
            numero_peças-=escolha
            usuario_joga = False
            computador_joga = True
            if escolha > 1:
                print("O usuario tirou %s peças" %escolha)
                if numero_peças != 0:
                    print("Agora resta %s peças no tabuleiro" %numero_peças)
            elif escolha == 1:
                print("O usuario tirou %s peça" %escolha)
                if numero_peças !=0:
                    print("Agora resta %s peça no tabuleiro" %numero_peças)


NIM = inicio()
