import random
number = random.randint(1, 100)
print("Welcome to the guessing game!")
print("I am thinking of a number between 1 and 100!")
print(number)

EASY = 10
HARD = 5
difficulty_level = input("Choose a difficulty level: easy or hard ").lower()

def difficulty():
    global number_of_attempts
    if difficulty_level == 'easy':
        number_of_attempts = EASY
    elif difficulty_level == 'hard':
        number_of_attempts = HARD
    else:
        print("invalid difficulty level! please enter either easy or hard!")
    return number_of_attempts

game_over = False

def check_the_number(number, user_choice):
    if user_choice > number:
        print("Too High!")
    elif user_choice < number:
        print("Too Low!")

while not game_over:
    for i in range(difficulty()):
        user_choice = int(input("Choose a number! "))
        if user_choice == number:
            print("Your choice is correct!")
            game_over = True
            break
        else: 
            check_the_number(number, user_choice)
            number_of_attempts -= 1
        print(f"You have {number_of_attempts} attempts left!")
    print("You have run out of attempts! Game over!")
    game_over = True
    
    