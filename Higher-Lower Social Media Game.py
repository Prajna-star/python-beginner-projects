from data import data
import random

# computer chooses the 2 options
choice = random.choices(data, k=2)
A = choice[0]
B = choice[1]

# the less followers guy becomes part of the next comparision
def next():
    global A
    if A['follower_count'] > B['follower_count']:
        A = B
    else:
        A = A


game_over = False
score = 0
while not game_over:
    # user input which one is higher
    print(f"A is {A['name']}, {A['description']}, {A['country']}, {A['follower_count']}")
    print(f"B is {B['name']}, {B['description']}, {B['country']}, {B['follower_count']}")
    user_choice = input("Choose between A and B: ").upper()
    
    if (user_choice == 'A' and max(A['follower_count'], B['follower_count']) == A['follower_count']) or (user_choice == 'B' and max(A['follower_count'], B['follower_count']) == B['follower_count']):
        next()
        B = random.choice(data)
        score += 1
    else:
        print(f"Game over! your score is {score}")
        game_over = True

