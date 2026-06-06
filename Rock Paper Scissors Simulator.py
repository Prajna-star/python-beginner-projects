import random
print("This is a rock, paper and scissors game! Find your luck with the computer!")
game = [0, 1, 2]
computer = random.choice(game)
print(computer)
user = input('''select '0' for Rock\n
or '1' for Paper\n
or '2' for Scissors!''') 
user_choice = game[int(user)]
print(f'''Computer chose {computer}\n You chose {user}''')
print(computer - user_choice)
if computer - user_choice == 1:
    print("You have lost the game!")
elif computer == user_choice:
    print("Its a draw!")
else:
    print("You have won!")