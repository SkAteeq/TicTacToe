P1 = input("Enter player one name   :   ") #Taking players names
P2 = input("Enter player Two name   :   ")
board = ["   " for i in range(9)]  # board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def print_board():
    row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def player_move(icon): #giving icons to players
    if icon == " X ":
        number = P1
    elif icon == " O ":
        number = P2
    print("your turn player : {}".format(number))
    choice = int(input("Enter Your move (1-9)   :   ").strip()) - 1
    if board[choice] == "   ":
        board[choice] = icon
    else:
        print()
        print("That Space is taken! ")

#checking Conditions and posibilities for win.


def is_Victory(icon):
    if(board[0] == icon and board[1] == icon and board[2] == icon) or \
        (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[6] == icon and board[7] == icon and board[8] == icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[1] == icon and board[4] == icon and board[7] == icon) or \
        (board[2] == icon and board[5] == icon and board[8] == icon) or \
        (board[0] == icon and board[4] == icon and board[8] == icon) or \
        (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False
def is_draw():
    if "   " not in board:
        return True
    else:
        return False


while True:
    print_board()
    player_move(" X ")
    print_board()
    if is_Victory(" X "):
        print("{} Wins!! Congratulations!".format(P1))
        break
    elif is_draw():
        print("Its Draw")
        break

    player_move(" O ")
    print_board()
    if is_Victory(" O "):
        print("{} Wins!! Congratulations!".format(P2))
        break
    elif is_draw():
        print("Its Draw")
        break

