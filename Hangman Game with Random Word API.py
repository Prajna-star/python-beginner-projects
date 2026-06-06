from random_word import RandomWords
r = RandomWords()
chosen_word = r.get_random_word().lower()
print(chosen_word)

blank = '_'*len(chosen_word)
print(blank)
lives = 6
current_display = []
game_over = False
user = []
while not game_over:
    display = ''
    user_input = input("Choose a letter ")
    if user_input in user:
        print("You have already guessed the letter! Choose another one!")
    else:
        user.append(user_input)
        for letter in chosen_word:
            if letter == user_input:
                display += letter
                current_display.append(letter)
            elif letter in current_display:
                display += letter
            else:
                display += '_'
        print(display)

        if '_' not in display:
            game_over = True
            print("You Win!")
        if user_input not in chosen_word:
            if lives == 0:
                print("You lose!")
                game_over = True
                break
            lives -= 1
            print(f"You lost a life. You have {lives} lives remaining!")
