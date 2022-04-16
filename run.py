# -- Write your code to expect a terminal of 80 characters wide and 24 rows high --

#Important
#ToDo:
# -- N.B heroku requires all inputs and print statements to have a newline character to work with heroku config --
#Colours in terminal
#RED text = player died
#GREEN text =
#BLUE text =


from colorama import Fore, Back, Style

# imports from helperFunctions.py
from helperFunctions import terminal_typing_effect





def intro_message():
    """
        This function is responsible for providing the introduciton graphic when the user starts the game
    """
    
    print()
    terminal_typing_effect("*************************************************\n", 0.025)
    terminal_typing_effect("*************************************************\n", 0.025)
    terminal_typing_effect("ESCAPE THE ATTIC", 0.025)
    #Find a graphic for here
    terminal_typing_effect("*************************************************\n", 0.025)
    terminal_typing_effect("*************************************************\n", 0.025)


"""
    



"""




def begin_game():
    """
        This function is the initial function that is called when the user plays the game.
        It introduces the user to the game and provides a storyline,

        The function also calls intro which displays graphic before game starts
    """

    intro_message()

    global username
    while True:

        username = input("Hello player, enter your name to begin \n")
        print(Fore.YELLOW + f"Hello {username}, can you escape the attic\n")

        if username == "":
            print("Hello!! are you there, please enter your name to begin an adventure!\n")
            continue
        else:
            #print("Hello you need a name to start\n")
            break
    terminal_typing_effect(f"Hello {username}, are you ready? Good luck! \n", 0.02)
    userOptionOne()

def userOptionOne():
    terminal_typing_effect("You awake to find yourself in a dark, cramped attic", 0.005)
    terminal_typing_effect("You notice boxes ")

def userOptionTwo():
    print("UserOPtions1")

def userOptionThree():
    print("UserOPtions1")