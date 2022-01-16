# Assignment: Week 2; Tic-Tac-Toe
# Authour: Katherine Arthur


def main():
    game_over = False
    x_turn = True
    turn = 1

    game_dictionary = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
    print(draw_grid(game_dictionary))
    while not game_over:
        (game_dictionary, game_over, player) = get_input(game_dictionary, x_turn)
        x_turn = not x_turn 
        print(draw_grid(game_dictionary))
        if game_over:
            print("Player " + player + " Wins!!")
        turn += 1
        if turn == 10:
            print("Cat's Game!")
            game_over = True
    

    

def draw_grid(game_dictionary):
    top = str(game_dictionary["1"]) + "|" +  str(game_dictionary["2"]) +  "|"  +  str(game_dictionary["3"])  + "\n"
    top_divide = "-+-+-" + "\n"
    middle = str(game_dictionary["4"]) + "|" +  str(game_dictionary["5"]) +  "|"  +  str(game_dictionary["6"]) + "\n"
    middle_divide = "-+-+-" + "\n"
    bottom = str(game_dictionary["7"]) + "|" +  str(game_dictionary["8"]) +  "|"  +  str(game_dictionary["9"]) + "\n"
   

    return(top + top_divide + middle + middle_divide + bottom) 

def get_player_input(player):
    player_input = input(player + "'s turn to choose a square(1-9): ")

    return(player_input)

def winner(game_dictionary, player):
    if ((game_dictionary["1"] == game_dictionary["2"] == game_dictionary["3"] == player) or
    (game_dictionary["4"] == game_dictionary["5"] == game_dictionary["6"] == player) or
    (game_dictionary["7"] == game_dictionary["8"] == game_dictionary["9"] == player) or
    (game_dictionary["1"] == game_dictionary["4"] == game_dictionary["7"] == player) or
    (game_dictionary["2"] == game_dictionary["5"] == game_dictionary["8"] == player) or
    (game_dictionary["3"] == game_dictionary["6"] == game_dictionary["9"] == player) or
    (game_dictionary["1"] == game_dictionary["5"] == game_dictionary["9"] == player) or
    (game_dictionary["3"] == game_dictionary["5"] == game_dictionary["7"] == player)):
        return True
    else:
        return False


def get_input(game_dictionary, x_turn):
    
    if x_turn:
        player = "X"
    else:
        player = "O"
    player_input = get_player_input(player)
    while player_input not in [ "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        player_input = get_player_input(player)

    while isinstance(game_dictionary[player_input], str):
        player_input = get_player_input(player)

    game_dictionary[player_input] = player

    if winner(game_dictionary, player):
        print("Player " + player + " wins!!")
        return(game_dictionary, True, player)
   

    return(game_dictionary, False, player)


if __name__ == "__main__":
    main()