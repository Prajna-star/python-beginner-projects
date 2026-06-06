# while loop in webpage!

print("Welcome to the hangman!")

chosen_word = "PrajnaDittakavi".lower()
blank = '_'*len(chosen_word)

print(blank)
game_over = False
selected_letters = []
lives = 6
while not game_over:
    user_imput = input("Select a letter: ")
    if user_imput in selected_letters:
        print("You have already selected the letter")
    elif user_imput not in chosen_word:
        selected_letters.append(user_imput)
        lives -= 1
        print(f"Your selected letter is not in the word. You lost a life. \nRemaining lives are {lives}")
    else:
        display = ''
        for letter in chosen_word:
            if letter == user_imput:
                display += user_imput
                selected_letters.append(user_imput)
            elif letter in selected_letters:
                display += letter
            else:
                display += '_'
        print(display)

    if '_' not in display:
        game_over = True
        print("You Win!")
    if lives == 0:
        game_over = True
        print("You lose!")