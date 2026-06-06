import random
num = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer = random.choices(num, k=2)
user = random.choices(num, k=2)

def calculate_score(cards):
    sum_cards = sum(cards)
    if sum_cards == 21 and len(cards) == 2:
        return 21
    if sum_cards > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum_cards
print(f"Computer card: {computer[0]}")
print(f"Your cards: {user}")

while True:
    sum_user = calculate_score(user)
    print(f"You current sum is {sum_user}.")
    if sum_user > 21:
        break
    user_input = input("Would you like to take another card? y or n ")
    if user_input == "y":
        user.append(random.choice(num))
        sum_user = calculate_score(user)
        print(sum_user)
        print(user)

    else:
        if sum_user < 17:
            print("You have to select another card!")
        else:
            break

sum_computer = calculate_score(computer)
while sum_computer !=  0 and sum_computer < 17:
    computer.append(random.choice(num))
    sum_computer = calculate_score(computer)

print(f"Your cards are {user} and the sum is {sum_user}. The computer's cards are {computer} and the sum is {sum_computer}.")

if sum_user > 21 and sum_computer > 21:
    print("You both lost!")
elif sum_user == sum_computer:
    print("Its a draw!")
elif sum_user > sum_computer:
    if sum_user > 21:
        print("You lost!")
    else:
        print("You win!")
elif sum_computer > sum_user:
    if sum_computer > 21:
        print("You won!")
    else:
        print("You lost!")
