###########################################################
# Computer Project # 2
# The game of Nim
#   Nested while loop
#       Display initial values
#       Promt for player to choose pile and number of stones
#       Display current values
#       Computer chooses opposite pile and takes one stone
#       Last one to pick a stone wins
#       Display winner
#   Offer to play again
###########################################################
#Display the rules of the game
print("\nWelcome to the game of Nim! I'm probably going to win...")
print('''Nim is a simple two-player game based on removing stones.
         The game begins with two piles of stones, numbered 1 and 2. 
         Players alternate turns. Each turn, a player chooses to remove one, 
         two, or three stones from some single pile. The player who removes the
         last stone wins the game.''')

play_str=input("Would you like to play? (0=no, 1=yes) ") #Ask to play

while int(play_str) != 0: #Human wants to play
    pile_1_stones = 5 #Initial stone amount
    pile_2_stones = 5 #Initial stone amount
    players_turn = True
    game_over = False
    print("Start --> Pile 1: 5    Pile 2: 5")
    computer_score = 0 #Initial computer score
    human_score = 0 #Initial human score
    
    while not game_over:
        if players_turn:
            a_str = input("Choose a pile (1 or 2):")
            a_int = int(a_str)
            
            if (a_int != 1 and a_int != 2) or (a_int == 1 and pile_1_stones == 0)\
            or (a_int == 2 and pile_2_stones == 0): #Human error
                    print(" Pile must be 1 or 2 and non-empty. Please try again.")
                    continue
            players_turn = True
    
            if a_int == 1: #Human picks first pile
                b_str = input(" Choose stones to remove from pile:")
                b_int = int(b_str)
                print(" Player -> Remove", b_int , "stones from pile", a_int)
                pile_1_stones = pile_1_stones - b_int
                print("Pile 1:", pile_1_stones ,  " Pile 2:", pile_2_stones )
                players_turn = False
            if a_int == 2: #Human picks second pile
                b_str = input(" Choose stones to remove from pile: ")
                b_int = int(b_str)
                print(" Player -> Remove", b_int , "stones from pile", a_int)
                pile_2_stones = pile_2_stones - b_int
                print("Pile 1:", pile_1_stones ,  " Pile 2:", pile_2_stones )
                players_turn = False
            
            if pile_1_stones == 0 and pile_2_stones == 0: #Human takes last stone
                game_over = True
                human_score += 1
                print("Player wins!") #Human wins
                print("Score -> human:", human_score, "; computer:", computer_score)
                break
        
        if not players_turn: #Computer takes from opposite pile
            if a_int == 1 and pile_2_stones == 0:
                   print("Computer -> Remove 1 stones from pile 1")
                   pile_1_stones = pile_1_stones - 1
                   print("Pile 1:", pile_1_stones ,  " Pile 2:", pile_2_stones)
            players_turn = True
            
            if a_int == 1 and pile_2_stones != 0: #Computer move when opposite pile is empty
                   print("Computer -> Remove 1 stones from pile 2")
                   pile_2_stones = pile_2_stones - 1
                   print("Pile 1:", pile_1_stones ,  " Pile 2:", pile_2_stones)
            players_turn = True
            
            if a_int == 2 and pile_1_stones != 0:
                   print("Computer -> Remove 1 stones from pile 1")
                   pile_1_stones = pile_1_stones - 1
                   print("Pile 1:", pile_1_stones ,  " Pile 2:", pile_2_stones)
            players_turn = True
            
            if a_int == 2 and pile_1_stones == 0: #Computer move when opposite pile is empty
                   print("Computer -> Remove 1 stones from pile 2")
                   pile_2_stones = pile_2_stones - 1
                   print("Pile 1:", pile_1_stones ,  " Pile 2:", pile_2_stones)
                   
            if pile_1_stones == 0 and pile_2_stones == 0: #Computer takes last stone
                game_over = True
                computer_score += 1 
                print("Computer wins!") #Computer wins
                print("Score -> human:", human_score, "; computer:", computer_score)
                
                break
        
    play_str = input("Would you like to play again? (0=no, 1=yes) ") #Ask to play again
else: #Human does not want to play
    print("\nThanks for playing! See you again soon!")


        