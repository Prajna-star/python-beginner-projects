print("Welcome to the treasure Island!")
print("Your mission is to find the treasure!")
first = input("Choose either left('l') or right('r')\n")
if first.lower() == 'l':
    print("Good! now you have reached the lake!")
    second = input("Would you like to swim('s') or wait('w')?\n")
    if second.lower() == 'w':
        print("Great! now you are safe on the boat!")
        third = input("You see 3 doors in front of you! Which one do you choose? Red('r'), Blue('b'), or Yellow('y')\n")
        if third.lower() == 'y':
            print("Congratulations! You found the treasure!")
        elif third.lower() == 'r':
            print("You lost! this is the room full of FIRE!")
        elif third.lower() == 'b':
            print("You lost! this room is full of Scorpions!")
        else:
            print("You lost! cause you entered the wrong key!")
    elif second.lower() == 's':
        print("You have lost the game! the lake is full of crocodiles!")
    else:
        print("You lost! cause you entered the wrong key!")    
elif first.lower() == 'r':
    print("You have lost the game! The right is the valley down fall!")
else:
    print("You lost! cause you entered the wrong key!")
    