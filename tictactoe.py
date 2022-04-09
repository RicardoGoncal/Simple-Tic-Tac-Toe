import random
import time

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    
    top = '+-------'*3 + '+'
    bottom = '+-------'*3 + '+'
    line_1 = ('|   {}   '*3 + '|').format(board[0][1],board[1][1],board[2][1])
    line_2 = ('|   {}   '*3 + '|').format(board[3][1],board[4][1],board[5][1])
    line_3 = ('|   {}   '*3 + '|').format(board[6][1],board[7][1],board[8][1])

    return top + '\n' + line_1 + '\n' + bottom + '\n' + line_2 + '\n' + bottom + '\n' +  line_3 + '\n' + bottom

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

    ctr = False

    while ctr != True:

        input_square = int(input('Digite um numero para jogar: '))
        # Lista dos espaços em branco
        lista_vazio = make_list_of_free_fields(board)
        # print(lista_vazio)

        # Faz o update do board de acordo com a validação
        if (input_square in lista_vazio) and (input_square > 0) and (input_square < 10):
            print('Numero do usuario: ', input_square)
            board[input_square-1][1] = "O"
            ctr = True
        else:
            input_square = int(input('Digite um numero valido para jogar: '))

    return board

def make_list_of_free_fields(board):

    lista_vazio = []
    print(board)
    
    for i in range(len(board)):

        if board[i][1] != "X" and board[i][1] != "O":
            lista_vazio.append(board[i][0] + 1)

    return lista_vazio


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

    if board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    elif board[3][1] == sign and board[4][1] == sign and board[5][1] == sign:
        return True
    elif board[6][1] == sign and board[7][1] == sign and board[8][1] == sign:
        return True
    elif board[0][1] == sign and board[4][1] == sign and board[8][1] == sign:
        return True
    elif board[2][1] == sign and board[4][1] == sign and board[6][1] == sign:
        return True
    elif board[0][1] == sign and board[3][1] == sign and board[6][1] == sign:
        return True
    elif board[1][1] == sign and board[4][1] == sign and board[7][1] == sign:
        return True
    elif board[2][1] == sign and board[5][1] == sign and board[8][1] == sign:
        return True

def draw_move(board):
    # The function draws the computer's move and updates the board.

    ctr = False

    while ctr != True:

        input_square = random.randint(1,9)
        # Lista dos espaços em branco
        lista_vazio = make_list_of_free_fields(board)
        print(lista_vazio)

        # Faz o update do board de acordo com a validação
        if (input_square in lista_vazio) and (input_square > 0) and (input_square < 10):
            print('Numero da maquina: ', input_square)
            board[input_square-1][1] = "X"
            ctr = True
        else:
            input_square = random.randint(1,9)

    return board


if __name__ == '__main__':


    # Preenchimento da tabela inicial com o inimigo iniciando o X
    board = []

    for i in range(9):
        
        if i == 4:
            board.append([i, 'X'])
        else:
            board.append([i, i + 1])


    d = display_board(board)

    print(d)

    # Função para o usuário escolher uma posição.

    finish = False
    empate = False
    acc = 1

    while finish != True and empate == False:

        board_game = enter_move(board)
        print(display_board(board_game))
        time.sleep(5)

        if victory_for(board_game, "O"):
            finish = True
            frase = "O vencedor é o usuario real."
            break
        else:
            empate = False
            acc = acc + 1

        board_game = draw_move(board)
        print(display_board(board_game))
        time.sleep(5)

        if victory_for(board_game, "X"):
            finish = True
            frase = "O vencedor é a maquina do mal."
            break
        else:
            empate = False
            acc = acc + 1

        if finish == False and acc == 9:
            finish = True
            empate = True
            frase = "Empate"
       
    
    # Exibe o vencedor do game
    print(frase)
        



