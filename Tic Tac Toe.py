# creating variables for total scores of X and O
score_x = 0
score_y = 0

def play():
    """Calls other functions to play the game"""
    
    # creating a grid for tic tac toe
    grid = ["1", "2", "3",
            "4", "5", "6",
            "7", "8", "9"]

    def display_grid():
        """displays the grid"""
        
        print(grid[0] + "|" + grid[1] + "|" + grid[2]) 
        print(grid[3] + "|" + grid[4] + "|" + grid[5]) 
        print(grid[6] + "|" + grid[7] + "|" + grid[8])

    def till_won():
        """checks whether one of the players has won or not"""
        
        if grid[0] == grid[4] == grid[8]:
            return False
        
        elif grid[2] == grid[4] == grid[6]:
            return False
        
        elif grid[0] == grid[1] == grid[2]:
            return False
        
        elif grid[3] == grid[4] == grid[5]:
            return False
        
        elif grid[6] == grid[7] == grid[8]:
            return False
        
        elif grid[1] == grid[4] == grid[7]:
            return False
        
        elif grid[0] == grid[3] == grid[6]:
            return False
        
        elif grid[2] == grid[5] == grid[8]:
            return False
        
        return True
    
    def play_game():
        """basically the base of the game"""
        
        # created a variable for X and O
        number = 0
        
        # a variable to see if its a tie
        chances = 0
        
        # to call the X or O
        symbol = ""
        global score_x
        global score_y
        
        # ensures that the game stops after a player has won or when it is a tie
        while till_won() == True:
            display_grid()
            chances += 1
            
            # when the chances reach 10 that means neither of the players has won;thus, it is a tie and ends the game
            if chances == 10:
                print("Oops! It's a tie!")
                playAgain()
                quit()
            
            # the player enters the position at which he/she wants to place the X or O
            position = int(input("Enter the position: ")) - 1

            # if number is even play X, else play O
            if number % 2 == 0:
                symbol = "X"
            else:
                symbol = "O"
            
            # 1 is added to the number after every chance to keep switching between X and O
            number += 1
            
            # this places the symbol at the position in the grid
            grid[position] = symbol
        
        display_grid()

        # to keep track of the score of both the players 
        if symbol == "X":
            score_x += 1
        else:
            score_y += 1
        print(symbol + " is the champion!") 
    
    play_game()

def playAgain():
    """to choose whether you want to play again or not"""
    
    play_again = input("If you want to play again type yes: ")
     
    # a loop to continue to play till the player says no
    while play_again[:3].lower() == "yes":
        play()
        play_again = input("If you want to play again type yes: ")
    
    print("Score of X: " + str(score_x))
    print("Score of O: " + str(score_y))
    print("See you soon!")

play()
playAgain()

    

    
