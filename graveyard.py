from helperFunctions import terminal_typing_effect, TERMINAL_TYPING_SPEED, showGraves, inventory_array, you_died, \
    you_win, graveyard_entrance_gate

alreadyDownNorthPath = False

def beginGraveyardPath():
    terminal_typing_effect("You approach the entrance of the graveyard\n", TERMINAL_TYPING_SPEED)
    showGraves()
    terminal_typing_effect("It is really dark, would you like to use your flashlight?\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#1. Use flashlight\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#2. Don't use flashlight\n", TERMINAL_TYPING_SPEED)

    #If the user has the flashlight in the inventory, then the user can equip the flashlight, otherwise tell the user they do not have the flashlight
    #check the user has a flashlight if(inventory contains flashlight -> then use

    useFlashlight = input("choose 1/2\n")
    if(useFlashlight == '1'):
        if("torch" in inventory_array):
            terminal_typing_effect("You turn on the torch\n", TERMINAL_TYPING_SPEED)
            terminal_typing_effect('"Ah, better I can see clearer"', TERMINAL_TYPING_SPEED)
        else:
            terminal_typing_effect("You do not have a torch in your inventory\n", TERMINAL_TYPING_SPEED)
    elif(useFlashlight == '2'):
        terminal_typing_effect("You chose not to use a torch\n", TERMINAL_TYPING_SPEED)

    terminal_typing_effect("As you look around, you realize the size of the graveyard \n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect('The drone had to of landed in here\n', TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You continue walking along the main road in the graveyard\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect('"This graveyard goes on for miles"\n', TERMINAL_TYPING_SPEED)
    terminal_typing_effect("As you get deeper into the graveyard you come to a crossroads in the graveyard\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You fiddle with the controller of the drone so you can hear where it is.\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("But you can hear it coming from the north east direction\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("But there are three paths in front of you\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Do you want to listen out for the drone?\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#1. Yes\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#2. No\n", TERMINAL_TYPING_SPEED)

    graveyardMainListenForDrone = input("Listen for drone Yes/No\n").lower()
    if(graveyardMainListenForDrone == 'yes'):
        droneBattery()
        terminal_typing_effect("The drone sounds like it is coming from the north east\n", TERMINAL_TYPING_SPEED)
    elif(graveyardMainListenForDrone == 'n'):
        terminal_typing_effect("Sure, best to save the battery until you get closer\n", TERMINAL_TYPING_SPEED)
    graveyardPaths()

def graveyardPaths():
    terminal_typing_effect("Which path do you want to try?\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#1. WEST\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#2. NORTH\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#3. EAST\n", TERMINAL_TYPING_SPEED)

    #while loop checks input for numeric chars only.
    #If alpha chars entered, the user is asked to enter numeric chars again
    while True:
        graveyardInputPath = input("Choose from the paths above \n").lower()
        if graveyardInputPath.isnumeric():
            break
        terminal_typing_effect("No alpha characters, Try again\n", TERMINAL_TYPING_SPEED)

    if(graveyardInputPath == '1'):
        graveyardWestPath()
    elif graveyardInputPath == '2':
        graveyardNorthPath()
    elif(graveyardInputPath == '3'):
        graveyardEastPath()

def graveyardWestPath():
    #mob path with dead end
    terminal_typing_effect("WEST PATH\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You have chosen to try the WEST path\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("After walking down the path\n", TERMINAL_TYPING_SPEED)
    graveyardWestPath1()

def graveyardWestPath1():
    terminal_typing_effect("You chose to walk down the right path\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("The tree line covers moon light\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("The batteries in the torch suddenly die\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Do you want to continue walking?\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Yes\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("No\n", TERMINAL_TYPING_SPEED)

    continueWalking = input("Choose yes/no\n")
    
    if(continueWalking == 'yes'):
        terminal_typing_effect("You continue walking in the dark\n", TERMINAL_TYPING_SPEED)
        terminal_typing_effect("You fall in a hole in the ground and die\n", TERMINAL_TYPING_SPEED)
        you_died()
    elif(continueWalking == '2'):
        terminal_typing_effect("You turn around and proceed to walk back to where the paths fork\n", TERMINAL_TYPING_SPEED)
        terminal_typing_effect("You trip over rock on the ground and split your head open, lose consciousness and die\n ", TERMINAL_TYPING_SPEED)
        you_died()


def graveyardNorthPath():
    alreadyDownNorthPath = True
    terminal_typing_effect("You chose the NORTH path\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("As you get closer to the drone, you see that the signal is getting stronger\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You find the drone by pushing the throttle and listening out for it\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Do you want to listen out for the drone?\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("YES\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("NO\n", TERMINAL_TYPING_SPEED)
    listenForDrone = input("Choose yes/no from above\n").lower()
    #put a check on this if/elif block to check alpha character only
    if(listenForDrone == 'yes'):
        droneBattery()
    elif (listenForDrone == 'no'):
        terminal_typing_effect("Ok\n", TERMINAL_TYPING_SPEED)


def droneBattery():
    droneBattery = 100
    batteryDepleted = 20
    droneBattery = droneBattery - batteryDepleted
    if(droneBattery <= 0):
        terminal_typing_effect("Drone battery is dead\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You need to be careful when using the drone battery\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect(f"Battery charge {droneBattery}\n", TERMINAL_TYPING_SPEED)

    terminal_typing_effect("After listening for the drone, it seems to be coming from the east path\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You carefully walk back to the main paths\n", TERMINAL_TYPING_SPEED)
    graveyardPaths()
    exit()

def graveyardEastPath():
    terminal_typing_effect("This is the winning path", TERMINAL_TYPING_SPEED)
    if(alreadyDownNorthPath is True):
        terminal_typing_effect("This is true\n", TERMINAL_TYPING_SPEED)
        terminal_typing_effect("Ok, the drone has to be down this path\n", TERMINAL_TYPING_SPEED)
    else:
        terminal_typing_effect("This is false\n", TERMINAL_TYPING_SPEED)
        terminal_typing_effect("Let\'s try this path \n ", TERMINAL_TYPING_SPEED)
    
    terminal_typing_effect('"I think I should listen for the drone again"\n', TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#1. Yes\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#2. No\n", TERMINAL_TYPING_SPEED)

    eastPathListenForDrone = input("Do you want to listen for the drone again\n").lower()

    if(eastPathListenForDrone == 'yes'):
        droneBattery()
        terminal_typing_effect("You hear the drone much clearer now \n", TERMINAL_TYPING_SPEED)
        foundDrone()
    elif(eastPathListenForDrone == 'no'):
        terminal_typing_effect("ok, it may be a little harder to find the drone\n", TERMINAL_TYPING_SPEED)

def foundDrone():
    terminal_typing_effect("You walk further down and notice it in a tree\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect('"I found it!!"\n', TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Ok, lets try and get out of here \n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You continue down the path and come to a fork in the path\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("You just want to get out of here\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("Choose a path\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#1. Left\n", TERMINAL_TYPING_SPEED)
    terminal_typing_effect("#2. Right\n", TERMINAL_TYPING_SPEED)

    foundDroneInput = input("Choose a path\n")

    if(foundDroneInput == '1'):
        terminal_typing_effect("Now that you have found the drone it is time to get out of here\n", TERMINAL_TYPING_SPEED)
        terminal_typing_effect('"The flashlight is running out of battery, so I better hurry"\n', TERMINAL_TYPING_SPEED)
        terminal_typing_effect("You begin to run, before the flash light runs out\n", TERMINAL_TYPING_SPEED)
        terminal_typing_effect("While running you trip on your shoe laces and die of a concussion\n", TERMINAL_TYPING_SPEED)
        you_died()

    elif(foundDroneInput == '2'):
        terminal_typing_effect("You turn on your flashlight\n", TERMINAL_TYPING_SPEED)
        terminal_typing_effect("You approach the graveyard gates\n", TERMINAL_TYPING_SPEED)
        graveyard_entrance_gate()
        terminal_typing_effect("With the drone in your hand you push the cemetery gate open, and vow never to return\n", TERMINAL_TYPING_SPEED)
        you_win()



        
