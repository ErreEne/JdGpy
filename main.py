board =["-","-","-",
        "-","-","-",
        "-","-","-"]

JogoLoop = True

def tabuleiro():
    print(board[0] + "|" + board[1] + "|" + board[2] + "        1" + "|" + "2" + "|" + "3")
    print(board[3] + "|" + board[4] + "|" + board[5] + "        4" + "|" + "5" + "|" + "6")
    print(board[6] + "|" + board[7] + "|" + board[8] + "        7" + "|" + "8" + "|" + "9")


def jogo():
    
    start = True
    startgame = 0
    while start==True: 
        tabuleiro()
        startgame = input("Digita 1 para começar o jogo:")
        startgame = int(startgame)
        if startgame == 1:
            while JogoLoop:
                jogada1()
                checkwin()
                jogada2()
                checkwin()
        elif startgame != 1:
            return



        



def jogada1():
    posicao = input("P1:Escolher uma posição entre 1-9:")
    posicao = int(posicao) - 1

    board[posicao] = "X"

    tabuleiro()

def jogada2():
    posicao2 = input("P2:Escolher uma posição entre 1-9:")
    posicao2 = int(posicao2) - 1

    board[posicao2] = "O"

    tabuleiro()


def empate():
    if board[0] != "-" and board[1] != "-" and board[2] != "-" and board[3] != "-" and board[4] != "-" and board[5] != "-" and board[6] != "-" and board[7] != "-" and board[8] != "-":
        print("Empate")
        start = False
        return


def WinX():
    #linhas
    if (board[0] == board[1] == board[2] == "X") or (board[3] == board[4] == board[5] == "X") or (board[6] == board[7] == board[8] == "X") :
        print("Jogador1 ganhou pelas linhas")
        JogoLoop = False
        return

        
    elif (board[0] == board[3] == board[6] == "X") or (board[1] == board[4] == board[7] != "X") or (board[2] == board[5] == board[8] == "X") :
        print("Jogador1 ganhou pelas colunas.")
        JogoLoop = False
        return

    elif (board[0] == board[4] == board[8] == "X") or (board[2] == board[4] == board[6] == "X"):
        print("Jogador1 ganhou pela diagonal")
        JogoLoop=False
        return

def WinO():
    #linhas
    if (board[0] == board[1] == board[2] == "O") or (board[3] == board[4] == board[5] == "O") or (board[6] == board[7] == board[8] == "O") :
        print("Jogador1 ganhou pelas linhas")
        JogoLoop = False
        return

    #colunas    
    elif (board[0] == board[3] == board[6] == "O") or (board[1] == board[4] == board[7] == "O") or (board[2] == board[5] == board[8] == "O") :
        print("Jogador1 ganhou pelas colunas.")
        JogoLoop = False
        return
    #diagonal
    elif (board[0] == board[4] == board[8] == "O") or (board[2] == board[4] == board[6] == "O"):
        print("Jogador1 ganhou pela diagonal")
        JogoLoop=False
        return

    return False



def checkwin():
    WinX()
    empate()
    WinO()
 
jogo()
